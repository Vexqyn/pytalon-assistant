"""Compatibility exports for topic and conversation pattern data.

The pattern database is split into focused modules, while this module keeps
existing imports working without changing any public names or values.
"""

from static_database.conversation_intents import (
    COMMON_SHORT_WORDS,
    COMMON_SINGLE_WORDS,
    generic_python_patterns,
    last_response_patterns,
    identity_patterns,
)
from static_database.topic_catalog import (
    TOPIC_KEYWORDS,
    TOPIC_REQUEST_PATTERNS,
    PRACTICE_REQUEST_PATTERNS,
    HELP_PATTERNS,
)
from static_database.topic_core import (
    SIMPLE_RESPONSES,
    QUESTION_WORDS,
    PYTHON_TERMS,
    COMMAND_PREFIXES,
)
from static_database.topic_matching import (
    TOPIC_MATCH_THRESHOLD,
    BEGINNER_PATTERNS,
    QUESTION_PATTERNS,
    NEGATION_WORDS,
    FILLER_WORDS,
)

__all__ = [
    'SIMPLE_RESPONSES', 'QUESTION_WORDS', 'PYTHON_TERMS', 'COMMAND_PREFIXES',
    'TOPIC_KEYWORDS', 'TOPIC_REQUEST_PATTERNS', 'PRACTICE_REQUEST_PATTERNS',
    'HELP_PATTERNS', 'TOPIC_MATCH_THRESHOLD', 'BEGINNER_PATTERNS',
    'QUESTION_PATTERNS', 'NEGATION_WORDS', 'FILLER_WORDS', 'COMMON_SHORT_WORDS',
    'COMMON_SINGLE_WORDS', 'generic_python_patterns', 'last_response_patterns',
    'identity_patterns',
]
