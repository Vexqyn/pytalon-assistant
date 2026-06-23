"""Shared utility functions for Pytalon."""

import io
import sys
import difflib
import re
from config import FILLER_WORDS, NEGATION_WORDS

# ========== NEGATION HANDLING ==========

_SINGLE_NEGATIONS = {w for w in NEGATION_WORDS if " " not in w}
_MULTI_NEGATIONS = {p for p in NEGATION_WORDS if " " in p}

# ------- Helper function to detect negation cues in text -------
def _text_has_negation(text):
    """True if text contains an explicit negation cue."""
    lowered = text.lower()
    words = set(lowered.split())
    if words & _SINGLE_NEGATIONS:
        return True
    return any(phrase in lowered for phrase in _MULTI_NEGATIONS)

# ------- Helper function to adjust similarity score based on negation cues -------
def _apply_negation_cap(score, user_text, reference_text):
    """Lower score when the reference is negative but the user did not negate."""
    if _text_has_negation(reference_text) and not _text_has_negation(user_text):
        return min(score, 0.5)
    return score

# ========== UTILITY FUNCTIONS ==========
# These functions provide common utilities used across the Pytalon

# Global Separator Function
def print_global_separator():
    """Prints a visual separator line for better readability"""
    global_separator = "\n" + "="*50
    print(global_separator)


# CODE PRACTICE SYSTEM Helper Functions

# ===== Step 1: Get multiline code input from the user =====
def get_multiline_code_input():
    """
    Gets multiple lines of Python code from the user.
    User types code line by line, then types 'DONE' to finish.
    
    Returns:
        String containing all the code lines joined together
    """
    print("\n📝 ENTER YOUR PYTHON CODE (type 'DONE' on a new line when finished):")
    print_global_separator()
    
    code_lines = []
    while True:
        line = input()
        # Check if user wants to stop entering code
        if line.strip().upper() == 'DONE':
            break
        code_lines.append(line)
    
    # Join all lines with newline characters
    return "\n".join(code_lines)


# ===== Step 2: Execute code and check for expected/forbidden keywords =====
def execute_and_check_code(code, expected_keywords=None, forbidden_keywords=None):
    """
    Safely executes the user's Python code and checks for required elements.
    
    Parameters:
        code:             The Python code string to execute
        expected_keywords: List of keywords that MUST be in the code
        forbidden_keywords: List of keywords that must NOT be in the code
    
    Returns:
        (success, output, error_message)
        - success: True if code ran correctly and passed all checks
        - output: What the code printed (if anything)
        - error_message: Description of any problems found
    """
    # ---- SETUP: Capture printed output ----
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    success = True
    error_message = ""
    output = ""
    
    try:
        # ---- EXECUTE: Run the code in isolated namespace ----
        namespace = {}
        exec(code, namespace)
        output = captured_output.getvalue()
        
        # ---- CHECK: Verify expected keywords are present ----
        if expected_keywords:
            # Find which expected keywords are missing
            missing_keywords = [
                kw for kw in expected_keywords 
                if kw.lower() not in code.lower()
            ]
            
            if missing_keywords:
                success = False
                error_message = f"Missing required elements: {', '.join(missing_keywords)}"
        
        # ---- CHECK: Verify forbidden keywords are absent ----
        if forbidden_keywords:
            # Find which forbidden keywords were used
            found_forbidden = [
                kw for kw in forbidden_keywords 
                if kw.lower() in code.lower()
            ]
            
            if found_forbidden:
                success = False
                error_message = f"Please don't use: {', '.join(found_forbidden)}"
                
    except SyntaxError as e:
        success = False
        error_message = f"Syntax Error: {str(e)}"
    except Exception as e:
        success = False
        error_message = f"Error: {str(e)}"
    finally:
        # ---- CLEANUP: Restore normal output ----
        sys.stdout = old_stdout
    
    return success, output, error_message


# ===== Step 3: Main practice session flow =====
def run_practice_session(topic_name, instructions, expected_keywords, example_code, custom_check_function=None):
    """
    Runs a complete interactive practice session for a specific topic.
    
    Flow:
    1. Shows instructions and example
    2. Gets user's code
    3. Executes and validates the code
    4. If correct: shows success message
    5. If wrong: shows error, lets user try again
    
    Parameters:
        topic_name:          Display name of the topic (e.g., "Variables")
        instructions:        What the user needs to do
        expected_keywords:   Keywords that must appear in the code
        example_code:        A working example to show the user
        custom_check_function: Optional extra validation function
    """
    # ---- SUB STEP 1: Show practice header and instructions ----
    print_global_separator()
    print(f"🧪 INTERACTIVE PRACTICE: {topic_name}")
    print_global_separator()
    
    print(f"\n📋 TASK:")
    print(instructions)
    
    print(f"\n💡 EXAMPLE SOLUTION:")
    print(f"{example_code}")
    
    print(f"\n🔑 Required elements: {', '.join(expected_keywords)}")

    # ----  SUB STEP 2: Main practice loop with attempt limit ----
    attempts = 0
    MAX_ATTEMPTS = 3

    while True:
        # Get user's code attempt
        user_code = get_multiline_code_input()

        # Check for empty submission
        if not user_code.strip():
            print("⚠️  Please enter some Python code!")
            continue

        # Execute the code and check for basic requirements
        success, output, error_message = execute_and_check_code(
            user_code,
            expected_keywords=expected_keywords
        )

        # Run custom validation if provided (for topic-specific checks)
        if success and custom_check_function:
            success, error_message = custom_check_function(user_code, output)

    # ---- SUB STEP 3: Show results ----
        if success:
            print_global_separator()
            print("✅ PERFECT! Your code is correct!")
            if output:
                print(f"\n📤 YOUR OUTPUT:")
                print(output)
            print(f"\n💡 Code structure and elements are correct!")
            print("✅ Practice complete! You can continue to the next topic.")
            print_global_separator()
            break
        else:
            attempts += 1
            print_global_separator()
            print(f"❌ Not quite right! {error_message}")
            if attempts >= MAX_ATTEMPTS:
                retry = input("\n🔹 You've tried several times. Try again? (yes/no): ").strip().lower()
                if retry in ['yes', 'y']:
                    attempts = 0
                    continue
                else:
                    print("✅ Skipping practice. You can always come back later!")
                    break
            else:
                print(f"\n🔄 Attempt {attempts}/{MAX_ATTEMPTS}. Please try again!")
                print_global_separator()

        
# ========= MENU DISPLAY FUNCTION ==========
def show_topic_menu(topics, prompt="Which topic would you like to start with?"):
    """
    Displays the full topic list and returns the chosen number (string) or 'exit'.
    """
    from validators import get_global_menu_choice # Imported here to avoid circular dependency

    print_global_separator()
    print("I can teach you Python basics! Here are the topics:")
    print_global_separator()
    for num, topic in topics.items():
        print(f"   {num}. {topic}")

    choice = get_global_menu_choice(
        f"\n🔹 {prompt} (1-13/exit): ",
        1,
        len(topics)
    )
    return choice

# ========= Helper: Smart Detection Function ==========

# Smart Detection Function for detecting the users intent during the conservation.
def smart_detection(s1, s2):
    """
    Compares two strings and returns a similarity score between 0 and 1.
    Checks for:
    - Sub‑string containment
    - Full‑string similarity
    - Each word of s1 against s2 and vice‑versa
    - Word‑order reversal
    - All words of one string present in the other (subset match)
    """
    if not s1 or not s2:
        return 0.0
    
    s1 = s1.lower().strip()
    s2 = s2.lower().strip()

    # Direct containment
    if s1 in s2 or s2 in s1:
        return 1.0

    # --- New check: all words of s2 appear in s1 (or vice‑versa) ---
    words1 = set(s1.split())
    words2 = set(s2.split())

    if words2 and words2.issubset(words1):
        # All keywords are present in the user’s topic phrase → strong match
        return 1.0
    if words1 and words1.issubset(words2):
        return 1.0
    # ----------------------------------------------------------------

    # Full‑string comparison
    best = difflib.SequenceMatcher(None, s1, s2).ratio()

    # Word‑by‑word comparisons
    for word in s1.split():
        score = difflib.SequenceMatcher(None, word, s2).ratio()
        if score > best:
            best = score

    for word in s2.split():
        score = difflib.SequenceMatcher(None, word, s1).ratio()
        if score > best:
            best = score

    # Handle swapped word order
    if " " in s2:
        reversed_s2 = " ".join(reversed(s2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_s2).ratio()
        if score > best:
            best = score

    return best

# Smart Validations for the Validators to detect the users intent during the conservation.
def smart_validators(s1, s2, w1, w2):
    """
    Validates the user's input based on smart detection logic.
    Parameters:
        - s1: User's input string
        - s2: Reference string to compare against
        - w1: Extracted keywords from user's input
        - w2: Extracted keywords from reference string
        Returns:
        - A similarity score between 0 and 1, with adjustments for negation cues.
        The function performs multiple checks:
        1. Direct containment of one string in the other.
        2. Subset match where all keywords of one string are present in the other.
        3. Full-string similarity using difflib.
        4. Word-by-word comparisons for both the main strings and the keywords.
        5. Handling of swapped word order.
        6. Adjusting the final score if negation cues are detected in the reference string but not in the user's input, 
           to prevent false positives in cases of negation.
    """

    s1 = s1.lower().strip()
    s2 = s2.lower().strip()

    w1 = w1.lower().strip()
    w2 = w2.lower().strip()
    
    # Require at least 2 overlapping keywords in both the main strings and the keyword sets for a strong match
    s1_clean = set(_extract_keywords(s1).split())
    s2_clean = set(_extract_keywords(s2).split())
    w1_words = set(w1.split())
    w2_words = set(w2.split())
    min_overlap = 1

    overlap1 = len(s1_clean & s2_clean)
    overlap2 = len(w1_words & w2_words)
    overlap3 = len(s1_clean & w2_words)
    overlap4 = len(w1_words & s2_clean)

    if (overlap1 >= min_overlap or overlap2 >= min_overlap) and (overlap3 >= min_overlap or overlap4 >= min_overlap):
        return _apply_negation_cap(1.0, s1, s2)
    if (overlap1 >= 1 or overlap2 >= 1) and (overlap3 >= 1 or overlap4 >= 1):
        return _apply_negation_cap(0.5, s1, s2)
    # ----------------------------------------------------------------
    
    # Full‑string comparison
    best = difflib.SequenceMatcher(None, s1, s2).ratio()
    
    # Word‑by‑word comparisons
    for word in s1.split():
        score = difflib.SequenceMatcher(None, word, s2).ratio()
        if score > best:
            best = score

    for word in s2.split():
        score = difflib.SequenceMatcher(None, word, s1).ratio()
        if score > best:
            best = score
    
    # String-by-string comparisons for keywords
    for word_w1 in w1.split():
        score = difflib.SequenceMatcher(None, word_w1, w2).ratio()
        if score > best:
            best = score
    
    for word_w2 in w2.split():
        score = difflib.SequenceMatcher(None, word_w2, w1).ratio()
        if score > best:
            best = score
    
    # Handle swapped word order for both the main strings and the keywords
    if " " in s2:
        reversed_s2 = " ".join(reversed(s2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_s2).ratio()
        if score > best:
            best = score
    
    if " " in w2:
        reversed_w2 = " ".join(reversed(w2.split()))
        score = difflib.SequenceMatcher(None, s1, reversed_w2).ratio()
        if score > best:
            best = score

    return _apply_negation_cap(best, s1, s2)

# ========== HELPER: Extract intent keywords from a string ==========

def _extract_keywords(text):
    """
    Extracts the most intent-carrying words from a string.
    Strips common filler words so smart_validators gets meaningful w1/w2.
    Returns a string of the remaining words joined by spaces.
    """

    cleaned = re.sub(r"[^\w\s']", '', text.lower().strip())
    words = cleaned.split()
    keywords = [w for w in words if w not in FILLER_WORDS]
    return ' '.join(keywords) if keywords else cleaned
