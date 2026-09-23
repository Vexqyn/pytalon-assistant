# memory_store.py
"""Permanent learner memory for Pytalon — pure Python JSON, no AI."""

import json
import os
from datetime import datetime
import re

import config

# ============================================================
# CONSTANTS — folder names and schema version
# ============================================================

# Code lives in Pytalon_Memory\ — learner data lives in Pytalon_Memory\store\
MEMORY_FOLDER_NAME = "Pytalon_Memory"
STORE_FOLDER_NAME = "store"
PROFILE_FILE = "learner_profile.json"
LONG_TERM_FILE = "long_term_memory.json"
EXPORT_FILE = "memory_report.txt"
SESSION_FOLDER_NAME = "session_snapshots"
SCHEMA_VERSION = 1

# In-RAM cache so post-write summaries do not re-read disk
_MEMORY_CACHE = {"profile": None, "long_term": None}
_PROJECT_ROOT_CACHE = None

# Words that mean "show me the structured box summary"
_BOX_STYLE_HINTS = {
    "stats",
    "stat",
    "report",
    "dump",
    "box",
    "admin",
    "full",
    "fullreport",
    "detailed",
}

# Words that mean "tell me where memory lives"
_PATH_ASK_HINTS = {
    "path",
    "folder",
    "location",
    "where",
    "directory",
    "dir",
}

# Words that mean "write the report to a text file"
_EXPORT_ASK_HINTS = {
    "export",
    "savefile",
    "savetofile",
    "writetofile",
    "memory_report",
    "memoryreport",
    "reportfile",
}

# Human line shown when we offer export — learner just has to ask
_EXPORT_OFFER_LINE = (
    "   • You can export your own memory as a report — "
    "just tell me and I will do it for you."
)
_EXPORT_OFFER_EXAMPLE = (
    '   • Example: say "export memory" or "export my memory as a report".'
)

# Phrases that start a rename request ("call me Ahmed")
_RENAME_PREFIXES = (
    "call me ",
    "name me ",
    "rename me to ",
    "rename me ",
    "change my name to ",
    "change my name ",
    "my name is ",
    "my name's ",
)

# ============================================================
# PATH + SAFE JSON I/O
# ============================================================

def find_project_root():
    """Return the folder that contains learning.py and config.py."""
    global _PROJECT_ROOT_CACHE
    if _PROJECT_ROOT_CACHE and os.path.isfile(
        os.path.join(_PROJECT_ROOT_CACHE, "learning.py")
    ):
        return _PROJECT_ROOT_CACHE

    start = os.path.abspath(os.path.dirname(__file__))
    current = start
    while True:
        # Walk up until we find the real Pytalon project root
        if os.path.isfile(os.path.join(current, "learning.py")) and os.path.isfile(
            os.path.join(current, "config.py")
        ):
            _PROJECT_ROOT_CACHE = current
            return current
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent

    _PROJECT_ROOT_CACHE = start
    return start

def memory_folder():
    """Return the project memory package folder (code + draft files)."""
    return os.path.join(find_project_root(), MEMORY_FOLDER_NAME)

def memory_dir():
    """Return (and create) the store folder where learner JSON is saved."""
    path = os.path.join(memory_folder(), STORE_FOLDER_NAME)
    os.makedirs(path, exist_ok=True)
    return path

def session_snapshots_dir():
    """Return (and create) the dated session snapshot folder under store/."""
    path = os.path.join(memory_dir(), SESSION_FOLDER_NAME)
    os.makedirs(path, exist_ok=True)
    return path

def _now():
    """Local timestamp for autosave fields."""
    return datetime.now().isoformat(timespec="seconds")

def _read_json(filename, default):
    """Read a memory JSON file; bad or missing files return the default."""
    path = os.path.join(memory_dir(), filename)
    if not os.path.isfile(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else default
    except (json.JSONDecodeError, OSError):
        return default

def _write_json(filename, data):
    """Save JSON atomically so a crash cannot leave a half-written file."""
    path = os.path.join(memory_dir(), filename)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)
    return data

def _invalidate_cache(kind=None):
    """Drop cached profile/long-term after external file changes."""
    if kind in (None, "profile"):
        _MEMORY_CACHE["profile"] = None
    if kind in (None, "long_term"):
        _MEMORY_CACHE["long_term"] = None

def _normalize_words(text):
    """Lowercase text and split on non-letters for style hint checks."""
    cleaned = "".join(ch if ch.isalpha() else " " for ch in (text or "").lower())
    return set(cleaned.split())

# ============================================================
# PROFILE — one permanent learner on this computer
# ============================================================

def default_profile():
    """Empty first-run profile shape."""
    return {
        "schema_version": SCHEMA_VERSION,
        "created_at": _now(),
        "updated_at": _now(),
        "name": None,
        "username": None,
        "display_name": None,
        "project_root": find_project_root(),
        "profile_complete": False,
    }

def load_profile():
    """Load learner profile from disk (cached after first read)."""
    if _MEMORY_CACHE["profile"] is not None:
        return _MEMORY_CACHE["profile"]
    data = _read_json(PROFILE_FILE, default_profile())
    _MEMORY_CACHE["profile"] = data
    return data

def save_profile(profile):
    """Autosave the profile and refresh the cache."""
    profile["updated_at"] = _now()
    profile["schema_version"] = SCHEMA_VERSION
    profile["project_root"] = find_project_root()
    if profile.get("name") and not profile.get("display_name"):
        profile["display_name"] = profile["name"]
    if profile.get("name"):
        profile["profile_complete"] = True
    _write_json(PROFILE_FILE, profile)
    _MEMORY_CACHE["profile"] = profile
    return profile

def ensure_learner_profile():
    """Return the permanent learner profile, asking only on first run."""
    profile = load_profile()

    # Already met this learner — greet, don't ask again
    if profile.get("profile_complete") and profile.get("name"):
        print(f"\nWelcome back, {profile['display_name']}! Ready to continue.")
        return profile

    # First run: collect a friendly name, username optional
    print("\nI'll remember you on this computer — no need to tell me every time.")
    name = input("What should I call you? ").strip() or "Learner"
    profile["name"] = name
    profile["display_name"] = name
    username = input("Username (optional, press Enter to skip): ").strip()
    profile["username"] = username or None
    saved = save_profile(profile)
    print(f"\nNice to meet you, {saved['display_name']}! I'll remember you next time.")
    return saved

def rename_learner(new_name):
    """Update the saved display name when the learner says 'call me X'."""
    profile = load_profile()
    cleaned = (new_name or "").strip()
    if not cleaned:
        return profile, "I need a name after that — for example: call me Ahmed"
    # Keep names short and human-readable
    cleaned = " ".join(cleaned.split())[:40]
    profile["name"] = cleaned
    profile["display_name"] = cleaned
    profile["profile_complete"] = True
    save_profile(profile)
    return profile, f"Got it — I'll call you {cleaned} from now on."

def try_extract_rename(user_text):
    """
    Return a new name if the learner asked to be renamed, else None.
    Examples: 'call me Ahmed', 'my name is Qasim'
    """
    text = (user_text or "").strip().lower()
    if not text:
        return None
    for prefix in _RENAME_PREFIXES:
        if text.startswith(prefix):
            rest = text[len(prefix):].strip(" ?!.!")
            rest = rest.strip()
            if not rest:
                return None
            # Not a rename: teaching phrases, questions and junk words
            skip = {
                "ready",
                "fine",
                "ok",
                "okay",
                "good",
                "here",
                "learning",
                "done",
                "confused",
                "stuck",
                "what",
                "who",
                "nothing",
                "nobody",
                "whatever",
                "anything",
                "someone",
                "something",
            }
            if rest in skip:
                return None
            # Guard the permanent profile: a question is never a rename.
            if "?" in text:
                return None
            
            # Guard: single-word responses that are clearly not a name
            if len(rest.split()) == 1:
                for word in ("not", "no", "maybe", "unsure", "dont", "don't"):
                    if rest.strip() == word:
                        return None
            cleaned = " ".join(rest.split())

            # Guard: must have at least one letter, and be 2-30 chars long
            has_alpha = any(ch.isalpha() for ch in cleaned)
            if not has_alpha or not 2 <= len(cleaned) <= 30:
                return None
            
            # Guard: Block common phrases that are clearly not a name
            _uncertain_phrases = {
                "not sure", "not sure about", "not sure man",
                "dont know", "don't know", "do not know",
                "no idea", "no ideas", "idk",
                "not sure yet", "still deciding", "dunno",
                "no name", "none", "nothing yet",
                "i don't know", "i dont know",
            }
            if cleaned in _uncertain_phrases:
                return None
            if not all(ch.isalpha() or ch in "'- " for ch in cleaned):
                return None
            if len(cleaned.split()) > 3:
                return None
            # Re-cap words lightly for a friendly name
            return " ".join(w.capitalize() for w in cleaned.split())
    return None

# ============================================================
# LONG-TERM PROGRESS — the learner database
# ============================================================

# Long-term memory helps the assistant to remember what the learner has completed, what they practiced, and their preferences.
def default_long_term():
    """Empty progress database shape."""
    return {
        "schema_version": SCHEMA_VERSION,
        "updated_at": _now(),
        "topics_learned": [],
        "practice_completed": {},
        "preferences": {
            "likes_examples": None,
            "last_topic": None,
            "defer_count": 0,
        },
        "stats": {
            "session_count": 0,
            "topics_total_completed": 0,
            "practice_attempts_total": 0,
            "last_session_date": None,
            "last_practice_date": None,
        },
        "sessions": [],
    }

# Load and save the long-term memory JSON file, with caching to avoid repeated disk reads.
def load_long_term():
    """Load long-term progress from disk (cached after first read)."""
    if _MEMORY_CACHE["long_term"] is not None:
        return _MEMORY_CACHE["long_term"]
    data = _read_json(LONG_TERM_FILE, default_long_term())

    # Fill newer keys if an older file is on disk
    base = default_long_term()
    for key, value in base.items():
        if key not in data:
            data[key] = value
    if "preferences" in data and isinstance(data["preferences"], dict):
        for key, value in base["preferences"].items():
            data["preferences"].setdefault(key, value)
    if "stats" in data and isinstance(data["stats"], dict):
        for key, value in base["stats"].items():
            data["stats"].setdefault(key, value)
    _MEMORY_CACHE["long_term"] = data
    return data

# Save the long-term memory JSON file, updating the timestamp and schema version, and refreshing the cache.
def save_long_term(data):
    """Autosave progress and refresh the cache."""
    data["updated_at"] = _now()
    data["schema_version"] = SCHEMA_VERSION
    _write_json(LONG_TERM_FILE, data)
    _MEMORY_CACHE["long_term"] = data
    return data

# Remember that a topic has been completed.
def remember_topic_completed(topic_name):
    """Mark a lesson topic as completed and update last-topic preference."""
    data = load_long_term()
    if topic_name and topic_name not in data["topics_learned"]:
        data["topics_learned"].append(topic_name)
    if topic_name:
        data.setdefault("preferences", {})["last_topic"] = topic_name
    stats = data.setdefault("stats", {})
    stats["topics_total_completed"] = len(data.get("topics_learned") or [])
    return save_long_term(data)

# Remember a practice attempt, including whether it was completed, and update the practice statistics.
def remember_practice(topic_name, completed):
    """Record a practice attempt (and whether it finished)."""
    data = load_long_term()
    practice = data.setdefault("practice_completed", {})
    stats_row = practice.get(topic_name, {"attempts": 0, "completed": False})
    stats_row["attempts"] = int(stats_row.get("attempts", 0)) + 1
    if completed:
        stats_row["completed"] = True
    stats_row["last_practice_at"] = _now()
    practice[topic_name] = stats_row
    totals = data.setdefault("stats", {})
    totals["practice_attempts_total"] = sum(
        int(row.get("attempts", 0)) for row in practice.values()
    )
    totals["last_practice_date"] = _now()
    return save_long_term(data)

# Remember a defer (pause / not-now) action.
def remember_defer():
    """Count a pause / not-now so memory can mention it later."""
    data = load_long_term()
    prefs = data.setdefault("preferences", {})
    prefs["defer_count"] = int(prefs.get("defer_count", 0)) + 1
    return save_long_term(data)

# Remember that a lesson was taught right now, even if it is not completed yet.
def remember_topic_taught(topic_name):
    """Update last-topic the moment teaching starts and track this session's taught topics."""
    if not topic_name:
        return load_long_term()
    data = load_long_term()
    data.setdefault("preferences", {})["last_topic"] = topic_name
    taught = data.setdefault("topics_taught_session", [])
    if topic_name not in taught:
        taught.append(topic_name)
    return save_long_term(data)

# Merge one session's derived style counters into the lifetime behavior database.
def remember_behavior_snapshot(snapshot):

    # Roll a session's derived patterns (never raw text) into long-term behavior totals.

    data = load_long_term()

    b = data.setdefault("behavior", {})

    for key in config.BEHAVIOR_COUNTER_KEYS:

        if key in snapshot:

            b[key] = int(b.get(key, 0) or 0) + int(snapshot.get(key) or 0)

    revisits = b.setdefault("topic_revisits", {})

    for topic, count in (snapshot.get("taught_counts") or {}).items():

        revisits[topic] = int(revisits.get(topic, 0) or 0) + int(count or 0)

    return save_long_term(data)

# Restore the session context from the long-term memory, so that the assistant can continue where it left off.
def seed_context_from_memory(context):
    """Copy permanent topics into the session RAM object."""
    data = load_long_term()
    if data.get("topics_taught_session"):
        # Previous session ended without a clean exit — start this one fresh
        data["topics_taught_session"] = []
        save_long_term(data)
    for topic in data.get("topics_learned", []):
        try:
            context.learn_topic(topic)
        except Exception:
            pass
    return context

# ============================================================
# SESSION SNAPSHOTS — optional per-exit JSON for offline review
# ============================================================

# Record the end of a session, including the topics touched, the derived style patterns, and the last state, and write an optional dated snapshot file for offline review.
def record_session_end(topics_touched=None, last_state="done", behavior_snapshot=None):
    """Bump session counters, merge derived style patterns, and write an optional dated snapshot file."""
    data = load_long_term()
    stats = data.setdefault("stats", {})
    stats["session_count"] = int(stats.get("session_count", 0)) + 1
    stats["last_session_date"] = _now()

    # Merge this session's derived patterns into the lifetime behavior database
    if behavior_snapshot:
        try:
            remember_behavior_snapshot(behavior_snapshot)
        except Exception:
            behavior_snapshot = None

    sessions = data.setdefault("sessions", [])
    touched = list(topics_touched or [])
    for taught_name in list(data.get("topics_taught_session") or []) + list(
        (behavior_snapshot or {}).get("taught_counts") or {}
    ):
        if taught_name not in touched:
            touched.append(taught_name)
    session_row = {
        "started_at": data.get("updated_at"),
        "ended_at": _now(),
        "topics_touched": touched,
        "last_state": last_state,
    }
    # Per-session style summary — derived ratios only, never raw text
    snapshot = behavior_snapshot or {}
    msgs = int(snapshot.get("messages_total") or 0)
    if msgs:
        session_row["style"] = {
            "messages": msgs,
            "casual_ratio": round(int(snapshot.get("casual_messages") or 0) / msgs, 2),
            "emoji_ratio": round(int(snapshot.get("emoji_messages") or 0) / msgs, 2),
            "question_ratio": round(int(snapshot.get("question_messages") or 0) / msgs, 2),
            "duration_minutes": snapshot.get("duration_minutes") or 0,
            "topics_taught": len(snapshot.get("taught_counts") or {}),
        }
    sessions.append(session_row)
    # Keep the list from growing without bound
    if len(sessions) > 50:
        del sessions[:-50]
    # Taught topics are session-scoped: archived into the session row, then reset
    data["topics_taught_session"] = []
    save_long_term(data)

    # Optional per-exit snapshot written for the founder's offline review
    try:
        stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        snap_path = os.path.join(session_snapshots_dir(), f"{stamp}_session.json")
        payload = {
            "schema_version": SCHEMA_VERSION,
            "saved_at": _now(),
            "profile": load_profile(),
            "long_term": data,
            "session": session_row,
        }
        with open(snap_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
    except OSError:
        pass
    return data

# Check if there is new practice in the current session.
def has_new_practice_this_session():
    """Check whether any practice was completed in the CURRENT session.

    Compares practice_completed[topic]['last_practice_at'] timestamps
    against the previous session's ended_at to detect new progress.
    This is session-aware: a topic completed in a PRIOR session does
    NOT count.
    """
    try:
        data = load_long_term()
        sessions = data.get("sessions", [])
        practice = data.get("practice_completed", {})

        # If there are no prior sessions, any completed practice counts
        if not sessions:
            for row in practice.values():
                if row.get("completed") and row.get("last_practice_at"):
                    return True
            return False

        # Get the end timestamp of the most recent session
        last_ended = sessions[-1].get("ended_at")

        # If we can't read ended_at, fall back to "any completed practice"
        if not last_ended:
            for row in practice.values():
                if row.get("completed") and row.get("last_practice_at"):
                    return True
            return False

        # Compare each topic's last_practice_at against the last session end
        for row in practice.values():
            if row.get("completed") and row.get("last_practice_at"):
                if row.get("last_practice_at") >= last_ended:
                    return True
        return False
    except Exception:
        return False

# learning.py imports this name on exit / interrupt paths
def remember_session_end(topics_touched=None, last_state="done", behavior_snapshot=None):

    # Alias used by learning.py when the session ends.

    return record_session_end(
        topics_touched=topics_touched,
        last_state=last_state,
        behavior_snapshot=behavior_snapshot,
    )

# ============================================================
# SUMMARIES — what Pytalon says out loud
# ============================================================

# Get the learner's display name for use in messages and reports.
def _learner_display_name():
    """Friendly name for greetings and reports."""
    profile = load_profile()
    return profile.get("display_name") or profile.get("name") or "Learner"

# Get the first topic that has not yet been completed, based on the predefined list of topics in intro.py.
def _next_unfinished_topic():
    """First menu topic not yet completed (rule-based suggestion)."""
    try:
        from intro import TOPICS
    except Exception:
        return None
    data = load_long_term()
    done = set(data.get("topics_learned") or [])
    revisits = (data.get("behavior") or {}).get("topic_revisits") or {}
    candidates = [name for _num, name in TOPICS.items() if name not in done]
    if not candidates:
        return None
    # Learners who revisited a topic get that topic suggested first
    return max(candidates, key=lambda n: int(revisits.get(n, 0) or 0))

# Build a short welcome-back summary that is shown once at startup, including the learner's name, completed topics, and suggested next topic.
def build_welcome_summary():
    """Short welcome-back flash shown once at startup."""
    try:
        name = _learner_display_name()
        data = load_long_term()
        topics = data.get("topics_learned") or []
        next_topic = _next_unfinished_topic()
        lines = [f"\nWelcome back, {name}!"]
        if not topics:
            lines.append("📌 No topics completed yet — let's start when you're ready.")
        else:
            shown = ", ".join(topics[:5])
            extra = f" (+{len(topics) - 5} more)" if len(topics) > 5 else ""
            lines.append(
                f"📌 So far: {len(topics)} topic(s) completed ({shown}{extra})."
            )
        if next_topic:
            lines.append(f"👉 Suggested next: {next_topic}")
        lines.append('💬 Ask me "what do you remember?" anytime for the full memory.')
        lines.append(_EXPORT_OFFER_LINE)
        return "\n".join(lines)
    except Exception:
        return ""

# Build a tiny recap printed after a lesson is stored, including the topic name, total completed topics, and suggested next topic.
def build_topic_saved_summary(topic_name):
    """Tiny recap printed after a lesson is stored."""
    try:
        data = load_long_term()
        n = len(data.get("topics_learned") or [])
        next_topic = _next_unfinished_topic()
        lines = [
            "",
            f"✅ Saved to memory: {topic_name}",
            f"📌 Total completed: {n} — ask \"what do you remember?\" anytime.",
        ]
        if next_topic and next_topic != topic_name:
            lines.append(f"👉 Suggested next: {next_topic}")
        return "\n".join(lines)
    except Exception:
        return ""

# Build a structured summary of the learner's profile and progress, used by both human-readable and box-style reports.
def build_summary_lines():
    """Structured fields used by both human and box report styles."""
    profile = load_profile()
    data = load_long_term()
    name = profile.get("display_name") or profile.get("name") or "Learner"
    user = profile.get("username")
    who = f"{name} (@{user})" if user else name
    topics = data.get("topics_learned") or []
    practice = data.get("practice_completed") or {}
    prefs = data.get("preferences") or {}
    stats = data.get("stats") or {}
    return {
        "who": who,
        "name": name,
        "username": user,
        "root": profile.get("project_root") or find_project_root(),
        "folder": memory_dir(),
        "topics": list(topics),
        "practice": practice,
        "last_topic": prefs.get("last_topic"),
        "taught_session": list(data.get("topics_taught_session") or []),
        "behavior": data.get("behavior") or {},
        "defer_count": prefs.get("defer_count", 0),
        "updated": data.get("updated_at"),
        "stats": stats,
        "next_topic": _next_unfinished_topic(),
    }

# Format the summary for human-readable output.
def _format_human_report(s):
    """Human assistant bullet list (default voice)."""
    practice = s.get("practice") or {}
    stats = s.get("stats") or {}
    lines = [
        "",
        "🧠 Here's what I remember about you (saved on this computer):",
        f"   • Name: {s['name']}",
        f"   • Username: {s['username'] or '(not set)'}",
        f"   • Project folder: {s['root']}",
        f"   • Memory store: {s['folder']}",
        f"   • Topics completed: {', '.join(s['topics']) if s['topics'] else 'none yet'}",
        f"   • Topics count: {len(s['topics'])}",
        f"   • Last topic: {s['last_topic'] or '(none yet)'}",
        f"   • Topics taught this session: {', '.join(s['taught_session']) if s['taught_session'] else 'none yet'}",
        f"   • Times you paused/deferred: {s['defer_count']}",
        f"   • Sessions remembered: {stats.get('session_count', 0)}",
        f"   • Practice attempts total: {stats.get('practice_attempts_total', 0)}",
        f"   • Memory last updated: {s['updated'] or '(unknown)'}",
    ]
    if s.get("next_topic"):
        lines.append(f"   • Suggested next topic: {s['next_topic']}")
    if practice:
        lines.append("   • Practice record:")
        for topic, row in practice.items():
            done = "done" if row.get("completed") else "not completed"
            lines.append(
                f"       - {topic}: {row.get('attempts', 0)} attempt(s), {done}"
            )
    else:
        lines.append("   • Practice record: none yet")
    try:
        from pytalon_body.behavior_learner import describe_behavior_lines
        lines.extend(describe_behavior_lines(s.get("behavior") or {}))
    except Exception:
        pass
    lines.append("   • I remember how you learn, not what you said — patterns and progress only, never full chats.")
    lines.append(_EXPORT_OFFER_LINE)
    lines.append(_EXPORT_OFFER_EXAMPLE)
    return "\n".join(lines)

# Format the summary for a structured box-style report.
def _format_box_report(s):
    """Structured box summary when the learner asks for stats/report/dump."""
    practice = s.get("practice") or {}
    stats = s.get("stats") or {}
    bar = "─" * 48
    lines = [
        "",
        "┌── PYTALON MEMORY SUMMARY " + "─" * 20 + "┐",
        f"│ Learner: {s['who']}",
        f"│ Project: {s['root']}",
        f"│ Memory store: {s['folder']}",
        "│",
        f"│ Topics completed ({len(s['topics'])})",
    ]
    if s["topics"]:
        for i, topic in enumerate(s["topics"], 1):
            lines.append(f"│   {i}. {topic}")
    else:
        lines.append("│   (none yet)")
    lines.append("│")
    lines.append("│ Practice")
    if practice:
        for topic, row in practice.items():
            done = "completed" if row.get("completed") else "not completed"
            lines.append(
                f"│   {topic} — {row.get('attempts', 0)} attempt(s), {done}"
            )
    else:
        lines.append("│   (none yet)")
    lines.append("│")
    lines.append(f"│ Sessions: {stats.get('session_count', 0)}")
    lines.append(f"│ Practice attempts: {stats.get('practice_attempts_total', 0)}")
    lines.append(f"│ Last topic: {s['last_topic'] or 'none yet'}")
    taught_session = s.get("taught_session") or []
    lines.append("│ Taught this session: " + (", ".join(taught_session) if taught_session else "none yet"))
    lines.append(f"│ Pauses/defers: {s['defer_count']}")
    if s.get("next_topic"):
        lines.append(f"│ Suggested next: {s['next_topic']}")
    lines.append(f"│ Last saved: {s['updated'] or 'unknown'}")
    lines.append("│")
    try:
        from pytalon_body.behavior_learner import describe_behavior_lines
        for style_line in describe_behavior_lines(s.get("behavior") or {}):
            lines.append("│ " + style_line.strip())
    except Exception:
        pass
    lines.append("│ Store: patterns + progress (never full chats)")
    lines.append("└" + bar + "┘")
    return "\n".join(lines)

# ============================================================
# MEMORY REPORT — always answer, never silent-fail
# ============================================================

# Format a memory summary in varios styles, including short, full, human-readable, box-style, and goodbye messages.
def format_memory_summary(style="full"):
    """
    Build a printable memory summary.

    style: 'short' | 'full' | 'human' | 'box' | 'goodbye'
    Always returns a string. Never raises.
    """
    try:
        s = build_summary_lines()
    except Exception:
        return (
            "\n🤖 Memory files live in Pytalon_Memory, but I could not read "
            "them right now. Nothing is lost on disk — try again."
        )

    if style == "short":
        n = len(s["topics"])
        last = s["last_topic"] or "none yet"
        return (
            f"\n📌 Memory: {s['who']} — {n} topic(s) done, last: {last}. "
            f"Say \"what do you remember?\" for details.\n"
            f"{_EXPORT_OFFER_LINE}"
        )

    if style == "goodbye":
        display = s["name"]
        stats = s.get("stats") or {}
        lines = [
            "",
            f"👋 Goodbye, {display}!",
            "📌 Here's your session memory summary:",
            f"   • Topics completed: {len(s['topics'])}"
            + (f" — {', '.join(s['topics'])}" if s["topics"] else ""),
            f"   • Last topic: {s['last_topic'] or 'none yet'}",
            f"   • Practice records: {len(s['practice'])} topic(s)",
            f"   • Pauses: {s['defer_count']}",
            f"   • Sessions remembered: {stats.get('session_count', 0)}",
            f"   • Saved in: {s['folder']}",
            "   • Next time I'll say welcome back — you won't re-enter your name.",
            _EXPORT_OFFER_LINE,
            _EXPORT_OFFER_EXAMPLE,
        ]
        return "\n".join(lines)

    if style == "box":
        return _format_box_report(s)

    if style == "human":
        return _format_human_report(s)

    # Default full = human assistant list (tests + trust voice)
    return _format_human_report(s)

# ============================================================
# MEMORY REPORT — human-readable, printable, exportable
# ============================================================

# Build a full human-readable memory report for the learner, used when they ask "what do you remember?".
def build_memory_report():
    """Full human-readable answer body for 'what do you remember?'."""
    return format_memory_summary("human")

# Print the full human-readable memory report to the console.
def print_memory_report():
    """Print the full human memory report."""
    print(build_memory_report())

# Export the full human-readable memory on user request, writing it to a text file in the memory store folder.
def export_memory_report():
    """Write the human report to Pytalon_Memory/memory_report.txt."""
    try:
        report = build_memory_report()
        path = os.path.join(memory_dir(), EXPORT_FILE)
        with open(path, "w", encoding="utf-8") as f:
            f.write(report.strip() + "\n")
        return path, report
    except Exception as exc:
        return None, (
            "\n🤖 I could not export the memory report right now "
            f"({exc}). Your saved JSON files are still safe."
        )

# ============================================================
# MEMORY ASK — always answer, never silent-fail
# ============================================================

# Handle user requests to see what the assistant remembers, including renaming, path inquiries, export requests, and report styles.
def handle_memory_ask(user_text=""):
    """
    Answer any 'what do you remember?' style question.

    Also handles: rename, path, export, box vs human report style.
    Always prints something useful.
    """
    text = (user_text or "").strip()
    lowered = text.lower()
    words = _normalize_words(text)

    # Rename: "call me Ahmed" / "my name is Qasim"
    new_name = try_extract_rename(text)
    if new_name:
        try:
            _profile, message = rename_learner(new_name)
            print(f"\n{message}")
            print('💬 Ask me "what do you remember?" anytime to see your profile.')
            print(_EXPORT_OFFER_LINE)
        except Exception:
            print("\nI could not save that name right now — try again in a moment.")
        return

    # Path questions
    if words & _PATH_ASK_HINTS or "memory path" in lowered:
        try:
            folder = memory_dir()
            root = find_project_root()
            print("\n📁 Your Pytalon memory is saved on this computer:")
            print(f"   • Project: {root}")
            print(f"   • Memory package: {memory_folder()}")
            print(f"   • Memory store (data): {folder}")
            print(f"   • Profile file: {os.path.join(folder, PROFILE_FILE)}")
            print(f"   • Progress file: {os.path.join(folder, LONG_TERM_FILE)}")
            print(_EXPORT_OFFER_LINE)
            print(_EXPORT_OFFER_EXAMPLE)
        except Exception:
            print(
                "\nI keep memory under a folder named Pytalon_Memory next to "
                "learning.py, but I could not open that path right now."
            )
        return

    # Export to text file — only when the learner asks; assistant does it for them
    wants_export = bool(words & _EXPORT_ASK_HINTS) or "export" in lowered
    if not wants_export:
        try:
            from config import MEMORY_EXPORT_PATTERNS
            wants_export = any(
                phrase in lowered for phrase in MEMORY_EXPORT_PATTERNS
            )
        except Exception:
            wants_export = False

    if wants_export:
        path, _report = export_memory_report()
        if path:
            print("\n📄 Done — you asked, so I exported your memory report for you.")
            print(f"   File: {path}")
            print('   I will not export unless you tell me (e.g. "export memory").')
        else:
            print(_report)
            print(_EXPORT_OFFER_LINE)
        return

    # Box-style when they ask for stats/report/dump
    style = "human"
    if words & _BOX_STYLE_HINTS:
        style = "box"

    try:
        print(format_memory_summary(style))
    except Exception:
        print(
            "\n🤖 I keep your memory in this project folder (Pytalon_Memory), "
            "but I could not read it right now. Nothing is lost on disk — "
            "try again, or check that the folder exists."
        )
