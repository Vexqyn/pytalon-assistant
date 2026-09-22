# conversation_context.py
"""Temporary session memory for Pytalon (RAM only — not permanent disk memory)."""

import datetime

# Permanent learner data lives in memory_store + Pytalon_Memory/.
# This class only tracks the current chat session.

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
        self.pending_topic = None
        self.topics_taught = []
        self.taught_counts = {}
        self.session_started_at = datetime.datetime.now().isoformat(timespec="seconds")
        self.style = {
            "messages_total": 0,
            "chars_total": 0,
            "caps_messages": 0,
            "emoji_messages": 0,
            "question_messages": 0,
            "casual_messages": 0,
        }

    # ------ HISTORY MANAGEMENT ------

    def add_to_history(self, user_input, Pytalon_response):
        """Add a user + Pytalon exchange to history using role/content schema."""
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "Pytalon", "content": Pytalon_response})

    def add_message_to_history(self, role, content):
        """Save a single message. role = 'user' or 'Pytalon'."""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Return the full conversation history."""
        return self.history

    def get_recent_history(self, n=5):
        """Return the most recent n messages."""
        return self.history[-n:]

    def clear_history(self):
        """Clear the conversation history."""
        self.history = []

    def get_last_message(self):
        """Return the last message, or None if empty."""
        if self.history:
            return self.history[-1]

        return None

    def get_pytalon_last_response(self):
        """Return Pytalon's most recent response."""
        for message in reversed(self.history):
            if message.get("role") == "Pytalon":
                return message["content"]

        return None

    # ------ TOPIC MANAGEMENT ------

    def learn_topic(self, topic_name):
        """Mark a topic as learned. Ignores duplicates."""
        if topic_name not in self.topics_learned:
            self.topics_learned.append(topic_name)

    def has_learned_topic(self, topic_name):
        """Return True if this topic was already completed."""
        return topic_name in self.topics_learned

    def get_learned_topics(self):
        """Return all completed topics."""
        return self.topics_learned

    def mark_topic_taught(self, topic_name):
        """Record that a lesson was taught this session (separate from completed)."""
        if not topic_name:
            return
        if topic_name not in self.topics_taught:
            self.topics_taught.append(topic_name)
        self.taught_counts[topic_name] = self.taught_counts.get(topic_name, 0) + 1

    def get_taught_topics(self):
        """Return all topics taught in this session, completed or not."""
        return list(self.topics_taught)

    def observe_input(self, text):
        """Feed one learner message to the style observer (derived counters only — raw text is never stored)."""
        try:
            from pytalon_body.behavior_learner import observe_text
            signal = observe_text(text or "")
        except Exception:
            return
        self.style["messages_total"] += 1
        self.style["chars_total"] += int(signal.get("chars") or 0)
        for key in ("caps", "emoji", "question", "casual"):
            if signal.get(key):
                self.style[key + "_messages"] += 1

    def note_event(self, kind):
        """Count one behavior event (answer / practice) for the session pattern database."""
        try:
            self.style[kind] = self.style.get(kind, 0) + 1
        except Exception:
            pass

    def get_behavior_snapshot(self):
        """Derived patterns for this session — no raw text, honoring the memory promise."""
        snapshot = dict(self.style)
        snapshot["taught_counts"] = dict(self.taught_counts)
        try:
            started = datetime.datetime.fromisoformat(self.session_started_at)
            snapshot["duration_minutes"] = round(
                (datetime.datetime.now() - started).total_seconds() / 60, 1
            )
        except Exception:
            snapshot["duration_minutes"] = 0
        return snapshot

    # ------ QUESTION MANAGEMENT ------

    def set_first_question(self, question):
        """Save the user's very first question of the session."""
        self.first_question = question

    def get_first_question(self):
        """Return the user's first question."""
        return self.first_question

    def set_last_question(self, question):
        """Save the user's most recent question."""
        self.last_question = question

    def get_last_question(self):
        """Return the user's most recent question."""
        return self.last_question

    # ------ STATE MANAGEMENT ------

    def set_state(self, new_state):
        """Update session state: greeting → menu → topic → practice → done."""
        self.current_state = new_state

    def get_state(self):
        """Return Pytalon's current state."""
        return self.current_state

    # ------ PENDING TOPIC ------

    def set_pending_topic(self, topic_name):
        """Remember a topic the learner asked to switch to mid-prompt."""
        self.pending_topic = topic_name

    def get_pending_topic(self):
        """Return the pending topic name, or None."""
        return self.pending_topic

    # ------ SUMMARY ------

    def get_summary(self):
        """Return a snapshot of the current session."""
        return {
            "total_messages": len(self.history),
            "topics_learned": self.topics_learned,
            "topics_taught": list(self.topics_taught),
            "topics_count": len(self.topics_learned),
            "current_state": self.current_state,
            "last_question": self.last_question,
            "first_question": self.first_question,
        }

# Module-level session instance
context = ConversationContext()
