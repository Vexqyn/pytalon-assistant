"""
PYTALON - Your Python Assistant
Created by: M Qasim Farooqi
Role: BS IT Student | Python Developer · AI Prompt Strategist · Game Systems Analyst | I build, analyze & create. Founder of Vexqyn
Version: 2.3
Category: Major Release (Stable Version)
Purpose: Learn Python basics through interactive teaching with 13 comprehensive topics
"""

from utils import print_global_separator, show_topic_menu
from validators import get_global_valid_input
from Pytalon_Memory.conversation_context import context
from intro import sys
from intro import (
    print_introduction,
    get_initial_topic_choice,
    TOPICS,
    TOPIC_NAME_TO_NUMBER,
)

# Merge basic + intermediate lessons into one dispatch table
def load_all_topics():
    """Merge basic and intermediate topic maps into one dispatch table."""
    from topics_basic import BASIC_TOPICS
    from topics_intermediate import INTERMEDIATE_TOPICS
    return {**BASIC_TOPICS, **INTERMEDIATE_TOPICS}

# Run the lesson the learner picked (no-op if the topic has no function)
def teach_selected_topic(selected_topic):
    """Run the lesson function for a topic, if one exists."""
    all_topics = load_all_topics()
    teach_func = all_topics.get(selected_topic)
    if teach_func:
        teach_func()

# Map teach-prompt answers: yes / no / defer / exit / switch topic
def handle_topic_switch(answer, current_choice):
    """Map yes/no/defer/exit/topic answers for the teach prompt."""
    if answer == 'exit':
        return 'exit', None

    if answer == 'no':
        print(f"\n🔹 Okay, skipping {TOPICS[current_choice]}.")
        context.set_state("menu")
        next_choice = show_topic_menu(TOPICS, "Which topic would you like instead?")
        if next_choice == 'exit':
            return 'exit', None
        return 'skip', next_choice

    if answer == 'defer':
        print("\n🤖 No problem! Take your time — I'll be here when you're ready.")
        print("   • Type 'continue', 'ready', or \"let's go\" to resume this topic")
        print("   • Or type 'show topics' to browse other topics")
        # Count the pause so memory can mention it later
        try:
            from Pytalon_Memory.memory_store import remember_defer
            remember_defer()
        except Exception:
            pass
        return 'defer', current_choice

    if answer in TOPIC_NAME_TO_NUMBER:
        print(f"\n🎯 Switching to {answer}!")
        context.set_pending_topic(None)
        return 'continue', TOPIC_NAME_TO_NUMBER[answer]

    # Plain yes (or similar) — stay on this topic
    return 'continue', current_choice

# Map answers after a lesson: switch / menu / exit / defer
def handle_learn_more_answer(answer, current_choice):
    """Map answers after a lesson: switch / menu / exit / defer."""
    if answer == 'exit':
        return 'exit', None

    if answer == 'no':
        return 'exit', None

    if answer == 'defer':
        print("\n🤖 No problem! Take your time — I'll be here when you're ready.")
        print("   • Type 'continue', 'ready', or \"let's go\" to resume")
        print("   • Or type 'show topics' to browse topics")
        try:
            from Pytalon_Memory.memory_store import remember_defer
            remember_defer()
        except Exception:
            pass
        return 'defer', current_choice

    if answer in TOPIC_NAME_TO_NUMBER:
        print(f"\n🎯 Switching to {answer}!")
        context.set_pending_topic(None)
        return 'switch', TOPIC_NAME_TO_NUMBER[answer]

    return 'menu', current_choice

# Keep teaching until the learner leaves — memory autosaves on each milestone
def run_teaching_loop(topic_choice):
    """Main teaching loop: ask → teach → continue/exit."""
    while True:
        selected_topic = TOPICS[topic_choice]
        print(f"\n🎯 Excellent choice! You selected: {selected_topic}")

        prompt_text = f"\n🔹 Would you like me to teach you about {selected_topic}? (yes/no/not now/exit): "
        try:
            from pytalon_body.behavior_learner import softened_prompt
            prompt_text = softened_prompt(prompt_text)
        except Exception:
            pass
        learn_topic = get_global_valid_input(prompt_text)

        action, topic_choice = handle_topic_switch(learn_topic, topic_choice)

        if action == 'exit':
            return

        if action == 'skip':
            continue

        if action == 'defer':
            continue

        # Use the topic after any mid-prompt switch
        selected_topic = TOPICS[topic_choice]
        print(f"\n📖 Teaching {selected_topic}...")
        context.set_state("topic")
        context.mark_topic_taught(selected_topic)
        try:
            from Pytalon_Memory.memory_store import remember_topic_taught
            remember_topic_taught(selected_topic)
        except Exception:
            pass
        teach_selected_topic(selected_topic)

        # Completed topics are saved only when practice is passed (see run_practice_session);
        # topics taught this session are tracked separately as patterns, not completions.

        pending_topic = context.get_pending_topic()

        if pending_topic:
            context.set_pending_topic(None)

            if pending_topic in TOPIC_NAME_TO_NUMBER:
                print(f"\n🎯 Switching to {pending_topic}!")
                topic_choice = TOPIC_NAME_TO_NUMBER[pending_topic]
                continue

        context.set_state("menu")
        print_global_separator()
        learn_more = get_global_valid_input(
            "\n🔹 Would you like to learn another topic? (yes/no/not now/exit): "
        )

        action, topic_choice = handle_learn_more_answer(learn_more, topic_choice)

        if action == 'exit':
            return

        if action == 'defer':
            continue

        if action == 'switch':
            continue

        topic_choice = show_topic_menu(TOPICS, "Which topic would you like to learn next?")

        if topic_choice == 'exit':
            return

# Close the session with a friendly wrap-up + permanent memory goodbye
def print_farewell_message():
    """Celebrate the session and show a short goodbye memory line."""
    context.set_state("done")
    print_global_separator()
    try:
        from Pytalon_Memory.memory_store import (
            format_memory_summary,
            remember_session_end,
            has_new_practice_this_session,
        )

        new_practice = has_new_practice_this_session()
        if new_practice:
            print("Congratulations! You've completed the Python basics tutorial 🐍 You learned what you wanted!")
            print("Keep practicing to enhance your skills. 🥷")
        else:
            print("Thanks for stopping by! You can come back anytime to learn more. 🐍")
        print_global_separator()
        remember_session_end(
            topics_touched=context.get_learned_topics(),
            last_state="done",
            behavior_snapshot=context.get_behavior_snapshot(),
        )
        goodbye = format_memory_summary("goodbye")
        if goodbye:
            print(goodbye)
    except Exception:
        pass

# Start Pytalon: intro → permanent memory welcome → teaching loop → goodbye
def main():
    """Start Pytalon: intro → memory welcome → teaching loop → goodbye."""
    print_introduction()

    try:
        try:
            from Pytalon_Memory.memory_store import (
                ensure_learner_profile,
                build_welcome_summary,
                seed_context_from_memory,
            )

            ensure_learner_profile()
            welcome = build_welcome_summary()

            if welcome:
                print(welcome)

            seed_context_from_memory(context)
        except Exception as exc:
            print(f"\n( I could not load saved memory this time: {exc} )")

        topic_choice = get_initial_topic_choice(context)

        if topic_choice == 'exit':
            try:
                from Pytalon_Memory.memory_store import format_memory_summary, remember_session_end
                remember_session_end(
                    topics_touched=context.get_learned_topics(),
                    last_state="exit",
                    behavior_snapshot=context.get_behavior_snapshot(),
                )
                goodbye = format_memory_summary("goodbye")

                if goodbye:
                    print(goodbye)
            except Exception:
                pass
            sys.exit(0)

        run_teaching_loop(topic_choice)
        print_farewell_message()

    except (KeyboardInterrupt, EOFError):
        print(
            "\n👋 Sorry, the program got interrupted or ended, "
            "it's not your fault restart again the assistant, Goodbye!"
        )
        try:
            from Pytalon_Memory.memory_store import format_memory_summary, remember_session_end
            remember_session_end(
                topics_touched=context.get_learned_topics(),
                last_state="interrupted",
                behavior_snapshot=context.get_behavior_snapshot(),
            )
            goodbye = format_memory_summary("goodbye")
            if goodbye:
                print(goodbye)
        except Exception:
            pass
        sys.exit(0)

if __name__ == '__main__':
    main()
