# validators.py
"""Input validation functions for Pytalon."""

import re
from config import (
    YES_RESPONSES, NO_RESPONSES, EXIT_RESPONSES,
    YES_EXAMPLES_RESPONSES, NO_EXAMPLES_RESPONSES,
    YES_QUESTION_RESPONSES, NO_QUESTION_RESPONSES,
    EXIT_QUESTION_RESPONSES, SIMPLE_RESPONSES,
    GREETING_PATTERNS, FAREWELL_PATTERNS, GRATITUDE_PATTERNS,
    CONFUSION_PATTERNS, TOPIC_KEYWORDS, TOPIC_REQUEST_PATTERNS,
    PRACTICE_REQUEST_PATTERNS, HELP_PATTERNS, TOPIC_MATCH_THRESHOLD,
    BEGINNER_PATTERNS, QUESTION_PATTERNS, NEGATION_WORDS,
    UNCERTAIN_RESPONSES, REPEAT_REQUEST_PATTERNS, CLARIFICATION_PATTERNS,
    SOCIAL_INTENTS, SUBSTANTIVE_INTENTS
)

from utils import smart_detection, smart_validators, _extract_keywords

# ========== VALIDATION FUNCTIONS ==========

# --------- MODULE-LEVEL SETS FOR PERFORMANCE ---------

YES_SET = {p.lower() for p in YES_RESPONSES}
NO_SET = {p.lower() for p in NO_RESPONSES}
EXIT_SET = {p.lower() for p in EXIT_RESPONSES}
 
YES_QUESTION_SET = {p.lower() for p in YES_QUESTION_RESPONSES}
NO_QUESTION_SET = {p.lower() for p in NO_QUESTION_RESPONSES}
EXIT_QUESTION_SET = {p.lower() for p in EXIT_QUESTION_RESPONSES}
 
YES_EXAMPLES_SET = {p.lower() for p in YES_EXAMPLES_RESPONSES}
NO_EXAMPLES_SET = {p.lower() for p in NO_EXAMPLES_RESPONSES}
 
# Single-word negation list (for fast lookup)
SINGLE_WORD_NEGATIONS = {w for w in NEGATION_WORDS if ' ' not in w}
MULTI_WORD_NEGATIONS = {p for p in NEGATION_WORDS if ' ' in p}

# ---- Generalized yes/no/exit validation with smart_validators and negation handling -------
def get_global_valid_input(prompt):
    """
    Gets validated yes/no/exit input from user, with smart_validators and negation handling.
    Returns: 'yes', 'no', or 'exit' based on user input.
     - First checks for exact matches in the predefined sets.
     - If no exact match, uses smart_validators to get similarity scores for 'yes', 'no', and 'exit'.
     - If 'yes' is the highest score and above threshold, checks for negation words in the input to avoid false positives.
     - If 'no' or 'exit' is the highest score and above threshold, returns those accordingly.
     - If no clear match, prompts user to try again.
    """
 
    while True:
        raw_input = input(prompt).strip().lower()
 
        # Exact matches (fast path)
        if raw_input in YES_SET:
            return 'yes'
        if raw_input in NO_SET:
            return 'no'
        if raw_input in EXIT_SET:
            return 'exit'
 
        # Extract intent keywords from user input once, reused across all comparisons
        w1 = _extract_keywords(raw_input)
 
        # Fuzzy match against the full response sets
        best_yes  = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in YES_SET),  default=0.0)
        best_no   = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in NO_SET),   default=0.0)
        best_exit = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in EXIT_SET), default=0.0)
 
        THRESHOLD = 0.75

        words = set(raw_input.split())
        user_negated = any(w in words for w in SINGLE_WORD_NEGATIONS) or any(
            phrase in raw_input for phrase in MULTI_WORD_NEGATIONS
        )

        if best_yes >= THRESHOLD and best_no >= THRESHOLD and best_yes == best_no and not user_negated:
            return 'yes'
        if best_yes >= THRESHOLD and best_yes > best_no and best_yes > best_exit:
            if user_negated:
                return 'no'
            return 'yes'
        if best_no >= THRESHOLD and best_no > best_exit and best_no > best_yes:
            return 'no'
        if best_exit >= THRESHOLD and best_exit > best_yes and best_exit > best_no:
            return 'exit'
 
        print("🤔 I didn't quite get that. Please answer with 'yes', 'no', or 'exit'.")

# ---- Specialized validation for menu choice input -------
def get_global_menu_choice(prompt, min_val=1, max_val=12):
    """
    Gets validated menu choice (number within range or 'exit').
    Returns: choice number as string, or 'exit'
    """
    while True:
        choice = input(prompt).strip().lower()
        
        if choice in ['exit', 'e', 'quit', 'bye', 'leave']:
            return 'exit'
        
        if not choice:
            print(f"📝 Just type a number from {min_val} to {max_val} to pick a topic, or 'exit' to leave!")
            continue

        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return choice

        print(f"📝 That's not a topic number! Pick {min_val}-{max_val}, or type 'exit'.")

# ---- Specialized validation for yes/no/exit input on questions, with smart_validators and negation handling -------
def get_global_user_question_valid_input(prompt):
    """
    Gets validated yes/no/exit input from user, with smart_validators and negation handling.
    Returns: 'yes', 'no', or 'exit' based on user input.
     - First checks for exact matches in the predefined sets.
     - If no exact match, uses smart_validators to get similarity scores for 'yes', 'no', and 'exit'.
     - If 'yes' is the highest score and above threshold, checks for negation words in the input to avoid false positives.
     - If 'no' or 'exit' is the highest score and above threshold, returns those accordingly.
     - If no clear match, prompts user to try again.
    """
 
    while True:
        raw_input = input(prompt).strip().lower()
 
        # Exact matches using question-specific sets
        if raw_input in YES_QUESTION_SET:
            return 'yes'
        if raw_input in NO_QUESTION_SET:
            return 'no'
        if raw_input in EXIT_QUESTION_SET:
            return 'exit'
 
        # Extract intent keywords from user input once, reused across all comparisons
        w1 = _extract_keywords(raw_input)
 
        # Fuzzy match against the full question response sets
        best_yes  = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in YES_QUESTION_SET),  default=0.0)
        best_no   = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in NO_QUESTION_SET),   default=0.0)
        best_exit = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in EXIT_QUESTION_SET), default=0.0)
 
        THRESHOLD = 0.75
        
        if best_yes >= THRESHOLD and best_yes > best_no and best_yes > best_exit:
            words = set(raw_input.split())
            if any(w in words for w in SINGLE_WORD_NEGATIONS):
                return 'no'
            if any(phrase in raw_input for phrase in MULTI_WORD_NEGATIONS):
                return 'no'
            return 'yes'
        if best_no >= THRESHOLD and best_no > best_exit:
            return 'no'
        if best_exit >= THRESHOLD:
            return 'exit'
 
        print("🤔 I didn't quite get that. Please answer with 'yes', 'no', or 'exit'.")

# ---- Specialized validation for yes/no input on examples, with smart_validators and negation handling -------
def get_global_examples_valid_input(prompt):
    """
    Gets validated yes/no input from user for examples question, with smart_validators and negation handling.
    Returns: 'yes' or 'no' based on user input.
     - First checks for exact matches in the predefined examples sets.
     - If no exact match, uses smart_validators to get similarity scores for 'yes' and 'no'.
     - If 'yes' is the highest score and above threshold, checks for negation words in the input to avoid false positives.
     - If 'no' is the highest score and above threshold, returns 'no'.
     - If no clear match, prompts user to try again.
    """
 
    while True:
        raw_input = input(prompt).strip().lower()
 
        # Exact matches using examples-specific sets
        if raw_input in YES_EXAMPLES_SET:
            return 'yes'
        if raw_input in NO_EXAMPLES_SET:
            return 'no'
 
        # Extract intent keywords from user input once, reused across all comparisons
        w1 = _extract_keywords(raw_input)
 
        # Fuzzy match against the full examples response sets
        best_yes = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in YES_EXAMPLES_SET), default=0.0)
        best_no  = max((smart_validators(raw_input, phrase, w1, _extract_keywords(phrase)) for phrase in NO_EXAMPLES_SET),  default=0.0)
 
        THRESHOLD = 0.65

        words = set(raw_input.split())
        user_negated = any(w in words for w in SINGLE_WORD_NEGATIONS) or any(
            phrase in raw_input for phrase in MULTI_WORD_NEGATIONS
        )

        if best_yes >= THRESHOLD and best_yes > best_no:
            if user_negated:
                return 'no'
            return 'yes'
        if best_yes >= THRESHOLD and best_no >= THRESHOLD and best_yes == best_no and not user_negated:
            return 'yes'
        if best_no >= THRESHOLD:
            if user_negated or best_no > best_yes:
                return 'no'
 
        print("🤔 I didn't quite get that. Please answer with 'yes' or 'no'.")

# ----- Specialized validation for getting the actual question content -------
def get_global_question_content_input(prompt):
    """
    Gets and validates the actual question text from user.
    Ensures input is a proper question (not just yes/no/exit).
    Returns: the question string
    """
    while True:
        question = input(prompt).strip()
        
        if not question:
            print("👋 I'm all ears! What's your Python question?")
            continue
        
        question_lower = question.lower()
        
        if question_lower in SIMPLE_RESPONSES:
            print("🤔 That sounds like a yes/no answer! I need an actual question — what do you want to know about Python?")
            continue
        
        if len(question) >= 10:
            return question
        
        print("\n🤔 That's a bit short! Try a complete question like:")
        print("   • 'Can you teach me Python?'")
        print("   • 'How do I learn variables?'")
        print("   • 'What is a function?'")
        print()

# ===== EMPTY OR UNRECOGNIZED INPUT MANAGEMENT =====

def handle_unrecognized_input(user_input):
    """Handles input that doesn't match any intent."""
    if not user_input:
        print("   ")
    elif len(user_input) < 10:
        print("""🤔 That seems a bit short! 
              Try saying something like 'Hello', 'Can you teach me Python?', or 'What topics do you have?'""")
    elif len(user_input) > 10000:
        print("""😊 Max. limit is upto 10000 characters.""")
    else:
        print("""🤔 I'm not sure what you mean! 
              Try saying 'Hi', asking a Python question, or telling me how I can help!""")


def handle_empty_input(user_input):
    """Handles completely empty input."""
    if not user_input:
        print("   ")
    else:
        print(f"😄 Thanks for your message! {user_input}")


# ========== NEW CONVERSATIONAL INTENT DETECTION ==========

def detect_conversation_intent(user_input):
    """
    Analyzes user input to detect the conversational intent.
    Returns a dict with intent type and confidence.

    Possible intents:
    - 'greeting': User is saying hello
    - 'farewell': User is saying goodbye
    - 'gratitude': User is thanking
    - 'confusion': User doesn't understand
    - 'topic_request': User wants to learn a specific topic
    - 'practice_request': User wants to practice
    - 'help_request': User wants to know options
    - 'yes_no': User is answering a yes/no question
    - 'general_question': User has a general question

    Every scorer runs on every input. The highest confidence wins.
    Order of the scorers below does not affect which intent gets returned.
    """
    user_input_lower = user_input.lower().strip()

    # ---- Empty input Handler ----
    if not user_input_lower:
        handle_empty_input(user_input)
        return {'intent': 'empty', 'confidence': 1.0}

    if len(user_input_lower) > 10000:
        handle_unrecognized_input(user_input)
        return {'intent': 'unrecognized', 'confidence': 1.0}

    # ---- Scores table: each scorer writes into this dict ----
    # Format: {intent_name: {'confidence': score, ...extra_info}}
    scores = {}

    def record(intent, confidence, **extra):
        # Keeping the highest score for each intent, and scoring any extra info if provided
        if intent not in scores or confidence > scores[intent]['confidence']:
            scores[intent] = {'confidence': confidence, **extra}

    # ---- Helper: Topic Request System ----
    def check_topic_request(user_text):
        best_score = 0.0
        best_topic = None
        best_length = 0

        for topic, keywords in TOPIC_KEYWORDS.items():
            score = smart_detection(user_text, topic.lower())

            # Special Case 1: If user just says "python", it shouldn't match topics that are about Python but not named exactly "Python"
            if user_text == "python" and "python" in topic.lower() and topic.lower() != "python":
                score = 0.0

            if score > best_score or (score == best_score and len(topic) > best_length):
                best_score = score
                best_topic = topic
                best_length = len(topic)

            for keyword in keywords:
                score = smart_detection(user_text, keyword.lower())
                if score > best_score or (score == best_score and len(topic) > best_length):
                    best_score = score
                    best_topic = topic
                    best_length = len(topic)

        # Special case 2: Handling generic "python" mentions that aren't specific enough to match a topic
        if best_topic and "python" in best_topic.lower():
            kws = TOPIC_KEYWORDS.get(best_topic, [])
            has_other = any(kw != "python" and kw in user_text for kw in kws)
            if not has_other:
                best_score = 0.0
                best_topic = None

        if best_score >= TOPIC_MATCH_THRESHOLD:
            return best_score, best_topic
        return 0.0, None

    # ---- Scorer 1: Topic request (smart detection) ----
    topic_phrase = user_input_lower
    for pattern in TOPIC_REQUEST_PATTERNS:
        if pattern in user_input_lower:
            start = user_input_lower.find(pattern) + len(pattern)
            topic_phrase = user_input_lower[start:].strip().rstrip('?.!')
            break

    topic_score, matched_topic = check_topic_request(topic_phrase)
    if matched_topic:
        record('topic_request', topic_score, topic=matched_topic)

    # ---- Scorer 2: Topic request (keyword fallback) ----
    seems_topic = (
        any(pattern in user_input_lower for pattern in TOPIC_REQUEST_PATTERNS)
        or any(
            any(kw in user_input_lower for kw in kws)
            for kws in TOPIC_KEYWORDS.values()
        )
    )
    if seems_topic:
        record('topic_request', 0.7)

    # ---- Scorer 3: Beginner / learning intent ----
    help_from_beginner = any(re.search(p, user_input_lower) for p in BEGINNER_PATTERNS)
    if help_from_beginner:
        record('help_request', 0.8, is_beginner=True)

    # ---- Scorer 4: Greetings ----
    greeting_hit = (
        any(phrase in user_input_lower for phrase in GREETING_PATTERNS if ' ' in phrase)
        or any(token in GREETING_PATTERNS for token in user_input_lower.split())
    )
    if greeting_hit:
        record('greeting', 0.9)

    # ---- Scorer 5: Farewells ----
    if any(pattern in user_input_lower for pattern in FAREWELL_PATTERNS):
        record('farewell', 0.9)

    # ---- Scorer 6: Gratitude ----
    if any(pattern in user_input_lower for pattern in GRATITUDE_PATTERNS):
        record('gratitude', 0.9)

    # ---- Scorer 7: Confusion ----
    if any(pattern in user_input_lower for pattern in CONFUSION_PATTERNS):
        record('confusion', 0.8)

    # ---- Scorer 8: Practice request ----
    if any(pattern in user_input_lower for pattern in PRACTICE_REQUEST_PATTERNS):
        record('practice_request', 0.8)

    # ---- Scorer 9: Help request ----
    help_from_patterns = any(pattern in user_input_lower for pattern in HELP_PATTERNS)
    if help_from_patterns:
        record('help_request', 0.8)

    # ---- Scorer 10: Yes / No / Exit ----
    if user_input_lower in YES_SET:
        record('yes_no', 0.95, answer='yes')
    if user_input_lower in NO_SET:
        record('yes_no', 0.95, answer='no')
    if user_input_lower in EXIT_SET:
        record('yes_no', 0.95, answer='exit')

    # ---- Scorer 11: General question patterns ----
    if any(re.search(p, user_input_lower) for p in QUESTION_PATTERNS):
        record('general_question', 0.7)

    # Scorer 12: Uncertain responses (maybe, not sure, etc.)
    if any(phrase in user_input_lower for phrase in UNCERTAIN_RESPONSES):
        record('uncertain', 0.75)

    # Scorer 13: Repeat request (say again, repeat that, etc.)
    if any(phrase in user_input_lower for phrase in REPEAT_REQUEST_PATTERNS):
        record('repeat_request', 0.85)

    # Scorer 14: Clarification request (define, explain more, etc.)
    if any(phrase in user_input_lower for phrase in CLARIFICATION_PATTERNS):
        record('clarification', 0.85)

    # ---- Boost help_request when multiple help signals co-fire ----
    if help_from_beginner and help_from_patterns and 'help_request' in scores:
        scores['help_request']['confidence'] = 0.95

    # ---- Compound intent: prefer substantive intent over social opener ----
    social_fired = SOCIAL_INTENTS & scores.keys()
    substantive_fired = SUBSTANTIVE_INTENTS & scores.keys()

    if social_fired and substantive_fired:
        for social in social_fired:
            del scores[social]

    # ---- Compound intent: prefer clarification over confusion ----
    if 'confusion' in scores and 'clarification' in scores:
        if scores['clarification']['confidence'] >= scores['confusion']['confidence']:
            del scores['confusion']

    # ---- Pick the winner ----
    if scores:
        best_intent = max(scores, key=lambda k: scores[k]['confidence'])
        result = {'intent': best_intent}
        result.update(scores[best_intent])
        return result

    # ---- Nothing matched ----
    handle_unrecognized_input(user_input)
    return {'intent': 'unrecognized', 'confidence': 0.0}