# intro.py
"""Introduction and session setup for Pytalon."""

from conversation_context import ConversationContext
from validators import detect_conversation_intent
from utils import show_topic_menu
import sys

# ----- Constants -----
NAME = "Pytalon"
VERSION = "2.0"
CATEGORY = "Major Release (Stable Version)"
DESCRIPTION = "A Tutor Companion Assistant developed to guide you with Python programming and learning."

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
    '13': 'Lists in Python'
}

# Reverse lookup: topic name → number
TOPIC_NAME_TO_NUMBER = {v: k for k, v in TOPICS.items()}


def print_introduction():
    """Print Pytalon's introduction message."""
    print(f"{NAME}, version {VERSION}, category: {CATEGORY}. \n{DESCRIPTION}")


def get_initial_topic_choice(context):
    """
    Run the conversational opening loop.
    Returns the user's first topic_choice (string number) or 'exit'.
    """
    opening_prompt = "\nHi there! 😄 What's on your mind? Ask me anything or pick a topic to start!"
    print(opening_prompt)
    
    retry_count = 0
    MAX_RETRIES = 2
    topic_choice = None
    intent = None
    
    while True:
        user_response = input("\n🔹 You: ")
        context.add_message_to_history('user', user_response)
        
        intent = detect_conversation_intent(user_response)
        
        # Empty / unrecognized fallback
        if intent['intent'] in ['empty', 'unrecognized']:
            retry_count += 1
            if retry_count >= MAX_RETRIES:
                print("\n🤖 No worries! Let me show you what I can teach you instead:")
                break
            continue
        
        retry_count = 0  # reset on good input
        
        if intent['intent'] == 'farewell':
            print("\n👋 Goodbye! Come back whenever you need me.")
            return 'exit'
        
        elif intent['intent'] == 'greeting':
            print("\n🤖 Hey! Great to see you! Ready to learn some Python? Let's dive in!")
            break
        
        elif intent['intent'] == 'topic_request':
            topic_name = intent.get('topic')
            if topic_name and topic_name in TOPIC_NAME_TO_NUMBER:
                print(f"\n🎯 Let's jump straight into {topic_name}!")
                topic_choice = TOPIC_NAME_TO_NUMBER[topic_name]
            else:
                print(f"\n🤖 I'm not sure about that topic. Here's what I can teach you:")
            break
        
        elif intent['intent'] == 'confusion':
            print("\n🤖 No worries! Let's start from the basics.")
            break
        
        elif intent['intent'] == 'general_question':
            context.set_first_question(user_response)
            context.set_last_question(user_response)
            print(f"\n🤖 Great question! We'll explore that as we learn. Let's get started!")
            break
        
        elif intent['intent'] == 'yes_no':
            answer = intent.get('answer')
            if answer == 'yes':
                print("\n🤖 Wonderful! What would you like to do? You can:")
                print("   • Tell me a topic (e.g., 'teach me variables')")
                print("   • Ask a question (e.g., 'what is a function?')")
                print("   • Type 'show topics' to see the full list.")
            elif answer == 'no':
                print("\n🤖 No problem! Take your time.")
                print("   • Tell me a topic when you're ready")
                print("   • Or type 'show topics' to browse the list")
            elif answer == 'exit':
                print("\n👋 Goodbye! Come back whenever you need me.")
                return 'exit'
            continue
        
        elif intent['intent'] == 'gratitude':
            print("\n🤖 You're welcome! What would you like to learn today?")
            print("   • Tell me a topic (e.g., 'teach me variables')")
            print("   • Or type 'show topics' to see the full list.")
            continue
        
        elif intent['intent'] == 'uncertain':
            print("\n🤖 No pressure! When you're ready, tell me a topic or type 'show topics'.")
            continue
        
        elif intent['intent'] == 'clarification':
            print(f"\n🤖 I'm {NAME}, your Python tutor! I can walk you through basics like variables, functions, and more.")
            print("   What would you like to start with?")
            continue
        
        elif intent['intent'] == 'repeat_request':
            print("\n🤖 Sure! Here's what I said:")
            print(opening_prompt.strip())
            continue
        
        elif intent['intent'] in ('help_request', 'practice_request'):
            if intent.get('is_beginner'):
                print("\n😊 Great! I'd love to help you get started with Python.")
                print("Here are the topics I can walk you through:")
            else:
                print("\n🤖 Sure thing! Let me show you the available topics.")
            break
        
        else:
            print("\n🤖 I'm not sure how to help with that yet. Try a topic name or type 'show topics'.")
            continue
    
    # If topic was directly requested, skip the menu
    if topic_choice:
        return topic_choice
    
    # Otherwise show menu
    topic_choice = show_topic_menu(TOPICS, "Which topic would you like to start with?")
    if topic_choice == 'exit':
        print("\n👋 Ok, goodbye! Come back whenever you need me")
        sys.exit(0)
    
    return topic_choice