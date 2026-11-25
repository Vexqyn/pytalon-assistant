"""Intent detection settings (static data)."""

# Words that must never open a lesson, even if they look like topics.
PROTECTED_TOPIC_WORDS = {
    'hello', 'hi', 'hey', 'help', 'thanks', 'thank', 'bye',
    'exit', 'quit', 'yes', 'no', 'ok', 'okay', 'sure', 'what',
    'who', 'why', 'how', 'when', 'where', 'which',
}

# Intent groups used to resolve conflicts between scored intents.
SOCIAL_INTENTS = {'greeting'}
SUBSTANTIVE_INTENTS = {
    'help_request',
    'topic_request',
    'practice_request',
    'general_question',
    'confusion',
    'clarification',
}
CONVERSATION_INTENTS = {
    'greeting', 'farewell', 'gratitude', 'confusion',
    'clarification', 'defer',
}
HIGH_PRIORITY_INTENTS = {
    'gratitude', 'clarification', 'general_question', 'defer',
}

# Confidence values for each scorer.
CONF_YES_NO = 0.95
CONF_DEFER = 0.85
CONF_GREETING = 0.9
CONF_FAREWELL = 0.9
CONF_GRATITUDE = 0.9
CONF_CONFUSION = 0.8
CONF_PRACTICE = 0.8
CONF_HELP = 0.8
CONF_HELP_BOOST = 0.95
CONF_GENERIC_PYTHON = 0.85
CONF_GENERAL_QUESTION = 0.7
CONF_UNCERTAIN = 0.75
CONF_REPEAT = 0.85
CONF_CLARIFICATION = 0.8
CONF_MEMORY = 0.95
CONF_MEMORY_SHORT = 0.9
CONF_TOPIC_FALLBACK = 0.7
CONF_TOPIC_KEYWORD = 0.7

# Natural human exit requests (not just the exact word "exit").
NATURAL_EXIT_PHRASES = (
    'i want to exit', 'i wanna exit', 'i want to leave', 'i wanna leave',
    'i need to leave', 'let me out', 'get me out', 'let me go',
    'i want to quit', 'i wanna quit', 'i need to go', 'time to go',
)

# Phrases that ask for the topic menu, not for saved memory.
TOPIC_MENU_PHRASES = (
    'show topics', 'show topic', 'list topics', 'topics list',
    'topic menu', 'topics menu', 'open topics', 'view topics',
    'topics please', 'all topics', 'what topics can', 'what topics do you',
    'show me topics', 'show me the topics',
)

# Words that mean "show me my saved profile / progress".
MEMORY_ASK_WORDS = {
    'tell', 'know', 'show', 'check', 'view', 'open', 'read',
    'what', 'whats', "what's", 'who', 'describe', 'explain',
    'give', 'drop', 'hit', 'sum', 'summarize', 'recall',
    'remember', 'saved', 'save', 'profile', 'stats',
}

# Phrases that mark a lesson / teaching request. Curiosity questions never
# contain these markers, so they can safely be treated as general questions.
TEACH_REQUEST_MARKERS = (
    'teach', 'teaching', 'learn', 'learning', 'lesson', 'lessons', 'class',
    'course', 'tutorial', 'study', 'practice', 'exercise', 'walk me',
    'explain to', 'show me how', 'get into', 'dive in', 'start the lesson',
)
