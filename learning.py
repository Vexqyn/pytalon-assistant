"""
PYTALON - Your Python Tutor Companion
Created by: M Qasim Farooqi
Role: BS IT Student | Python Developer · AI Prompt Strategist · Game Systems Analyst | I build, analyze & create. Founder of Vexqyn 
Version: 2.2
Category: General Availability (Stable Version)
Purpose: Learn Python basics through interactive teaching with 13 comprehensive topics
"""

# ----- Module imports -----
from utils import print_global_separator, show_topic_menu
from validators import (
    get_global_valid_input,
    get_global_examples_valid_input,
)
from conversation_context import ConversationContext
from intro import sys

# ----- Session Setup -----
context = ConversationContext()

# ========== SECTION 1: INTRO & SETUP ==========
from intro import (
    print_introduction,
    get_initial_topic_choice,
    TOPICS,
    TOPIC_NAME_TO_NUMBER,
)

print_introduction()

# ========== CONVERSATIONAL OPENING & FIRST TOPIC SELECTION ==========
try:
    topic_choice = get_initial_topic_choice(context)
    if topic_choice == 'exit':
        # Goodbye message already printed by intro.py's farewell handler
        sys.exit(0)

# ===== MAIN TEACHING LOOP =====
    while True:
        selected_topic = TOPICS[topic_choice]
        print(f"\n🎯 Excellent choice! You selected: {selected_topic}")

        # ---- Ask if user wants to learn this topic ----
        learn_topic = get_global_valid_input(
            f"\n🔹 Would you like me to teach you about {selected_topic}? (yes/no/exit): "
        )
        if learn_topic == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break
        elif learn_topic == 'no':
            print(f"\n🔹 Okay, skipping {selected_topic}.")
            topic_choice = show_topic_menu(TOPICS, "Which topic would you like instead?")
            if topic_choice == 'exit':
                print("\n👋 Goodbye!")
                break
            continue

        print(f"\n📖 Teaching {selected_topic}...")

        # ==================================
        # IMPORT TOPIC MODULES
        # ==================================
        from topics_basic import BASIC_TOPICS
        from topics_intermediate import INTERMEDIATE_TOPICS

        # Combine both dictionaries
        ALL_TOPICS = {**BASIC_TOPICS, **INTERMEDIATE_TOPICS}

        # Single dispatch
        teach_func = ALL_TOPICS.get(selected_topic)
        if teach_func:
            teach_func()

        # ========== SECTION 7: CONTINUE OR EXIT ==========
        print_global_separator()
        learn_more = get_global_valid_input(
            "\n🔹 Would you like to learn another topic? (yes/no/exit): "
        )

        if learn_more == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break
        elif learn_more == 'no':
            break

        # Show menu for next topic
        topic_choice = show_topic_menu(TOPICS, "Which topic would you like to learn next?")
        if topic_choice == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break

    # ========== FINAL MESSAGE ==========
    print_global_separator()
    print("Congratulations! You've completed the Python basics tutorial 🐍 You learned what you wanted!")
    print("Keep practicing to enhance your skills. 🥷")
    print_global_separator()

except (KeyboardInterrupt, EOFError):
    print("\n👋 Sorry, the program got interrupted or ended, it's not your fault restart again the assistant, Goodbye!")
    sys.exit(0)
