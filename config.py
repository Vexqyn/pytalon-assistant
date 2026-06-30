# config.py
"""Constants and response lists for Pytalon's input validation."""

# ----- RESPONSE CATEGORIES (Constants for better readability) -----
YES_RESPONSES = [
    # Simple yes
    'yes', 'y', 'yeah', 'yep', 'yup', 'sure', 'okay', 'ok', 'alright', 'of course',
    'absolutely', 'definitely', 'for sure', 'indeed', 'correct',
    # Ready / let's go
    "let's go", 'lets go', "let's do it", 'lets do it', "let's learn", 'lets learn',
    "let's start", 'lets start', "let's begin", 'lets begin', 'go ahead', 'proceed',
    'go for it', 'do it', 'run it', 'send it',
    # Ready states
    "i'm ready", 'im ready', 'ready', 'ready to learn', 'ready to go', 'i am ready',
    'i am so ready', 'so ready', 'been ready',
    # Teaching / learning intent
    'teach me', 'teach me this topic', 'i want to learn this topic',
    'i want to learn', 'i want to learn more', 'wanted to learn more',
    'show me', 'show me more', 'continue', 'keep going',
    # Gen-Z / Millennial slang - hype
    'lock in', 'lock in bro', 'lock in bro! i want to learn',
    'fr', 'fr fr', 'no cap', 'bet', 'bet bet',
    'slay', 'periodt', 'say less', 'say less bro', 'say less fam',
    'lowkey yes', 'highkey yes', 'lowkey wanna learn', 'highkey wanna learn',
    'hit me', 'hit me with it', 'drop it', 'drop the knowledge',
    'spill', 'spill it', 'yasss', 'yass', 'yas',
    # Casual hype phrases
    "fr! let's do it!", 'ngl! i am excited to learn this topic',
    'tbh! i want to learn this topic', 'yeah! teach me man',
    "of course! lets learn this new topic", 'lock in bro! i want to learn',
    # Millennial casual
    'sounds good', 'sounds great', 'works for me', 'im down', "i'm down",
    'i am down', 'totally', 'totes', '100', '100 percent',
    'one hundred percent', 'a hundred percent',
    'heck yes', 'heck yeah', 'hell yeah', 'oh yeah', 'oh yes',
    'yesss', 'yessir', 'yes sir', 'legit yes',
    # Short positive confirmations
    'sure thing', 'sure man', 'sure bro', 'you bet', 'you got it',
    'on it', 'im on it', "i'm on it", 'lets get it', "let's get it",
    'lets get started', "let's get started", 'lets go bro', 'lets gooo',
    'lesgo',
    # Missing common affirmations
    'right on', 'word', 'true', 'true that', 'big yes', 'hard yes', 'hell to the yes',
    'yeppers', 'yeet', 'yessum', 'yessiree', 'fo sho', 'for sho', '4sho', 'mos def',
    # Casual/Texting style
    'kk', 'k', 'mhm', 'uh huh', 'uhuh', 'mmhmm', 'ya', 'yaaas', 'yeeeees',
    # Non-native / Simple
    'ja', 'si', 'oui', 'da', 'hai', 'correcto', 'affirmative', 'roger', 'copy that',
    # Contextual learning affirmations
    'hit me with it', 'i am listening', 'im listening', 'ready when you are',
    'lay it on me', 'bring it on', 'i am all ears', 'im all ears', 'let her rip',
    # Typos (common)
    'yeha', 'yse', 'yew', 'yeh', 'yeap', 'yepyep', 'yupyup', 'okkey', 'okei', 'oke',
]

NO_RESPONSES = [
    # Simple no
    'no', 'n', 'nope', 'nah', 'nah bro', 'nah fam', 'nah man',
    'negative', 'not really', 'not at all', 'no way', 'no thanks',
    # Skip / pass
    'pass', 'skip', 'skip the topic', 'move on', 'move on to next topic',
    'skip it', 'pass on this', 'ima pass', "i'm gonna pass",
    # Not now
    'not now', 'not right now', 'not at the moment', 'skip for now', 'pass for now', 
    'hmmm! not sure yet', 'not sure yet', 'need to think about it', 'let me think about it',
    'nah! not interested right now', 'nuh uh! not interested right now',
    # Not interested
    'not interested', 'not feeling it', "i'm not feeling it", 'im not feeling it',
    "i don't feel like it", 'i dont feel like it', 'not in the mood',
    "i'm not in the mood", 'im not in the mood', 'not vibing with it',
    # Good / fine
    "i'm good", 'im good', 'i am good', "i'm fine", 'im fine', 'i am fine',
    "i'm okay", 'im okay', 'i am okay', 'all good', 'all good bro',
    # Gen-Z / Millennial slang
    'nuh uh', 'nuh uh! i am good for now', 'nah! i am not going to continue further',
    'hard pass', 'big pass', 'imma pass', 'gonna pass',
    'nope nope', 'nahh', 'lowkey no', 'lowkey dont want to',
    'im chillin', "i'm chillin", 'im good chillin',
    # Longer natural phrases
    'i dont have plans to learn this topic', 'i dont want to learn anything',
    'no way! i dont want to learn', 'not on my watch today! no learning today',
    "i'll pass", 'i am fine dont want to learn today',
    'i am not going to continue further',
    # Soft negatives
    'not particularly', 'not exactly', 'hardly', 'barely', 'not quite',
    # Casual/Texting
    'nop', 'noper', 'nopity nope', 'nahh', 'naah', 'naw', 'hell naw', 'heck naw',
    # Non-native / Simple
    'nein', 'non', 'nyet', 'iie', 'negatory', 'negative ghost rider',
    # Contextual rejection
    'i am set', 'im set', 'i am good to go', 'im good to go', 'no need thanks',
    'pass hard', 'skip me', 'dont need it', 'not necessary',
    # Typos
    'noo', 'nooo', 'nope nope nope', 'nopee', 'nahh man', 'naa', 'na',
]

EXIT_RESPONSES = [
    # Direct exit commands
    'exit', 'e', 'quit', 'bye', 'goodbye', 'leave', 'end', 'stop',
    'done', 'finish', 'finished', 'close', 'shut it down',
    # Enough
    "that's enough", 'enough', 'enough for today', 'enough for now',
    'thats enough', 'thats enough for today',
    # Dipping out slang
    'dipping', 'dipping out', 'dipping out for now', 'im dipping',
    "i'm dipping", 'im out', "i'm out", 'i am out', 'im outta here',
    "i'm outta here", 'peace', 'peace out', 'peace bro',
    'im ghost', "i'm ghost", 'bouncing', 'im bouncing',
    "i'm gonna bounce, so bye for now", 'gonna bounce', 'im gonna bounce',
    # Bye variations
    'bye bye', 'byeee', 'cya', 'ciao', 'ttyl', 'ttyl bro',
    'talk later', 'catch you later', 'catch ya later', 'see ya', 'see you',
    'see you later', 'see ya later', 'aight bye', 'alright bye',
    # Quitting / stopping
    'i want to exit', 'i want to quit', 'i want to stop', 'i want to leave',
    'exit the session', 'end the session', 'quit the session',
    'i am taking a relaxing break', 'taking a break', 'need a break',
    'gonna take a break', 'imma take a break',
    # Gen-Z exit slang
    'logging off', 'log off', 'im logging off',
    'im done fr', 'done fr', 'i am done fr',
    'nah! i dont want to study', 'nuh uh! no more i am quiting',
    'clear out for today! no learning',
    'sorry! but i do not want to learn anything',
    'i am out right now maybe later', 'later bro', 'later fam',
    'no more for today', 'calling it', 'calling it a day', 'calling it quits',
    'wrap it up', 'wrapping up', 'im wrapping up',
    # Casual exits
    'im bouncing out', 'bounce out', 'im heading out', 'heading out', 'later', 
    'im gonna head out', 'gonna head out', 'im clocking out', 'clocking out',
    # Non-native / Simple
    'exit now', 'quit now', 'stop now', 'end now', 'close program', 'shut down',
    # Exhaustion signals
    'im tired', 'i am tired', 'tired', 'exhausted', 'brain fried', 'need rest',
    'taking a break now', 'break time', 'time for a break',
    # Abrupt exits
    'gtg', 'g2g', 'gotta go', 'got to go', 'have to go', 'must go',
    'afk', 'brb',
    # Typos
    'exti', 'quti', 'leve', 'goobye', 'byee', 'byeeee', 'exist', 
]

YES_EXAMPLES_RESPONSES = [
    # Simple yes
    'yes', 'y', 'yeah', 'yep', 'yup', 'sure', 'ok', 'okay', 'of course',
    'absolutely', 'definitely', 'for sure', 'go ahead', 'do it',
    # Show me
    'show me', 'show me examples', 'show examples', 'show me the examples',
    'show me some examples', 'show me more', 'show it', 'show the breakdown',
    'show me the breakdown', 'give me examples', 'give me some examples',
    # I want to see
    'i want to see examples', 'i want to see it', 'i want to see',
    'i want the breakdown', 'i want the details', 'let me see', 'let me see it',
    "let's see it", 'lets see it', 'let me check it out', 'i want to check it out',
    # Please / yes please
    'yes please', 'please show me', 'please show', 'please go ahead',
    'please do', 'yeah please', 'yep please',
    # Example specifically
    'example', 'examples please', 'examples', 'gimme examples', 'gimme an example',
    'gimme the examples', 'hit me with examples', 'drop the examples', 'wanna see examples',
    'wanna know the examples', 'i want to see the examples', 'i want to see an example',
    # Of course variants
    'of course! i want to see the example', 'of course i want',
    'of course! i want the breakdown', 'of course! show me the breakdown', 
    'of course! Man show me the examples', 'of course! lets see the examples', 
    'of course! show me the examples', 'of course! Man',
    'of course man break it down', 'of course! man, break it down',
    # Gen-Z / slang
    'fr! i want to see examples', 'ngl! i am excited to see examples',
    'tbh! i want to see examples', 'yeah! show me more examples',
    'ok! i want to see more examples', 'yup! show me some examples!',
    'hit me', 'hit me with it', 'bring it', 'drop it', 'spill it',
    'bet show me', 'bet', 'say less', 'say less show me',
    'lowkey wanna see', 'lowkey want to see', 'highkey wanna see',
    'no cap show me', 'fr show me', 'send it',
    # Breakdown / details
    'break it down', 'break it down please', 'break it down man', 'i want the breakdown',
    'show me the breakdown', 'give me the breakdown', 'i want to see the breakdown',
    'let me see the breakdown', 'i want to see the details', 'show me the details',
    'give me the details', 'let me see the details',
    # Natural phrases
    "i'd like to see", 'id like to see', 'i want that', 'give it to me', 'give me',
    'that would be great', 'that would help', 'would love to see',
    'sounds good show me', 'works for me', 'im down to see',
    # Enthusiastic about examples
    'show me what you got', 'show me the magic', 'drop the examples',
    'let me see the examples', 'example time', 'time for examples',
    'demo it', 'show demo', 'demonstrate', 'walk me through it',
    # Impatient but yes
    'just show me', 'already show me', 'show me already', 'gimme gimme',
    # Specific to examples
    'need an example', 'need examples', 'example needed', 'sample please',
    'give me a sample', 'show sample', 'sample code', 'show me sample',
    # Non-native
    'example please', 'examples please sir', 'please examples',
]

NO_EXAMPLES_RESPONSES = [
    # Simple no
    'no', 'n', 'nope', 'nah', 'no thanks', 'not now', 'not really',
    'no need', 'no need for examples', 'all good',
    # Skip
    'skip', 'skip it', 'skip examples', 'no examples', 'skip showing examples',
    'skip this particular example', 'just skip', 'ima skip', 'imma skip it',
    # Good without it
    "i'm good", 'im good', 'i am good', "i'm fine without", 'im fine without',
    'i am fine without', "i'm straight", 'im straight', 'i am straight',
    'good without it', 'i am good without examples',
    # Of course variants
    'of course! i am good without examples', 'of course! i dont need examples',
    'of course! Man, don\'t show me examples', 'of course! i am good without it',
    'of course! i don\'t want to see breakdown', 'of course! i am good without the breakdown',
    # Gen-Z / slang
    'nah! i dont want to see examples', 'nuh uh! i am fine without examples',
    'i am good dont show me examples', 'bruh! i dont want to see examples',
    'i am straight nuh uh! i am good without examples', 'i am good nah!',
    'hard pass on examples', 'pass on the examples', 'ima pass on this',
    'lowkey dont want examples', 'not feeling the examples',
    'nah fam', 'nah bro no examples', 'nah no examples',
    'its fine', "it's fine", 'i get it already', 'i got it',
    'i understand already', 'already get it', 'no worries skip it',
    # Confident no
    'got it already', 'already got it', 'i understand it', 'understood',
    'clear enough', 'makes sense already', 'concept clear',
    # Skip specific
    'skip the examples', 'no examples needed', 'examples unnecessary',
    'without examples', 'no demo needed', 'skip demo',
    # Impatient no
    'just move on', 'keep going', 'dont stop', 'continue without',
    'no need to show', 'dont show me',
    # Non-native
    'examples not needed', 'i understand no examples',
]

YES_QUESTION_RESPONSES = [
    # Simple yes
    'yes', 'y', 'yeah', 'yep', 'yup', 'sure', 'of course', 'absolutely',
    'definitely', 'for sure',
    # I have a question
    'i have a question', 'i want to ask a question', 'i have a quick question',
    'i got a question', 'got a question', 'i have something to ask',
    'i wanted to ask you something', 'i wanna ask something', 'i wanna ask',
    'lemme ask', 'let me ask', 'can i ask', 'can i ask something',
    'can i ask you something', 'i need to ask', 'i need to ask something',
    # Help / teach
    'can you help me', 'can you help', 'help me', 'help', 'i need help',
    'i need some help', 'can you teach', 'can you teach me', 'question',
    # Yeah / sure variants
    'yeah! can you help me', 'yeah! i have a question', 'yeah sure',
    'yeah go ahead', 'sure thing', 'sure bro',
    # Gen-Z / slang
    'fr i have a question', 'ngl i have a question', 'lowkey have a question',
    'lowkey wanna ask', 'quick q', 'quick question', 'got a quick q',
    'i got a quick one', 'lemme pick your brain', 'can i pick your brain',
    'i need the tea on this', 'spill on this',
    'can you break it down', 'break it down for me',
    # Curiosity
    'i am curious', 'been wondering', 'i have been wondering',
    'i was thinking', 'just wondering',
    # Question-specific affirmations
    'i got a quick one', 'quick one', 'just one question', 'single question',
    'actually yes', 'wait yes', 'hold up yes',
    # Curiosity signals
    'i am wondering', 'ive been thinking', 'thought about this',
    'curious about', 'curious mind wants to know',
    # Direct question markers
    'query', 'inquiry', 'doubt', 'i have a doubt', 'i got a doubt',
    # Non-native question indicators
    'please answer', 'tell me why', 'explain why', 'clarify this',
]

NO_QUESTION_RESPONSES = [
    # Simple no
    'no', 'n', 'nope', 'nah', 'not really', 'nothing', 'none',
    'no thanks', 'no worries', 'all good', 'im good',
    # No questions
    'no questions', 'no questions for now', 'i do not have a question',
    'i dont have a question', 'i have no questions', 'i got no questions',
    'nothing to ask', 'nothing for now', 'nothing at the moment',
    'no! i do not have a question', 'nah! i do not want to ask a question',
    'nuh uh! i do not want to ask anything', 'nuh! i do not have any questions',
    # Skip
    'skip questions', 'skip it', 'just skip', 'no need',
    # Gen-Z / slang
    'nah fam no questions', 'nah bro im good', 'im straight no questions',
    'lowkey no questions', 'nah im good', 'all clear', 'crystal clear',
    'i understood everything', 'i get it', 'i got it', 'makes sense',
    'it all makes sense', 'understood',
    'we good', "we're good", 'we are good', 'im cool', "i'm cool",
    # Crystal clear indicators
    'crystal', 'clear as day', 'clear as crystal', 'loud and clear',
    'i follow', 'following', 'tracking', 'i track',
    # No need to ask
    'no need to ask', 'nothing comes to mind', 'blank for now',
    'mind is blank', 'all good here',
    # Impatient no-question
    'move along', 'proceed please', 'carry on', 'next please',
    # Non-native
    'no questions sir', 'all clear sir', 'nothing sir',
]

EXIT_QUESTION_RESPONSES = [
    # Direct exit
    'exit', 'e', 'quit', 'bye', 'goodbye', 'leave', 'stop', 'done',
    'end', 'finish', 'close',
    # I want to exit
    'i want to exit', 'i want to quit', 'i want to leave', 'i want to stop',
    'i want to leave now', 'exit the session', 'end the session',
    # Nah / done with it
    'nuh uh! i want to exit', 'nah! i want to exit', 'no! i want to exit',
    'nah! i am fine', 'i am good for now', 'i am fine for now',
    "i'm good for now", 'im good for now', 'im done for now',
    "i'm done for now", 'done for today', 'done for now',
    'sorry! but i do not want to learn anything',
    # Gen-Z / slang
    'im out', "i'm out", 'im outta here', "i'm outta here",
    'peace', 'peace out', 'dipping', 'im dipping', 'bouncing',
    'logging off', 'log off', 'ttyl', 'catch you later', 'later',
    'aight im out', 'aight bye', 'aight im done',
    'done fr', 'im done fr', 'calling it', 'calling it a day',
    'wrapping up', 'wrap it up', "that's all for now", 'thats all for now',
    # Exit during question phase
    'forget my question', 'never mind exiting', 'cancel question exit',
    'no question just exit', 'exit without question',
    # Frustrated exit
    'im done asking', 'done with questions', 'question phase over',
]

SIMPLE_RESPONSES = ['yes', 'y', 'no', 'n', 'ok', 'okay', 'exit', 'e', 'quit', 'bye']

QUESTION_WORDS = [
    'what', 'how', 'why', 'when', 'where', 'who', 'which', 
    'can', 'is', 'are', 'do', 'does', 'should', 'could', 'would', 'will'
]

PYTHON_TERMS = [
    'python', 'function', 'variable', 'hello world', 'relational operator',
    'assignment operator', 'logical operator', 'type conversion', 'input function',
    'comments', 'strings', 'programming', 'coding', 'data types', 'conditional statements',
    'if statement', 'else statement', 'elif statement', 'nested conditionals', 'Indexing & Slicing',
    'Strings Operations', 'Strings Formating'
]

# ----- CONVERSATIONAL PATTERNS -----
GREETING_PATTERNS = [
    'hi', 'hello', 'hey', 'good morning', 'good afternoon', 
    'good evening', 'howdy', 'what\'s up', 'sup', 'yo',
    'heya', 'hi there', 'hello there', 'greetings'
]

FAREWELL_PATTERNS = [
    'bye', 'goodbye', 'see you', 'see ya', 'cya',
    'take care', 'catch you later', 'peace out', 'farewell',
    'have a good day', 'good night', 'until next time', 'adios'
]

GRATITUDE_PATTERNS = [
    'thanks', 'thank you', 'thx', 'ty', 'appreciate it',
    'much appreciated', 'thank you so much', 'thanks a lot',
    'awesome thanks', 'great thanks', 'perfect thanks'
]

CONFUSION_PATTERNS = [
    'i don\'t understand', 'not clear', 'confused', 
    'what do you mean', 'explain again', 'i\'m lost',
    'can you repeat', 'say that again', 'huh', 'what',
    'i didn\'t get it', 'didn\'t understand', 'unclear',
    'i\'m not following', 'i don\'t get it'
]

# Uncertain responses (optional category for maybe/not sure)
UNCERTAIN_RESPONSES = [
    'maybe', 'perhaps', 'possibly', 'could be', 'not sure',
    'i dont know', 'i dunno', 'dunno', 'uncertain', 'undecided',
    'leaning yes', 'leaning no', '50 50', 'fifty fifty',
    'kinda', 'sorta', 'sort of', 'kind of',  'maybe later',
    'not sure yet'
]

# Repeat request patterns
REPEAT_REQUEST_PATTERNS = [
    'say again', 'come again', 'repeat that', 'repeat please',
    'one more time', 'again please', 'can you repeat', 'please repeat',
    'what did you say', 'i missed that', 'didnt catch that',
    'last part again', 'from the top', 'explain again',
]

# Clarification patterns
CLARIFICATION_PATTERNS = [
    'what do you mean by', 'define', 'define please',
    'meaning of', 'definition of', 'what is meant by',
    'in other words', 'simpler terms', 'layman terms',
    'breakdown of', 'elaborate', 'expand on',
]

TOPIC_KEYWORDS = {
    'Hello World': [
        'hello world', 'first program', 'print statement', 'printing', 'basic output'
    ],
    'Functions': [
        'function', 'functions', 'def', 'method', 'reusable code', 'modular'
    ],
    'Variables': [
        'variable', 'variables', 'var', 'storage', 'assign', 'assignment', 'store value'
    ],
    'Relational operators': [
        'relational operator', 'relational operators', 'relational',
        'comparison', 'compare', 'equal to', 'greater than', 'less than', '==', '!=', '>=', '<=', '>', '<'
    ],
    'Assignment operators': [
        'assignment operator', 'assignment operators', 'assignment',
        '+=', '-=', '*=', '/=', '%=', '//=', '**=', 'shortcut operators'
    ],
    'Logical operators': [
        'logical operator', 'logical operators', 'logical',
        'and or not', 'boolean logic', 'true false'
    ],
    'Type conversion': [
        'type conversion', 'type conversions', 'convert', 'conversion',
        'type cast', 'int()', 'str()', 'float()', 'bool()'
    ],
    'Input function': [
        'input function', 'input()', 'input', 'user input', 'keyboard input',
        'get input', 'read input'
    ],
    'Comments in Python': [
        'comments', 'comment', '#', 'documentation', 'explain code', 'notes'
    ],
    'Strings in Python': [
        'strings', 'string', 'text', 'character', 'words', 'sentence',
        'concatenate', 'slicing', 'string operations', 'string formatting'
    ],
    'Data types in Python': [
        'data types', 'data type', 'datatypes', 'integer', 'float', 'boolean',
        'list', 'tuple', 'dictionary', 'data type in python'
    ],
    'Conditional statements': [
        'conditional statements', 'conditional statement', 'conditionals',
        'if else', 'elif', 'condition', 'decision', 'branch', 'choose', 'if statement'
    ],
}

TOPIC_REQUEST_PATTERNS = [
    'teach me', 'tell me about', 'i want to learn', 'explain to me',
    'show me how', 'how do i', 'what is', 'what are', 'how to',
    'can you teach', 'i need to learn', 'help me with', 'i want to know',
    'tell me more', 'elaborate on', 'what about', 'i\'d like to learn',
    'wanna learn', 'tryna learn', 'tryna get into', 'lowkey tryna learn',
    'tryna understand', 'need to learn', 'tryna get good at', 'tryna master',
    'tryna study', 'tryna figure out', 'wanted to learn', 'i wanted to learn',
    'i wanna learn', 'im tryna learn', 'lemme learn', 'let me learn',
    'hook me up with', 'drop some knowledge on', 'school me on',
    'break it down for me', 'spill the tea on', 'fill me in on',
    'help me learn', 'can you help me', 'i needed help'
]

PRACTICE_REQUEST_PATTERNS = [
    'let me practice', 'want to practice', 'give me exercises',
    'test me', 'quiz me', 'challenge me', 'try it myself',
    'let me try', 'i want to code', 'coding practice', 'hands on'
]

HELP_PATTERNS = [
    'help', 'what can you do', 'how does this work', 
    'what should i do', 'options', 'menu', 'what\'s available',
    'what topics', 'show topics', 'list topics'
]

# Threshold for Smart Detection in Conservation Intent Detection - can be adjusted based on testing and user feedback for better accuracy
TOPIC_MATCH_THRESHOLD = 0.65


BEGINNER_PATTERNS = [
    r'\bbeginner\b', r'\bnewbie\b', r'\bnovice\b',
    r'\bi\s+(want|wanted|would like|need)\s+to\s+(learn|lean|study)\b',
    r'\bteach me\b', r'\bcan you teach\b',
    r'\blearn python\b', r'\bpython beginner\b',
    r'\bgetting started\b',
    r'\bhelp me learn\b', r'\bcan you help me\b',
    r'\b(i\s+)?need(ed)?\s+help\b', r'\bhelp me (with|to)\b',
]

QUESTION_PATTERNS = [
    r'\bwhat\b', r'\bhow\b', r'\bwhy\b', r'\bwhen\b',
    r'\bwhere\b', r'\bwho\b', r'\bwhich\b', r'\bcan\b',
    r'\bcould\b', r'\bwould\b', r'\bshould\b', r'\bexplain\b'
]

# Expanded negation words for better detection in user input, especially for yes/no validation
NEGATION_WORDS = {
    # Existing
    'no', 'not', "don't", 'dont', 'nope', 'nah', 'naw', 'never', 
    'none', 'nobody', 'nothing', 'nowhere', 'neither', 'nor',
    'cannot', "can't", 'could not', "couldn't", 'would not', "wouldn't",
    'should not', "shouldn't", 'is not', "isn't", 'are not', "aren't",
    'was not', "wasn't", 'were not', "weren't", 'hard pass', 'big pass',
    
    # ---- Add these for better coverage ----
    'not sure', 'not really', 'not interested', 'not feeling it',
    'not at all', 'not now', 'not right now', 'not at the moment',
    'not exactly', 'not particularly', 'not quite', 'not necessary',
    'not in the mood', 'not vibing with it', 'not on my watch',
    'maybe not', 'probably not', 'definitely not',
    'not sure yet', "i don't think so", 'i dont think so',
    'no way', 'no thanks', 'no need', 'no worries',
}

FILLER_WORDS = {
        'i', 'me', 'my', 'the', 'a', 'an', 'is', 'it', 'to', 'do',
        'of', 'in', 'on', 'at', 'be', 'am', 'are', 'was', 'were',
        'this', 'that', 'and', 'or', 'but', 'so', 'for', 'with',
        'just', 'like', 'bro', 'man', 'fam', 'yo', 'hey', 'hi', 
        'hello', 'please', 'thanks', 'thank you', 'appreciate it',
}