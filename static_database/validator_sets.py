"""Small validator-specific word sets and normalization helpers."""

_EXIT_FIRST_WORDS = {
    'exit', 'quit', 'bye', 'goodbye', 'leave', 'end', 'stop',
    'close', 'finish', 'finished', 'done', 'later', 'logout', 'logoff',
    'cancel', 'abort', 'terminate', 'shutdown', 'shut', 'signoff', 'signout',

    # farewell / departure variants
    'adios', 'adieu', 'farewell', 'sayonara', 'ciao', 'arrivederci',
    'aufwiedersehen', 'wiedersehen', 'seeya', 'seeyah', 'byebye',
    'bye-bye', 'laters', 'lata', 'peaceout', 'catchya', 'cyall',
    'goodnight', 'nite', 'nighty', 'gn',
}

_CASUAL_FILLERS = {
    'dude', 'dudes', 'bro', 'bros', 'man', 'fam', 'buddy', 'pal',
    'homie', 'dawg', 'brother', 'please', 'pls', 'yo',
    'ok', 'okay', 'yeah', 'yep', 'yup', 'now', 'today', 'fr',
    'friend', 'mate', 'chief', 'boss', 'thanks', 'thx',
    'quickly', 'soon', 'alright', 'hey', 'hi', 'sure',
    'right', 'then', 'again', 'gang', 'gurl', 'girl', 'sir',
    'madam', 'maam', 'ma', 'dear', 'hun', 'honey', 'plz',
    'sup', 'wassup', 'wsg', 'wyd', 'yall', 'cuz', 'cousin',

    # new address forms
    'cuh', 'blud', 'bruv', 'blood', 'playa', 'compadre',
    'amigo', 'mon', 'ami', 'partner', 'chum', 'matey', 'sib',
    'folks', 'guys', 'gals', 'ladies', 'gents', 'yous',
    "y'all", "ya'll",
    'bby', 'bb', 'boo', 'sweetie', 'sweetheart', 'love',
    'sister', 'dearie', 'mister', 'miss', 'mr', 'ms',

    # new greetings / interjections
    'hiya', 'heya', 'howdy', 'greetings', 'ssup', 'heyo',

    # new attitudinal fillers
    'seriously', 'actually', 'literally', 'honestly', 'truthfully',
    'definitely', 'totally', 'absolutely', 'truly', 'really',

    # new acknowledgment / gratitude fillers
    'ty', 'tysm', 'yw', 'cheers', 'ta',
    'okie', 'oke', 'okey', 'okeydokey',
    'ya', 'yea', 'yeh', 'yah', 'yiss',
}

_TEACH_OK_REST = {
    'this', 'it', 'topic', 'this topic', 'about it', 'about this',
    'about this topic', 'please', 'bro', 'man', 'dude', 'fam', 'buddy',
    'more', 'now', 'ok', 'okay',
    'again', 'next', 'part', 'lesson', 'step', 'example',
    'slowly', 'for me',
    'from scratch', 'from the start', 'in detail', 'in simple terms',
    'with examples', 'with practice', 'step by step',
    'properly', 'thoroughly', 'fully', 'clearly', 'plainly', 'well',
    'something', 'something new', 'everything', 'all', 'a bit',

    # new rest-of-phrase entries
    'the topic', 'the lesson', 'the concept', 'the idea', 'the subject',
    'some more', 'a bit more', 'a little more', 'a lot',
    'the whole thing', 'from the beginning', 'from the very start',
    'with code', 'with output', 'with an example', 'with a demo',
    'in plain english', 'in layman terms', 'like a beginner',
    'over and over', 'one more time',
    'as a demo', 'as a refresher',
    'to me', 'to us', 'for us',
    'tonight', 'tomorrow',
    'first', 'starting now', 'right now', 'for now',
    'bit by bit', 'one bit at a time',
    'with visuals', 'with a visual',
    'the full thing', 'the long version', 'the short version',
    'all of it', 'the whole shebang',
    'without jargon', 'in detail please',
    'simply', 'easily', 'gently', 'patiently',
}

_TEACH_PREFIXES = (
    'please ',
    'yes ',
    'ok ',
    'okay ',
    'yeah ',
    'can you ',
    'could you ',
    'you can ',
    'go ahead ',
    'go on ',
    'sure ',
    'would you ',
    'will you ',
    'please can you ',
    'could you please ',
    'would you please ',
    'can you please ',
    'i want you to ',
    'i would like you to ',
    'alright ',
    'yep ',
    'yup ',
    'sure thing ',
    'go ahead and ',
    'go on and ',
    'will you please ',
    'could you kindly ',
    'kindly ',
    'pls ',
    'plz ',
    'yes please ',
    'ok please ',
)

SIMPLE_TOKENS = {
    'yes', 'yeah', 'yep', 'yup', 'no', 'nope', 'nah', 'ok', 'okay',
    'sure', 'exit', 'quit', 'bye', 'afk', 'brb', 'later', 'maybe',
    'defer', 'skip', 'pass', 'continue', 'ready',
    'course',
    'finished', 'pause', 'wait', 'again', 'next',
    'teach', 'explain', 'practice',
    'cancel', 'abort', 'logout', 'logoff', 'question', 'help',
    'topic', 'lesson',
    'hmm', 'huh', 'well', 'just', 'resume', 'restart', 'reset',
    'tonight', 'tomorrow', 'now', 'k', 'kk', 'okie', 'ya', 'ye',

    # new simple tokens
    'yeah man', 'yes sir', 'no sir', 'yes ma', 'no ma',
    'ty', 'tysm', 'thx', 'cheers',
    'aight', 'ight', 'oke', 'okey', 'okeydokey',
    'hmmph', 'hmpf', 'meh',
    'go', 'go on', 'go ahead',
    'lol', 'lmao',
    'nvm', 'nm', 'np',
    'sorry', 'oops', 'my bad',
    'quick', 'fast', 'soon',
    'fine', 'cool', 'nice', 'great', 'noice',
    'clarify', 'define', 'describe', 'show', 'tell',
    'sec', 'min', 'mo',
}

_SKIP_PHRASES = (
    'skip',
    'skip it',
    'skip the',
    'skip this',
    'skip topic',
    'pass on',
    'move on',
    'next topic',
    'next please',
    'skip this lesson',
    'skip the lesson',
    'pass this time',
    'not this topic',
    'move to another topic',
    'skip this topic',
    'pass this lesson',
    'move on please',
    'choose another topic',
    'skip that',
    'skip ahead',
    'skip forward',
    'skip over',
    'jump to next',
    'next one',
    'move to next',
    'change topic',
    'switch topic',
    'different topic',
    'something else',
    'anything else',
    'not this one',
)

_UNCERTAIN_TOKENS = (
    'maybe', 'perhaps', 'not sure', 'unsure', 'dunno', 'idk',
    'possibly', 'probably', 'i think', 'i guess', 'on the fence',
    'not certain', 'not decided', 'could be', 'might be',
    'idk yet', 'maybe not', 'possibly not', 'doubtful', 'unclear',
    'confused', 'mixed feelings', 'hesitant', 'undecided',
    'pass for now', 'ask later', 'come back to me',
)

# ---------------------------------------------------------------------------
# Append block 1 — daily-life casual forms
# ---------------------------------------------------------------------------

_EXIT_FIRST_WORDS.update({
    'cya', 'ttyl', 'gtg', 'peace', 'out', 'dismiss', 'depart',
    'laterz', 'dip', 'ghosting', 'sliding', 'bouncing',
})

_CASUAL_FILLERS.update({
    'yo', 'mate', 'buddy', 'friend', 'pal', 'chief', 'boss',
    'thanks', 'thx', 'quickly', 'soon', 'alright',
    'dawg', 'homie', 'bud', 'bub', 'hun', 'love', 'silly',
    'sista', 'sis', 'kin', 'cuzz',
})

_TEACH_OK_REST.update({
    'again', 'next', 'part', 'lesson', 'step', 'example',
    'slowly', 'for me', 'fully', 'well', 'properly', 'clearly',
    'simply', 'fast', 'quick', 'fast please', 'quick please',
})

_TEACH_PREFIXES += (
    'let us ',
    'lets ',
    "let's ",
    'i need you to ',
    'i want to be taught ',
    'show me ',
    'help me ',
    "let's go and ",
    'lets go and ',
    'allow me to ask ',
    'any chance you could ',
    'any way you could ',
)

SIMPLE_TOKENS.update({
    'c',  # single-letter continue
    'cont', 'done', 'finish',
    'more', 'all', 'none', 'back',
    'start', 'begin', 'go',
    'nice one', 'great job', 'well done',
})

_SKIP_PHRASES += (
    'skip a step',
    'skip the intro',
    'not now skip',
    'pass for now',
    'on to the next',
    'skip please',
    'skip this round',
    'skip this part',
    'skip that one',
    'skip that part',
    'skip the topic',
    'move along',
    'move past this',
    'next up',
    'next lesson',
)

_UNCERTAIN_TOKENS += (
    'not sure yet',
    'unsure about this',
    'hmm not sure',
    'hold on',
    'let me think',
    'give me a second',
    'hang on',
    'wait a sec',
    'give me a mo',
    'one sec please',
    'gimme a moment',
    'let me chew on it',
    'let me mull it over',
    'i need a moment',
)

# ---------------------------------------------------------------------------
# Append block 2 — polished / formal forms
# (the four tuple entries that previously duplicated the base have been removed)
# ---------------------------------------------------------------------------

_EXIT_FIRST_WORDS.update({
    'logout', 'logoff', 'signoff', 'signout', 'kill', 'exitnow',
    'departing', 'resigning', 'bowing',
})

_CASUAL_FILLERS.update({
    'okay', 'sure', 'right', 'then', 'now', 'again',
    'bro', 'man', 'fam', 'gang', 'bestie', 'queen', 'king',
    'bosslady', 'bossman', 'champ', 'tiger', 'sunshine',
})

_TEACH_OK_REST.update({
    'from scratch', 'from the start', 'in detail', 'in simple terms',
    'with examples', 'with practice', 'step by step',
    'for a beginner', 'for dummies', 'like i am five',
    'with a quick example', 'with a small example',
    'with a real example', 'with a good example',
    'with output please',
})

_TEACH_PREFIXES += (
    'could you be so kind and ',
    'could you be so kind as to ',
    'if you could ',
    'if you would ',
    'if you would be so kind ',
    'at your convenience ',
)

SIMPLE_TOKENS.update({
    'explain', 'question', 'help', 'topic', 'lesson',
    'why', 'how', 'what', 'when', 'where', 'who',
    'stop', 'end', 'leave', 'quit',
    'proceed', 'proceed please', 'please proceed',
})

_SKIP_PHRASES += (
    'different one please',
    'i want a different lesson',
    'give me another subject',
    'this one is not for me',
    'i will try another one',
    'try another topic please',
    'let us switch topics',
    'change the subject please',
    'another lesson please',
)

_UNCERTAIN_TOKENS += (
    'perhaps later',
    'maybe next time',
    'i will decide later',
    'still on the fence',
    'ask me tomorrow',
    'let us revisit later',
    'perhaps another time',
    'maybe in a bit',
)

# ---------------------------------------------------------------------------
# Append block 3 — ultra-casual / Gen-Z forms
# ---------------------------------------------------------------------------

_EXIT_FIRST_WORDS.update({
    'late', 'outtie', 'deuces', 'bounce', 'dip',
    'outy', 'outie', 'dueces', 'skrt',
})

_CASUAL_FILLERS.update({
    'aight', 'ight', 'aiight', 'aite', 'brah', 'bruh', 'brudda',
    'cuzzo', 'cuz', 'fam', 'g', 'brother', 'sista', 'sis',
    'gang gang', 'famalam', 'chile', 'homes', 'homeslice',
    'brosky', 'broseph', 'bae',
})

_TEACH_OK_REST.update({
    'a bit at a time', 'one step at a time', 'slowly but surely',
    'the basics', 'the fundamentals', 'the essentials',
    'at my own pace', 'whenever you can', 'when you have time',
})

_TEACH_PREFIXES += (
    'please show me how to ',
    'could you walk me through ',
    'walk me through ',
    'teach ',
    'kindly please ',
    'please kindly ',
    'now please ',
    "i'd appreciate it if you'd ",
)

SIMPLE_TOKENS.update({
    'afk', 'brb', 'hold', 'wait a sec', 'one moment',
    'quickly', 'now', 'soon', 'later',
    'sec', 'min', 'mo', 'secs', 'mins',
})

_SKIP_PHRASES += (
    'nothing for now',
    'not this time',
    'another time',
    'leave it for later',
    'not rn',
    'not today',
    'nah not rn',
    'skip later',
    'skip for now',
    'leave this topic for later',
)

_UNCERTAIN_TOKENS += (
    'i am not sure',
    'not yet sure',
    'unsure still',
    'need to think',
    'still deciding',
    'still weighing',
    'i have not decided',
    'let me sleep on it',
    'dunno yet honestly',
    'might decide later',
)