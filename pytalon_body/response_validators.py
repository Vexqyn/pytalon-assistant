# pytalon_body/response_validators.py
"""
Input validation functions for Pytalon.

These are the "muscles" of the body: they ask the learner a question,
read a line, and return a clean decision like 'yes', 'no', 'defer',
'exit', or a topic name.
"""

from config import (
    YES_RESPONSES,
    NO_RESPONSES,
    EXIT_RESPONSES,
    YES_EXAMPLES_RESPONSES,
    NO_EXAMPLES_RESPONSES,
    YES_QUESTION_RESPONSES,
    NO_QUESTION_RESPONSES,
    EXIT_QUESTION_RESPONSES,
    SIMPLE_RESPONSES,
    DEFER_PATTERNS,
    NEGATION_WORDS,
    _TEACH_PREFIXES,
    _TEACH_OK_REST,
    _CASUAL_FILLERS,
    _EXIT_FIRST_WORDS,
    SIMPLE_TOKENS,
    _SKIP_PHRASES,
    _UNCERTAIN_TOKENS,
)

from utils import smart_validators, _extract_keywords
from conversation_context import context


# ==========================================================
# CUSTOM NORMALIZATION / EXACT MATCHING
# ==========================================================


# Canon phrase: lowercase, strip punctuation, keep letters/digits/spaces/apostrophes
def _canon_phrase(phrase):
    """
    Lowercase and strip punctuation so two answers can be compared directly.

    'of course! dude...' → 'of course dude'
    'exit bro!' → 'exit bro'
    Keeps letters, digits, spaces, and apostrophes only.
    """
    cleaned = phrase.lower().strip()
    chars = []
    for ch in cleaned:
        if ch.isalnum() or ch.isspace() or ch == "'":
            chars.append(ch)
        else:
            chars.append(' ')
    return ' '.join(''.join(chars).split())


# Normalize an answer for exact-set matching (alias used by the intent engine)
def _normalize_answer(text):
    """Normalize a learner answer for exact-set matching."""
    return _canon_phrase(text)


# Build a set of canonical phrases for fast exact matching
def _build_response_set(phrases):
    """Build a lowercase set with trailing punctuation stripped."""
    return {_canon_phrase(phrase) for phrase in phrases}


# ==========================================================
# YES / NO / EXIT / DEFER SETS
# ==========================================================


# Build sets for fast exact matching
YES_SET = _build_response_set(YES_RESPONSES)
NO_SET = _build_response_set(NO_RESPONSES)
EXIT_SET = _build_response_set(EXIT_RESPONSES)


# Question-phase yes/no/exit sets for fast exact matching
YES_QUESTION_SET = _build_response_set(YES_QUESTION_RESPONSES)
NO_QUESTION_SET = _build_response_set(NO_QUESTION_RESPONSES)
EXIT_QUESTION_SET = _build_response_set(EXIT_QUESTION_RESPONSES)


# Examples-phase yes/no sets for fast exact matching
YES_EXAMPLES_SET = _build_response_set(YES_EXAMPLES_RESPONSES)
NO_EXAMPLES_SET = _build_response_set(NO_EXAMPLES_RESPONSES)


# Defer-phase sets for fast exact matching
DEFER_SET = _build_response_set(DEFER_PATTERNS)


# Single-word vs multi-word negations for fast lookup
SINGLE_WORD_NEGATIONS = {word for word in NEGATION_WORDS if ' ' not in word}
MULTI_WORD_NEGATIONS = {phrase for phrase in NEGATION_WORDS if ' ' in phrase}


# Multi-word yes phrases for custom "contains" rule: "of course! dude" → yes
_YES_CONTAIN_PHRASES = tuple(sorted(
    (phrase for phrase in YES_SET if ' ' in phrase),
    key=len,
    reverse=True,
))


# Score thresholds for the match engine (the examples prompt is more forgiving)
MATCH_THRESHOLD = 0.75
EXAMPLES_MATCH_THRESHOLD = 0.65


# ==========================================================
# CUSTOM RULES FOR YES / NO / EXIT / DEFER
# ==========================================================


# Understand when the learner used a negation (no, don't, not really, ...).
def _user_said_no(input_text):
    """True when the learner used a negation (no, don't, not really, ...)."""
    words = set(input_text.split())

    if any(word in words for word in SINGLE_WORD_NEGATIONS):
        return True

    return any(phrase in input_text for phrase in MULTI_WORD_NEGATIONS)


# Understand when the learner clearly asked to skip/pass (not a real yes).
def _skip_phrase_wins(input_text):
    """True when the line clearly asks to skip/pass (not a real yes)."""
    return any(phrase in input_text for phrase in _SKIP_PHRASES)


# Name another topic mid-prompt: "teach me lists" is a topic switch, not a yes
def _names_other_topic(text):
    """True when the line names another lesson — that's a switch, not bare yes."""
    try:
        from intro import TOPIC_NAME_TO_NUMBER
    except Exception:
        return False
    lowered = text.lower()
    for topic_name in TOPIC_NAME_TO_NUMBER:
        if topic_name.lower() in lowered:
            return True
    return False


# Affirmative phrase containment that is normalized and may have casual extras
def _contains_affirmative_phrase(normalized):
    """
    True when a known multi-word yes phrase appears as whole words,
    and any extra words are only casual fillers (dude/bro/man...).

    Word rule — no scoring involved.
    Matches:  'of course! dude'  ('of course' + filler 'dude')
    Skips:    'teach me variables' ('teach me' + topic word → not yes)
    """
    if not normalized:
        return False

    padded = f" {normalized} "
    for phrase in _YES_CONTAIN_PHRASES:
        marker = f" {phrase} "
        if marker not in padded:
            continue

        leftover = padded.replace(marker, ' ', 1).split()
        if not leftover:
            return True
        if all(word in _CASUAL_FILLERS for word in leftover):
            return True

    return False


# "teach me (this)" = yes for the current topic; "teach me lists" = a topic switch
def _teach_request_means_yes(normalized):
    """
    Treat 'teach me' style confirmations as yes for the current topic.

    Matches the intent of the learner (assistant-level):
      teach me / teach me! / please teach me / can you teach me /
      teach me this / teach me about this
    Does NOT steal topic switches like 'teach me lists'.
    """
    if not normalized:
        return False

    if _user_said_no(normalized) or _skip_phrase_wins(normalized):
        return False

    if _names_other_topic(normalized):
        return False

    text = normalized
    for prefix in _TEACH_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
            break

    words = text.split()
    if len(words) >= 2 and words[0] == 'teach' and words[1] == 'me':
        rest = ' '.join(words[2:]).strip()
        if rest in _TEACH_OK_REST:
            return True
        if all(
            word in _CASUAL_FILLERS or word in _TEACH_OK_REST or word in {'about', 'the'}
            for word in words[2:]
        ):
            return True

    # "i want you to teach me", "go ahead and teach me"
    if 'teach me' in text:
        after = text.split('teach me', 1)[1].strip()
        if not after or after in _TEACH_OK_REST:
            return True
        if all(word in _CASUAL_FILLERS or word in _TEACH_OK_REST for word in after.split()):
            return True

    return False


# An exit command that is normalized and may have casual extras: "exit bro!", "bye man", "quit please"
def _is_exit_command(normalized):
    """True when the line is an exit command (exact set or first word)."""
    if not normalized:
        return False

    if normalized in EXIT_SET:
        return True

    # Exact short aliases that must not fire as first-word on longer lines
    if normalized in {'e', 'exit', 'quit', 'bye', 'leave', 'goodbye'}:
        return True

    words = normalized.split()
    first_word = words[0]
    if first_word not in _EXIT_FIRST_WORDS:
        return False
    if len(words) == 1:
        return True
    # Multi-word: only an exit if every following word is a casual filler
    # or another exit word itself (e.g. "exit now", "bye bye").
    # "stop using print" -> "using"/"print" are not fillers -> not an exit.
    return all(
        word in _CASUAL_FILLERS or word in _EXIT_FIRST_WORDS
        for word in words[1:]
    )


# Short yes/no/exit/defer-style answer - skips full intent detection
def _looks_like_simple_answer(input_text):
    """
    True when the line is probably just yes/no/exit/defer.

    Used so we do not run full intent detection (and its error prints)
    on short answers like 'yes!' or 'of course! dude'.
    """
    cleaned = _normalize_answer(input_text)

    if not cleaned:
        return True

    if cleaned in YES_SET or cleaned in NO_SET or cleaned in EXIT_SET or cleaned in DEFER_SET:
        return True

    # Casual yes with extras: 'of course dude', 'of course! bro'
    if _contains_affirmative_phrase(cleaned):
        return True

    # 'Teach me' / 'please teach me' — short confirmations, not topic menus
    if _teach_request_means_yes(cleaned):
        return True

    words = cleaned.split()

    if _is_exit_command(cleaned):
        return True

    if len(words) > 6:
        return False

    for word in words:
        if word in SIMPLE_TOKENS:
            return True

        # Typos: yess / yessss, yeahh, yaaa — not a topic switch
        if word.startswith('yes') or word.startswith('yep') or word.startswith('yeah'):
            return True

        if word.startswith('no') and len(word) <= 6:
            return True

        if word.startswith('cours'):  # course / courses
            return True

    return False


# Determine if a line mixes yes-like and no-like signals.
def _is_mixed_yes_no(input_text):
    """
    True when the line mixes yes-like and no-like signals.

    Examples: 'yes maybe no', 'maybe yes no' — ask, do not skip or continue.
    A clear decline with extra words ('nope right now') is NOT mixed.
    """
    has_uncertain = any(token in input_text for token in _UNCERTAIN_TOKENS)
    words = set(input_text.split())

    explicit_yes = any(
        word in words
        for word in ('yes', 'yeah', 'yep', 'yup', 'sure', 'ok', 'okay', 'y')
    )
    explicit_no = any(
        word in words
        for word in ('no', 'nope', 'nah', 'naw', 'n')
    )

    # Clear no (nope/no) without a yes word → treat as decline, not mixed
    if explicit_no and not explicit_yes:
        return False

    # Uncertain + both yes and no words ("yes maybe no")
    if has_uncertain and explicit_yes and explicit_no:
        return True

    # Both words present ("yes and no") even without maybe
    if explicit_yes and explicit_no:
        return True

    # A score alone never makes a mixed answer; only explicit words do ("nope right" vs "right on")
    return False


# Ask the learner what they meant when yes and no are mixed.
def _print_mixed_clarify():
    """Ask the learner what they meant when yes and no are mixed."""
    print("\n🤔 I want to get this right — I heard both yes and no.")
    print("   • Type 'yes' to continue with this topic")
    print("   • Type 'no' or 'skip' to move on")
    print("   • Type 'not now' if you want to pause")


# Best smart_validators score of an answer against a phrase set
def _best_similarity(user_text, phrase_set):
    """Highest smart_validators score of user_text against any phrase in phrase_set."""
    user_keywords = _extract_keywords(user_text)

    return max(
        (
            smart_validators(user_text, phrase, user_keywords, _extract_keywords(phrase))
            for phrase in phrase_set
        ),
        default=0.0,
    )

# ==========================================================
# GENERAL YES / NO / DEFER / EXIT VALIDATION
# ==========================================================

def get_global_valid_input(prompt):
    """
    Ask for a yes / no / defer / exit answer and validate it.

    Returns:
        'yes', 'no', 'defer', 'exit', or a topic name if the learner
        asked to switch topics mid-prompt.
    """
    while True:
        raw_input = input(prompt).strip().lower()

        # Session style observer — derived counters only, raw text is never stored
        try:
            from conversation_context import context as _session_context
            _session_context.observe_input(raw_input)
        except Exception:
            pass

        normalized = _normalize_answer(raw_input)

        # Fast path: exact match (punctuation already stripped)
        if normalized in YES_SET:
            return 'yes'

        if normalized in NO_SET:
            return 'no'

        if normalized in EXIT_SET:
            return 'exit'

        if normalized in DEFER_SET:
            return 'defer'

        # "stop using print" is not an exit — ask, do not throw the session away
        _exit_words = normalized.split()
        if (
            _exit_words
            and _exit_words[0] in _EXIT_FIRST_WORDS
            and len(_exit_words) > 1
            and not all(
                word in _CASUAL_FILLERS or word in _EXIT_FIRST_WORDS
                for word in _exit_words[1:]
            )
        ):
            print("\n🤔 I heard stop/end/leave — I do not want to guess.")
            print("   • Type 'exit' to leave")
            print("   • Type 'yes' to continue this topic")
            print("   • Or rephrase what you meant (for example about print)")
            continue

        # "exit man!", "bye bro", "exit bro!" — exit command with casual extras
        if _is_exit_command(normalized):
            return 'exit'

        # Clear skip instruction wins over casual yes ("yeah man! skip the topic")
        if _skip_phrase_wins(normalized):
            return 'no'

        # Known yes phrase inside extra words, e.g. of course! dude -> yes
        # e.g. "of course! dude..." contains "of course" → yes
        if not _user_said_no(normalized) and _contains_affirmative_phrase(normalized):
            return 'yes'

        # "Teach me" at a yes/no teach prompt = yes for the current topic
        if _teach_request_means_yes(normalized):
            return 'yes'

        # Mid-prompt topic switch / memory — only when this is not a simple answer
        if not _looks_like_simple_answer(normalized):
            from pytalon_body.intent_engine import detect_conversation_intent

            requested = detect_conversation_intent(raw_input)

            # Learner asked what we remember mid-prompt — print report, then re-ask
            if requested.get('intent') == 'memory_request':
                try:
                    from Pytalon_Memory.memory_store import handle_memory_ask
                    handle_memory_ask(raw_input.lower())
                except Exception:
                    print("\nI could not open saved memory right now — try again in a moment.")
                continue

            # Rename request mid-prompt ("call me Ahmed") — save name, re-ask
            try:
                from Pytalon_Memory.memory_store import try_extract_rename
                new_name = try_extract_rename(raw_input)
            except Exception:
                new_name = None
            if new_name:
                try:
                    from Pytalon_Memory.memory_store import rename_learner
                    _profile, message = rename_learner(new_name)
                    print(f"\n{message}")
                except Exception:
                    print("\nI could not save that name right now — try again.")
                continue

            if requested.get('intent') == 'memory_manage':
                print(
                    "\nI only autosave name and progress on this computer. "
                    "Say \"what do you remember?\" to view them."
                )
                continue

            if requested['intent'] == 'topic_request' and requested.get('topic'):
                switch_raw = input(
                    f"\n No problem! Want to switch to {requested['topic']} instead? (yes/no): "
                ).strip().lower()
                switch_norm = _normalize_answer(switch_raw)

                if switch_norm in YES_SET or _contains_affirmative_phrase(switch_norm):
                    context.set_pending_topic(requested['topic'])
                    return requested['topic']

                continue

        # Score the answer against each set
        compare_text = normalized or raw_input
        best_yes = _best_similarity(compare_text, YES_SET)
        best_no = _best_similarity(compare_text, NO_SET)
        best_exit = _best_similarity(compare_text, EXIT_SET)
        best_defer = _best_similarity(compare_text, DEFER_SET)

        threshold = MATCH_THRESHOLD
        user_negated = _user_said_no(compare_text)

        # Mixed yes + no (e.g. "yes maybe no") — clarify and wait for a clear answer
        if _is_mixed_yes_no(compare_text):
            _print_mixed_clarify()
            continue

        # Clear decline with extra words: "nope right now", "nope right no"
        compare_words = set(compare_text.split())
        explicit_yes_word = compare_words & {'yes', 'yeah', 'yep', 'yup', 'ok', 'okay', 'sure'}
        if ('nope' in compare_words or 'nah' in compare_words) and not explicit_yes_word:
            return 'no'

        # Defer wins when it clearly beats the other answers
        if (
            best_defer >= threshold
            and best_defer > best_yes
            and best_defer > best_no
            and best_defer > best_exit
        ):
            return 'defer'

        # Tie between yes and no: negation tips it to no
        if best_yes >= threshold and best_no >= threshold and best_yes == best_no:
            if user_negated:
                return 'no'
            return 'yes'

        if best_yes >= threshold and best_yes > best_no and best_yes > best_exit:
            if user_negated:
                return 'no'
            return 'yes'

        if best_no >= threshold and best_no > best_exit and best_no > best_yes:
            return 'no'

        if best_exit >= threshold and best_exit > best_yes and best_exit > best_no:
            return 'exit'

        print("🤔 I didn't quite get that. Please answer with 'yes', 'no', or 'exit'.")


# ==========================================================
# MENU CHOICE VALIDATION
# ==========================================================


# Ask for a topic number (1-13) or exit.
def get_global_menu_choice(prompt, min_val=1, max_val=13):
    """
    Ask for a topic number (or exit).

    Returns:
        The chosen number as a string, or 'exit'.
    """
    while True:
        choice = input(prompt).strip().lower()

        # Session style observer — derived counters only, raw text is never stored
        try:
            from conversation_context import context as _session_context
            _session_context.observe_input(choice)
        except Exception:
            pass

        choice_norm = _normalize_answer(choice)

        # Exact aliases + casual extras: "exit bro!", "bye man", "quit please"
        if choice in ('exit', 'e', 'quit', 'bye', 'leave') or _is_exit_command(choice_norm):
            return 'exit'

        if choice and not choice.isdigit() and not _looks_like_simple_answer(choice):
            from pytalon_body.intent_engine import detect_conversation_intent
            memory_intent = detect_conversation_intent(choice)

            if memory_intent.get('intent') == 'memory_request':
                try:
                    from Pytalon_Memory.memory_store import handle_memory_ask
                    handle_memory_ask(choice)
                except Exception:
                    print("\nI could not open saved memory right now — try again in a moment.")
                continue

            if memory_intent.get('intent') == 'memory_manage':
                print(
                    "\nI only autosave name and progress on this computer. "
                    "Say \"what do you remember?\" to view them."
                )
                continue

        if not choice:
            print(
                f"📝 Just type a number from {min_val} to {max_val} "
                f"to pick a topic, or 'exit' to leave!"
            )
            continue

        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return choice

        print(f"📝 That's not a topic number! Pick {min_val}-{max_val}, or type 'exit'.")


# ==========================================================
# QUESTION-PHASE YES / NO / EXIT VALIDATION
# ==========================================================


# Ask yes / no / exit during the question phase.
def get_global_user_question_valid_input(prompt):
    """
    Ask whether the learner has a question (yes / no / exit).

    Returns:
        'yes', 'no', or 'exit'.
    """
    while True:
        raw_input = input(prompt).strip().lower()

        # Session style observer — derived counters only, raw text is never stored
        try:
            from conversation_context import context as _session_context
            _session_context.observe_input(raw_input)
        except Exception:
            pass

        normalized = _normalize_answer(raw_input)

        if normalized in YES_QUESTION_SET:
            return 'yes'

        if normalized in NO_QUESTION_SET:
            return 'no'

        if normalized in EXIT_QUESTION_SET:
            return 'exit'

        if _skip_phrase_wins(normalized):
            return 'no'

        compare_text = normalized or raw_input
        best_yes = _best_similarity(compare_text, YES_QUESTION_SET)
        best_no = _best_similarity(compare_text, NO_QUESTION_SET)
        best_exit = _best_similarity(compare_text, EXIT_QUESTION_SET)

        threshold = MATCH_THRESHOLD

        if _is_mixed_yes_no(compare_text):
            _print_mixed_clarify()
            continue

        if best_yes >= threshold and best_yes > best_no and best_yes > best_exit:
            if _user_said_no(compare_text):
                return 'no'
            return 'yes'

        if best_no >= threshold and best_no > best_exit:
            return 'no'

        if best_exit >= threshold:
            return 'exit'

        print("🤔 I didn't quite get that. Please answer with 'yes', 'no', or 'exit'.")


# ==========================================================
# EXAMPLES-PHASE YES / NO VALIDATION
# ==========================================================


# Ask yes / no at the examples prompts.
def get_global_examples_valid_input(prompt):
    """
    Ask whether the learner wants code examples (yes / no).

    Returns:
        'yes' or 'no'.
    """
    while True:
        raw_input = input(prompt).strip().lower()

        # Session style observer — derived counters only, raw text is never stored
        try:
            from conversation_context import context as _session_context
            _session_context.observe_input(raw_input)
        except Exception:
            pass

        normalized = _normalize_answer(raw_input)

        if normalized in YES_EXAMPLES_SET:
            return 'yes'

        if normalized in NO_EXAMPLES_SET:
            return 'no'

        if _skip_phrase_wins(normalized):
            return 'no'

        # Memory and question intents are answered before yes/no scoring runs
        if raw_input:
            try:
                from pytalon_body.intent_engine import detect_conversation_intent
                mem_intent = detect_conversation_intent(raw_input)
                if mem_intent.get('intent') == 'memory_request':
                    try:
                        from Pytalon_Memory.memory_store import handle_memory_ask
                        handle_memory_ask(raw_input)
                    except Exception:
                        print("\nI could not open saved memory right now — try again in a moment.")
                    continue
            except Exception:
                pass

        compare_text = normalized or raw_input
        best_yes = _best_similarity(compare_text, YES_EXAMPLES_SET)
        best_no = _best_similarity(compare_text, NO_EXAMPLES_SET)

        threshold = EXAMPLES_MATCH_THRESHOLD
        user_negated = _user_said_no(compare_text)

        if _is_mixed_yes_no(compare_text):
            _print_mixed_clarify()
            continue

        if best_yes >= threshold and best_yes > best_no:
            if user_negated:
                return 'no'
            return 'yes'

        if (
            best_yes >= threshold
            and best_no >= threshold
            and best_yes == best_no
            and not user_negated
        ):
            return 'yes'

        if best_no >= threshold:
            if user_negated or best_no > best_yes:
                return 'no'

        print("🤔 I didn't quite get that. Please answer with 'yes' or 'no'.")


# ==========================================================
# ACTUAL QUESTION TEXT VALIDATION
# ==========================================================


# Ask for the real question text (not a yes / no answer).
def get_global_question_content_input(prompt):
    """
    Ask for the learner's real question text (not a yes/no).

    Returns:
        The question string (at least 10 characters).
    """
    while True:
        question = input(prompt).strip()

        if not question:
            print("👋 I'm all ears! What's your Python question?")
            continue

        question_lower = question.lower()

        if question_lower in SIMPLE_RESPONSES:
            print(
                "🤔 That sounds like a yes/no answer! "
                "I need an actual question — what do you want to know about Python?"
            )
            continue

        if len(question) >= 10:
            return question

        print("\n🤔 That's a bit short! Try a complete question like:")
        print("   • 'Can you teach me Python?'")
        print("   • 'How do I learn variables?'")
        print("   • 'What is a function?'")
        print()


# ==========================================================
# BEHAVIOR OBSERVATION WRAPPERS
# ==========================================================

# Wrap the global validators so every FINAL answer feeds the behavior observer exactly once.
def _with_answer_observation(fn):

    # Return a validator wrapper that records the final answer kind (patterns only).

    def wrapper(prompt, *args, **kwargs):

        answer = fn(prompt, *args, **kwargs)

        try:

            from conversation_context import context as _session_context

            if answer in ("yes", "no", "defer", "exit"):

                _session_context.note_event("answer_" + str(answer))

        except Exception:

            pass

        return answer

    return wrapper


# All global validators are wrapped so the session observer sees the final answer kind.
get_global_valid_input = _with_answer_observation(get_global_valid_input)

get_global_menu_choice = _with_answer_observation(get_global_menu_choice)

get_global_user_question_valid_input = _with_answer_observation(get_global_user_question_valid_input)

get_global_examples_valid_input = _with_answer_observation(get_global_examples_valid_input)