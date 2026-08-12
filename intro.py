# intro.py
"""Introduction and session setup for Pytalon."""
from config import last_response_patterns, identity_patterns
from conversation_context import ConversationContext
from validators import detect_conversation_intent
from utils import show_topic_menu
import sys

# ----- Constants -----
NAME = "Pytalon"
VERSION = "2.1"
CATEGORY = "Hotfix (Stable Version)"
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

# ----- Introduction Functions -----
def print_introduction():
    """Print Pytalon's introduction message."""
    print(f"{NAME}, version {VERSION}, category: {CATEGORY}. \n{DESCRIPTION}")

# ---- Conversation Functions -----
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

        # ---- Check for "last response" style questions before intent dispatch ----
        user_lower = user_response.lower()
        
        if any(pattern in user_lower for pattern in last_response_patterns):
            last_response = context.get_pytalon_last_response()
            if last_response:
                print(f"\n📃 My last response was: {last_response}")
            else:
                print("\n🤖 I haven't said anything yet! Ask me something or pick a topic to start!")
            continue

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
            greeting_response = "\n🤖 Hey! Great to see you! Ready to learn some Python? Let's dive in!"
            print(greeting_response)
            context.add_message_to_history('Pytalon', greeting_response)
            continue
        
        elif intent['intent'] == 'topic_request':
            topic_name = intent.get('topic')
            if topic_name and topic_name in TOPIC_NAME_TO_NUMBER:
                print(f"\n🎯 Let's jump straight into {topic_name}!")
                topic_choice = TOPIC_NAME_TO_NUMBER[topic_name]
            else:
                print(f"\n🤖 I'm not sure about that topic. Here's what I can teach you:")
            break
        
        elif intent['intent'] == 'confusion':
            confusion_response = "\n🤖 No worries! Let's start from the basics."
            print(confusion_response)
            context.add_message_to_history('Pytalon', confusion_response)
            # Break so the topic menu is shown after this message
            break
        
        elif intent['intent'] == 'general_question':
            context.set_first_question(user_response)
            context.set_last_question(user_response)
            general_response = f"\n🤖 Great question! We'll explore that as we learn. Let's get started!"
            print(general_response)
            context.add_message_to_history('Pytalon', general_response)
            continue
        
        elif intent['intent'] == 'yes_no':
            answer = intent.get('answer')
            if answer == 'yes':
                yes_response = "\n🤖 Wonderful! What would you like to do? You can:\n   • Tell me a topic (e.g., 'teach me variables')\n   • Ask a question (e.g., 'what is a function?')\n   • Type 'show topics' to see the full list."
                print(yes_response)
                context.add_message_to_history('Pytalon', yes_response)
            elif answer == 'no':
                no_response = "\n🤖 No problem! Take your time.\n   • Tell me a topic when you're ready\n   • Or type 'show topics' to browse the list"
                print(no_response)
                context.add_message_to_history('Pytalon', no_response)
            elif answer == 'exit':
                print("\n👋 Goodbye! Come back whenever you need me.")
                return 'exit'
            continue
        
        elif intent['intent'] == 'gratitude':
            gratitude_response = "\n🤖 You're welcome! What would you like to learn today?\n   • Tell me a topic (e.g., 'teach me variables')\n   • Or type 'show topics' to see the full list."
            print(gratitude_response)
            context.add_message_to_history('Pytalon', gratitude_response)
            continue
        
        elif intent['intent'] == 'uncertain':
            uncertain_response = "\n🤖 No pressure! When you're ready, tell me a topic or type 'show topics'."
            print(uncertain_response)
            context.add_message_to_history('Pytalon', uncertain_response)
            continue
        
        elif intent['intent'] == 'clarification':

            # Check if it's an identity question for more detailed response
            user_lower = user_response.lower()

            if any(pattern in user_lower for pattern in identity_patterns):
                clarification_response = f"\n🤖 I'm {NAME}, version {VERSION}!\n   {DESCRIPTION}\n   I can teach you Python basics like:\n   • Variables and data types\n   • Functions and control flow\n   • Strings, lists, and more\n   What would you like to start with?"
                print(clarification_response)
                context.add_message_to_history('Pytalon', clarification_response)
            else:
                clarification_response = f"\n🤖 I'm {NAME}, your Python tutor! I can walk you through basics like variables, functions, and more.\n   What would you like to start with?"
                print(clarification_response)
                context.add_message_to_history('Pytalon', clarification_response)
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
