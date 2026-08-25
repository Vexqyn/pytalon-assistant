# config.py
"""Constants and response lists for Pytalon's input validation."""

# ============================================================
# RESPONSE DATABASE — Natural Human Conversation
# ============================================================

# ----- YES RESPONSES (Complete sentences people actually say) -----

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

    # Teach me variants
    "please teach me", "teach me please", "yes teach me",
    "teach me the topic", "teach me bro", "teach me man", "teach me master",

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
    'yeah! show me more', 'ok! i want to learn more', 'yup! teach me this topic',
    'yeah man!', 'yeah bro!', 'ok bro!', 'ok man!', 'yup bro!', 'yup man!',

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

    # ===== NATURAL CONVERSATIONAL YES SENTENCES =====

    # Complete sentences people actually say
    "yes, that sounds great",
    "yeah, I'm ready to learn",
    "of course, I want to learn this",
    "absolutely, teach me",
    "sure, why not",
    "yeah man, let's do it",
    "okay, I'm listening",
    "alright, go ahead",
    "I'm ready to learn",
    "let's get started",
    "yes please, teach me",
    "yeah, I want to learn more",
    "definitely, show me",
    "for sure, I'm interested",
    "yes, that would be helpful",
    "yeah bro, let's go",
    "ok, I'm ready",
    "alright, let's do this",
    "yeah, teach me something new",
    "sure, I'm all ears",
    "absolutely, I want to understand this",
    "yes, I need to learn this",
    "yeah, hit me with it",
    "of course man, let's learn",
    "yes, go ahead",
    "yeah, I'm excited to learn",
    "okay, let's dive in",
    "for sure, I want to know more",
    "yes, I'm interested in this topic",
    "yeah, show me what you got",
    "definitely, I want to understand",
    "sure, I'm ready when you are",
    "yes, let's learn together",
    "yeah, I'm curious about this",
    "of course, I want to see examples",
    "yes, break it down for me",
    "yeah teach me something",
    "of course I want to learn",
    "sure man I'm ready",
    "yeah bro teach me",
    "yes I want to learn this topic",
    "absolutely teach me more",
    "yeah I'm down to learn",
    "of course I'm interested",
    "yes show me how",
    "yeah let's learn together",
    "for sure I want to understand",
    "yes please I need this",
    "yeah I want to know more",
    "of course I want to see",
    "yes I'm curious about this",
    "yes let's do it", "yeah let's do it",
    "ok let's go", "okay let's go", "ok let's do this",
    "let's begin", "let's start now", "start now",
    "hit me with it", "lay it on me", "bring it on",
    "i'm all in", "im all in", "all in", "count me in",
    "down for it", "down to learn", "down to do this",
    "game on", "let's roll", "lets roll", "rock and roll",
    "fire it up", "fire away", "shoot", "go for it",
    "i'm game", "im game", "i'm down", "im down",
    "sounds like a plan", "sounds good", "sounds perfect",
    "perfect", "excellent", "awesome", "amazing",
    "great idea", "good idea", "brilliant", "love it",
    "would love to", "would love to learn", "love to learn",
    "please do", "please teach", "please go ahead",
    "by all means", "certainly", "definitely yes",
    "affirmative", "roger that", "copy that", "10-4",
    "aye aye", "aye aye captain", "sir yes sir",
    "you got it", "got it", "understood", "crystal clear",
    "let's get cracking", "let's get to it", "time to learn",
    "ready when you are", "whenever you're ready",
    "lead the way", "show me the way", "guide me",
    "i'm yours", "im yours", "all yours", "at your service"
]


# ----- NO RESPONSES (Complete sentences people actually say) -----

NO_RESPONSES = [
    # Simple no
    'no', 'n', 'nope', 'nah', 'nah bro', 'nah fam', 'nah man',
    'negative', 'not really', 'not at all', 'no way', 'no thanks',

    # Skip / pass
    'pass', 'skip', 'skip the topic', 'move on', 'move on to next topic',
    'skip it', 'pass on this', 'ima pass', "i'm gonna pass",

    # Not now - moved to DEFER_PATTERNS
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
    'nop', 'noper', 'nopity nope', 'naah', 'naw', 'hell naw', 'heck naw',

    # Non-native / Simple
    'nein', 'non', 'nyet', 'iie', 'negatory', 'negative ghost rider',

    # Contextual rejection
    'i am set', 'im set', 'i am good to go', 'im good to go', 'no need thanks',
    'pass hard', 'skip me', 'dont need it', 'not necessary',

    # Don't teach / rejection phrases
    "don't teach me", "dont teach me", "do not teach me",
    "don't teach me this", "dont teach me this",
    "don't teach", "dont teach",
    "i don't want you to teach me", "i dont want you to teach me",
    "please don't teach me", "no don't teach me",
    "stop teaching me", "skip teaching me",

    # Typos
    'noo', 'nooo', 'nope nope nope', 'nopee', 'nahh man', 'naa', 'na',

    # ===== NATURAL CONVERSATIONAL NO SENTENCES =====

    # Complete sentences people actually say
    "no, I'm not ready yet",
    "nah, I don't want to learn this",
    "not really, I'm not interested",
    "no thanks, maybe later",
    "I'm not sure about this topic",
    "nah man, I'm good",
    "no, I don't want to learn this right now",
    "not at all, I'm not feeling it",
    "no, I'd rather skip this",
    "nah, not interested in this topic",
    "not right now, maybe later",
    "no, I'm good for now",
    "nah bro, I'm not feeling it",
    "I don't think so, not right now",
    "no way, I'm not interested",
    "nah, I want to learn something else",
    "not yet, maybe next time",
    "no, I'm not in the mood",
    "nah, I'll pass on this one",
    "not today, I'm tired",
    "no, I don't want to study this",
    "nah, teach me something else",
    "not really, I'm not into this",
    "no, let's skip this topic",
    "nah man, I'm good with what I know",
    "no thanks, I'm fine",
    "not right now, I'm busy",
    "nah, I don't need this",
    "no, I'm not interested in learning this",
    "nah bro, teach me something easier",
    "not yet, I'm not ready",
    "no, I want to learn something else",
    "nah, I'm good for today",
    "not really, I don't need this topic",
    "no, let's move on",
    "nah I don't want to learn this",
    "no I'm not interested",
    "not really man",
    "nah I'm good for now",
    "no thanks not now",
    "nah not this topic",
    "no I want something else",
    "not interested in this",
    "nah I'll pass",
    "no I don't need this",
    "not today maybe tomorrow",
    "nah I'm not feeling this",
    "no I'm done with this topic",
    "nah teach me something different",
    "no I don't want to learn about this",
    "nope not happening", "nope nope nope", "no way jose",
    "no chance", "no dice", "no can do", "no go",
    "not a chance", "not in a million years", "never",
    "absolutely not", "definitely not", "certainly not",
    "no thank you", "no thanks at all", "thanks but no thanks",
    "i'll pass", "i pass", "passing", "hard pass",
    "big pass", "mega pass", "ultimate pass",
    "not my thing", "not for me", "doesn't interest me",
    "couldn't care less", "don't care", "whatever",
    "meh", "nah", "nope", "nuh uh", "un uh",
    "i'm good", "im good", "i am good", "i'm fine", "im fine",
    "all good", "all set", "good to go", "set for now",
    "nothing for me", "nothing thanks", "no need",
    "skip it", "skip this", "moving on", "next please",
    "not today", "maybe never", "never mind", "forget it",
    "cancel that", "scratch that", "nevermind",
    "i'm out", "im out", "i'm done", "im done", "done with this"
]


# ----- EXIT RESPONSES (Complete sentences people actually say) -----

EXIT_RESPONSES = [
    # Direct exit commands
    'exit', 'e', 'quit', 'leave', 'end', 'stop',
    'done', 'finish', 'finished', 'close', 'shut it down',

    # Done / enough
    "that's enough", 'enough', 'enough for today', 'enough for now',
    'thats enough', 'thats enough for today',

    # Dipping out slang
    'dipping', 'dipping out', 'dipping out for now', 'im dipping',
    "i'm dipping", 'im out', "i'm out", 'i am out', 'im outta here',
    "i'm outta here", 'peace', 'peace out', 'peace bro',
    'im ghost', "i'm ghost", 'bouncing', 'im bouncing',
    "i'm gonna bounce, so bye for now", 'gonna bounce', 'im gonna bounce',

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
    'im bouncing out', 'bounce out', 'im heading out', 'heading out',
    'im gonna head out', 'gonna head out', 'im clocking out', 'clocking out',

    # Non-native / Simple
    'exit now', 'quit now', 'stop now', 'end now', 'close program', 'shut down',

    # Exhaustion signals
    'im tired', 'i am tired', 'tired', 'exhausted', 'brain fried', 'need rest',
    'taking a break now', 'break time', 'time for a break',

    # Abrupt exits
    'gtg', 'g2g', 'gotta go', 'got to go', 'have to go', 'must go',
    # Typos
    'exti', 'quti', 'leve', 'goobye', 'byee', 'byeeee', 'exist',

    # ===== NATURAL CONVERSATIONAL EXIT SENTENCES =====

    # Complete sentences people actually say
    "I need to go now",
    "I'm done for today",
    "that's all for now",
    "I have to leave",
    "let's wrap it up",
    "I'm finished for today",
    "I should get going",
    "that's enough for today",
    "I want to exit now",
    "I'm going to stop here",
    "I'm done learning for now",
    "let's end this session",
    "I'm going to leave now",
    "that's it for me today",
    "I'm logging off",
    "I need to take a break",
    "I'm going to call it a day",
    "let's stop here",
    "I'm done with this session",
    "I'm going to quit now",
    "that's all I have time for",
    "I'm heading out",
    "I'm done for the day",
    "let's finish here",
    "I want to end this",
    "I'm going to go now",
    "that's enough learning for today",
    "I'm going to take a break now",
    "I'm clocking out",
    "let's wrap this up",
    "ok I'm done for today",
    "alright I'm leaving now",
    "bye I'm done learning",
    "I'm finished with this session",
    "that's it I'm going now",
    "alright I'm out",
    "okay I'm done with this",
    "done for the day",
    "that's enough I'm leaving",
    "I'm going to stop now",
    "time to go",
    "gotta go now",
    "I'm leaving now",
    "that's all bye",
    "okay I'm gonna go",
    "alright I'm heading out",
    "done with this for now",
    "I'm calling it a day",
    "that's enough for me",
    "time to wrap this up",
    "okay I'm finishing now"
]
# ============================================================
# EXAMPLE RESPONSES
# ============================================================

# ------ YES EXAMPLES RESPONSES  -------
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

    # Casual affirmations (mirror of YES_RESPONSES so they work here too)
    'yeah man!', 'yeah man', 'yeah bro!', 'yeah bro', 'ok bro!', 'ok man!',
    'yup bro!', 'yup bro', 'yup man!', 'yup man',
    'sure thing', 'sure man', 'sure bro', 'hell yeah', 'heck yes',
    'oh yeah', 'oh yes', 'yesss', 'yessir', 'yes sir',
    'yeah!', 'yeah', 'yep!', 'yep', 'yup!', 'yup', 'sure!', 'ok!',
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

# ----- NO EXAMPLES RESPONSES  -------
NO_EXAMPLES_RESPONSES = [
    # Simple no
    'no', 'n', 'nope', 'nah', 'no thanks', 'not really',
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

# ============================================================
# QUESTION PHASE RESPONSES
# ============================================================

# ----- YES QUESTION RESPONSES  -------
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

# ----- NO QUESTION RESPONSES  -------
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

# ---- EXIT QUESTION RESPONSES  -------
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
    'logging off', 'log off', 'ttyl', 'catch you later',
    'aight im out', 'aight bye', 'aight im done',
    'done fr', 'im done fr', 'calling it', 'calling it a day',
    'wrapping up', 'wrap it up', "that's all for now", 'thats all for now',

    # Exit during question phase
    'forget my question', 'never mind exiting', 'cancel question exit',
    'no question just exit', 'exit without question',

    # Frustrated exit
    'im done asking', 'done with questions', 'question phase over',
]

# ============================================================
# CONVERSATIONAL PATTERNS (Natural sentences)
# ============================================================

GREETING_PATTERNS = [
    # Simple greetings
    'hi', 'hello', 'hey', 'good morning', 'good afternoon',
    'good evening', 'howdy', 'what\'s up', 'sup', 'yo',
    'heya', 'hi there', 'hello there', 'greetings', 'hey there',
    'hiya', 'hiya!', 'hi there!', 'hello there!', 'hey there!',
    'hai', 'hallou', 'hola', 'bonjour', 'ciao', 'namaste',
    'howdy partner', 'what\'s happening', 'what\'s cracking', 'what\'s good',
    'yo yo', 'yo yo yo', 'ey', 'ayy', 'ayyyy', 'ello', 'ello mate',
    'g\'day', 'howzit', 'how goes it', 'how do you do',

    # ===== NATURAL CONVERSATIONAL GREETINGS =====
    "hello, i'm ready to learn",
    "hi, how are you doing",
    "hey, what's up",
    "good morning, i want to learn python",
    "hello, can you teach me something",
    "hi there, i'm new to this",
    "hey, i'm here to learn",
    "what's up, i'm ready to start",
    "hello, i'm looking for python help",
    "hi, i want to learn programming",
    "hey, how does this work",
    "good afternoon, i'm ready to learn",
    "hello, i need help with python",
    "hi, i'm interested in learning",
    "hey, what can you teach me",
    "good evening, i'm here to learn",
    "hello there, i want to start learning",
    "hi, i'm new to python",
    "hey, teach me something",
    "what's up, i'm ready to learn today",
    "hey man what's up",
    "hi i want to learn python",
    "hello i'm ready to start",
    "what's good i'm here to learn",
    "hey i want to learn programming",
    "hi how are you",
    "hello i need help with python",
    "hey i'm interested in learning",
    "what's up man",
    "hi i'm new here",
    "hey there buddy", "hello friend", "hiya pal", "hey mate",
    "how's it going", "how are things", "how's life",
    "good to see you", "nice to see you", "long time no see",
    "what's new", "what's been up", "how have you been",
    "hey, ready to learn", "hi, let's get started",
    "hello, i'm back", "hey again", "hi once more",
    "good morning sunshine", "morning!", "afternoon!",
    "evening!", "night owl here", "late night coding",
    "just started", "new here", "first time",
    "returning student", "back for more", "ready for lesson"
]

FAREWELL_PATTERNS = [
    # Simple farewells
    'bye', 'goodbye', 'see you', 'see ya', 'cya',
    'take care', 'catch you later', 'peace out', 'farewell',
    'have a good day', 'good night', 'until next time', 'adios',
    'bye bye', 'bye-bye', 'byee', 'byeee', 'laters', 'laterz',
    'ttyl', 'ttfn', 'toodles', 'toodle-oo', 'cheerio', 'cheers',
    'so long', 'fare thee well', 'godspeed', 'safe travels',
    'have a good one', 'take it easy', 'stay safe', 'be well',
    'peace', 'peace out', 'deuces', 'outtie', 'audios', 'adios amigo',
    'sayonara', 'au revoir', 'auf wiedersehen', 'arrivederci',
    'catch ya later', 'catch ya on the flip side', 'see you on the other side',
    'gotta run', 'gotta jet', 'gotta dash', 'gotta split',
    'off i go', 'heading out', 'rolling out', 'bouncing out',
    'logging off now', 'signing off', 'clocking out',

    # ===== NATURAL CONVERSATIONAL FAREWELLS =====
    "goodbye, thanks for your help",
    "see you later, i learned a lot",
    "bye for now, i'll be back",
    "take care, thanks for teaching me",
    "goodbye, i'm done for today",
    "see you next time",
    "bye, i really appreciate your help",
    "until next time, thank you",
    "goodbye, i'll come back when i need help",
    "see ya, thanks for your time",
    "bye, i'm going to practice what i learned",
    "see you around, thank you",
    "take care, i'll be back soon",
    "goodbye, this was really helpful",
    "bye for now, i'll continue later",
    "see you, i need to go",
    "goodbye, i'm done for now",
    "later, i'll come back",
    "see you later, i need to study more",
    "bye, thanks for everything",
    "bye man take care",
    "see you later bro",
    "goodbye i'm leaving now",
    "later i'm done",
    "see you i'm heading out",
    "take care man",
    "bye for now i'll be back",
    "see you around",
    "goodbye thanks for your time",
    "later bro i'm out",
    "bye friend", "farewell friend", "goodbye everyone",
    "thanks for everything, bye", "appreciate it, later",
    "that's all folks", "show's over", "curtain call",
    "signing off for now", "logging out", "going offline",
    "end of session", "session complete", "lesson done",
    "class dismissed", "school's out", "that's a wrap"
]

GRATITUDE_PATTERNS = [
    # Simple gratitude
    'thanks', 'thank you', 'thx', 'appreciate it',
    'much appreciated', 'thank you so much', 'thanks a lot',
    'awesome thanks', 'great thanks', 'perfect thanks',
    'thankyou', 'thankyou!', 'thanks!', 'thx!',
    'thank u', 'thank u so much', 'ty', 'tyvm', 'tyvm!',
    'thanks a bunch', 'thanks a million', 'thanks a ton',
    'many thanks', 'big thanks', 'huge thanks', 'mega thanks',
    'thank you kindly', 'thanks kindly', 'much obliged',
    'gracias', 'merci', 'danke', 'arigato', 'gracias amigo',
    'cheers', 'cheers mate', 'cheers man', 'cheers bro',

    # ===== NATURAL CONVERSATIONAL GRATITUDE =====
    "thanks, that was helpful",
    "thank you for teaching me",
    "i really appreciate your help",
    "thanks for explaining that",
    "thank you, that makes sense now",
    "awesome, thanks for the help",
    "great, i understand now",
    "thanks for the explanation",
    "thank you, i appreciate it",
    "that was really helpful, thanks",
    "i appreciate you taking the time to teach me",
    "thanks, you're a great teacher",
    "thank you, i learned a lot",
    "really appreciate the help",
    "thanks for breaking it down",
    "thank you for your time",
    "awesome, thanks for your help",
    "i appreciate your patience",
    "thank you, that was very helpful",
    "thanks for making it easy to understand",
    "thanks man i appreciate it",
    "thank you this helped a lot",
    "appreciate it bro",
    "thanks for your time man",
    "thank you i understand now",
    "really appreciate your help",
    "thanks that was clear",
    "thank you for explaining",
    "i appreciate you",
    "thanks a lot this helped",
    "thank you so very much", "thanks so very much",
    "can't thank you enough", "cannot thank you enough",
    "you're a lifesaver", "you're the best", "you rock",
    "saved my day", "made my day", "this is gold",
    "exactly what i needed", "perfect explanation",
    "crystal clear now", "finally get it", "clicked for me",
    "lightbulb moment", "aha moment", "eureka",
    "thanks for the clarity", "thanks for the insight",
    "learned so much", "so helpful", "super helpful",
    "incredibly helpful", "amazing help", "fantastic",
    "you explain so well", "great teacher", "best tutor",
    "thank you thank you thank you", "thanks thanks thanks",
    "omg thank you", "omg thanks", "wow thank you",
    "this helped tremendously", "helped a ton", "helped big time"
]

CONFUSION_PATTERNS = [
    # Simple confusion
    'i don\'t understand', 'not clear', 'confused',
    'explain again', 'i\'m lost',
    'can you repeat', 'say that again', 'huh',
    'i didn\'t get it', 'didn\'t understand', 'unclear',
    'i\'m not following', 'i don\'t get it',
    'what?', 'eh?', 'pardon', 'excuse me', 'come again',
    'say what', 'huh what', 'what was that', 'what did u say',
    'i have no idea', 'no clue', 'clueless', 'baffled',
    'perplexed', 'bewildered', 'stumped', 'puzzled',
    'mind blank', 'brain freeze', 'mental block',
    'doesn\'t compute', 'not computing', 'error 404',

    # ===== NATURAL CONVERSATIONAL CONFUSION =====
    "i don't understand this",
    "this is confusing",
    "i'm not following what you're saying",
    "can you explain that again",
    "that doesn't make sense to me",
    "i'm lost, can you repeat that",
    "i didn't understand that",
    "what do you mean by that",
    "i'm not sure i understand",
    "can you say that differently",
    "that's confusing, explain again",
    "i'm not getting it",
    "can you simplify that for me",
    "i'm confused about what you mean",
    "that went over my head",
    "i don't get it, can you explain",
    "i'm struggling to understand",
    "can you break that down more",
    "i'm not clear on that",
    "say that again, i didn't catch it",
    "huh i don't get it",
    "what does that mean",
    "i'm confused",
    "not following you",
    "that makes no sense",
    "can you explain in simpler words",
    "i don't understand what you're saying",
    "say that differently please",
    "i'm lost bro",
    "that was confusing",
    "i'm totally lost", "completely lost", "utterly confused",
    "this makes zero sense", "makes no sense at all",
    "i have no clue what you mean", "no idea what that means",
    "can you dumb it down", "explain like i'm five", "eli5",
    "speak english please", "in plain english", "simple terms",
    "break it down barney style", "step by step please",
    "my brain hurts", "head spinning", "mind blown",
    "that flew over my head", "went right over my head",
    "missed that completely", "didn't catch any of that",
    "say it slower", "too fast", "way too complicated",
    "what language is that", "greek to me", "chinese to me",
    "alien language", "technobabble", "jargon overload"
]

UNCERTAIN_RESPONSES = [
    # Simple uncertain
    'could be', 'not sure',
    'i dont know', 'i dunno', 'dunno', 'uncertain', 'undecided',
    'leaning yes', 'leaning no', '50 50', 'fifty fifty',
    'kinda', 'sorta', 'sort of', 'kind of',
    'not sure yet',

    # ===== NATURAL CONVERSATIONAL UNCERTAINTY =====
    "i'm not sure yet",
    "i don't know if i want to learn this",
    "i'm undecided right now",
    "maybe, i need to think about it",
    "not sure, let me decide later",
    "i'm not sure if i'm ready",
    "maybe later, i need to think",
    "i'm uncertain about this topic",
    "not sure, maybe next time",
    "i don't know yet, let me think",
    "i'm not sure i want to learn this",
    "maybe, i'll decide later",
    "i'm still thinking about it",
    "not sure if i'm interested",
    "i'm not certain yet",
    "maybe, let me consider it",
    "i'm not sure, ask me later",
    "not sure, i need more time",
    "i'm undecided on this",
    "maybe, i'll let you know",
    "hmm i'm not sure",
    "i don't know yet",
    "not sure man",
    "maybe i'm not sure",
    "uncertain right now",
    "let me think about it first",
    "not sure if i'm ready",
    "maybe later i'm not sure",
    "hmm let me think",
    "i'll think about it"
]

# ============================================================
# DEFER/PAUSE PATTERNS — Temporary deferral, not rejection
# ============================================================

DEFER_PATTERNS = [
    # Temporary absence indicators
    'afk', 'brb', 'ttyl', 'be right back', 'away from keyboard',
    'back in a bit', 'back soon', 'returning shortly',
    'brb a sec', 'brb in a min', 'brb in a minute', 'brb shortly',
    'afk for a bit', 'afk for a minute', 'afk for a sec',
    'stepping away', 'stepping out', 'away for a moment',
    'gotta step away', 'need to step away', 'gone for a sec',
    'be back in a flash', 'be right back', 'back in a flash',

    # Explicit deferral
    'not now', 'not right now', 'not at the moment', 'in a bit',
    'some other time', 'later', 'continue later', 'pause for now',
    'come back later', "i'll continue later", "let's do this later",
    'maybe later', 'perhaps later', 'possibly later',
    'not today', 'another time', 'another day', 'next time',
    'rain check', 'take a rain check', 'raincheck',
    'later gator', 'catch you later', 'see you later',
    'come back to this', 'return to this', 'pick this up later',
    'save for later', 'bookmark this', 'flag for later',

    # Pause/hold requests
    'pause', 'hold on', 'wait a moment', 'give me a minute',
    'wait', 'hold up', 'one moment', 'one sec', 'one second',
    'just a moment', 'just a sec', 'give me a second',
    'wait a sec', 'wait a minute', 'wait a moment',
    'hold your horses', 'hold the phone', 'wait wait wait',
    'slow down', 'slow it down', 'one at a time',
    'give me a moment to think', 'let me think', 'thinking',

    # Busy/occupied
    "i'm busy", 'im busy', 'busy right now', "can't now", 'cant now',
    'swamped', 'occupied', 'tied up', 'hectic right now',
    'got my hands full', 'hands full', 'up to my ears',
    'in the middle of something', 'in the middle of work',
    'working on something', 'doing something', 'occupied atm',
    'at work right now', 'at work', 'in a meeting', 'in class',
    'driving', 'cooking', 'eating', 'on the phone', 'on a call',
    'with family', 'with friends', 'running errands', 'out right now',

    # Uncertainty-as-deferral
    'maybe', 'perhaps', 'possibly', 'not sure', 'uncertain',
    'i might', 'i may', 'could be', 'leaning towards later',
    'probably later', 'most likely later', 'thinking about it',
    'considering it', 'mulling it over', 'weighing options',
    'on the fence', 'undecided', 'torn', '50/50',
    'idk yet', 'i don\'t know yet', 'not decided',
    'let me decide later', 'decide later', 'figure it out later'

    # Life happens
    'emergency', 'urgent', 'something came up', 'came up',
    'got interrupted', 'interruption', 'distracted',
    'need to go', 'have to go', 'gotta run', 'running late',
    'late for', 'appointment', 'meeting soon', 'deadline',
    'family thing', 'family emergency', 'personal matter',
    'not feeling well', 'feeling sick', 'under the weather',
    'tired', 'exhausted', 'burnt out', 'brain dead',
    'need a break', 'mental break', 'recharge', 'reset'
]

REPEAT_REQUEST_PATTERNS = [
    'say again', 'come again', 'repeat that', 'repeat please',
    'one more time', 'again please', 'can you repeat', 'please repeat',
    'what did you say', 'what\'s you said', 'whats you said', 'what did you said',
    'i missed that', 'didnt catch that', 'what you said', 'what was that you said',
    'last part again', 'from the top', 'explain again', 'repeat what you said',
    'say that again', 'run that by me again', 'go over that again',
    'what was that', 'what did u say', 'what u said', 'whatcha say',
    'i didnt hear that', 'didn\'t hear', 'missed it', 'missed that',
    'one more time please', 'again one more time', 'repeat once more',
    'can you say that again', 'could you repeat', 'would you repeat',
    'play it back', 'replay that', 'rewind', 'back up a bit',
    'what was the last thing', 'last thing you said', 'previous message',
    'scroll up', 'look up', 'what did u just say'
]

CLARIFICATION_PATTERNS = [
    'what do you mean by', 'define', 'define please',
    'meaning of', 'definition of', 'what is meant by',
    'in other words', 'simpler terms', 'layman terms',
    'breakdown of', 'elaborate', 'expand on',
    'explain', 'explain please', 'explain more', 'explain further',
    'clarify', 'clarify please', 'clarify that', 'make it clear',
    'what does that mean', 'what is the meaning', 'what does this mean',
    'how does that work', 'how do you mean', 'in what way',
    'can you elaborate', 'can you explain', 'can you clarify',
    'i need clarification', 'need more info', 'more details please',
    'give me more info', 'tell me more', 'go deeper', 'dig deeper',
    'what exactly', 'what precisely', 'specifically what',
    'give example', 'show example', 'example please', 'for example',
    'what do you mean exactly', 'what do u mean', 'what u mean',

    # Identity questions
    'who are you', 'what are you', 'what\'s your name',
    'what is your name', 'tell me about yourself',
    'introduce yourself', 'what can you do',
    'what\'s your purpose', 'what are you supposed to do',
    'what do you mean',
    'who made you', 'who created you', 'who is your creator',
    'are you a bot', 'are you ai', 'are you human',
    'what are your capabilities', 'what can you help with'
]


# ============================================================
# SIMPLE RESPONSES (Quick commands)
# ============================================================

SIMPLE_RESPONSES = ['yes', 'y', 'no', 'n', 'ok', 'okay', 'exit', 'e', 'quit', 'bye']


# ============================================================
# QUESTION WORDS & KEYWORDS
# ============================================================

QUESTION_WORDS = [
    'what', 'how', 'why', 'when', 'where', 'who', 'which',
    'can', 'is', 'are', 'do', 'does', 'should', 'could', 'would', 'will'
]

PYTHON_TERMS = [
    'python', 'function', 'variable', 'relational operator',
    'assignment operator', 'logical operator', 'type conversion', 'input function',
    'comments', 'strings', 'programming', 'coding', 'data types', 'conditional statements',
    'if statement', 'else statement', 'elif statement', 'nested conditionals', 'Indexing & Slicing',
    'Strings Operations', 'Strings Formating'
]


# ============================================================
# COMMAND PREFIX CHARACTERS
# ============================================================

COMMAND_PREFIXES = ['/', '\\', '!', '@', '#', '$', '%', '^', '&', '*']

# ============================================================
# TOPIC KEYWORDS
# ============================================================

TOPIC_KEYWORDS = {
    'Hello World': [
        'hello world', 'hellow world', 'world hellow', 'world hello', 'first program', 'print statement',
        'printing', 'basic output', 'world', 'program'
    ],
    'Functions': [
        'functions', 'function', 'funtions', 'functons', 'def', 'method', 'reusable code', 'modular'
    ],
    'Variables': [
        'variables', 'variable', 'varaibles', 'var', 'storage', 'assign', 'assignment', 'store value'
    ],
    'Relational operators': [
        'relational operators', 'relational operator', 'relational',
        'comparison', 'compare', 'equal to', 'greater than', 'less than', '==', '!=', '>=', '<=', '>', '<'
    ],
    'Assignment operators': [
        'assignment operators', 'assignment operator', 'assignment',
        '+=', '-=', '*=', '/=', '%=', '//=', '**=', 'shortcut operators'
    ],
    'Logical operators': [
        'logical operators', 'logical operator', 'logical',
        'and operator', 'or operator', 'not operator',
        'boolean logic', 'true false', 'boolean operators',
        'and or', 'and or not', 'logical and', 'logical or', 'logical not',
        'and or operators', 'boolean and', 'boolean or', 'boolean not'
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
        'comments in python', 'comments', 'comment', '#', 'documentation', 'explain code', 'notes'
    ],
    'Strings in Python': [
        'strings in python', 'strings', 'string', 'python strings',
        'text', 'character', 'words', 'sentence',
        'concatenate', 'slicing', 'string operations', 'string formatting',
        'string methods', 'str type'
    ],
    'Data types in Python': [
        'data types in python', 'data types', 'data type', 'datatypes', 'integer', 'float', 'boolean',
        'tuple', 'dictionary', 'data type in python', 'int', 'bool', 'dict',
        'int type', 'float type', 'bool type'
    ],
    'Conditional statements': [
        'conditional statements', 'conditional statement', 'conditionals',
        'if else', 'elif', 'condition', 'decision', 'branch', 'choose', 'if statement',
        'if', 'else', 'elif statement', 'conditonal', 'conditional'
    ],
    'Lists in Python': [
        'lists in python', 'lists', 'list', 'array', 'arrays', 'list in python',
        'python lists', 'append', 'list operations', 'list methods',
        'indexing', 'slicing', 'listts', 'lsts'
    ]
}

# ============================================================
# TOPIC REQUEST PATTERNS
# ============================================================

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
    'let me try', 'i want to code', 'coding practice', 'hands on',
    'wnt to practice', 'i wnt to practice', 'want to pratice'
]

HELP_PATTERNS = [
    'help', 'what can you do', 'how does this work',
    'what should i do', 'options', 'menu', 'what\'s available',
    'what topics', 'show topics', 'list topics',

    # Extended variations for better recognition
    'show me topics', 'show me the topics', 'list all topics',
    'what topics do you have', 'what can you teach',
    'what topics are available', 'display topics',
    'see all topics', 'see the topics', 'view topics'
]

# ============================================================
# PATTERN DETECTION THRESHOLDS
# ============================================================

TOPIC_MATCH_THRESHOLD = 0.55

BEGINNER_PATTERNS = [
    r'\bbeginner\b', r'\bnewbie\b', r'\bnovice\b',
    r'\bi\s+(want|wanted|would like|need)\s+to\s+(learn|lean|study)\b',
    r'\blearn python\b', r'\bpython beginner\b',
    r'\bgetting started\b',
    r'\bhelp me learn\b', r'\bcan you help me\b',
    r'\b(i\s+)?need(ed)?\s+help\b', r'\bhelp me (with|to)\b',
]

QUESTION_PATTERNS = [
    r'\bwhat\b', r'\bhow\b', r'\bwhy\b', r'\bwhen\b',
    r'\bwhere\b', r'\bwho\b', r'\bwhich\b',
    r'\bcould\b', r'\bwould\b', r'\bshould\b', r'\bexplain\b'
]

# ============================================================
# NEGATION WORDS
# ============================================================

NEGATION_WORDS = {
    # Existing
    'no', 'not', "don't", 'dont', 'nope', 'nah', 'naw', 'never',
    'none', 'nobody', 'nothing', 'nowhere', 'neither', 'nor',
    'cannot', "can't", 'could not', "couldn't", 'would not', "wouldn't",
    'should not', "shouldn't", 'is not', "isn't", 'are not', "aren't",
    'was not', "wasn't", 'were not', "weren't", 'hard pass', 'big pass',

    # Added for better coverage
    'not sure', 'not really', 'not interested', 'not feeling it',
    'not at all',
    'not exactly', 'not particularly', 'not quite', 'not necessary',
    'not in the mood', 'not vibing with it', 'not on my watch',
    'maybe not', 'probably not', 'definitely not',
    'not sure yet', "i don't think so", 'i dont think so',
    'no way', 'no thanks', 'no need', 'no worries',
}

# ============================================================
# FILLER WORDS & COMMON SHORT WORDS
# ============================================================

FILLER_WORDS = {
    'i', 'me', 'my', 'the', 'a', 'an', 'is', 'it', 'to', 'do',
    'of', 'in', 'on', 'at', 'be', 'am', 'are', 'was', 'were',
    'this', 'that', 'and', 'or', 'but', 'so', 'for', 'with',
    'just', 'like', 'bro', 'man', 'fam', 'yo', 'hey', 'hi',
}

COMMON_SHORT_WORDS = {
    'the', 'for', 'but', 'of', 'in', 'on', 'at', 'to', 'is', 'it',
    'a', 'an', 'as', 'by', 'hello', 'hi', 'hey', 'thanks',
    'yes', 'no', 'ok', 'okay', 'sure', 'yeah', 'yep', 'yup', 'nah', 'nope',
    'exit', 'quit', 'bye', 'thank', 'help', 'menu', 'topics', 'learn', 'teach',
    'practice', 'example', 'show', 'skip', 'next', 'back', 'done', 'finish',
    'stop', 'continue', 'more', 'all', 'none', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine', 'ten', 'later'
}

COMMON_SINGLE_WORDS = {
    'hello', 'hi', 'hey', 'thanks', 'thank', 'python', 'later',
    'bye', 'exit', 'quit', 'yes', 'no', 'ok', 'okay', 'sure', 'help'
}

# ============================================================
# GENERIC PATTERNS
# ============================================================

generic_python_patterns = [
    'teach me python', 'learn python', 'python tutorial',
    'start with python', 'python basics', 'python course',
    'getting started with python', 'python for beginners',
    'i want to learn python', 'help me learn python'
]

last_response_patterns = [
    'last response', 'last reply', 'last message',
    'what did you say', 'what was your last',
    'whats your last', 'your last response', 'your last reply',
    'your last message', 'repeat what you said', 'say that again',
    'what did you said', 'what you said', 'what was that you said', 'what did you say again'
]

identity_patterns = [
    'who are you', 'what are you', 'what\'s your name',
    'what is your name', 'tell me about yourself',
    'introduce yourself', 'what can you do',
    'what\'s your purpose', 'what are you supposed to do',
    'Who are you?', 'What are you?', 'What is your purpose?', 'What can you do?',
    'who are yu', 'what are yu', 'what is your purpose', 'what can you do',
    'who r u', 'what r u', 'what is ur purpose', 'what'
]
