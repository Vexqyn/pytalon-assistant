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
 - The module provides functions to observe text, evaluate behavior, describe learned traits, and generate adaptive opening lines and prompts.
 - Designed to be safe and privacy-conscious, with no retention of specific messages or personal identifiers.
 - Developed on Pure Python with no external dependencies beyond the standard library and the config module.
"""

import re

import config


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


def describe_behavior_lines(behavior):

    # Human-readable memory-report lines — patterns only, never messages.

    try:

        traits = evaluate(behavior)

    except Exception:

        return []

    lines = []

    if traits["voice"] == "casual":

        lines.append("   • Your style: casual 😄 — I'll match that vibe.")

    else:

        lines.append("   • Your style: steady and focused — I'll keep it clean.")

    if traits["likes_offers"]:

        lines.append("   • You usually accept offers — I'll keep suggesting examples and practice.")

    if traits["revisited_topics"]:

        tops = sorted(traits["revisited_topics"].items(), key=lambda kv: -kv[1])[:3]

        joined = ", ".join(f"{topic} ({count}×)" for topic, count in tops)

        lines.append(f"   • Topics you revisited: {joined}")

    return lines


def session_opening_line():

    # Tone-adaptive conversational opening, chosen from learned patterns.

    behavior = {}

    defer_count = 0

    try:

        from Pytalon_Memory.memory_store import load_long_term

        data = load_long_term()

        behavior = data.get("behavior") or {}

        defer_count = int((data.get("preferences") or {}).get("defer_count", 0) or 0)

    except Exception:

        pass

    traits = evaluate(behavior, defer_count=defer_count)

    if traits["voice"] == "casual":

        return "Yo yo! 😄 What's on your mind? Ask me anything or pick a topic — let's go!"

    if traits["gentle_pacing"]:

        return "Hi there! 😊 What's on your mind? No rush at all — ask anything or pick a topic whenever you're ready."

    return "Hi there! 😄 What's on your mind? Ask me anything or pick a topic to start!"


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
