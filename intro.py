# intro.py
"""Introduction and session setup for Pytalon."""

import sys

# Loaded when the opening loop runs (keeps import light for startup)
detect_conversation_intent = None
show_topic_menu = None
last_response_patterns = None
identity_patterns = None

# ----- Constants (single source for version / intro text) -----
NAME = "Pytalon"
VERSION = "2.3"
CATEGORY = "Major Release (Stable Version)"
DESCRIPTION = (
    "A Python Assistant developed to guide you with "
    "Python programming and learning."
)

TOPICS = {
    '1': 'Hello World',
    '2': 'Functions',
    '3': 'Variables',
    '4': 'Relational operators',
    '5': 'Assignment operators',
    '6': 'Logical operators',
    '7': 'Type conversion',
    '8': 'Input function',
    '9': 'Comments in Python',
    '10': 'Strings in Python',
    '11': 'Data types in Python',
    '12': 'Conditional statements',
    '13': 'Lists in Python',
}

# Reverse lookup: topic name → number
TOPIC_NAME_TO_NUMBER = {topic_name: number for number, topic_name in TOPICS.items()}

# ============================================================
# INTRODUCTION
# ============================================================

def print_introduction():
    """Print Pytalon's introduction — only place this text lives."""
    print(f"{NAME}, version {VERSION}, category: {CATEGORY}. \n{DESCRIPTION}")

# ============================================================
# CONVERSATIONAL OPENING
# ============================================================

def _print_identity_clarification(context):
    """Give a fuller self-introduction when the learner asks who Pytalon is."""
    clarification_response = (
        f"\n🤖 I'm {NAME}, version {VERSION}!\n"
        f"   {DESCRIPTION}\n"
        f"   I can teach you Python basics like:\n"
        f"   • Variables and data types\n"
        f"   • Functions and control flow\n"
        f"   • Strings, lists, and more\n"
        f"   What would you like to start with?"
    )
    print(clarification_response)
    context.add_message_to_history('Pytalon', clarification_response)

def _print_generic_clarification(context):
    """Give a short self-introduction for general clarification requests."""
    clarification_response = (
        f"\n🤖 I'm {NAME}, your Python assistant! I can walk you through "
        f"basics like variables, functions, and more.\n"
        f"   What would you like to start with?"
    )
    print(clarification_response)
    context.add_message_to_history('Pytalon', clarification_response)

def _reply_and_remember(context, message):
    """Print a Pytalon reply and store it in conversation history."""
    print(message)
    context.add_message_to_history('Pytalon', message)

def _dispatch_intent(context, user_response, intent, state):
    """
    Handle one recognized intent during the opening conversation.

    `state` is a small dict used to share retry_count / topic_choice
    across the loop without globals.

    Returns:
        'continue' — keep chatting
        'break'    — show the topic menu next
        'exit'     — say goodbye
    """
    intent_name = intent['intent']

    # Learner asked what we remember — answer with the saved report
    if intent_name == 'memory_request':
        try:
            from Pytalon_Memory.memory_store import handle_memory_ask
            handle_memory_ask(user_response.lower())
        except Exception:
            print("\nI could not open saved memory right now — try again in a moment.")
        return 'continue'

    # Learner asked to be renamed — update permanent profile, keep chatting
    try:
        from Pytalon_Memory.memory_store import try_extract_rename, rename_learner
        new_name = try_extract_rename(user_response)
    except Exception:
        new_name = None
    if new_name:
        try:
            _profile, message = rename_learner(new_name)
            print(f"\n{message}")
            print('💬 Ask me "what do you remember?" anytime to see your profile.')
        except Exception:
            print("\nI could not save that name right now — try again in a moment.")
        return 'continue'

    # Memory wipe / delete — explain only, never auto-delete files
    if intent_name == 'memory_manage':
        print(
            "\nI only autosave your name and learning progress on this computer. "
            "Ask \"what do you remember?\" to see what's saved."
        )
        return 'continue'

    if intent_name == 'farewell':
        return 'exit'

    if intent_name == 'greeting':
        _reply_and_remember(
            context,
            "\n🤖 Hey! Great to see you! Ready to learn some Python? Let's dive in!",
        )
        return 'continue'

    if intent_name == 'topic_request':
        topic_name = intent.get('topic')

        if topic_name and topic_name in TOPIC_NAME_TO_NUMBER:
            print(f"\n🎯 Let's jump straight into {topic_name}!")
            state['topic_choice'] = TOPIC_NAME_TO_NUMBER[topic_name]
            context.set_state("topic")
        else:
            print(f"\n🤖 I'm not sure about that topic. Here's what I can teach you:")

        return 'break'

    if intent_name == 'confusion':
        _reply_and_remember(
            context,
            "\n🤖 No worries! Let's start from the basics.",
        )
        return 'break'

    if intent_name == 'general_question':
        context.set_first_question(user_response)
        context.set_last_question(user_response)
        _reply_and_remember(
            context,
            "\n🤖 Great question! We'll explore that as we learn. Let's get started!",
        )
        return 'continue'

    if intent_name == 'yes_no':
        return _handle_yes_no_opening(context, intent)

    if intent_name == 'gratitude':
        _reply_and_remember(
            context,
            "\n🤖 You're welcome! What would you like to learn today?\n"
            "   • Tell me a topic (e.g., 'teach me variables')\n"
            "   • Or type 'show topics' to see the full list.",
        )
        return 'continue'

    if intent_name == 'uncertain':
        _reply_and_remember(
            context,
            "\n🤖 No pressure! When you're ready, tell me a topic or type 'show topics'.",
        )
        return 'continue'

    if intent_name == 'defer':
        _reply_and_remember(
            context,
            "\n🤖 No problem! Take your time — I'll be here when you're ready.\n"
            "   • Type 'continue', 'ready', or \"let's go\" to resume\n"
            "   • Or type 'show topics' to browse again",
        )
        return 'continue'

    if intent_name == 'clarification':
        user_lower = user_response.lower()

        if any(pattern in user_lower for pattern in identity_patterns):
            _print_identity_clarification(context)
        else:
            _print_generic_clarification(context)

        return 'continue'

    if intent_name == 'repeat_request':
        last_response = context.get_pytalon_last_response()

        if last_response:
            print("\n🤖 Sure! Here's what I said:")
            print(last_response)
        else:
            print(
                "\n🤖 I haven't said anything yet! "
                "Ask me something or pick a topic to start!"
            )

        return 'continue'

    if intent_name in ('help_request', 'practice_request'):
        if intent.get('is_beginner'):
            print("\n😊 Great! I'd love to help you get started with Python.")
            print("Here are the topics I can walk you through:")
        else:
            print("\n🤖 Sure thing! Let me show you the available topics.")

        return 'break'

    print(
        "\n🤖 I'm not sure how to help with that yet. "
        "Try a topic name or type 'show topics'."
    )
    return 'continue'

def _handle_yes_no_opening(context, intent):
    """Handle yes / no / exit answers during the opening chat."""
    answer = intent.get('answer')

    if answer == 'yes':
        _reply_and_remember(
            context,
            "\n🤖 Wonderful! What would you like to do? You can:\n"
            "   • Tell me a topic (e.g., 'teach me variables')\n"
            "   • Ask a question (e.g., 'what is a function?')\n"
            "   • Type 'show topics' to see the full list.",
        )
        return 'continue'

    if answer == 'no':
        _reply_and_remember(
            context,
            "\n🤖 No problem! Take your time.\n"
            "   • Tell me a topic when you're ready\n"
            "   • Or type 'show topics' to browse the list",
        )
        return 'continue'

    if answer == 'exit':
        return 'exit'

    return 'continue'

def _ensure_intro_deps():
    """Load config patterns + validators/utils on first chat turn."""
    global detect_conversation_intent, show_topic_menu
    global last_response_patterns, identity_patterns

    if last_response_patterns is None:
        from config import (
            last_response_patterns as _lrp,
            identity_patterns as _idp,
        )
        last_response_patterns = _lrp
        identity_patterns = _idp

    if detect_conversation_intent is None:
        from validators import detect_conversation_intent as _detect
        detect_conversation_intent = _detect

    if show_topic_menu is None:
        from utils import show_topic_menu as _menu
        show_topic_menu = _menu

def get_initial_topic_choice(context):
    """
    Run the conversational opening loop.

    Returns:
        The user's first topic_choice (string number) or 'exit'.
    """
    _ensure_intro_deps()
    context.set_state("greeting")

    try:
        from pytalon_body.behavior_learner import session_opening_line
        opening_prompt = "\n" + session_opening_line()
    except Exception:
        opening_prompt = "\nHi there! 😄 What's on your mind? Ask me anything or pick a topic to start!"
    print(opening_prompt)

    context.set_state("menu")

    max_retries = 2
    state = {
        'retry_count': 0,
        'topic_choice': None,
    }

    while True:
        user_response = input("\n🔹 You: ")
        context.add_message_to_history('user', user_response)
        context.observe_input(user_response)
        user_lower = user_response.lower()

        # 'What did you say last?' questions come before intent dispatch
        if any(pattern in user_lower for pattern in last_response_patterns):
            last_response = context.get_pytalon_last_response()

            if last_response:
                print(f"\n📃 My last response was: {last_response}")
            else:
                print(
                    "\n🤖 I haven't said anything yet! "
                    "Ask me something or pick a topic to start!"
                )

            continue

        try:
            from Pytalon_Memory.memory_store import (
                try_extract_rename,
                rename_learner,
            )
            new_name = try_extract_rename(user_response)
        except Exception:
            new_name = None

        if new_name:
            try:
                _profile, message = rename_learner(new_name)
                print(f"\n{message}")
                print('💬 Ask me "what do you remember?" anytime to see your profile.')
            except Exception:
                print("\nI could not save that name right now — try again in a moment.")
            state['retry_count'] = 0
            continue

        intent = detect_conversation_intent(user_response)

        if intent['intent'] in ['empty', 'unrecognized']:
            state['retry_count'] += 1

            if state['retry_count'] >= max_retries:
                print("\n🤖 No worries! Let me show you what I can teach you instead:")
                break

            continue

        state['retry_count'] = 0

        action = _dispatch_intent(context, user_response, intent, state)

        if action == 'exit':
            return 'exit'

        if action == 'break':
            break

    # Direct topic request skips the menu
    if state['topic_choice']:
        context.set_state("topic")
        return state['topic_choice']

    # Otherwise show the menu
    context.set_state("menu")
    topic_choice = show_topic_menu(TOPICS, "Which topic would you like to start with?")

    if topic_choice == 'exit':
        return 'exit'

    context.set_state("topic")
    return topic_choice
