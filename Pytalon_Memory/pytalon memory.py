import json
import os
from datetime import datetime


class PytalonAssistant:
    def __init__(self):
        self.name = "Pytalon Assistant"
        self.version = "2.3"
        self.creator = "M. Qasim. Farooqi (Acubura)"
        self.memory = []
        self.conversation_history = []
        self.load_memory()
        self.context_messages = []

    def add_to_memory(self, entry):
        self.memory.append({
            "timestamp": datetime.now().isoformat(),
            "entry": entry,
        })
        self.save_memory()

    def save_memory(self):
        with open("memory.json", "w") as f:
            json.dump(self.memory, f, indent=2)

    def load_memory(self):
        if os.path.exists("memory.json"):
            with open("memory.json", "r") as f:
                self.memory = json.load(f)

    def respond(self, user_input):
        self.context_messages.append("User: " + user_input)
        if len(self.context_messages) > 20:
            self.context_messages = self.context_messages[-20:]
        self.add_to_memory("User: " + user_input)
        reply = "Memory stored."
        self.context_messages.append("Pytalon: " + reply)
        return reply


if __name__ == "__main__":
    pytalon = PytalonAssistant()
    print("Pytalon: Hi, I'm Pytalon Assistant. Just talk to me naturally. I'll learn as we go.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["exit", "quit", "bye"]:
            print("Pytalon: Goodbye! I'll remember our conversation.")
            break
        response = pytalon.respond(user_input)
        print("Pytalon: " + response)
