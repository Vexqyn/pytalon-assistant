# utils.py
"""Shared utility functions for Pytalon (menus, practice, custom matching)."""

import io
import sys
import difflib

from config import (
    FILLER_WORDS,
    NEGATION_WORDS,
    COMMON_SHORT_WORDS,
    COMMAND_PREFIXES,
    PRACTICE_INPUT_RESPONSES,
)

# ============================================================
# NEGATION HANDLING — keep "no" from scoring like "yes"
# ============================================================

# Single words vs multi-word phrases both count as negation cues
_SINGLE_NEGATIONS = {word for word in NEGATION_WORDS if " " not in word}
_MULTI_NEGATIONS = {phrase for phrase in NEGATION_WORDS if " " in phrase}

def _text_has_negation(text):
    """True if text contains an explicit negation cue."""
    lowered = text.lower()
    words = set(lowered.split())

    if words & _SINGLE_NEGATIONS:
        return True

    return any(phrase in lowered for phrase in _MULTI_NEGATIONS)

# Cap score when the lesson says no but the learner did not negate
def _apply_negation_cap(score, user_text, reference_text):
    """Lower score when the reference is negative but the user did not negate."""
    if _text_has_negation(reference_text) and not _text_has_negation(user_text):
        return min(score, 0.5)

    return score

# ============================================================
# GLOBAL SEPARATOR
# ============================================================

# Visual break between teaching sections
def print_global_separator():
    """Prints a visual separator line for better readability."""
    global_separator = "\n" + "=" * 50
    print(global_separator, flush=True)

# ============================================================
# CODE PRACTICE SYSTEM
# ============================================================

# Exact end markers (and close typos) so "Don" does not hang practice
_CODE_END_TOKENS = {
    'DONE', 'DON', 'DUN', 'DN', 'DONW', 'DOME', 'DNOE', 'DONEE', 'DONED',
    'FIN', 'FINISH', 'FINNISH', 'FINSIH', 'END', 'STOP', 'QUIT',
    'OK', 'OKAY', 'THATS ALL', "THAT'S ALL", 'SUBMIT', 'SEND',
}

# Check if the learner's input line indicates they are finished entering code.
def _is_code_end_marker(line):
    """
    True when the learner means 'I'm finished entering code'.

    Accepts DONE and common typos (Don, Dun, Fin, ...) so practice
    does not hang waiting for a perfect DONE.
    """
    cleaned = line.strip().upper().rstrip('!?.',)

    if not cleaned:
        return False

    if cleaned in _CODE_END_TOKENS:
        return True

    # Close variants of DONE / DON
    if cleaned.startswith('DON') or cleaned.startswith('DUN'):
        return True

    if cleaned.startswith('DONE'):
        return True

    if cleaned in ('DO', 'D'):
        # Too short — might be real code; do not end
        return False

    return False

# Get multiple lines of Python code from the user, ending with 'DONE' or a close typo.
def get_multiline_code_input():
    """
    Get multiple lines of Python code from the user.

    The learner types code line by line, then types 'DONE' (or a close
    typo like 'Don') to finish.

    Returns:
        A string containing all the code lines joined with newlines.
    """
    if sys.stdin.closed:
        print("⚠️ Input stream is closed. Restarting practice session...", flush=True)
        return ""

    print(
        "\n📝 ENTER YOUR PYTHON CODE (type 'DONE' on a new line when finished; "
        "'Don'/'Dun' also work if you typo):",
        flush=True,
    )
    print_global_separator()

    code_lines = []

    try:
        while True:
            line = input()

            if _is_code_end_marker(line):
                token = line.strip().upper().rstrip('!?.',)

                if token != 'DONE':
                    print("   ✓ Got it — treating that as DONE.", flush=True)

                break

            code_lines.append(line)

    except EOFError:
        print(
            "\n⚠️ It's not your fault input ended unexpectedly, using entered code...",
            flush=True,
        )

    return "\n".join(code_lines)

# A simple check for common infinite-loop patterns in the code, to prevent runaway loops during practice.
def _find_infinite_loop_pattern(code):
    """Return the first infinite-loop pattern found in code, or None."""
    infinite_loop_patterns = [
        'while True',
        'while 1',
        'while(True)',
        'while(1)',
        'while (True)',
        'while (1)',
        'while 1==1',
        'while 1 == 1',
    ]

    code_lower = code.lower()

    for pattern in infinite_loop_patterns:
        if pattern.lower() in code_lower:
            return pattern

    return None

# Build a safe namespace for executing learner code, blocking exit() and quit(), and providing canned input responses.
def _build_practice_namespace():
    """
    Build a safe namespace for learner code.

    Blocks exit()/quit() and feeds canned answers to input() so the
    real terminal is never read during practice.
    """
    def _blocked_exit(*args, **kwargs):
        raise Exception("exit() is not allowed in practice exercises")

    def _blocked_quit(*args, **kwargs):
        raise Exception("quit() is not allowed in practice exercises")

    practice_input_values = list(PRACTICE_INPUT_RESPONSES)

    def _practice_input(prompt=""):
        print(prompt, end="")

        if practice_input_values:
            return practice_input_values.pop(0)

        return PRACTICE_INPUT_RESPONSES[-1] if PRACTICE_INPUT_RESPONSES else ''

    return {
        'exit': _blocked_exit,
        'quit': _blocked_quit,
        'input': _practice_input,
    }

# A step limit trace function to prevent runaway loops during code execution.
def _make_step_limit_trace(step_limit=200000):
    """Create a sys.settrace callback that stops runaway loops."""
    step_count = 0

    def _step_limit_trace(frame, event, arg):
        nonlocal step_count

        if event == 'line':
            step_count += 1

            if step_count > step_limit:
                raise Exception(
                    "Your code ran too many steps and was stopped — this usually "
                    "means an infinite loop (for example 'while x:' where x never "
                    "changes). Check your loop condition!"
                )

        return _step_limit_trace

    return _step_limit_trace

# Check for required keywords in the code and return an error message if any are missing.
def _check_expected_keywords(code, expected_keywords):
    """Return an error message if any required keyword is missing, else ''."""
    if not expected_keywords:
        return ''

    missing_keywords = []
    for keyword in expected_keywords:
        if not _keyword_token_found(keyword, code):
            missing_keywords.append(keyword)

    if missing_keywords:
        return f"Missing required elements: {', '.join(missing_keywords)}"

    return ''

# Found a keyword as a standalone token (not part of a longer token) in the code.
def _keyword_token_found(keyword, code):
    """True when keyword appears as a token (not a substring of a longer token).

    For single-character operators like '>', this prevents matching inside '>='.
    For multi-character operators like '>=', this allows them to be found even
    when shorter operators like '>' exist nearby — since we match the longest
    tokens first when sorting expected_keywords.

    A keyword whose own last character is non-alphanumeric and structural
    (like '(' in 'type(' or ' ' in 'def ') uses that character as its own
    trailing boundary. A keyword starting with '.' allows an alnum char
    before it (method-call context: 'lst.append()').
    """
    kw_lower = keyword.lower()
    code_lower = code.lower()
    kw_len = len(kw_lower)

    # Keyword starts with '.' — allow alnum before it (method calls).
    kw_starts_with_dot = kw_len > 0 and kw_lower[0] == '.'

    # Keyword ends with a structural non-alnum char ('(', ' ', etc.) —
    # that char is its own trailing boundary; we only check the char before.
    kw_trailing_is_boundary = (
        kw_len > 0
        and not (kw_lower[-1].isalnum() or kw_lower[-1] == '_')
    )

    pos = 0
    while True:
        pos = code_lower.find(kw_lower, pos)
        if pos == -1:
            return False

        # --- before boundary ---
        if pos == 0:
            before_ok = True
        else:
            before_char = code_lower[pos - 1]
            if kw_starts_with_dot:
                # '.append(' may follow an alnum object name like 'lst.'
                before_ok = True
            elif kw_trailing_is_boundary and kw_len == 1:
                # Single-char operator ('=', '>', '<', ...): a neighbouring
                # operator char means this is part of a compound ('==', '>=',
                # '+=', '!=') - the second '=' of '==' is not a standalone '='.
                before_ok = (
                    not (before_char.isalnum() or before_char == '_')
                    and before_char not in '=<>+-*/%!&|^~'
                )
            else:
                before_ok = not (
                    before_char.isalnum() or before_char == '_'
                )

        # --- after boundary ---
        after_pos = pos + kw_len
        if after_pos >= len(code_lower):
            after_ok = True
        else:
            after_char = code_lower[after_pos]
            if kw_trailing_is_boundary and kw_len == 1:
                # Single-char non-alnum keyword (e.g. '>', '<', '=', '+', etc.).
                # The char after must NOT be another operator character, otherwise
                # this keyword is part of a compound (e.g. '>' inside '>=').
                if after_char.isalnum() or after_char == '_':
                    after_ok = True
                elif after_char in (
                    ' ', '\t', '\n',
                    '(', ')', '[', ']', '{', '}',
                    ',', ';', ':', '"', "'", '.',
                ):
                    after_ok = True
                else:
                    # Another operator char (like '=' after '>', or '+' after '+')
                    # — this keyword is inside a compound, reject it.
                    after_ok = False
            elif kw_trailing_is_boundary:
                # Multi-char keyword ending with structural char
                # (e.g. 'type(', 'def ', 'print(') — that char is the boundary.
                after_ok = True
            else:
                after_ok = not (
                    after_char.isalnum() or after_char == '_'
                )

        if before_ok and after_ok:
            return True
        pos += 1
    return False

# Check for forbidden keywords in the code and return an error message if any are found.
def _check_forbidden_keywords(code, forbidden_keywords):
    """Return an error message if any forbidden keyword is present, else ''."""
    if not forbidden_keywords:
        return ''

    found_forbidden = [
        keyword
        for keyword in forbidden_keywords
        if keyword.lower() in code.lower()
    ]

    if found_forbidden:
        return f"Please don't use: {', '.join(found_forbidden)}"

    return ''

# Execute the user's code in a safe namespace, check for required and forbidden keywords, and return the result.
def execute_and_check_code(code, expected_keywords=None, forbidden_keywords=None):
    """
    Safely execute the user's Python code and check for required elements.

    Parameters:
        code: The Python code string to execute
        expected_keywords: Keywords that MUST appear in the code
        forbidden_keywords: Keywords that must NOT appear in the code

    Returns:
        (success, output, error_message)
            success — True if code ran and passed all checks
            output  — What the code printed (if anything)
            error_message — Description of any problems found
    """
    success = True
    error_message = ""
    output = ""

    # Block infinite loops before stdout is redirected
    detected_pattern = _find_infinite_loop_pattern(code)

    if detected_pattern:
        success = False
        error_message = (
            f"⚠️ Infinite loops are not allowed in practice mode "
            f"(detected: {detected_pattern})"
        )
        return success, output, error_message

    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    try:
        namespace = _build_practice_namespace()
        step_limit_trace = _make_step_limit_trace()
        sys.settrace(step_limit_trace)

        exec(code, namespace)
        output = captured_output.getvalue()

        missing_error = _check_expected_keywords(code, expected_keywords)

        if missing_error:
            success = False
            error_message = missing_error

        forbidden_error = _check_forbidden_keywords(code, forbidden_keywords)

        if forbidden_error:
            success = False
            error_message = forbidden_error

    except SyntaxError as e:
        success = False
        error_message = f"Syntax Error: {str(e)}"

    except SystemExit:
        success = False
        error_message = "⚠️ Code attempted to exit. Please don't use exit() in practice."

    except Exception as e:
        success = False
        error_message = f"Error: {str(e)}"

    finally:
        sys.stdout = old_stdout
        sys.settrace(None)
        captured_output.close()

    return success, output, error_message

# Show the success banner after a correct practice attempt, including any output.
def _show_practice_success(output):
    """Print the success banner after a correct practice attempt."""
    print_global_separator()
    print("✅ PERFECT! Your code is correct!", flush=True)

    if output:
        print(f"\n📤 YOUR OUTPUT:", flush=True)
        print(output, flush=True)

    print(f"\n💡 Code structure and elements are correct!", flush=True)
    print("✅ Practice complete! You can continue to the next topic.", flush=True)
    print_global_separator()

# Handle a failed practice attempt, showing the error and deciding what to do next.
def _handle_practice_failure(error_message, attempts, max_attempts):
    """
    Show a failed attempt and decide what to do next.

    Returns:
        'retry'     — ask for another attempt
        'reset'     — clear attempt count and keep going
        'skip'      — leave the practice session
        'exit'      — leave the practice session with a goodbye
    """
    print_global_separator()
    print(f"❌ Not quite right! {error_message}", flush=True)

    if attempts >= max_attempts:
        from validators import get_global_valid_input

        retry = get_global_valid_input(
            "\n🔹 You've tried several times. Try again? (yes/no): "
        )

        if retry == 'yes':
            return 'reset'

        if retry == 'exit':
            print("👋 Exiting practice session. See you next time!", flush=True)
            return 'exit'

        print("✅ Skipping practice. You can always come back later!", flush=True)
        return 'skip'

    print(f"\n🔄 Attempt {attempts}/{max_attempts}. Please try again!", flush=True)
    print_global_separator()
    return 'retry'

# Practice session flow: show instructions, get code, validate, repeat until success or exit
def run_practice_session(
    topic_name,
    instructions,
    expected_keywords,
    example_code,
    custom_check_function=None,
):
    """
    Run a complete interactive practice session for a specific topic.

    Flow:
        1. Show instructions and example
        2. Get the learner's code
        3. Execute and validate the code
        4. If correct — show success
        5. If wrong — show error and let the learner try again

    Parameters:
        topic_name            Display name of the topic (e.g., "Variables")
        instructions          What the learner needs to do
        expected_keywords     Keywords that must appear in the code
        example_code          A working example to show the learner
        custom_check_function Optional extra validation function
    Returns:
        True if the learner completed the practice successfully,
        False if they skipped or exited without completing it.
    """
    print_global_separator()
    print(f"🧪 INTERACTIVE PRACTICE: {topic_name}", flush=True)
    print_global_separator()

    print(f"\n📋 TASK:", flush=True)
    print(instructions, flush=True)

    print(f"\n💡 EXAMPLE SOLUTION:", flush=True)
    print(f"{example_code}", flush=True)

    print(f"\n🔑 Required elements: {', '.join(expected_keywords)}", flush=True)

    attempts = 0
    max_attempts = 3

    try:
        from Pytalon_Memory.conversation_context import context as _session_context
        _session_context.note_event("practice_start")
    except Exception:
        pass

    while True:
        user_code = get_multiline_code_input()

        if not user_code.strip():
            print("⚠️  Please enter some Python code!", flush=True)
            continue

        success, output, error_message = execute_and_check_code(
            user_code,
            expected_keywords=expected_keywords,
        )

        if success and custom_check_function:
            success, error_message = custom_check_function(user_code, output)

        # Remember practice result so "what do you remember?" can show it
        if success:
            try:
                from Pytalon_Memory.conversation_context import context as _session_context
                _session_context.note_event("practice_pass")
            except Exception:
                pass
            _show_practice_success(output)
            try:
                from Pytalon_Memory.memory_store import remember_practice, remember_topic_completed, build_topic_saved_summary
                remember_practice(topic_name, True)
                remember_topic_completed(topic_name)
                recap = build_topic_saved_summary(topic_name)
                if recap:
                    print(recap)
            except Exception:
                pass
            return True

        attempts += 1
        next_action = _handle_practice_failure(error_message, attempts, max_attempts)

        if next_action in ('skip', 'exit'):
            try:
                from Pytalon_Memory.conversation_context import context as _session_context
                _session_context.note_event("practice_fail")
            except Exception:
                pass
            try:
                from Pytalon_Memory.memory_store import remember_practice
                remember_practice(topic_name, False)
            except Exception:
                pass
            return False

        if next_action == 'reset':
            attempts = 0

# ============================================================
# MENU DISPLAY
# ============================================================

def show_topic_menu(topics, prompt="Which topic would you like to start with?"):
    """
    Display the full topic list and return the chosen number (string) or 'exit'.
    """
    from validators import get_global_menu_choice  # late import: avoids circular dependency

    print_global_separator()
    print("I can teach you Python basics! Here are the topics:", flush=True)
    print_global_separator()

    for num, topic in topics.items():
        print(f"   {num}. {topic}", flush=True)

    return get_global_menu_choice(
        f"\n🔹 {prompt} (1-13/exit): ",
        1,
        len(topics),
    )

# ============================================================
# SMART DETECTION — for user input vs String matching
# ============================================================

def smart_detection(s1, s2):
    """
    Compare two strings and return a similarity score between 0 and 1.

    Checks for:
        - Sub-string containment
        - Full-string similarity
        - Each word of s1 against s2 and vice-versa
        - Word-order reversal
        - All words of one string present in the other (subset match)
    """
    if not s1 or not s2:
        return 0.0

    s1 = s1.lower().strip()
    s2 = s2.lower().strip()

    # Containment on whole tokens/phrases so 'if' does not match 'life'
    s1_padded = ' ' + ' '.join(s1.split()) + ' '
    s2_padded = ' ' + ' '.join(s2.split()) + ' '

    if s1_padded in s2_padded or s2_padded in s1_padded:
        return 1.0

    words1 = set(s1.split())
    words2 = set(s2.split())

    if words2 and words2.issubset(words1):
        return 1.0

    if words1 and words1.issubset(words2):
        return 1.0

    best = difflib.SequenceMatcher(None, s1, s2).ratio()

    for word in s1.split():
        score = difflib.SequenceMatcher(None, word, s2).ratio()

        if score > best:
            best = score

    for word in s2.split():
        score = difflib.SequenceMatcher(None, word, s1).ratio()

        if score > best:
            best = score

    if " " in s2:
        reversed_s2 = " ".join(reversed(s2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_s2).ratio()

        if score > best:
            best = score

    return best

# ============================================================
# SMART VALIDATORS — for user input vs lesson content
# ============================================================

def smart_validators(s1, s2, w1, w2):
    """
    Validate the user's input based on smart detection logic.

    Parameters:
        s1 — User's input string
        s2 — Reference string to compare against
        w1 — Extracted keywords from the user's input
        w2 — Extracted keywords from the reference string

    Returns:
        A similarity score between 0 and 1, with adjustments for negation cues.

    The function performs multiple checks:
        1. Direct containment of one string in the other.
        2. Subset match where all keywords of one string appear in the other.
        3. Full-string similarity using difflib.
        4. Word-by-word comparisons for both main strings and keywords.
        5. Handling of swapped word order.
        6. Adjusting the final score when negation cues appear in the
           reference but not in the user's input.
    """
    s1 = s1.lower().strip()
    s2 = s2.lower().strip()

    w1 = w1.lower().strip()
    w2 = w2.lower().strip()

    # Filter common short words so they cannot force a false positive
    s1_clean = {w for w in _extract_keywords(s1).split() if w not in COMMON_SHORT_WORDS}
    s2_clean = {w for w in _extract_keywords(s2).split() if w not in COMMON_SHORT_WORDS}
    w1_words = {w for w in w1.split() if w not in COMMON_SHORT_WORDS}
    w2_words = {w for w in w2.split() if w not in COMMON_SHORT_WORDS}

    min_overlap = 2

    overlap1 = len(s1_clean & s2_clean)
    overlap2 = len(w1_words & w2_words)
    overlap3 = len(s1_clean & w2_words)
    overlap4 = len(w1_words & s2_clean)

    # Strong match: enough overlap in both main strings AND keyword sets
    if (
        (overlap1 >= min_overlap or overlap2 >= min_overlap)
        and (overlap3 >= min_overlap or overlap4 >= min_overlap)
    ):
        return _apply_negation_cap(1.0, s1, s2)

    # Weaker match: at least 1 overlap in each
    if (overlap1 >= 1 or overlap2 >= 1) and (overlap3 >= 1 or overlap4 >= 1):
        return _apply_negation_cap(0.5, s1, s2)

    best = difflib.SequenceMatcher(None, s1, s2).ratio()

    for word in s1.split():
        score = difflib.SequenceMatcher(None, word, s2).ratio()

        if score > best:
            best = score

    for word in s2.split():
        score = difflib.SequenceMatcher(None, word, s1).ratio()

        if score > best:
            best = score

    for word_w1 in w1.split():
        score = difflib.SequenceMatcher(None, word_w1, w2).ratio()

        if score > best:
            best = score

    for word_w2 in w2.split():
        score = difflib.SequenceMatcher(None, word_w2, w1).ratio()

        if score > best:
            best = score

    if " " in s2:
        reversed_s2 = " ".join(reversed(s2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_s2).ratio()

        if score > best:
            best = score

    if " " in w2:
        reversed_w2 = " ".join(reversed(w2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_w2).ratio()

        if score > best:
            best = score

    return _apply_negation_cap(best, s1, s2)

# ============================================================
# KEYWORD EXTRACTION
# ============================================================

def _extract_keywords(text):
    """
    Extract the most intent-carrying words from a string.

    Strips common filler words and punctuation so smart_validators
    gets meaningful w1/w2.

    Returns:
        A string of the remaining words joined by spaces.
    """
    text = text.lower().strip()

    # Keep alphanumerics, spaces, and apostrophes (for don't / I'm)
    cleaned_chars = []

    for char in text:
        if char.isalnum() or char.isspace() or char == "'":
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(' ')

    cleaned = ''.join(cleaned_chars)
    words = cleaned.split()
    keywords = [word for word in words if word not in FILLER_WORDS]

    return ' '.join(keywords) if keywords else cleaned

# ============================================================
# COMMAND PREFIX CLEANUP
# ============================================================

def remove_command_prefix(text):
    """
    Remove command-style prefixes from user input.

    Handles cases like: /lists, !functions, #variables, \\loops, etc.

    Checks whether the first character is a command prefix and removes
    it along with any following whitespace. Uses COMMAND_PREFIXES from
    config.py. Custom implementation without lstrip() or strip().

    Args:
        text: The input text to clean

    Returns:
        Text with a leading command prefix removed if present
    """
    if not text or len(text) <= 1:
        return text

    first_char = text[0]
    is_command_prefix = False

    for prefix in COMMAND_PREFIXES:
        if first_char == prefix:
            is_command_prefix = True
            break

    if not is_command_prefix:
        return text

    cleaned = text[1:]
    start_index = 0

    while start_index < len(cleaned) and cleaned[start_index] == ' ':
        start_index += 1

    return cleaned[start_index:] if start_index < len(cleaned) else cleaned
