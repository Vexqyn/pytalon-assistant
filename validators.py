# validators.py
"""
Compatibility layer — real body lives in pytalon_body/.

Only names actually used by Pytalon modules are re-exported here
so imports stay short: `from validators import get_global_valid_input`.
"""

# Re-export the body validators so teaching code stays simple
from pytalon_body.response_validators import (
    get_global_valid_input,
    get_global_menu_choice,
    get_global_examples_valid_input,
)

# Re-export intent detection (memory_request, topic_request, ...)
from pytalon_body.intent_engine import (
    detect_conversation_intent,
)

__all__ = [
    'get_global_valid_input',
    'get_global_menu_choice',
    'get_global_examples_valid_input',
    'detect_conversation_intent',
]
