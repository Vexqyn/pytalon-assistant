"""Memory system settings (static data)."""

# Folder and file names.
MEMORY_FOLDER_NAME = "Pytalon_Memory"
STORE_FOLDER_NAME = "store"
PROFILE_FILE = "learner_profile.json"
LONG_TERM_FILE = "long_term_memory.json"
EXPORT_FILE = "memory_report.txt"
SESSION_FOLDER_NAME = "session_snapshots"
SCHEMA_VERSION = 1

# Words that mean "show me the structured box summary".
_BOX_STYLE_HINTS = {
    "stats", "stat", "report", "dump", "box", "admin",
    "full", "fullreport", "detailed",
}

# Words that mean "tell me where memory lives".
_PATH_ASK_HINTS = {
    "path", "folder", "location", "where", "directory", "dir",
}

# Words that mean "write the report to a text file".
_EXPORT_ASK_HINTS = {
    "export", "savefile", "savetofile", "writetofile",
    "memory_report", "memoryreport", "reportfile",
}

_EXPORT_OFFER_LINE = (
    "   • You can export your own memory as a report — "
    "just tell me and I will do it for you."
)
_EXPORT_OFFER_EXAMPLE = (
    '   • Example: say "export memory" or "export my memory as a report".'
)

# Phrases that start a rename request ("call me Ahmed").
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

# Single words that are clearly not a name.
_RENAME_SKIP_WORDS = {
    "ready", "fine", "ok", "okay", "good", "here", "learning",
    "done", "confused", "stuck", "what", "who", "nothing",
    "nobody", "whatever", "anything", "someone", "something",
    "not", "no", "maybe", "unsure", "dont", "don't",
}

# Phrases that are clearly not a name.
_RENAME_UNCERTAIN_PHRASES = {
    "not sure", "not sure about", "not sure man",
    "dont know", "don't know", "do not know",
    "no idea", "no ideas", "idk",
    "not sure yet", "still deciding", "dunno",
    "no name", "none", "nothing yet",
    "i don't know", "i dont know",
}
