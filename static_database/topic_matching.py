"""Patterns used to classify topic-related requests."""

TOPIC_MATCH_THRESHOLD = 0.65

BEGINNER_PATTERNS = [
    r'\bbeginner\b', r'\bnewbie\b', r'\bnovice\b',
    r'\bi\s+(want|wanted|would like|need)\s+to\s+(learn|lean|study)\b',
    r'\blearn python\b', r'\bpython beginner\b',
    r'\bgetting started\b',
    r'\bhelp me learn\b', r'\bcan you help me\b',
    r'\b(i\s+)?need(ed)?\s+help\b', r'\bhelp me (with|to)\b',

    # Additional beginner regexes
    r'\bnew to programming\b', r'\bnew to coding\b',
    r'\bstarting python\b', r'\bpython from zero\b',
    r'\babsolute beginner\b', r'\bnever programmed\b',
    r'\bfirst time coding\b', r'\bteach me like a beginner\b',
    r'\bjust starting out\b', r'\bcompletely new\b',
    r'\btotal beginner\b', r'\bbeginner here\b',
    r'\bi know nothing\b', r'\bknow nothing about\b',
    r'\bnew to this\b', r'\bstarting from scratch\b',
    r'\bscratch please\b', r'\bfirst timer\b',
    r'\bnoob\b', r'\bn00b\b',
]

QUESTION_PATTERNS = [
    r'\bwhat\b', r'\bhow\b', r'\bwhy\b', r'\bwhen\b',
    r'\bwhere\b', r'\bwho\b', r'\bwhich\b',
    r'\bcould\b', r'\bwould\b', r'\bshould\b', r'\bexplain\b',

    # Additional question regexes
    r'\bcan\b', r'\bmay\b', r'\bmight\b', r'\bwhereas\b',
    r'\bwhat if\b', r'\bhow can\b', r'\bhow do i\b',
    r'\bwhose\b', r'\bwhom\b', r'\bwhether\b',
    r'\bdescribe\b', r'\bdefine\b', r'\bclarify\b',
]

NEGATION_WORDS = {
    # Basic negations
    'no', 'not', "don't", 'dont', 'nope', 'nah', 'naw', 'never',
    'none', 'nobody', 'nothing', 'nowhere', 'neither', 'nor',
    'cannot', "can't", 'could not', "couldn't", 'would not', "wouldn't",
    'should not', "shouldn't", 'is not', "isn't", 'are not', "aren't",
    'was not', "wasn't", 'were not', "weren't", 'hard pass', 'big pass',

    # Soft / partial negations
    'not sure', 'not really', 'not interested', 'not feeling it',
    'not at all',
    'not exactly', 'not particularly', 'not quite', 'not necessary',
    'not in the mood', 'not vibing with it', 'not on my watch',
    'maybe not', 'probably not', 'definitely not', 'absolutely not',
    'certainly not',
    'not sure yet', "i don't think so", 'i dont think so',
    'no way', 'no thanks', 'no need', 'no worries',

    # Additional negation forms
    'never mind', 'no longer', 'not anymore', 'without',
    'hardly', 'barely',
    'not now', 'not today', 'do not', 'does not', 'wont',
    'never ever', 'not ever', 'not once',
    'lost interest', 'no longer interested', 'not for me',
}

FILLER_WORDS = {
    'i', 'me', 'my', 'the', 'a', 'an', 'is', 'it', 'to', 'do',
    'of', 'in', 'on', 'at', 'be', 'am', 'are', 'was', 'were',
    'this', 'that', 'and', 'or', 'but', 'so', 'for', 'with',
    'just', 'like', 'bro', 'man', 'fam', 'yo', 'hey', 'hi',

    # Additional fillers
    'really', 'very', 'please', 'maybe', 'well', 'actually',
    'basically', 'probably', 'still', 'already', 'again',
    'some', 'any', 'kinda', 'sorta', 'gonna', 'wanna', 'gotta',
    'tho', 'though', 'btw', 'tbh', 'ngl', 'yall',
}
