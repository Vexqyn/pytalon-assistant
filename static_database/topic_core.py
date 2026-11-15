"""Core vocabulary used by topic and command detection."""

SIMPLE_RESPONSES = [
    'yes', 'y', 'no', 'n', 'ok', 'okay', 'exit', 'e', 'quit', 'bye',
    'yeah', 'yep', 'nope', 'nah', 'sure', 'fine', 'done', 'stop',
    'hmm', 'huh', 'what', 'wait', 'continue', 'next',
    'alright', 'go', 'start', 'begin', 'skip', 'back', 'more',
    'repeat', 'again', 'later', 'now', 'ready', 'pause', 'resume',
    'teach', 'learn', 'show', 'tell', 'help', 'menu', 'topics',
]

QUESTION_WORDS = [
    'what', 'how', 'why', 'when', 'where', 'who', 'which',
    'can', 'is', 'are', 'do', 'does', 'should', 'could', 'would', 'will',
    'whose', 'whom', 'whether', 'shall', 'may', 'might', 'must',
    'explain', 'describe', 'define', 'clarify',
]

PYTHON_TERMS = [
    'python', 'function', 'variable', 'relational operator',
    'assignment operator', 'logical operator', 'type conversion', 'input function',
    'comments', 'strings', 'programming', 'coding', 'data types', 'conditional statements',
    'if statement', 'else statement', 'elif statement', 'nested conditionals',
    'Indexing & Slicing', 'Strings Operations', 'Strings Formating',
    'indexing & slicing', 'strings operations', 'strings formatting',
    'indexing', 'slicing', 'formatting',
    'operators', 'expressions', 'statements', 'syntax', 'indentation',
    'whitespace', 'keywords', 'identifiers', 'literals', 'booleans',
    'none', 'numbers', 'integers', 'floats', 'characters', 'sequences',
    'iteration', 'recursion', 'scope', 'namespaces', 'modules', 'packages',
    'libraries', 'imports', 'builtins', 'standard library',
]

COMMAND_PREFIXES = ['/', '\\', '!', '@', '#', '$', '%', '^', '&', '*',
                    '>', ':', ';', '|', '~', '?', '-', '+', '.']
