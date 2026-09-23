# pytalon_body/__init__.py
"""
Pytalon Body
============

Body of Pytalon: input validation + conversation intent.

    response_validators.py  — yes / no / exit / examples / menu
    intent_engine.py        — detect what the learner means

Import submodules directly (this package init stays light for fast launch):

    from pytalon_body.response_validators import get_global_valid_input
    from pytalon_body.intent_engine import detect_conversation_intent
"""

# No re-exports — eager imports slow learning.py startup.
__all__ = []
