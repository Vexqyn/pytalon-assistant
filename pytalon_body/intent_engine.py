# pytalon_body/intent_engine.py
"""
Conversation intent detection for Pytalon.

This is the "nervous system" of the body: it looks at what the learner
typed and decides what they mean (greeting, topic request, defer, ...).
"""

import re

from config import (
    GREETING_PATTERNS,
    FAREWELL_PATTERNS,
    GRATITUDE_PATTERNS,
    CONFUSION_PATTERNS,
    TOPIC_KEYWORDS,
    TOPIC_REQUEST_PATTERNS,
    PRACTICE_REQUEST_PATTERNS,
    HELP_PATTERNS,
    TOPIC_MATCH_THRESHOLD,
    BEGINNER_PATTERNS,
    QUESTION_PATTERNS,
    UNCERTAIN_RESPONSES,
    REPEAT_REQUEST_PATTERNS,
    CLARIFICATION_PATTERNS,
    DEFER_PATTERNS,
    COMMON_SINGLE_WORDS,
    generic_python_patterns,
    MEMORY_REQUEST_PATTERNS,
    MEMORY_SUMMARY_PATTERNS,
    MEMORY_SHORT_WORDS,
    MEMORY_CLARIFICATION_PATTERNS,
    MEMORY_ABOUT_ME_PHRASES,
    MEMORY_ABOUT_ME_TOKENS,
)

from utils import (
    assistant_reply,
    build_small_talk_reply,
    is_gibberish,
    remove_command_prefix,
    smart_detection,
)
from static_database.intent_settings import (
    PROTECTED_TOPIC_WORDS,
    SOCIAL_INTENTS,
    SUBSTANTIVE_INTENTS,
    CONVERSATION_INTENTS,
    HIGH_PRIORITY_INTENTS,
    CONF_YES_NO,
    CONF_DEFER,
    CONF_GREETING,
    CONF_FAREWELL,
    CONF_GRATITUDE,
    CONF_CONFUSION,
    CONF_PRACTICE,
    CONF_HELP,
    CONF_HELP_BOOST,
    CONF_GENERIC_PYTHON,
    CONF_GENERAL_QUESTION,
    CONF_UNCERTAIN,
    CONF_REPEAT,
    CONF_CLARIFICATION,
    CONF_MEMORY,
    CONF_MEMORY_SHORT,
    CONF_TOPIC_KEYWORD,
    MEMORY_ASK_WORDS,
    NATURAL_EXIT_PHRASES,
    TOPIC_MENU_PHRASES,
    TEACH_REQUEST_MARKERS,
)
from static_database.response_phrases import (
    CLARIFY_QUESTIONS,
    NATURAL_FALLBACKS,
    RECOVERY_MESSAGES,
)
from static_database.small_talk import EMOJI_REPLES


from pytalon_body.response_validators import (
    YES_SET,
    NO_SET,
    EXIT_SET,
    DEFER_SET,
    _normalize_answer,
    _user_said_no,
    _is_mixed_yes_no,
)
from static_database.validator_settings import YES_WORDS, NO_WORDS
# Intent groups and confidence values live in static_database/intent_settings.py


# ==========================================================
# PRECOMPILED PATTERNS — split into phrases and single tokens
# ==========================================================

def _split_patterns(patterns):
    phrases = []
    tokens = set()
    for pattern in patterns:
        if ' ' in pattern:
            phrases.append(pattern)
        else:
            tokens.add(pattern)
    return phrases, tokens


_GREETING_PHRASES, _GREETING_TOKENS = _split_patterns(GREETING_PATTERNS)
_GRATITUDE_PHRASES, _GRATITUDE_TOKENS = _split_patterns(GRATITUDE_PATTERNS)
_FAREWELL_PHRASES, _FAREWELL_TOKENS = _split_patterns(FAREWELL_PATTERNS)
_HELP_PHRASES, _HELP_TOKENS = _split_patterns(HELP_PATTERNS)
_GENERIC_PHRASES, _GENERIC_TOKENS = _split_patterns(generic_python_patterns)


def _match_patterns(text, phrases, tokens):
    """True when a single-token pattern or a multi-word phrase matches."""
    words = {word.strip('!?.,') for word in text.split()}
    if tokens & words:
        return True
    return any(phrase in text for phrase in phrases)


# ==========================================================
# TOPIC MATCHING
# ==========================================================

# Check the user input for a topic request, returning the best match and score.
def _check_topic_request(user_text):
    """
    Find the best topic match for a phrase.

    Returns:
        (score, topic_name) or (0.0, None) when nothing is strong enough.
    """
    user_text_clean = user_text.rstrip('!?.,').strip()
    user_text_lower = user_text.lower()

    # Protected social words never open a lesson.
    if user_text_clean.lower() in PROTECTED_TOPIC_WORDS:
        return 0.0, None

    # Exact topic name is the strongest signal
    for topic in TOPIC_KEYWORDS.keys():
        if user_text_clean.lower() == topic.lower():
            return 1.0, topic

    def _block_common_single(score, topic, kw_lower=""):
        # Common single words (hello, help, ...) must not lock onto a topic
        if user_text_clean in COMMON_SINGLE_WORDS:
            if len(user_text_clean.split()) == 1 and topic.lower() != user_text_clean:
                topic_keywords = [k.lower() for k in TOPIC_KEYWORDS.get(topic, [])]
                if user_text_clean.lower() not in topic_keywords:
                    return 0.0

        # If the user typed "python" alone, don't match a topic that starts with "python" unless they also mentioned another keyword
        if (
            "python" in user_text_lower.split()
            and len(user_text_clean.split()) == 1
            and kw_lower
        ):
            kw_words = kw_lower.split()
            if len(kw_words) > 1 and kw_words[0] == "python":
                return 0.0
        return score

    # Collect every topic score so we can fall back if the winner is too generic
    candidates = []
    user_tokens = set(user_text_lower.split())

    def _keyword_score(keyword):
        """Score one keyword without letting short words match loosely."""
        kw_lower = keyword.lower()

        # Multi-word keywords must appear as a phrase.
        if ' ' in kw_lower:
            return 1.0 if kw_lower in user_text_lower else 0.0

        # Single-word keywords need a whole-token match, or a strong
        # similarity for longer words only.
        if len(kw_lower) < 3:
            return 0.0
        if kw_lower in user_tokens:
            return 1.0
        if len(kw_lower) < 5:
            return 0.0
        return smart_detection(user_text, kw_lower)

    for topic, keywords in TOPIC_KEYWORDS.items():
        score = _block_common_single(smart_detection(user_text, topic.lower()), topic)

        for keyword in keywords:
            kw_lower = keyword.lower()
            if kw_lower in PROTECTED_TOPIC_WORDS:
                continue
            kw_score = _block_common_single(_keyword_score(keyword), topic, kw_lower)
            if kw_score > score:
                score = kw_score

        if score > 0.0:
            candidates.append((score, len(topic), topic))

    # Highest score first; longer topic name wins ties
    candidates.sort(reverse=True)

    for score, _length, topic in candidates:
        # A bare "python" mention is not specific enough — try the next candidate
        if "python" in topic.lower():
            keywords = TOPIC_KEYWORDS.get(topic, [])
            has_other = any(
                kw != "python" and kw in user_text
                for kw in keywords
            )
            if not has_other:
                continue

        if score >= TOPIC_MATCH_THRESHOLD:
            return score, topic

    return 0.0, None

# Extract the topic phrase from a user input like "teach me variables" or "I want to learn functions".
def _extract_topic_phrase(user_input_lower, user_input_clean):
    """
    Pull the topic phrase out of sentences like "teach me variables".
    Falls back to the cleaned full input when no request pattern is present.
    """
    topic_phrase = user_input_clean

    for pattern in TOPIC_REQUEST_PATTERNS:
        if pattern in user_input_lower:
            start = user_input_lower.find(pattern) + len(pattern)
            topic_phrase = user_input_lower[start:].strip().rstrip('?.!')
            topic_phrase = remove_command_prefix(topic_phrase)
            break

    return topic_phrase


# ==========================================================
# FALLBACK HANDLERS
# ==========================================================

# Helpers for the recovery ladder.
def _learner_name():
    try:
        from Pytalon_Memory.memory_store import load_profile
        profile = load_profile()
        return profile.get("display_name") or profile.get("name") or "there"
    except Exception:
        return "there"


def _last_topic():
    try:
        from Pytalon_Memory.memory_store import load_long_term
        return (load_long_term().get("preferences") or {}).get("last_topic")
    except Exception:
        return None


# Graded recovery ladder. Returns a structured result; never prints,
# never mocks the learner. The app layer renders the message.
def handle_unrecognized_input(user_input, profile=None):
    """
    Recover from unclear input in graded steps.

    Order:
        1. Empty / over-limit
        2. Known yes/no/exit/defer (never 'unrecognized')
        3. Emoji emotion reply
        4. Greeting / gratitude / farewell
        5. Help (capabilities overview)
        6. Near-topic phrase
        7. Friendly small talk / clarifying question (never a menu, never mocked)
    """
    if not user_input:
        return {'kind': 'empty', 'intent': 'empty', 'message_key': 'empty', 'text': RECOVERY_MESSAGES['empty']}

    if len(user_input) > 10000:
        return {'kind': 'too_long', 'intent': 'too_long', 'message_key': 'too_long', 'text': RECOVERY_MESSAGES['too_long']}

    normalized = _normalize_answer(user_input)
    text = normalized or user_input.lower().strip()

    # Known answers — never treat as unrecognized
    if text in YES_SET or text in NO_SET or text in EXIT_SET or text in DEFER_SET:
        return {'kind': 'answer', 'intent': 'answer', 'message_key': 'answer', 'text': RECOVERY_MESSAGES['answer']}

    # Emoji emotion: reply to the feeling, repeats included. Never mock.
    try:
        from pytalon_body.behavior_learner import read_emoji_emotion
        emotion = read_emoji_emotion(user_input)
    except Exception:
        emotion = None

    if emotion:
        replies = EMOJI_REPLES.get(emotion) or EMOJI_REPLES.get('amusement') or (("Hmm, I hear you. 💙", None),)
        pair = replies[0]
        reply = str(pair[0])
        if pair[1]:
            reply = f"{reply} {pair[1]}"
        return {'kind': 'emoji', 'intent': 'emoji', 'message_key': 'emoji', 'text': reply}

    if _match_patterns(text, _GREETING_PHRASES, _GREETING_TOKENS):
        name = _learner_name()
        return {'kind': 'greeting', 'intent': 'greeting', 'message_key': 'greeting',
                'text': f"Hey {name}! Ask me anything, or type 'help' for options."}

    if _match_patterns(text, _GRATITUDE_PHRASES, _GRATITUDE_TOKENS):
        return {'kind': 'gratitude', 'intent': 'gratitude', 'message_key': 'gratitude',
                'text': RECOVERY_MESSAGES['gratitude']}

    if _match_patterns(text, _FAREWELL_PHRASES, _FAREWELL_TOKENS):
        return {'kind': 'farewell', 'intent': 'farewell', 'message_key': 'farewell',
                'text': RECOVERY_MESSAGES['farewell']}

    if _match_patterns(text, _HELP_PHRASES, _HELP_TOKENS) or _match_patterns(
        text, _GENERIC_PHRASES, _GENERIC_TOKENS
    ):
        name = _learner_name()
        return {'kind': 'help', 'intent': 'help_request', 'message_key': 'help',
                'text': (
                    f"I'm Pytalon, {name} — a customizable assistant. I can:\n"
                    "   • Chat with you about anything\n"
                    "   • Remember your progress and profile (type 'what do you remember?')\n"
                    "   • Teach Python as a plugin when you ask (type 'show topics')\n"
                    "   • Adapt to your style as we talk"
                )}

    # Near-topic phrase from the keyword database
    _score, topic = _check_topic_request(text)
    if topic:
        return {'kind': 'near_topic', 'intent': 'near_topic', 'message_key': 'near_topic', 'topic': topic}

    # Slang / small talk / gibberish — one friendly reply, never a menu, never mocked.
    small_talk_reply = build_small_talk_reply(user_input, profile=profile, name=_learner_name())
    kind = 'clarify' if is_gibberish(user_input) else 'small_talk'
    return {'kind': kind, 'intent': kind, 'message_key': kind, 'text': small_talk_reply}


def handle_empty_input(user_input):
    """Return a structured result for empty input."""
    if not user_input:
        return {'kind': 'empty', 'message_key': 'empty', 'text': RECOVERY_MESSAGES['empty']}
    return {'kind': 'thanks', 'message_key': 'thanks', 'text': RECOVERY_MESSAGES['thanks']}


def render_recovery(result):
    """Render a recovery result into text for the app layer to print."""
    if not result:
        return RECOVERY_MESSAGES['steady_fallback']
    if result.get('text'):
        return result['text']
    key = result.get('message_key', 'steady_fallback')
    text = RECOVERY_MESSAGES.get(key, RECOVERY_MESSAGES['steady_fallback'])
    if result.get('topic'):
        text = text.format(topic=result['topic'], topic_lower=result['topic'].lower())
    return text


# ==========================================================
# INTENT DETECTION
# ==========================================================

# Analyze user input to detect the conversational intent, returning a dict with the best-matching intent, confidence score, and any extra info.
def detect_conversation_intent(user_input, profile=None):
    """
    Analyze user input to detect the conversational intent.

    Returns a dict with:
        intent       — best-matching intent name
        confidence   — score between 0 and 1
        ...extra     — e.g. topic=, answer=, is_beginner=

    Possible intents:
        greeting, farewell, gratitude, confusion, topic_request,
        practice_request, help_request, yes_no, general_question,
        uncertain, defer, repeat_request, clarification,
        empty, unrecognized

    Every scorer runs on every input. The highest confidence wins.
    Scorer order does not decide the winner.
    """
    # Use the live behavior profile when the caller does not supply one,
    # so the recovery ladder always matches the learner's current style.
    if profile is None:
        try:
            from pytalon_body.behavior_learner import get_style_profile
            profile = get_style_profile()
        except Exception:
            profile = None

    user_input_lower = user_input.lower().strip()
    normalized = _normalize_answer(user_input_lower)

    # Empty / too long — no point scoring further
    if not user_input_lower:
        assistant_reply(handle_empty_input(user_input).get('text') or '')
        return {'intent': 'empty', 'confidence': 1.0}

    if len(user_input_lower) > 10000:
        recovery = handle_unrecognized_input(user_input, profile)
        assistant_reply(render_recovery(recovery))
        handled_intent = recovery.get('intent') or 'unrecognized'
        return {'intent': handled_intent, 'confidence': 1.0, 'recovery': recovery}

    # Known short answers (yes!, of course!, afk, ...) — no "unrecognized" print
    if normalized in YES_SET:
        return {'intent': 'yes_no', 'confidence': CONF_YES_NO, 'answer': 'yes'}

    if normalized in NO_SET:
        return {'intent': 'yes_no', 'confidence': CONF_YES_NO, 'answer': 'no'}

    if normalized in EXIT_SET:
        return {'intent': 'yes_no', 'confidence': CONF_YES_NO, 'answer': 'exit'}

    if normalized in DEFER_SET:
        return {'intent': 'defer', 'confidence': CONF_DEFER}

    # Remove command-style prefixes (/lists, !functions, ...) for topic matching
    user_input_clean = remove_command_prefix(user_input_lower)

    # Each scorer writes here. Highest confidence per intent is kept.
    scores = {}

    def record(intent, confidence, **extra):
        if intent not in scores or confidence > scores[intent]['confidence']:
            scores[intent] = {'confidence': confidence, **extra}

    # ---- Scorer 1: Topic request (smart detection) ----
    topic_phrase = _extract_topic_phrase(user_input_lower, user_input_clean)
    topic_score, matched_topic = _check_topic_request(topic_phrase)

    if matched_topic:
        record('topic_request', topic_score, topic=matched_topic)

    # ---- Scorer 2: Topic request (keyword fallback) ----
    input_tokens = set(user_input_lower.split())

    def _keyword_in_input(keyword):
        kw_lower = keyword.lower()
        if kw_lower in PROTECTED_TOPIC_WORDS:
            return False
        if ' ' in kw_lower:
            return kw_lower in user_input_lower
        if len(kw_lower) < 3:
            return False
        return kw_lower in input_tokens

    seems_topic = (
        any(pattern in user_input_lower for pattern in TOPIC_REQUEST_PATTERNS)
        or any(
            _keyword_in_input(keyword)
            for keywords in TOPIC_KEYWORDS.values()
            for keyword in keywords
        )
    )

    if seems_topic:
        record('topic_request', CONF_TOPIC_KEYWORD)

    # ---- Scorer 3: Beginner / learning intent ----
    help_from_beginner = any(re.search(p, user_input_lower) for p in BEGINNER_PATTERNS)

    if help_from_beginner:
        record('help_request', CONF_HELP, is_beginner=True)

    # ---- Scorer 4: Greetings ----
    greeting_hit = (
        any(phrase in user_input_lower for phrase in GREETING_PATTERNS if ' ' in phrase)
        or any(token in GREETING_PATTERNS for token in user_input_lower.split())
    )

    if greeting_hit:
        record('greeting', CONF_GREETING)

    # ---- Scorer 5: Farewells ----
    if any(pattern in user_input_lower for pattern in FAREWELL_PATTERNS):
        record('farewell', CONF_FAREWELL)

    # ---- Scorer 5b: natural human exit requests ----
    if any(phrase in user_input_lower for phrase in NATURAL_EXIT_PHRASES):
        record('farewell', CONF_FAREWELL)

    # ---- Scorer 6: Gratitude ----
    # Single-word patterns match whole tokens so 'ty' does not hit 'type'
    gratitude_tokens = {
        token.strip('!?.,')
        for token in user_input_lower.split()
    }

    if any(
        (pattern in user_input_lower) if ' ' in pattern else (pattern in gratitude_tokens)
        for pattern in GRATITUDE_PATTERNS
    ):
        record('gratitude', CONF_GRATITUDE)

    # ---- Scorer 7: Confusion ----
    if any(pattern in user_input_lower for pattern in CONFUSION_PATTERNS):
        record('confusion', CONF_CONFUSION)

    # ---- Scorer 8: Practice request ----
    if any(pattern in user_input_lower for pattern in PRACTICE_REQUEST_PATTERNS):
        record('practice_request', CONF_PRACTICE)

    # ---- Scorer 9: Help request ----
    help_from_patterns = any(pattern in user_input_lower for pattern in HELP_PATTERNS)

    if help_from_patterns:
        record('help_request', CONF_HELP)

    # ---- Scorer 10: Generic Python learning request ----
    if any(pattern in user_input_lower for pattern in generic_python_patterns):
        record('help_request', CONF_GENERIC_PYTHON, is_beginner=True)

    # ---- Scorer 11: Yes / No / Exit ----
    if normalized in YES_SET:
        record('yes_no', CONF_YES_NO, answer='yes')

    if normalized in NO_SET:
        record('yes_no', CONF_YES_NO, answer='no')

    if normalized in EXIT_SET:
        record('yes_no', CONF_YES_NO, answer='exit')

    # ---- Scorer 11b: casual yes / no (word level) ----
    tokens = set(normalized.split())
    yes_hits = tokens & YES_WORDS
    no_hits = tokens & NO_WORDS

    # A casual phrase like "yeah whatever" mixes a yes word with an
    # indifference word, so it is chat — not a yes for a lesson.
    if no_hits and not yes_hits:
        record('yes_no', CONF_YES_NO - 0.05, answer='no')
    elif yes_hits and not no_hits and not _user_said_no(normalized) and not _is_mixed_yes_no(normalized):
        record('yes_no', CONF_YES_NO - 0.05, answer='yes')

    # ---- Scorer 12: General question patterns ----
    if any(re.search(p, user_input_lower) for p in QUESTION_PATTERNS):
        record('general_question', CONF_GENERAL_QUESTION)

    # ---- Scorer 13: Uncertain responses ----
    if any(phrase in user_input_lower for phrase in UNCERTAIN_RESPONSES):
        record('uncertain', CONF_UNCERTAIN)

    # ---- Scorer 14: Defer / pause request ----
    if any(phrase in user_input_lower for phrase in DEFER_PATTERNS):
        record('defer', CONF_DEFER)

    # ---- Scorer 15: Repeat request ----
    if any(phrase in user_input_lower for phrase in REPEAT_REQUEST_PATTERNS):
        record('repeat_request', CONF_REPEAT)

    # ---- Scorer 16: Clarification request ----
    if any(phrase in user_input_lower for phrase in CLARIFICATION_PATTERNS):
        record('clarification', CONF_CLARIFICATION)

    # ---- Scorer 17: Pytalon memory request ----
    # Wipe/delete phrases explain only — they never auto-delete files
    if any(phrase in user_input_lower for phrase in MEMORY_CLARIFICATION_PATTERNS):
        record('memory_manage', CONF_MEMORY)

    # What do you remember? / stats / about me — always answer with a report
    if any(phrase in user_input_lower for phrase in MEMORY_REQUEST_PATTERNS):
        record('memory_request', CONF_MEMORY)
    elif any(phrase in user_input_lower for phrase in MEMORY_SUMMARY_PATTERNS):
        record('memory_request', CONF_MEMORY)
    elif any(phrase in user_input_lower for phrase in MEMORY_ABOUT_ME_PHRASES):
        # "bro tell me about myself", "know about me", "on me", ...
        record('memory_request', CONF_MEMORY)
    elif any(word in MEMORY_SHORT_WORDS for word in user_input_lower.split()):
        # "show topics" is the topic menu, not a memory question
        if not any(phrase in user_input_lower for phrase in TOPIC_MENU_PHRASES):
            record('memory_request', CONF_MEMORY_SHORT)
    else:
        # about-me style: myself/profile + tell/know/show/check/save words
        tokens = set(user_input_lower.replace(',', ' ').replace('!', ' ').split())
        about_hit = bool(tokens & MEMORY_ABOUT_ME_TOKENS) or 'myself' in user_input_lower
        ask_words = MEMORY_ASK_WORDS
        if about_hit and (tokens & ask_words or 'about' in user_input_lower):
            record('memory_request', CONF_MEMORY)
        elif 'about me' in user_input_lower or 'about myself' in user_input_lower:
            record('memory_request', CONF_MEMORY)

    # Boost help when several help signals fire together
    if help_from_beginner and help_from_patterns and 'help_request' in scores:
        scores['help_request']['confidence'] = CONF_HELP_BOOST

    # Prefer a real request over a social opener ("hi, teach me variables")
    social_fired = SOCIAL_INTENTS & scores.keys()
    substantive_fired = SUBSTANTIVE_INTENTS & scores.keys()

    if social_fired and substantive_fired:
        for social in social_fired:
            if any(
                scores[sub]['confidence'] >= scores[social]['confidence']
                for sub in substantive_fired
            ):
                del scores[social]

    # Prefer conversation intents over a bare topic request
    if 'topic_request' in scores and CONVERSATION_INTENTS & scores.keys():
        for conv_intent in CONVERSATION_INTENTS & scores.keys():
            if scores[conv_intent]['confidence'] >= scores['topic_request']['confidence']:
                del scores['topic_request']
                break

    # Prefer gratitude / clarification / general_question over unnamed topic_request
    if (
        'topic_request' in scores
        and HIGH_PRIORITY_INTENTS & scores.keys()
        and not scores['topic_request'].get('topic')
    ):
        del scores['topic_request']

    # Direct curiosity questions ("what is a function?") are general questions,
    # never lesson requests — a bare topic match must not steal them.
    if 'general_question' in scores and 'topic_request' in scores:
        asks_lesson = any(marker in user_input_lower for marker in TEACH_REQUEST_MARKERS)
        if not asks_lesson and scores['general_question']['confidence'] > 0:
            del scores['topic_request']

    # Memory questions always win unless the learner named a real topic
    named_topic = scores.get('topic_request', {}).get('topic')

    if 'memory_manage' in scores and not named_topic:
        return {'intent': 'memory_manage', 'confidence': scores['memory_manage']['confidence']}

    if 'memory_request' in scores and not named_topic:
        return {
            'intent': 'memory_request',
            'confidence': scores['memory_request']['confidence'],
        }

    # Pick the winner
    if scores:
        best_intent = max(scores, key=lambda key: scores[key]['confidence'])
        result = {'intent': best_intent}
        result.update(scores[best_intent])
        return result

    # Nothing matched the scorers — run the graded recovery ladder.
    recovery = handle_unrecognized_input(user_input, profile)
    handled_intent = recovery.get('intent') or 'unrecognized'

    if handled_intent == 'unrecognized':
        # True fallthrough: one reply, flagged for the retry counter.
        assistant_reply(render_recovery(recovery))
        return {'intent': 'unrecognized', 'confidence': 0.0, 'recovery': recovery}

    # The ladder handled it (emoji, small talk, clarify, near topic, ...):
    # hand the handled intent back so the app layer replies exactly once.
    return {'intent': handled_intent, 'confidence': 0.0, 'recovery': recovery}
