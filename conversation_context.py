# conversation_context.py

class ConversationContext:
    """
    Tracks the state of the conversation so Pytalon remembers
    what's happening and can respond intelligently.

    """

    def __init__(self):
        self.history = []
        self.topics_learned = []
        self.first_question = None
        self.last_question = None
        self.current_state = "greeting"

    # ------ HISTORY MANAGEMENT ------

    def add_to_history(self, user_input, Pytalon_response):
        """Adds a user + Pytalon exchange to history."""
        self.history.append({
            "user_input": user_input,
            "Pytalon_response": Pytalon_response
        })

    def add_message_to_history(self, role, content):
        """Saves a single message. role = 'user' or 'Pytalon'"""
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        """Returns the full conversation history."""
        return self.history

    def get_recent_history(self, n=5):
        """Returns the most recent n messages."""
        return self.history[-n:]

    def clear_history(self):
        """Clears the conversation history."""
        self.history = []

    def get_last_message(self):
        """Returns the last message, or None if empty."""
        if self.history:
            return self.history[-1]
        return None

    def get_pytalon_last_response(self):
        """Returns Pytalon most recent response."""
        for message in reversed(self.history):
            if message.get("role") == "Pytalon":
                return message["content"]
        return None

    # ------ TOPIC MANAGEMENT ------

    def learn_topic(self, topic_name):
        """Marks a topic as learned. Ignores duplicates."""
        if topic_name not in self.topics_learned:
            self.topics_learned.append(topic_name)

    def has_learned_topic(self, topic_name):
        """Returns True if this topic was already completed."""
        return topic_name in self.topics_learned

    def get_learned_topics(self):
        """Returns all completed topics."""
        return self.topics_learned

    # ------ QUESTION MANAGEMENT ------

    def set_first_question(self, question):
        """Saves the user's very first question of the session."""
        self.first_question = question

    def get_first_question(self):
        """Returns the user's first question."""
        return self.first_question

    def set_last_question(self, question):
        """Saves the user's most recent question."""
        self.last_question = question

    def get_last_question(self):
        """Returns the user's most recent question."""
        return self.last_question

    # ------ STATE MANAGEMENT ------

    def set_state(self, new_state):
        """
        Updates Pytalon current state.
        States: greeting → menu → topic → practice → done
        """
        self.current_state = new_state

    def get_state(self):
        """Returns Pytalon current state."""
        return self.current_state

    # ------ SUMMARY ------

    def get_summary(self):
        """Returns a snapshot of the current session."""
        return {
            "total_messages": len(self.history),
            "topics_learned": self.topics_learned,
            "topics_count": len(self.topics_learned),
            "current_state": self.current_state,
            "last_question": self.last_question,
            "first_question": self.first_question
        }