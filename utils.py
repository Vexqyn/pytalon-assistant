# utils.py
"""Shared utility functions for Pytalon (menus, practice engine, custom matching)."""

import ast
import collections
import difflib
import io
import random
import re
import string
import sys
import unicodedata
import zlib

from config import (
    FILLER_WORDS,
    NEGATION_WORDS,
    COMMON_SHORT_WORDS,
    COMMAND_PREFIXES,
    PRACTICE_INPUT_RESPONSES,
)
from static_database.practice_runtime import (
    ANSWER_TOKENS,
    BLOCKED_ATTRIBUTES,
    BLOCKED_CALLS,
    CODE_END_TOKENS,
    EXIT_PHRASES,
    EXIT_TOKENS,
    MAX_EMPTY_SUBMISSIONS,
)
from static_database.practice_specs import PRACTICE_SPECS
from static_database.small_talk import (
    COMMON_WORDS,
    EMOJI_REPLES,
    GIBBERISH_REPLIES,
    SMALL_TALK_REACTIONS,
    SMALL_TALK_FOLLOWUPS,
    SLANG_WORDS,
    STRETCH_PATTERN,
)
from static_database.validator_settings import MIN_OVERLAP

_EMOTION_MOODS = {
    'amusement': 'laughter',
    'happiness': 'casual',
    'sadness': 'sadness',
    'anger': 'anger',
    'confusion': 'confusion',
    'approval': 'approval',
    'gratitude': 'gratitude',
    'love': 'love',
    'sarcasm': 'confusion',
    'mockery': 'laughter',
    'awkwardness': 'confusion',
    'exhaustion': 'exhaustion',
    'curiosity': 'curiosity',
    'shock': 'shock',
    'confidence': 'confidence',
    'excitement': 'excitement',
}

_reply_history = collections.deque(maxlen=8)
_turn_history = collections.deque(maxlen=8)
_reply_counter = 0

# One assistant reply = one line with the 🤖 prefix. Used by every reply path.
def assistant_reply(text):
    """Print one assistant reply in the standard format: new line + 🤖 + text."""
    clean = str(text or "").strip()
    if clean.startswith("🤖"):
        clean = clean[1:].strip()
    print(f"\n🤖 {clean}", flush=True)

# Pick a reply variant by content + rotating salt, skipping repeats.
def pick_reply_variant(variants, text, salt=0):
    """Return a non-repeating reply variant from a tuple of reply strings."""
    global _reply_counter
    _reply_counter += 1
    key = f"{text}|{salt}|{_reply_counter}"
    idx = zlib.crc32(key.encode("utf-8")) % len(variants)
    reply = str(variants[idx])
    if reply in _reply_history:
        idx = (idx + 1) % len(variants)
        reply = str(variants[idx])
    _reply_history.append(reply)
    return reply

# Safely fill $name / $topic placeholders in a reply template.
def fill_reply_template(template, name="", topic="", topic_hint=""):
    """Fill reply placeholders with safe_substitute semantics."""
    filled = string.Template(str(template)).safe_substitute(
        name=name,
        topic=topic,
        topic_hint=topic_hint,
    )
    return str(filled)

# Shrink stretched words ("loooool" -> "lol").
def shrink_stretched(text):
    """Shrink stretched words so casual text matches its base word."""
    return re.sub(STRETCH_PATTERN, r"\1\1", str(text or "").strip().lower())

# True when no known word is close to the typed words (real gibberish).
def is_gibberish(text):
    """True when typed words are not near any known word (real gibberish)."""
    shrunk = shrink_stretched(text)
    words = [w for w in re.findall(r"[a-z']+", shrunk) if len(w) > 2]
    if not words:
        return True
    for word in words:
        if difflib.get_close_matches(word, list(COMMON_WORDS), n=1, cutoff=0.6):
            return False
    return True

# Words that mark a casual "chill / over it" message.
_INDIFFERENCE_WORDS = frozenset({
    'whatever', 'meh', 'idk', 'dunno', 'kinda', 'sorta', 'nahh', 'nah', 'nahh',
})

# Slang that points at light laughter in a short casual message.
_LAUGHTER_WORDS = frozenset({
    'lol', 'haha', 'hehe', 'lmao', 'rofl', 'hahaha', 'loll', 'ahoy', 'ohh', 'lolz',
})

# Small-talk reactions for a mood, as (reaction, follow-up) pairs.
def _small_talk_pairs(mood):
    pairs = SMALL_TALK_REACTIONS.get(mood) or ()
    if not pairs:
        pairs = (("I'm listening, $name. 😄", "what's on your mind?"),)
    return pairs

# Pick a reaction pair for a mood, skipping repeats, stable per content.
def _small_talk_reply(mood, text, name=""):
    pairs = _small_talk_pairs(mood)
    key = f"{mood}|{shrink_stretched(text)}"
    idx = zlib.crc32(key.encode("utf-8")) % len(pairs)
    reaction, followup = pairs[idx]
    reply = str(reaction)
    if followup:
        reply = f"{reply} {str(followup)}"

    if reply in _reply_history:
        idx = (idx + 1) % len(pairs)
        reaction, followup = pairs[idx]
        reply = str(reaction)
        if followup:
            reply = f"{reply} {str(followup)}"

    _reply_history.append(reply)
    return reply

# Build one natural small-talk reply from static parts. Returns plain text.
def build_small_talk_reply(text, profile=None, context=None, name=""):
    """
    Combine a mood reaction + optional follow-up into one small-talk reply.

    Reads the emoji emotion and slang signals, picks a reaction from the
    static data, fills the safe placeholders and avoids repeating replies.
    """
    global _reply_counter
    _reply_counter += 1

    original = str(text or "")
    shrunk = shrink_stretched(original)
    tokens = {
        word.strip("!?.,'\"")
        for word in shrunk.split()
        if word.strip("!?.,'\"")
    }

    emotion = None
    try:
        from pytalon_body.behavior_learner import read_emoji_emotion
        emotion = read_emoji_emotion(original)
    except Exception:
        emotion = None

    mood = None
    if emotion:
        mood = _EMOTION_MOODS.get(emotion, 'casual')
    elif tokens & SLANG_WORDS:
        mood = 'casual'
    elif original.strip().endswith("?"):
        mood = 'question'

    if mood is None or mood not in SMALL_TALK_REACTIONS:
        # Nothing matched a small-talk mood — real gibberish gets a friendly
        # clarifying line, everything else falls back to casual chat.
        mood = 'gibberish' if is_gibberish(original) else 'casual'

    if mood == 'gibberish':
        reply = pick_reply_variant(GIBBERISH_REPLIES, original, salt=7)
        keyboard_reply = next(
            (r for r in GIBBERISH_REPLIES if "keyboard" in str(r).lower()),
            GIBBERISH_REPLIES[0],
        )
        return fill_reply_template(keyboard_reply, name=name)

    if mood == 'casual':
        # Chill / indifference messages get the friendly "over it" reply.
        if tokens & _INDIFFERENCE_WORDS:
            pairs = _small_talk_pairs('casual')
            for reaction, followup in pairs:
                if "over it" in str(reaction).lower():
                    reply = str(reaction)
                    if followup:
                        reply = f"{reply} {str(followup)}"
                    return fill_reply_template(reply, name=name)

        # Short laughter-heavy slang ("lol bro") gets the friendly laugh reply.
        if tokens & _LAUGHTER_WORDS and len(tokens) <= 3:
            pairs = _small_talk_pairs('casual')
            for reaction, followup in pairs:
                if "what's up" in str(reaction).lower():
                    reply = str(reaction)
                    if followup:
                        reply = f"{reply} {str(followup)}"
                    return fill_reply_template(reply, name=name)

    reply = _small_talk_reply(mood, original, name=name)

    # Laughter moods ("ngl", "lol", "haha", ...) reply with the friendly
    # laugh line so small talk keeps the energy of the moment.
    if mood == 'laughter':
        pairs = _small_talk_pairs('laughter')
        for reaction, followup in pairs:
            if "okay what happened" in str(reaction).lower():
                reply = str(reaction)
                if followup:
                    reply = f"{reply} {str(followup)}"
                return fill_reply_template(reply, name=name)

    return fill_reply_template(reply, name=name)



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
# PRACTICE ENGINE — AST-based, no hardcoded style guards
# ============================================================
#
# Flow:
#   1. Syntax check + safety check (AST). Unsafe code never runs.
#   2. Requirement is described as an "output expectation", not as a
#      coding style. Any safe code that produces real output passes.
#   3. Output check: real stdout, or a function return the task asks for.
#
# Note: in-process exec is not a hard security wall. The AST gate, the
# blocked names, and the step limit make this safe for a local teaching
# tool, but it is not an operating-system sandbox.

class PracticeExit(Exception):
    """The learner asked to leave the practice session."""


class UnsafeCode(Exception):
    """The submitted code is not safe to run."""


class _SafetyChecker(ast.NodeVisitor):
    """Walks the AST and rejects anything that is not safe to run."""

    def visit_Import(self, node):
        raise UnsafeCode("imports are not allowed in practice")

    def visit_ImportFrom(self, node):
        raise UnsafeCode("imports are not allowed in practice")

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
            raise UnsafeCode(f"{node.func.id}() is not allowed in practice")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if node.attr in BLOCKED_ATTRIBUTES or (
            node.attr.startswith("__") and node.attr.endswith("__")
        ):
            raise UnsafeCode("special attributes are not allowed in practice")
        self.generic_visit(node)

    def visit_While(self, node):
        # while True:  /  while 1:  -> real infinite loop, caught by the AST
        if isinstance(node.test, ast.Constant) and node.test.value in (True, 1):
            raise UnsafeCode("infinite loops are not allowed in practice")
        self.generic_visit(node)


def analyze_code(code):
    """Phase 1: parse and safety-check. Returns the AST tree."""
    tree = ast.parse(code)
    _SafetyChecker().visit(tree)
    return tree


def _build_practice_namespace():
    """Build a namespace with a safe canned input() for learner code."""
    practice_input_values = list(PRACTICE_INPUT_RESPONSES)

    def _practice_input(prompt=""):
        print(prompt, end="")
        if practice_input_values:
            return practice_input_values.pop(0)
        return PRACTICE_INPUT_RESPONSES[-1] if PRACTICE_INPUT_RESPONSES else ''

    return {'input': _practice_input}


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
                    "means an infinite loop. Check your loop condition!"
                )

        return _step_limit_trace

    return _step_limit_trace


def _run_and_observe(tree):
    """Phase 2: run checked code. Returns (ok, stdout, error, namespace)."""
    namespace = _build_practice_namespace()
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    ok = True
    error = None

    try:
        sys.settrace(_make_step_limit_trace())
        exec(compile(tree, '<practice>', 'exec'), namespace)
    except SystemExit:
        ok = False
        error = "the code tried to exit the practice session"
    except Exception as exc:
        ok = False
        error = f"{type(exc).__name__}: {exc}"
    finally:
        sys.stdout = old_stdout
        sys.settrace(None)

    return ok, buffer.getvalue(), error, namespace


def _probe_function(namespace, name, inputs):
    """Return the value of a function the task asked for, or None."""
    fn = namespace.get(name)
    if not callable(fn):
        return None
    try:
        return fn(*inputs)
    except Exception:
        return None


def evaluate_code(tree, spec):
    """Phase 3: decide whether the run produced real observable output."""
    ok, stdout, error, namespace = _run_and_observe(tree)
    if not ok:
        return False, error or "the code did not run cleanly"

    expectation = spec.get('output', {'kind': 'any_stdout'})

    if expectation.get('kind') == 'function_return':
        value = _probe_function(
            namespace, expectation['name'], expectation.get('inputs', [])
        )
        if value not in (None, ''):
            return True, f"returned {value!r}"

    if stdout.strip():
        return True, stdout

    return False, "the code ran but produced no observable output"


def _persist_behavior():
    """Save the derived behavior delta so learning survives a crash."""
    try:
        from Pytalon_Memory.conversation_context import context
        from Pytalon_Memory.memory_store import remember_behavior_snapshot
        remember_behavior_snapshot(context.get_behavior_delta())
        context.mark_behavior_persisted()
    except Exception:
        pass


def _normalize_line(line):
    return ' '.join(line.strip().lower().rstrip('!?.').split())


def _classify_line(line):
    """Classify one input line as 'done', 'exit', or None."""
    key = _normalize_line(line)

    if key in EXIT_TOKENS:
        return 'exit'
    if key in CODE_END_TOKENS:
        return 'done'
    if any(phrase in key for phrase in EXIT_PHRASES):
        return 'exit'
    # exit() / quit() / sys.exit() typed as a line
    if key in ('exit()', 'quit()', 'sys.exit()', 'exit ()', 'quit ()'):
        return 'exit'
    return None


def _is_stray_answer(lines, line):
    """Drop a leading leftover answer token that is not code."""
    if lines:
        return False

    key = _normalize_line(line)
    if key in ANSWER_TOKENS:
        print(f"🤖 I ignored '{line.strip()}' — that looked like an answer, not code.")
        return True
    return False


def read_practice_code():
    """Read code lines until a completion marker. Returns a list of lines."""
    lines = []
    while True:
        line = input()
        kind = _classify_line(line)

        if kind == 'exit':
            raise PracticeExit()

        if kind == 'done':
            return lines

        if _is_stray_answer(lines, line):
            continue

        lines.append(line)


# Practice session flow: show instructions, read code, validate, repeat
def run_practice_session(topic_name):
    """
    Run one interactive practice session for a topic.

    Pass rule: the code must be syntactically valid, safe to run, and
    produce real observable output. Any safe Python code counts — the
    engine does not enforce a coding style.

    Returns True if the learner completed it, False if they left.
    """
    spec = PRACTICE_SPECS.get(topic_name)
    if spec is None:
        return False

    print_global_separator()
    print(f"🧪 INTERACTIVE PRACTICE: {topic_name}", flush=True)
    print_global_separator()

    print(f"\n📋 TASK:", flush=True)
    print(spec['instructions'], flush=True)

    print(f"\n💡 EXAMPLE SOLUTION:", flush=True)
    print(spec['example'], flush=True)

    print(f"\n🔑 Hints: {', '.join(spec.get('hints', []))}", flush=True)

    try:
        from Pytalon_Memory.conversation_context import context as _session_context
        _session_context.note_event("practice_start")
    except Exception:
        pass

    empty_streak = 0

    while True:
        # Every attempt gets a fresh, clearly separated code prompt block.
        print(
            "\n📝 ENTER YOUR PYTHON CODE (type 'DONE' on a new line when finished; "
            "say 'skip' or 'exit' to leave):",
            flush=True,
        )
        print_global_separator()

        try:
            lines = read_practice_code()
        except PracticeExit:
            print("\n👋 No problem — leaving practice. You can come back anytime!", flush=True)
            try:
                from Pytalon_Memory.memory_store import remember_practice
                remember_practice(topic_name, False)
            except Exception:
                pass
            _persist_behavior()
            return False

        if not lines:
            empty_streak += 1

            if empty_streak >= MAX_EMPTY_SUBMISSIONS:
                print_global_separator()
                print("✅ No worries — skipping practice. You can always come back later!", flush=True)
                print_global_separator()
                try:
                    from Pytalon_Memory.memory_store import remember_practice
                    remember_practice(topic_name, False)
                except Exception:
                    pass
                _persist_behavior()
                return False

            print_global_separator()
            print(
                f"📝 Type some Python code, or say 'skip' to move on "
                f"({empty_streak}/{MAX_EMPTY_SUBMISSIONS}).",
                flush=True,
            )
            print_global_separator()
            continue

        empty_streak = 0
        code = "\n".join(lines)

        try:
            tree = analyze_code(code)
        except SyntaxError as exc:
            print_global_separator()
            print(f"🤔 That has a syntax problem ({exc.msg}). Have another go!", flush=True)
            print_global_separator()
            continue
        except UnsafeCode as exc:
            print_global_separator()
            print(f"🛡️ {exc}. Try a safer version!", flush=True)
            print_global_separator()
            continue

        passed, detail = evaluate_code(tree, spec)

        if passed:
            print_global_separator()
            print("✅ Nice — it runs safely and shows real output!", flush=True)

            if detail:
                print(f"\n📤 YOUR OUTPUT:\n{detail}", flush=True)

            print_global_separator()

            try:
                from Pytalon_Memory.conversation_context import context as _session_context
                _session_context.note_event("practice_pass")
            except Exception:
                pass

            try:
                from Pytalon_Memory.memory_store import (
                    remember_practice,
                    remember_topic_completed,
                    build_topic_saved_summary,
                )
                remember_practice(topic_name, True)
                remember_topic_completed(topic_name)
                recap = build_topic_saved_summary(topic_name)
                if recap:
                    print(recap, flush=True)
            except Exception:
                pass

            _persist_behavior()
            return True

        print_global_separator()
        print(f"❌ Not quite. {detail}", flush=True)
        print_global_separator()
        print("🔄 Try again, or say 'skip' to move on.", flush=True)
        print()

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

    numbers = sorted(int(n) for n in topics)
    low, high = numbers[0], numbers[-1]

    return get_global_menu_choice(
        f"\n🔹 {prompt} ({low}-{high}/exit): ",
        low,
        high,
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

    Returns a similarity score between 0 and 1, with adjustments for
    negation cues.
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

    min_overlap = MIN_OVERLAP

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
