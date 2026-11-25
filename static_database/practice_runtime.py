"""Practice engine runtime data (static configuration).

These values configure how the practice sandbox reads input, ends a
submission, and judges safety. The engine logic lives in utils.py.
"""

# Exact whole-token markers that mean "I am finished entering code".
CODE_END_TOKENS = {
    'done', 'don', 'dun', 'dn', 'donee', 'doned',
    'finish', 'fin', 'finnish', 'finsih',
    'submit', 'send', 'thats all', "that's all", 'end',
}

# Exact whole-token exit commands.
EXIT_TOKENS = {
    'exit', 'quit', 'bye', 'leave', 'stop', 'cancel', 'enough',
}

# Natural human exit requests. Matched as whole phrases inside a line.
EXIT_PHRASES = (
    'i want to exit', 'i wanna exit', 'let me out', 'get me out',
    'exit practice', 'leave practice', 'i want to leave',
    'i want to quit', 'i wanna leave', 'skip practice',
    'i am done', 'im done', 'not now', 'take a break',
    'i need a break', 'i want a break', 'let me go',
)

# How many empty / "Done"-only submissions before practice is skipped.
MAX_EMPTY_SUBMISSIONS = 4

# Lines that are clearly a leftover answer, not code.
ANSWER_TOKENS = {
    'yes', 'yeah', 'yep', 'yup', 'no', 'nope', 'nah',
    'ok', 'okay', 'sure', 'defer', 'not now', 'skip',
}

# Calls that are never allowed in practice code.
BLOCKED_CALLS = {
    'exec', 'eval', 'compile', '__import__', 'open', 'breakpoint',
    'exit', 'quit', 'globals', 'locals', 'vars', 'getattr', 'setattr',
    'delattr', 'memoryview', 'help',
}

# Attribute names that are never allowed in practice code.
BLOCKED_ATTRIBUTES = {
    '__class__', '__bases__', '__subclasses__', '__globals__',
    '__builtins__', '__import__', '__code__', '__closure__',
    '__getattribute__', '__setattr__', '__delattr__',
}
