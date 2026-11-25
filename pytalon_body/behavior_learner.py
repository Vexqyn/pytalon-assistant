# pytalon_body/behavior_learner.py
"""
Behavioral learner for Pytalon.

This module observes and learns from the learner's behavior patterns,
not their specific words. It tracks derived metrics like slang usage,
message length, emoji frequency, and answer tendencies to adapt the
assistant's responses accordingly.

 - No personal data is stored or processed; only abstracted behavioral signals are used.
 - The learning is rule-based and transparent, with thresholds and patterns defined in the config module.
 - No external services are called; all processing is local and self-contained.
 - Designed to be safe and privacy-conscious, with no retention of specific messages or personal identifiers.
 - Pure Python with no external dependencies beyond the standard library and the config module.
"""

import re

import config
from static_database.emoji_database import (
    EMOJI_BY_GENERATION,
    EMOJI_EMOTION,
    EMOJI_MEANING,
    GENERATION_MARKERS,
    GENERATION_STYLE_EMOJI,
)

# Emoji sets used to guess which generation a learner writes like.
_GENZ_EMOJI = set(EMOJI_MEANING.keys()) - {'😂'}
_MILLENNIAL_EMOJI = {'😂', '🤣', '😜', '😅', '😍', '🙌', '💕'}
_BOOMER_EMOJI = {'👍', '❤️', '😊', '😮', '🎉', '👋'}


def _guess_generation(text):
    """Guess the writer's generation from emoji and slang. Patterns only."""
    text = text or ""
    scores = {}

    for ch in text:
        if ch in _GENZ_EMOJI:
            scores['gen_z'] = scores.get('gen_z', 0) + 1
        elif ch in _MILLENNIAL_EMOJI:
            scores['millennial'] = scores.get('millennial', 0) + 1
        elif ch in _BOOMER_EMOJI:
            scores['boomer'] = scores.get('boomer', 0) + 1

    words = set(re.findall(r"[a-z']+", text.lower()))
    for generation, markers in GENERATION_MARKERS.items():
        if words & set(markers):
            scores[generation] = scores.get(generation, 0) + 1

    if not scores:
        return None
    return max(scores, key=scores.get)


def read_emoji_emotion(text):
    """Return the dominant emotion of the emojis in text, or None.

    Repeats amplify the emotion because each emoji counts.
    """
    text = text or ""
    counts = {}

    for ch in text:
        emotion = EMOJI_EMOTION.get(ch)
        if emotion:
            counts[emotion] = counts.get(emotion, 0) + 1

    if not counts:
        return None
    return max(counts, key=counts.get)


def _style_emoji(generation):
    """One representative emoji for a generation."""
    return GENERATION_STYLE_EMOJI.get(generation or "millennial", "😄")


def observe_text(text):

    # Derive style signals from ONE learner message. Returns counters only.

    text = text or ""

    lowered = text.lower()

    words = set(re.findall(r"[a-z']+", lowered))

    casual = bool(words & config.BEHAVIOR_CASUAL_MARKERS)

    has_emoji = any(
        lo <= ord(ch) <= hi
        for ch in text
        for lo, hi in config.BEHAVIOR_EMOJI_RANGES
    )

    return {
        "chars": len(text),
        "caps": bool(text) and text == text.upper() and any(c.isalpha() for c in text),
        "emoji": has_emoji,
        "question": text.rstrip().endswith("?"),
        "casual": casual,
        "generation": _guess_generation(text),
    }


def evaluate(behavior, defer_count=0):

    # Turn derived counters into learned traits. Honest thresholds, no magic.

    b = behavior or {}

    msgs = int(b.get("messages_total") or 0)

    casual_ratio = (int(b.get("casual_messages") or 0) / msgs) if msgs else 0.0

    emoji_ratio = (int(b.get("emoji_messages") or 0) / msgs) if msgs else 0.0

    casual_enough = (
        casual_ratio >= config.BEHAVIOR_CASUAL_RATIO_THRESHOLD
        or emoji_ratio >= config.BEHAVIOR_EMOJI_RATIO_THRESHOLD
    )

    voice = (
        "casual"
        if msgs >= config.BEHAVIOR_MIN_MESSAGES_FOR_VOICE and casual_enough
        else "steady"
    )

    yes = int(b.get("answer_yes") or 0)

    no = int(b.get("answer_no") or 0)

    total_answers = yes + no

    likes_offers = (
        total_answers >= config.BEHAVIOR_MIN_ANSWERS_FOR_OFFERS
        and yes >= no
        and (yes / total_answers) >= config.BEHAVIOR_LIKES_OFFERS_RATIO
    )

    gentle_pacing = (
        int(defer_count or 0) >= config.BEHAVIOR_GENTLE_PACING_DEFERS
        or (
            total_answers >= config.BEHAVIOR_GENTLE_MIN_ANSWERS
            and no > yes
        )
    )

    revisits = {
        topic: int(count or 0)
        for topic, count in (b.get("topic_revisits") or {}).items()
        if int(count or 0) >= config.BEHAVIOR_REVISIT_THRESHOLD
    }

    return {
        "voice": voice,
        "casual_ratio": round(casual_ratio, 2),
        "emoji_ratio": round(emoji_ratio, 2),
        "likes_offers": likes_offers,
        "gentle_pacing": gentle_pacing,
        "revisited_topics": revisits,
    }


def detect_generation(behavior):

    # Read the accumulated generation counters (never raw text).

    counts = {}

    for key, value in (behavior or {}).items():
        if key.startswith("generation_"):
            counts[key[len("generation_"):]] = int(value or 0)

    if not counts or sum(counts.values()) == 0:
        return None

    return max(counts, key=counts.get)


def get_style_profile():

    # Merge static defaults (config) with dynamic counters (memory + live session).

    behavior = {}
    defer_count = 0

    try:
        from Pytalon_Memory.memory_store import load_long_term
        data = load_long_term()
        behavior = dict(data.get("behavior") or {})
        defer_count = int((data.get("preferences") or {}).get("defer_count", 0) or 0)
    except Exception:
        pass

    # Add the live session so adaptation happens during this session too.
    live = {}
    try:
        from Pytalon_Memory.conversation_context import context
        live = context.get_behavior_snapshot()
        for key in config.BEHAVIOR_COUNTER_KEYS:
            if key in live:
                behavior[key] = int(behavior.get(key, 0) or 0) + int(live.get(key, 0) or 0)
    except Exception:
        pass

    # Once the live session has enough messages, let it steer the style;
    # otherwise use the lifetime profile (this is what the opening uses).
    live_msgs = int(live.get("messages_total") or 0) if live else 0
    if live_msgs >= config.BEHAVIOR_MIN_MESSAGES_FOR_VOICE:
        traits = evaluate(live, defer_count=defer_count)
    else:
        traits = evaluate(behavior, defer_count=defer_count)

    traits["generation"] = detect_generation(behavior)
    return traits


def pick_emoji(category, generation=None):

    # Pick an emoji that matches the learner's generation.

    generation = generation or "millennial"
    bucket = EMOJI_BY_GENERATION.get(generation) or EMOJI_BY_GENERATION["millennial"]
    options = bucket.get(category) or EMOJI_BY_GENERATION["millennial"].get(category) or ["✨"]
    return options[0]


def describe_behavior_lines(behavior):

    # Human-readable memory-report lines — patterns only, never messages.

    try:
        traits = evaluate(behavior)
    except Exception:
        return []

    lines = []

    generation = detect_generation(behavior)
    emoji = _style_emoji(generation)

    if traits["voice"] == "casual":
        lines.append(f"   • Your style: casual {emoji} — I'll match that vibe.")
    else:
        lines.append(f"   • Your style: steady and focused {emoji} — I'll keep it clean.")

    if traits["likes_offers"]:
        lines.append("   • You usually accept offers — I'll keep suggesting examples and practice.")

    if traits["revisited_topics"]:
        tops = sorted(traits["revisited_topics"].items(), key=lambda kv: -kv[1])[:3]
        joined = ", ".join(f"{topic} ({count}×)" for topic, count in tops)
        lines.append(f"   • Topics you revisited: {joined}")

    generation = detect_generation(behavior)
    if generation:
        lines.append(f"   • Your emoji style: {generation} — I'll match it.")

    return lines


def session_opening_line():

    # Tone-adaptive conversational opening, chosen from learned patterns.

    traits = get_style_profile()
    generation = traits.get("generation")
    wave = GENERATION_STYLE_EMOJI.get(generation, "😄")

    generation = traits.get("generation")

    if traits["voice"] == "casual" or generation in ("gen_z", "gen_alpha"):
        return f"Yo yo! {wave} What's on your mind? Type 'help' to see what I can do."

    if traits["gentle_pacing"]:
        return f"Hi there! {wave} What's on your mind? No rush at all — type 'help' for options."

    return f"Hi there! {wave} What's on your mind? Type 'help' for options."


def softened_prompt(text):

    # Return a gentler prompt variant for learners who often pause (rule-based).

    try:
        from Pytalon_Memory.memory_store import load_long_term
        prefs = load_long_term().get("preferences") or {}
        if int(prefs.get("defer_count", 0) or 0) >= config.BEHAVIOR_GENTLE_PACING_DEFERS:
            return text.replace(
                "Would you like me to teach you about",
                "No pressure at all — feel like learning about",
            )
    except Exception:
        pass

    return text
