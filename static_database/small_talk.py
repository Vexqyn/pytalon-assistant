"""Small-talk phrase data for Pytalon (static data only).

These are reply PARTS: reactions keyed by mood, follow-up questions and
the friendly clarifying lines used when a message is gibberish.

The source code combines these parts into one reply; only finished
phrases are ever spoken. No logic lives here.
"""

# Slang tokens that mark a message as casual chat rather than a lesson ask.
SLANG_WORDS = frozenset({
    'lol', 'lmao', 'rofl', 'haha', 'hehe', 'hahaha', 'ahoy', 'loll',
    'bruh', 'bro', 'brah', 'dude', 'fam', 'gang', 'mate', 'man',
    'ngl', 'fr', 'frfr', 'frfrfr', 'lowkey', 'highkey', 'idk', 'tbh',
    'omg', 'wtf', 'wth', 'rn', 'rly', 'ikr', 'ngmi', 'bet', 'slay',
    'vibe', 'vibes', 'slaps', 'gyat', 'skibidi', 'sigma', 'ong', 'deadass',
    'yasss', 'yeet', 'sheesh', 'ouch', 'ouchie', 'periodt', 'locked',
    'whatever', 'kinda', 'sorta', 'dunno', 'nah', 'nahh', 'nay',
})

# Reaction parts per mood: (reaction, follow-up). Follow-up may be None.
# $name and $topic are filled safely by the source code.
SMALL_TALK_REACTIONS = {
    'greeting': (
        ("Hey $name! 😄", "What's up?"),
        ("Yo! 😄", "What's going on?"),
        ("Hey hey! 😄", "How's it going?"),
    ),
    'casual': (
        ("haha what's up? 😄", None),
        ("Sounds like you're over it right now 😅", "want to just chat, or is something bugging you?"),
        ("bet 😄", "so what are we talking about?"),
        ("lolll 😂", None),
        ("ok but fr 😄", "so what are we on about?"),
    ),
    'laughter': (
        ("💀 okay what happened? tell me", None),
        ("haha! 😄", "what was the joke?"),
        ("big laugh 😂", None),
    ),
    'sadness': (
        ("I hear you — that's a tough one. 💙", None),
        ("sending you a hug 🤍", None),
        ("oof, that got heavy 😢", None),
    ),
    'excitement': (
        ("no way! 😮 that's exciting", "tell me more!"),
        ("oh nice! 😄", None),
    ),
    'question': (
        ("oh good question 🤔", "what exactly are you wondering?"),
        ("great question 😄", None),
    ),
    'approval': (
        ("no cap! 😎", None),
        ("bet 😄", None),
        ("fr fr 😄", None),
    ),
    'gratitude': (
        ("anytime, $name! 💙", None),
        ("of course! 😄", None),
    ),
    'anger': (
        ("I can tell that's frustrating 😠", "want to talk about it?"),
        ("oof, that's annoying 😤", None),
    ),
    'confusion': (
        ("no worries, it can be confusing 🤨", "want me to explain it another way?"),
        ("hmm 🤔", None),
    ),
    'curiosity': (
        ("oh I like that 🤔", "tell me more?"),
        ("interesting! 😄", None),
    ),
    'shock': (
        ("whoa 😮", "wait, what?"),
        ("no way 😮", None),
    ),
    'confidence': (
        ("love the confidence 💪", None),
        ("that's huge 😄", None),
    ),
    'exhaustion': (
        ("sounds exhausting 😮‍💨", "take a breath?"),
        ("that's rough 😔", None),
    ),
    'love': (
        ("aww 😍", None),
        ("that's sweet 💖", None),
    ),
}

# Follow-up questions used when a reaction has none of its own.
SMALL_TALK_FOLLOWUPS = (
    "So, what's on your mind?",
    "Anyway — what are we learning today?",
    "How's your day going?",
    "What's the latest with you?",
)

# Friendly clarifying lines for gibberish / keyboard mash. Varied, never a menu.
GIBBERISH_REPLIES = (
    "Ha, did you fall asleep on your keyboard? 😄 What were you going to say?",
    "lolll, I lost the thread 😂 Say that again?",
    "hmm, my brain just buffered 🤔 Try putting that another way?",
    "ok but what even means that 😅",
)

# Emotion -> reply parts. (reply, follow-up). Follow-up may be None.
EMOJI_REPLES = {
    'amusement': (
        ("💀 okay what happened? tell me", None),
        ("lolll 😂", "What was the joke?"),
        ("haha! 😄", None),
    ),
    'happiness': (
        ("Glad that made you happy! 😊", None),
        ("Yay! 😄", None),
    ),
    'sadness': (
        ("I hear you — that's a tough one. 💙", None),
        ("sending you a hug 🤍", None),
        ("that really got to you 😢", None),
    ),
    'anger': (
        ("I can tell that's frustrating. I'm here to help.", None),
        ("oof, that's annoying 😤", None),
    ),
    'confusion': (
        ("That's confusing, I get it. Want me to explain?", None),
        ("hmm, we can untangle that 🤨", None),
    ),
    'approval': (
        ("Nice! Glad that worked for you. ✨", None),
        ("bet! 😄", None),
    ),
    'gratitude': (
        ("You're welcome! 💙", None),
        ("anytime! 😄", None),
    ),
    'love': (
        ("That's sweet! 💖", None),
        ("aww 😍", None),
    ),
    'sarcasm': (
        ("I see what you did there. 😄", None),
        ("fair point 😄", None),
    ),
    'mockery': (
        ("Fair point! 😄", None),
        ("haha ok 😄", None),
    ),
    'awkwardness': (
        ("Awkward moment, huh? We've all been there.", None),
        ("lol we all have 😄", None),
    ),
    'exhaustion': (
        ("Sounds exhausting. Take a breath! 💙", None),
        ("go easy on yourself 😔", None),
    ),
    'curiosity': (
        ("Curious about that? Ask away! 😄", None),
        ("ooh good one 🤔", None),
    ),
    'shock': (
        ("Wow, that's a surprise! 😮", None),
        ("no way 😮", None),
    ),
    'confidence': (
        ("Love the confidence! 💪", None),
        ("that's awesome 😄", None),
    ),
    'excitement': (
        ("That's exciting! 🎉", None),
        ("no way! 😮", None),
    ),
}

# Regex source for shrinking stretched words ("loooool" -> "lol").
STRETCH_PATTERN = r"(.)\1{2,}"

# Common English words used only for near-miss detection (difflib).
COMMON_WORDS = (
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it',
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but',
    'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will',
    'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out',
    'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can',
    'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into',
    'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than',
    'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also',
    'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way',
    'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most',
    'us', 'is', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had',
    'does', 'did', 'doing', 'done', 'am', 'art', 'area', 'thing', 'things',
)
