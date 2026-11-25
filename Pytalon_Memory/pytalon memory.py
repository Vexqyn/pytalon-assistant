"""Pytalon session journal — derived events only, never raw chat text.

This module is used by ``Pytalon_Memory.memory_store`` when a session
ends. It keeps the original file and repairs its logic: no message text
is ever written, only abstracted patterns and progress events.
"""

import json
import os
from datetime import datetime

# The only fields the journal will ever store. Raw text is not allowed.
ALLOWED_FIELDS = {
    "messages_total", "casual_messages", "emoji_messages",
    "answer_yes", "answer_no", "practice_pass", "practice_fail",
    "topic", "state", "generation",
}

MAX_EVENTS = 200


class SessionJournal:
    """A small, privacy-respecting journal of derived session events."""

    def __init__(self, store_dir):
        self.path = os.path.join(store_dir, "session_journal.json")
        self.events = self._load()["events"]

    def _load(self):
        if os.path.isfile(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as handle:
                    data = json.load(handle)
                if isinstance(data, dict) and isinstance(data.get("events"), list):
                    return data
            except (json.JSONDecodeError, OSError):
                pass
        return {"schema_version": 2, "events": []}

    def record(self, kind, **fields):
        """Record one derived event. Any raw text field is dropped."""
        clean = {key: value for key, value in fields.items() if key in ALLOWED_FIELDS}
        self.events.append({
            "at": datetime.now().isoformat(timespec="seconds"),
            "kind": kind,
            **clean,
        })
        self._save()

    def recent(self, limit=20):
        """Return the most recent derived events."""
        return self.events[-limit:]

    def _save(self):
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as handle:
            json.dump(
                {"schema_version": 2, "events": self.events[-MAX_EVENTS:]},
                handle,
                indent=2,
                ensure_ascii=False,
            )
        os.replace(tmp, self.path)


def open_journal(store_dir):
    """Open (or create) the session journal in a store folder."""
    return SessionJournal(store_dir)


if __name__ == "__main__":
    # Standalone demo: write one derived event, then read it back.
    import sys

    store_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "store"
    )
    os.makedirs(store_dir, exist_ok=True)

    journal = open_journal(store_dir)
    journal.record(
        "demo",
        messages_total=3,
        casual_messages=2,
        emoji_messages=1,
        state="done",
    )
    print("Journal file:", journal.path)
    for event in journal.recent():
        print(event)
