"""Common words and patterns for conversation-level intents."""

COMMON_SHORT_WORDS = {
    'the', 'for', 'but', 'of', 'in', 'on', 'at', 'to', 'is', 'it',
    'a', 'an', 'as', 'by', 'hello', 'hi', 'hey', 'thanks',
    'yes', 'no', 'ok', 'okay', 'sure', 'yeah', 'yep', 'yup', 'nah', 'nope',
    'exit', 'quit', 'bye', 'thank', 'help', 'menu', 'topics', 'learn', 'teach',
    'practice', 'example', 'show', 'skip', 'next', 'back', 'done', 'finish',
    'stop', 'continue', 'more', 'all', 'none', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine', 'ten', 'later',

    # Additional short words
    'loop', 'loops', 'list', 'lists', 'tuple', 'tuples', 'set', 'sets',
    'dict', 'dictionary', 'class', 'object', 'file', 'error', 'debug',
    'go', 'start', 'begin', 'pause', 'resume', 'repeat', 'again',
    'another', 'first', 'last', 'prev',
}

COMMON_SINGLE_WORDS = {
    'hello', 'hi', 'hey', 'thanks', 'thank', 'python', 'later',
    'bye', 'exit', 'quit', 'yes', 'no', 'ok', 'okay', 'sure', 'help',
    'what', 'who', 'why', 'how', 'when', 'where', 'menu', 'topics',
    'continue', 'ready', 'wait', 'stop', 'done', 'next', 'back',
    'practice', 'examples', 'example', 'code', 'learn', 'teach',
    'and', 'or', 'not',

    # Additional single words
    'loop', 'list', 'tuple', 'set', 'dict', 'class', 'object', 'file',
    'error', 'debug', 'test', 'module', 'import',
    'function', 'variable', 'operator', 'string', 'int', 'float',
    'bool', 'type', 'strings', 'lists', 'loops', 'operators',
}

generic_python_patterns = [
    'teach me python', 'learn python', 'python tutorial',
    'start with python', 'python basics', 'python course',
    'getting started with python', 'python for beginners',
    'i want to learn python', 'help me learn python',
    'python 101', 'intro to python', 'introduction to python',
    'python fundamentals', 'python foundation', 'python essentials',
    'beginner python', 'new to python', 'first language python',
    'python crash course', 'python bootcamp', 'python class',
    'python lesson', 'python training', 'python coaching',
    'study python', 'study python basics', 'python study guide',
    'python roadmap', 'python path', 'python journey',
    'coding in python', 'programming in python', 'scripting in python',
    'python coding', 'python programming', 'python scripting',
    'i am new to python', 'im new to python', 'python beginner here',
    'absolute beginner python', 'zero to python', 'start coding python',
    'start programming python', 'python from scratch', 'python step by step',

    # Additional generic patterns
    'python for newbies', 'python starter', 'learn python from scratch',
    'learn to code python', 'python for absolute beginners',
    'dummies guide to python', 'python in 30 days',
    'python daily', 'daily python', 'python practice',
    'python refresher', 'refresh my python', 'relearn python',
]

last_response_patterns = [
    'last response', 'last reply', 'last message',
    'what did you say', 'what was your last',
    'whats your last', 'your last response', 'your last reply',
    'your last message', 'repeat what you said', 'say that again',
    'what did you said', 'what you said', 'what was that you said',
    'what did you say again',
    'previous response', 'previous reply', 'previous message',
    'what you just said', 'what you last said', 'the last thing',
    'last output', 'your last words', 'earlier response',

    # Additional phrasings
    'say that again please', 'say it again', 'can you repeat',
    'can you repeat that', 'one more time', 'pardon', 'excuse me',
    'come again', 'say what',
    'what was your previous answer', 'repeat the explanation',
    'what did you just explain', 'can you recap your answer',
]

identity_patterns = [
    'who are you', 'what are you', "what's your name",
    'what is your name', 'tell me about yourself',
    'introduce yourself', 'what can you do',
    "what's your purpose", 'what are you supposed to do',
    'Who are you?', 'What are you?', 'What is your purpose?', 'What can you do?',
    'who are yu', 'what are yu', 'what is your purpose',
    'who r u', 'what r u', 'what is ur purpose',
    'tell me who you are', 'tell me what you are',
    'your identity', 'your intro',
    'about pytalon', 'about the tutor', 'about this tutor',
    'about the assistant', 'about this assistant',
    'about my assistant', 'about your assistant',
    'who is this', 'what is this', 'what is this app',
    'what is this program', 'are you pytalon', 'is this pytalon',

    # Additional identity phrasings
    'what are you called', 'what should i call you',
    'what do i call you', 'tell me about you',
    'describe yourself', 'what is this bot',
    'what is pytalon', 'what does pytalon do',
    'are you a python tutor', 'how can you help me learn',
    'what lessons can you teach',
]
