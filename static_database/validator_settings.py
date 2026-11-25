"""Answer-validation settings (static data)."""

# Score needed for a similarity-based match.
MATCH_THRESHOLD = 0.75
EXAMPLES_MATCH_THRESHOLD = 0.65

# Minimum shared keywords for a strong match.
MIN_OVERLAP = 2

# Explicit answer words used to break ties and catch mixed answers.
YES_WORDS = {'yes', 'yeah', 'yep', 'yup', 'ok', 'okay', 'sure', 'y', 'ye'}
NO_WORDS = {'no', 'nope', 'nah', 'naw', 'n', 'whatever'}
DECLINE_WORDS = {'nope', 'nah'}
