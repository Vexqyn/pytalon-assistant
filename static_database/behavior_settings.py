"""Behavior learning settings: derived style signals and thresholds.

Pytalon learns HOW the learner behaves, never WHAT they said.
All values here are static configuration data. Code that reads them
lives in pytalon_body/behavior_learner.py and Pytalon_Memory/.
"""

# Casual / slang markers (lowercase words that signal a casual voice)
BEHAVIOR_CASUAL_MARKERS = frozenset({
    'lol', 'lmao', 'rofl', 'bro', 'bruh', 'dude', 'yo', 'fr', 'frfr',
    'ngl', 'lowkey', 'highkey', 'deadass', 'ong', 'bet', 'wanna',
    'gonna', 'gotta', 'pls', 'plz', 'thx', 'ty', 'kk', 'haha', 'hehe',
    'lit', 'sus', 'smh', 'tbh', 'idk', 'vibes', 'vibe', 'gg', 'yess',
    'yesss', 'nah', 'nahh', 'cap',
})

# Emoji / symbol codepoint ranges treated as expressive style signals
BEHAVIOR_EMOJI_RANGES = (
    (0x1F300, 0x1FAFF),
    (0x2600, 0x27BF),
    (0x2B00, 0x2BFF),
    (0x2190, 0x21FF),
    (0x2764, 0x2764),
    (0xFE0F, 0xFE0F),
)

# Behavior counter keys that roll into the lifetime database
BEHAVIOR_COUNTER_KEYS = (
    'messages_total', 'chars_total', 'caps_messages', 'emoji_messages',
    'question_messages', 'casual_messages',
    'answer_yes', 'answer_no', 'answer_defer', 'answer_exit',
    'practice_start', 'practice_pass', 'practice_fail',
    'generation_boomer', 'generation_gen_x', 'generation_millennial',
    'generation_gen_z', 'generation_gen_alpha',
)

# Voice thresholds: messages needed + casual/emoji ratio to mirror a casual tone
BEHAVIOR_MIN_MESSAGES_FOR_VOICE = 3
BEHAVIOR_CASUAL_RATIO_THRESHOLD = 0.30
BEHAVIOR_EMOJI_RATIO_THRESHOLD = 0.25

# Offer threshold: answers needed + yes-rate to keep suggesting examples/practice
BEHAVIOR_MIN_ANSWERS_FOR_OFFERS = 4
BEHAVIOR_LIKES_OFFERS_RATIO = 0.60

# Pacing thresholds: after these, prompts become gentler
BEHAVIOR_GENTLE_PACING_DEFERS = 2
BEHAVIOR_GENTLE_MIN_ANSWERS = 6

# Revisit threshold: teach-count after which a topic counts as revisited
BEHAVIOR_REVISIT_THRESHOLD = 2
