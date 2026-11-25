"""Emoji database categorized by generation (static data).

Meanings reflect how each generation actually uses these emojis, so
Pytalon can mirror the learner instead of using an emoji the wrong way.
Only emoji categories are ever stored, never message text.
"""

EMOJI_BY_GENERATION = {
    "boomer": {
        "greeting": ["👋"],
        "laughter": ["😂"],
        "sadness": ["😢"],
        "approval": ["👍"],
        "surprise": ["😮"],
        "love": ["❤️"],
        "sarcasm": ["🙄"],
        "encouragement": ["💪"],
        "celebration": ["🎉"],
    },
    "gen_x": {
        "greeting": ["👋", "🤙"],
        "laughter": ["😂", "🤣"],
        "sadness": ["😢"],
        "approval": ["👍", "🙌"],
        "surprise": ["😲"],
        "love": ["❤️", "💕"],
        "sarcasm": ["🙄"],
        "encouragement": ["💪"],
        "celebration": ["🎉", "🍾"],
    },
    "millennial": {
        "greeting": ["👋", "🙌"],
        "laughter": ["😂", "🤣"],
        "sadness": ["😢", "😭"],
        "approval": ["👍", "🙌"],
        "surprise": ["😮", "😱"],
        "love": ["❤️", "💖"],
        "sarcasm": ["🙄"],
        "encouragement": ["💪", "✨"],
        "celebration": ["🎉", "🥂"],
    },
    "gen_z": {
        "greeting": ["👋", "🤙", "💅"],
        "laughter": ["💀", "😭", "🤣"],
        "sadness": ["😢", "🫠"],
        "approval": ["👍", "🔥", "💅"],
        "surprise": ["😮", "👁️👄👁️"],
        "love": ["🫶", "❤️", "💖"],
        "sarcasm": ["🤡", "💅", "🧍"],
        "encouragement": ["💪", "✨", "🫡"],
        "celebration": ["🎉", "🪦", "🔥"],
    },
    "gen_alpha": {
        "greeting": ["👋", "🦄"],
        "laughter": ["🤣", "😆"],
        "sadness": ["😢"],
        "approval": ["👍", "🔥"],
        "surprise": ["😮", "🤯"],
        "love": ["❤️", "💜"],
        "sarcasm": ["🙃"],
        "encouragement": ["💪", "🌟"],
        "celebration": ["🎉", "🎊"],
    },
}

# Real semantic drift, so an emoji is never used the wrong way.
EMOJI_MEANING = {
    "😂": {"millennial": "laughter", "gen_z": "old-fashioned laughter"},
    "💀": {"gen_z": "I'm dead (laughter)", "millennial": "exhaustion"},
    "😭": {"gen_z": "laughter", "millennial": "sadness"},
    "🤡": {"gen_z": "mockery"},
    "🫶": {"gen_z": "warmth"},
    "🧍": {"gen_z": "awkwardness"},
    "👁️👄👁️": {"gen_z": "shock"},
    "🪦": {"gen_z": "I'm dead (emphasis)"},
    "💅": {"gen_z": "sarcasm"},
}

# One representative emoji per generation, used to open a session.
GENERATION_STYLE_EMOJI = {
    "boomer": "👋",
    "gen_x": "🤙",
    "millennial": "🙌",
    "gen_z": "🔥",
    "gen_alpha": "🦄",
}

# Emotion each emoji expresses. Repeats amplify the emotion.
EMOJI_EMOTION = {
    '💀': 'amusement', '😭': 'sadness', '🤣': 'amusement', '😂': 'amusement',
    '😊': 'happiness', '😄': 'happiness', '🙂': 'happiness', '🎉': 'happiness',
    '😢': 'sadness', '😔': 'sadness', '💔': 'sadness',
    '😡': 'anger', '😠': 'anger', '🤬': 'anger',
    '🤔': 'confusion', '😵': 'confusion', '😵‍💫': 'confusion',
    '👍': 'approval', '🔥': 'approval', '✨': 'approval', '🙌': 'approval',
    '🙏': 'gratitude', '❤️': 'love', '💖': 'love', '🫶': 'love',
    '💅': 'sarcasm', '🤡': 'mockery', '🧍': 'awkwardness',
    '🫠': 'exhaustion', '👀': 'curiosity', '👁️👄👁️': 'shock',
    '😎': 'confidence', '🤩': 'excitement', '🥰': 'love',
    '😋': 'happiness', '😆': 'amusement', '🤪': 'amusement',
    '😅': 'amusement', '🥰': 'love',
}

# Slang markers that point to a generation.
GENERATION_MARKERS = {
    "gen_z": (
        'lol', 'lmao', 'ngl', 'fr', 'frfr', 'lowkey', 'highkey',
        'sus', 'cap', 'bet', 'vibe', 'vibes', 'slay', 'rizz',
        'gyat', 'skibidi', 'sigma', 'no cap', 'deadass', 'ong',
    ),
    "millennial": (
        'lol', 'lmao', 'rofl', 'tbh', 'omg', 'yolo', 'fomo',
        'adulting', 'basic', 'squad', 'goals',
    ),
    "gen_x": (
        'whatever', 'as if', 'talk to the hand', 'booyah',
    ),
}
