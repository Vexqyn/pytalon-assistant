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

from utils import smart_detection, remove_command_prefix

from pytalon_body.response_validators import (
    YES_SET,
    NO_SET,
    EXIT_SET,
    DEFER_SET,
    _normalize_answer,
)

# Social fluff vs real learning requests — used when ranking intents
SOCIAL_INTENTS = {'greeting'}

SUBSTANTIVE_INTENTS = {
    'help_request',
    'topic_request',
    'practice_request',
    'general_question',
    'confusion',
    'clarification',
}

# Prefer these conversation intents over a bare topic request
CONVERSATION_INTENTS = {
    'greeting',
    'farewell',
    'gratitude',
    'confusion',
    'clarification',
    'defer',
}

# Always prefer these over an unnamed topic_request
HIGH_PRIORITY_INTENTS = {
    'gratitude',
    'clarification',
    'general_question',
    'defer',
}


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

    # Exact topic name is the strongest signal
    for topic in TOPIC_KEYWORDS.keys():
        if user_text_clean.lower() == topic.lower():
            return 1.0, topic

    def _block_common_single(score, topic, kw_lower=""):
        # Common single words (hello, help, ...) must not lock onto a topic
        if user_text_clean in COMMON_SINGLE_WORDS:
            if len(user_text_clean.split()) == 1 and topic.lower() != user_text_clean:
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

    for topic, keywords in TOPIC_KEYWORDS.items():
        score = _block_common_single(smart_detection(user_text, topic.lower()), topic)

        for keyword in keywords:
            kw_lower = keyword.lower()
            kw_score = _block_common_single(
                smart_detection(user_text, kw_lower),
                topic,
                kw_lower,
            )
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

# Handle unrecognized input by checking for greetings, gratitude, farewells, help requests, or near-topic phrases.
def handle_unrecognized_input(user_input):
    """
    Handle unclear input using the config database when possible.

    Order:
        1. Empty / over-limit
        2. Known yes/no/exit/defer (never 'unrecognized')
        3. Config DB: greeting / gratitude / farewell / help / topic
        4. Short vs general 'not sure' with helpful examples from HELP_PATTERNS
    """
    from pytalon_body.response_validators import (
        _normalize_answer,
        YES_SET,
        NO_SET,
        EXIT_SET,
        DEFER_SET,
    )

    if not user_input:
        print("   ")
        return

    if len(user_input) > 10000:
        print("Max. limit is upto 10000 characters.")
        return

    normalized = _normalize_answer(user_input)
    text = normalized or user_input.lower().strip()
    words = set(text.split())

    # Known answers — never treat as unrecognized
    if text in YES_SET or text in NO_SET or text in EXIT_SET or text in DEFER_SET:
        return

    # ---- Config DB recovery ----
    greeting_hit = (
        any(phrase in text for phrase in GREETING_PATTERNS if ' ' in phrase)
        or any(token in GREETING_PATTERNS for token in words)
    )
    if greeting_hit:
        print("\n🤖 Hey! I'm Pytalon — your Python assistant.")
        print("   • Say a topic (e.g., 'teach me variables')")
        print("   • Or type 'show topics' for the full list")
        return

    gratitude_hit = any(
        (phrase in text) if ' ' in phrase else (phrase in {w.strip('!?.,') for w in words})
        for phrase in GRATITUDE_PATTERNS
    )
    if gratitude_hit:
        print("\n🤖 You're welcome! What would you like to learn next?")
        print("   • Tell me a topic or type 'show topics'")
        return

    if any(pattern in text for pattern in FAREWELL_PATTERNS):
        print("\n👋 Goodbye! Come back whenever you need me.")
        return

    if any(pattern in text for pattern in HELP_PATTERNS) or any(
        pattern in text for pattern in generic_python_patterns
    ):
        print("\n🤖 I can teach you Python basics!")
        print("   • Type 'show topics' for the full list")
        print("   • Or say 'teach me variables', 'teach me functions', ...")
        return

    # Near-topic phrase from the keyword database
    topic_score, topic = _check_topic_request(text)
    if topic:
        print(f"\n🤖 Did you mean {topic}?")
        print(f"   • Type 'teach me {topic.lower()}' or just say the topic name")
        print("   • Or type 'show topics' to browse everything")
        return

    # Short vs general unclear — examples pulled from HELP_PATTERNS style
    if len(text) < 10:
        print("That seems a bit short! ☺️")
        print(
            "Try something like 'Hello', 'Can you teach me Python?', "
            "or 'show topics' 🤔"
        )
        return

    print("I'm not sure what you mean! 😅")
    print(
        "Try 'Hi', a topic name (e.g., 'teach me lists'), "
        "or 'show topics' to see what I can teach."
    )

# Handle completely empty input by printing a blank line or a thank-you message.
def handle_empty_input(user_input):
    """Handles completely empty input."""
    if not user_input:
        print("   ")

    else:
        print(f"😄 Thanks for your message! {user_input}")


# ==========================================================
# INTENT DETECTION
# ==========================================================

# Analyze user input to detect the conversational intent, returning a dict with the best-matching intent, confidence score, and any extra info.
def detect_conversation_intent(user_input):
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
    user_input_lower = user_input.lower().strip()
    normalized = _normalize_answer(user_input_lower)

    # Empty / too long — no point scoring further
    if not user_input_lower:
        handle_empty_input(user_input)
        return {'intent': 'empty', 'confidence': 1.0}

    if len(user_input_lower) > 10000:
        handle_unrecognized_input(user_input)
        return {'intent': 'unrecognized', 'confidence': 1.0}

    # Known short answers (yes!, of course!, afk, ...) — no "unrecognized" print
    if normalized in YES_SET:
        return {'intent': 'yes_no', 'confidence': 0.95, 'answer': 'yes'}

    if normalized in NO_SET:
        return {'intent': 'yes_no', 'confidence': 0.95, 'answer': 'no'}

    if normalized in EXIT_SET:
        return {'intent': 'yes_no', 'confidence': 0.95, 'answer': 'exit'}

    if normalized in DEFER_SET:
        return {'intent': 'defer', 'confidence': 0.85}

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
    seems_topic = (
        any(pattern in user_input_lower for pattern in TOPIC_REQUEST_PATTERNS)
        or any(
            any(keyword in user_input_lower for keyword in keywords)
            for keywords in TOPIC_KEYWORDS.values()
        )
    )

    if seems_topic:
        record('topic_request', 0.7)

    # ---- Scorer 3: Beginner / learning intent ----
    help_from_beginner = any(re.search(p, user_input_lower) for p in BEGINNER_PATTERNS)

    if help_from_beginner:
        record('help_request', 0.8, is_beginner=True)

    # ---- Scorer 4: Greetings ----
    greeting_hit = (
        any(phrase in user_input_lower for phrase in GREETING_PATTERNS if ' ' in phrase)
        or any(token in GREETING_PATTERNS for token in user_input_lower.split())
    )

    if greeting_hit:
        record('greeting', 0.9)

    # ---- Scorer 5: Farewells ----
    if any(pattern in user_input_lower for pattern in FAREWELL_PATTERNS):
        record('farewell', 0.9)

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
        record('gratitude', 0.9)

    # ---- Scorer 7: Confusion ----
    if any(pattern in user_input_lower for pattern in CONFUSION_PATTERNS):
        record('confusion', 0.8)

    # ---- Scorer 8: Practice request ----
    if any(pattern in user_input_lower for pattern in PRACTICE_REQUEST_PATTERNS):
        record('practice_request', 0.8)

    # ---- Scorer 9: Help request ----
    help_from_patterns = any(pattern in user_input_lower for pattern in HELP_PATTERNS)

    if help_from_patterns:
        record('help_request', 0.8)

    # ---- Scorer 10: Generic Python learning request ----
    if any(pattern in user_input_lower for pattern in generic_python_patterns):
        record('help_request', 0.85, is_beginner=True)

    # ---- Scorer 11: Yes / No / Exit ----
    if normalized in YES_SET:
        record('yes_no', 0.95, answer='yes')

    if normalized in NO_SET:
        record('yes_no', 0.95, answer='no')

    if normalized in EXIT_SET:
        record('yes_no', 0.95, answer='exit')

    # ---- Scorer 12: General question patterns ----
    if any(re.search(p, user_input_lower) for p in QUESTION_PATTERNS):
        record('general_question', 0.7)

    # ---- Scorer 13: Uncertain responses ----
    if any(phrase in user_input_lower for phrase in UNCERTAIN_RESPONSES):
        record('uncertain', 0.75)

    # ---- Scorer 14: Defer / pause request ----
    if any(phrase in user_input_lower for phrase in DEFER_PATTERNS):
        record('defer', 0.85)

    # ---- Scorer 15: Repeat request ----
    if any(phrase in user_input_lower for phrase in REPEAT_REQUEST_PATTERNS):
        record('repeat_request', 0.85)

    # ---- Scorer 16: Clarification request ----
    if any(phrase in user_input_lower for phrase in CLARIFICATION_PATTERNS):
        record('clarification', 0.8)

    # ---- Scorer 17: Pytalon memory request ----
    # Wipe/delete phrases explain only — they never auto-delete files
    if any(phrase in user_input_lower for phrase in MEMORY_CLARIFICATION_PATTERNS):
        record('memory_manage', 0.95)

    # What do you remember? / stats / about me — always answer with a report
    if any(phrase in user_input_lower for phrase in MEMORY_REQUEST_PATTERNS):
        record('memory_request', 0.95)
    elif any(phrase in user_input_lower for phrase in MEMORY_SUMMARY_PATTERNS):
        record('memory_request', 0.95)
    elif any(phrase in user_input_lower for phrase in MEMORY_ABOUT_ME_PHRASES):
        # "bro tell me about myself", "know about me", "on me", ...
        record('memory_request', 0.95)
    elif any(word in MEMORY_SHORT_WORDS for word in user_input_lower.split()):
        record('memory_request', 0.9)
    else:
        # about-me style: myself/profile + tell/know/show/check/save words
        tokens = set(user_input_lower.replace(',', ' ').replace('!', ' ').split())
        about_hit = bool(tokens & MEMORY_ABOUT_ME_TOKENS) or 'myself' in user_input_lower
        ask_words = {
            'tell', 'know', 'show', 'check', 'view', 'open', 'read',
            'what', 'whats', "what's", 'who', 'describe', 'explain',
            'give', 'drop', 'hit', 'sum', 'summarize', 'recall',
            'remember', 'saved', 'save', 'profile', 'stats',
        }
        if about_hit and (tokens & ask_words or 'about' in user_input_lower):
            record('memory_request', 0.95)
        elif 'about me' in user_input_lower or 'about myself' in user_input_lower:
            record('memory_request', 0.95)

    # Boost help when several help signals fire together
    if help_from_beginner and help_from_patterns and 'help_request' in scores:
        scores['help_request']['confidence'] = 0.95

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

    # Nothing matched
    handle_unrecognized_input(user_input)
    return {'intent': 'unrecognized', 'confidence': 0.0}
