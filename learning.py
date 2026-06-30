"""
PYTALON - Your Python Tutor Companion
Created by: M Qasim Farooqi
Role: BS IT Student | Python Developer · AI Prompt Strategist · Game Systems Analyst | I build, analyze & create. Founder of Vexqyn 
Version: 2.0
Category: Major Release (Stable Version)
Purpose: Learn Python basics through interactive teaching with 13 comprehensive topics
"""

# ----- Module imports -----
from utils import print_global_separator, run_practice_session, show_topic_menu
from validators import (
    get_global_valid_input,
    get_global_user_question_valid_input,
    get_global_menu_choice,
    get_global_examples_valid_input,
    get_global_question_content_input,
    detect_conversation_intent,
    handle_unrecognized_input,
    handle_empty_input,
)
from conversation_context import ConversationContext
from intro import sys

# ----- Session Setup -----
context = ConversationContext()

# ========== SECTION 1: INTRO & SETUP ==========
from intro import (
    print_introduction,
    get_initial_topic_choice,
    TOPICS,
    TOPIC_NAME_TO_NUMBER,
)

print_introduction()

# ========== CONVERSATIONAL OPENING & FIRST TOPIC SELECTION ==========
try:
    topic_choice = get_initial_topic_choice(context)

# ===== MAIN TEACHING LOOP =====
    while True:
        selected_topic = TOPICS[topic_choice]
        print(f"\n🎯 Excellent choice! You selected: {selected_topic}")

        # ---- Ask if user wants to learn this topic ----
        learn_topic = get_global_valid_input(
            f"\n🔹 Would you like me to teach you about {selected_topic}? (yes/no/exit): "
        )
        if learn_topic == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break
        elif learn_topic == 'no':
            print(f"\n🔹 Okay, skipping {selected_topic}.")
            topic_choice = show_topic_menu(TOPICS, "Which topic would you like instead?")
            if topic_choice == 'exit':
                print("\n👋 Goodbye!")
                break
            continue

        print(f"\n📖 Teaching {selected_topic}...")

        # ---- TEACHING FUNCTION CALLS BASED ON TOPIC SELECTION ----
        from topics_basic import BASIC_TOPICS
        teach_func = BASIC_TOPICS.get(selected_topic)
        if teach_func:
            teach_func()

        # ========== SECTION 6: TOPICS 7-13 ==========
        elif selected_topic == 'Type conversion':
            # ======================================================
            # TOPIC 7: TYPE CONVERSION
            # ======================================================
            print_global_separator()
            print("7. Type Conversion in Python:")

            def explain_type_conversion():
                print("\n   🔄 What is type conversion?")
                print("\n🔄 TYPE CONVERSION: CHANGING DATA TYPES")
                print_global_separator()

                print("""
                🎯 WHAT IS IT?
                Type conversion is changing a variable from 
                one DATA TYPE to another.

                📋 TWO TYPES OF CONVERSION:

                1️⃣ IMPLICIT CONVERSION (Automatic)
                Python does it automatically when needed.

                Example:
                num_int = 10      # Integer
                num_float = 5.5   # Float
                result = num_int + num_float  # Python converts 10 → 10.0
                print(result)     # Output: 15.5 (Float)

                2️⃣ EXPLICIT CONVERSION (Manual)
                YOU control it using functions.

                🔧 EXPLICIT CONVERSION FUNCTIONS:
                int()     → Converts to INTEGER
                float()   → Converts to FLOAT  
                str()     → Converts to STRING
                bool()    → Converts to BOOLEAN

                💻 EXAMPLES:
                # String to Integer
                age_str = "25"
                age_int = int(age_str)      # "25" → 25

                # Integer to String  
                score = 95
                score_str = str(score)      # 95 → "95"

                # Float to Integer (cuts decimal)
                price = 19.99
                price_int = int(price)      # 19.99 → 19

                💡 PRACTICAL USE:
                • User input is ALWAYS string → Convert to numbers
                • Calculations need numbers → Convert strings
                • Display numbers in text → Convert to strings

                ⚠️ COMMON ERRORS:
                int("hello")   # ❌ Error: Can't convert text to number!
                int("10.5")    # ❌ Error: Use float() first!
                """)

                print_global_separator()
                print("Implicit = Python decides, Explicit = YOU decide!")
                print_global_separator()

            explain_type_conversion()

            # ---- PRACTICE: TYPE CONVERSION ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with type conversion? (yes/no): "
            )
            if practice == 'yes':
                def check_conversion_practice(code, output):
                    """Checks if conversion functions and type() are used properly"""
                    conversion_functions = ['int(', 'float(', 'str(', 'bool(']
                    found_functions = [func for func in conversion_functions if func in code]

                    if len(found_functions) < 2:
                        return False, (
                            f"Use at least 2 type conversion functions! "
                            f"Found: {found_functions if found_functions else 'none'}"
                        )
                    if 'print' not in code:
                        return False, "Use print() to show the converted values!"
                    if 'type(' not in code:
                        return False, "Use type() to show the data type before and after conversion!"
                    return True, ""

                run_practice_session(
                    topic_name="Type Conversion",
                    instructions="Create a string variable 'num_str' with a number value. Convert it to int and float. Print the type before and after each conversion!",
                    expected_keywords=['num_str', 'int', 'float', 'type', 'print'],
                    example_code=(
                        "num_str = '42'\n"
                        "print(f'Original type: {type(num_str)}')\n"
                        "num_int = int(num_str)\n"
                        "print(f'After int(): {num_int}, Type: {type(num_int)}')\n"
                        "num_float = float(num_str)\n"
                        "print(f'After float(): {num_float}, Type: {type(num_float)}')"
                    ),
                    custom_check_function=check_conversion_practice,
                )

            print("Great! You learned about type conversion!")

        elif selected_topic == 'Input function':
            # ======================================================
            # TOPIC 8: INPUT FUNCTION
            # ======================================================
            print_global_separator()
            print("8. Input Function in Python:")

            def explain_input_function():
                print("\n   🖊️ What is the input function?")
                print("\n🖊️ INPUT FUNCTION: GETTING USER DATA")
                print_global_separator()

                print("""
                🎯 WHAT IS IT?
                The input() function allows your program to 
                TAKE INPUT from the user during execution.

                🔧 HOW TO USE IT:
                syntax: variable = input("Prompt message: ")

                💡 EXAMPLE USAGE:
                name = input("Enter your name: ")   # User types their name
                print("Hello, " + name + "!")        # Greets the user

                age = input("Enter your age: ")      # User types their age
                age_next_year = int(age) + 1         # Convert to int and add 1
                print("Next year, you will be " + str(age_next_year) + " years old.")

                🔑 IMPORTANT NOTE:
                The input() function ALWAYS returns a STRING.
                Convert to other types (int, float) as needed!

                ⚠️ COMMON MISTAKES:
                age = input("Enter your age: ")
                next_age = age + 1   # ❌ Error: Can't add int to str!

                Correct way:
                age = int(input("Enter your age: "))
                next_age = age + 1   # ✅ Works perfectly!
                """)

                print_global_separator()
                print("Input function makes your program INTERACTIVE!")
                print_global_separator()

            explain_input_function()

            # ---- PRACTICE: INPUT FUNCTION ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with input function? (yes/no): "
            )
            if practice == 'yes':
                def check_input_practice(code, output):
                    """Checks if input() is used properly"""
                    if 'input(' not in code:
                        return False, "You need to use the input() function!"
                    if 'print' not in code:
                        return False, "Use print() to display the gathered information!"
                    if '=' not in code:
                        return False, "Store the input result in a variable!"
                    if len(code.split('\n')) < 2:
                        return False, "Ask for at least 2 pieces of information!"
                    return True, ""

                run_practice_session(
                    topic_name="Input Function",
                    instructions="Write a program that asks for a user's name and age using input(). Then print a message using both values!",
                    expected_keywords=['input(', 'print'],
                    example_code=(
                        "name = input('Enter your name: ')\n"
                        "age = input('Enter your age: ')\n"
                        "print(f'Hello {name}, you are {age} years old!')"
                    ),
                    custom_check_function=check_input_practice,
                )

            print("Great! You learned about the input function!")

        elif selected_topic == 'Comments in Python':
            # ======================================================
            # TOPIC 9: COMMENTS IN PYTHON
            # ======================================================
            print_global_separator()
            print("9. Comments in Python:")

            def explain_comments():
                print("\n   📝 What are comments?")
                print("\n📝 COMMENTS: EXPLAINING YOUR CODE")
                print_global_separator()

                print("""
                🎯 WHAT ARE THEY?
                Comments are notes in your code that are ignored by Python.
                They help explain what your code does.

                🔧 HOW TO WRITE THEM:
                # This is a single-line comment
                # You can write anything here

                ''' This is a multi-line comment
                You can write multiple lines here
                Python will ignore all of them '''

                💡 EXAMPLES:
                # This program calculates the area of a rectangle
                length = 10
                width = 5
                area = length * width  # Calculate area

                🔑 TIPS:
                • Use comments to explain complex logic
                • Comment out code you want to test later
                • Keep comments up-to-date with your code

                ⚠️ COMMON MISTAKES:
                Don't over-comment simple lines!
                """)

                print_global_separator()
                print("Comments help OTHERS (and FUTURE YOU) understand your code!")
                print_global_separator()

            explain_comments()

            # ---- PRACTICE: COMMENTS ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with comments? (yes/no): "
            )
            if practice == 'yes':
                def check_comments_practice(code, output):
                    """Checks if comments are used properly"""
                    if '#' not in code:
                        return False, "Use at least one single-line comment with #!"
                    if 'print(' not in code:
                        return False, "Include actual Python code along with comments!"

                    comment_lines = [
                        line for line in code.split('\n') if line.strip().startswith('#')
                    ]
                    if len(comment_lines) < 3:
                        return False, (
                            f"Add at least 3 comment lines! You have {len(comment_lines)}."
                        )
                    return True, ""

                run_practice_session(
                    topic_name="Comments",
                    instructions="Write a small Python program with at least 3 lines of code. Add comments explaining what each part does! Use both single-line (#) and inline comments.",
                    expected_keywords=['#', 'print'],
                    example_code=(
                        "# This program greets the user\n"
                        "name = 'Student'  # Store the name\n"
                        "# Print the greeting\n"
                        "print(f'Hello, {name}!')"
                    ),
                    custom_check_function=check_comments_practice,
                )

            print("Great! You learned about comments!")

        elif selected_topic == 'Strings in Python':
            # ======================================================
            # TOPIC 10: STRINGS IN PYTHON
            # ======================================================
            print_global_separator()
            print("10. Strings in Python:")

            # ----------------------------------------------------------
            # Sub-topic 1: String Basics & Creation
            # ----------------------------------------------------------
            def teach_string_basics():
                """Teach string basics"""
                print_global_separator()
                print("📘 PART 1: String Basics & Creation")
                print_global_separator()

                print("""
            📝 BASIC STRING EXAMPLES:
            name = 'Alice'                    # Single quotes
            greeting = "Hello, World!"        # Double quotes
            paragraph = '''This is a           # Multi-line string
            multi-line string that
            spans several lines.'''

            🎯 KEY POINTS:
            • Strings can use single, double, or triple quotes
            • Triple quotes allow multi-line strings
            • Strings are IMMUTABLE (cannot be modified)
            • Use len() to get string length
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    text = "Python Programming"
                    print(f"\n   text = \"{text}\"")
                    print(f"   Length: {len(text)} characters")
                    print(f"   Type: {type(text)}")
                    print(f"   Uppercase: {text.upper()}")
                    print(f"   Lowercase: {text.lower()}")

            # ----------------------------------------------------------
            # Sub-topic 2: Indexing & Slicing
            # ----------------------------------------------------------
            def teach_string_indexing():
                """Teach string indexing and slicing"""
                print_global_separator()
                print("📘 PART 2: Indexing & Slicing")
                print_global_separator()

                print("""
            🔤 INDEXING (Accessing individual characters):
            Python uses ZERO-BASED indexing

            Positions:   0   1   2   3   4   5
            String:     P   y   t   h   o   n
            Index:      0   1   2   3   4   5
            Negative:  -6  -5  -4  -3  -2  -1

            🔪 SLICING (Getting parts of string):
            Syntax: string[start:end:step]
            • start: Starting index (inclusive)
            • end: Ending index (exclusive)
            • step: Jump size
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    text = "PythonProgramming"
                    print(f"\n   text = \"{text}\"")
                    print(f"   text[0] = '{text[0]}'           # First character")
                    print(f"   text[-1] = '{text[-1]}'         # Last character")
                    print(f"   text[0:6] = \"{text[0:6]}\"     # Characters 0 to 5")
                    print(f"   text[6:] = \"{text[6:]}\"       # From index 6 to end")
                    print(f"   text[::-1] = \"{text[::-1]}\"   # Reversed string")

            # ----------------------------------------------------------
            # Sub-topic 3: String Operations
            # ----------------------------------------------------------
            def teach_string_operations():
                """Teach string operations"""
                print_global_separator()
                print("📘 PART 3: String Operations")
                print_global_separator()

                print("""
            ⚙️ CONCATENATION (+): Joining strings
            str1 = "Hello"
            str2 = "World"
            result = str1 + " " + str2  # "Hello World"

            🔁 REPLICATION (*): Repeating strings
            laugh = "ha" * 3  # "hahaha"
            separator = "-" * 20  # "--------------------"

            🔍 MEMBERSHIP (in/not in): Check substring
            text = "Python is awesome"
            has_python = "Python" in text  # True
            has_java = "Java" not in text  # True
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    str1 = "Hello"
                    str2 = "World"
                    print(f"\n   str1 = \"{str1}\"")
                    print(f"   str2 = \"{str2}\"")
                    print(f"   Concatenation: str1 + ' ' + str2 = \"{str1 + ' ' + str2}\"")
                    print(f"   Replication: 'ha' * 3 = \"{'ha' * 3}\"")
                    print(f"   Membership: 'Python' in 'Python Programming' = {'Python' in 'Python Programming'}")

            # ----------------------------------------------------------
            # Sub-topic 4: String Methods
            # ----------------------------------------------------------
            def teach_string_methods():
                """Teach string methods"""
                print_global_separator()
                print("📘 PART 4: String Methods")
                print_global_separator()

                print("""
            🛠️ COMMON STRING METHODS:

            ✂️ TRIMMING:
            spaced = "   Hello   "
            stripped = spaced.strip()      # "Hello"
            left_stripped = spaced.lstrip() # "Hello   "
            right_stripped = spaced.rstrip() # "   Hello"

            🔎 SEARCHING:
            text = "Python Programming"
            find_pro = text.find("Pro")    # 7 (index where found)
            count_n = text.count("n")      # 2 (count of 'n')

            🔀 SPLITTING & JOINING:
            sentence = "Python,Java,C++"
            languages = sentence.split(",") # ["Python", "Java", "C++"]
            new_sentence = "-".join(languages) # "Python-Java-C++"

            🔧 REPLACING:
            text = "I love Java"
            new_text = text.replace("Java", "Python") # "I love Python"
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    text = "   Python Programming   "
                    print(f"\n   text = \"{text}\"")
                    print(f"   strip(): \"{text.strip()}\"")
                    print(f"   upper(): \"{text.upper()}\"")
                    print(f"   lower(): \"{text.lower()}\"")
                    print(f"   replace('Python', 'Java'): \"{text.replace('Python', 'Java')}\"")
                    print(f"   split(): {text.strip().split()}")

            # ----------------------------------------------------------
            # Sub-topic 5: String Formatting
            # ----------------------------------------------------------
            def teach_string_formatting():
                """Teach string formatting"""
                print_global_separator()
                print("📘 PART 5: String Formatting")
                print_global_separator()

                print("""
            🎨 STRING FORMATTING METHODS:

            1️⃣ f-strings (Python 3.6+): RECOMMENDED!
            name = "Alice"
            age = 25
            message = f"My name is {name} and I am {age} years old."
            # Result: "My name is Alice and I am 25 years old."

            2️⃣ format() method:
            message = "My name is {} and I am {} years old.".format(name, age)

            3️⃣ % formatting (old style):
            message = "My name is %s and I am %d years old." % (name, age)

            🎯 NUMBER FORMATTING:
            price = 49.9999
            formatted = f"Price: ${price:.2f}"  # "Price: $50.00"

            pi = 3.1415926535
            formatted_pi = f"Pi: {pi:.4f}"     # "Pi: 3.1416"
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    name = "Alice"
                    age = 25
                    price = 49.9999
                    print(f"\n   name = \"{name}\", age = {age}, price = {price}")
                    print(f"   f-string: f'Name: {name}, Age: {age}' = \"{f'Name: {name}, Age: {age}'}\"")
                    print("   format(): 'Name: {}, Age: {}' = \"" + 'Name: {}, Age: {}'.format(name, age) + "\"")
                    print(f"   Number formatting: f'Price: ${price:.2f}' = \"{f'Price: ${price:.2f}'}\"")

            # ----------------------------------------------------------
            # Sub-topic 6: Common Errors & Best Practices
            # ----------------------------------------------------------
            def teach_string_errors():
                """Teach common string errors and best practices"""
                print_global_separator()
                print("📘 PART 6: Common Errors & Best Practices")
                print_global_separator()

                print("""
            ⚠️ COMMON STRING ERRORS:

            1️⃣ IMMUTABILITY ERROR:
            text = "Hello"
            text[0] = "J"  # ❌ ERROR! Strings are immutable

            Correct approach:
            text = "J" + text[1:]  # ✅ Creates new string "Jello"

            2️⃣ ESCAPE CHARACTERS:
            # Wrong: path = "C:\\new folder"  # \\n is newline!
            # Right: path = "C:\\\\new folder" or r"C:\\new folder"

            Common escape sequences:
            \\n → New line
            \\t → Tab
            \\\\ → Backslash
            \\" → Double quote
            \\' → Single quote

            3️⃣ MIXING DATA TYPES:
            age = 25
            # Wrong: message = "I am " + age + " years old"
            # Right: message = "I am " + str(age) + " years old"
            # Better: message = f"I am {age} years old"

            💡 BEST PRACTICES:
            1. Use f-strings for formatting (Python 3.6+)
            2. Remember strings are IMMUTABLE
            3. Use .strip() to clean user input
            4. Prefer .join() for concatenating many strings
            5. Use raw strings (r"") for paths and regex
                """)

            # --- Run all string sub-topics sequentially ---
            def teach_all_string_topics():
                """Teach all string topics in sequence"""
                teach_string_basics()
                teach_string_indexing()
                teach_string_operations()
                teach_string_methods()
                teach_string_formatting()
                teach_string_errors()

            # --- Main entry point for the Strings chapter ---
            def explain_strings():
                """Comprehensive guide to Python strings"""
                print("\n   💬 What are strings?")
                print("\n💬 STRINGS: TEXT DATA IN PYTHON")
                print_global_separator()

                print("""
            🎯 WHAT ARE STRINGS?
            Strings are SEQUENCES OF CHARACTERS used to store and manipulate text.
            In Python, strings are IMMUTABLE (cannot be changed once created).

            🔧 CREATING STRINGS:
            • Single quotes: 'Hello'
            • Double quotes: "World"
            • Triple quotes: '''Multi-line strings''' or \"\"\"Also multi-line\"\"\"
                """)

                topics_learned = []  # tracks sub-topics already covered

                while True:
                    # Display the strings sub-menu
                    print("\n📚 STRINGS TOPIC MENU:")
                    print("   1. String Basics & Creation")
                    print("   2. Indexing & Slicing")
                    print("   3. String Operations")
                    print("   4. String Methods")
                    print("   5. String Formatting")
                    print("   6. Common Errors & Best Practices")
                    print("   7. All topics (Complete guide)")
                    print("   8. I'm done with strings (exit strings)")

                    topic_choice = get_global_menu_choice(
                        "\n🔹 Which string topic would you like to learn? (1-8/exit): ", 1, 8
                    )

                    if topic_choice == 'exit':
                        print("\n✅ Returning to main menu...")
                        return

                    if topic_choice == '8':
                        print("\n✅ Exiting strings section...")
                        return

                    # Prevent re-teaching the same sub-topic unless the user explicitly wants a review
                    if topic_choice in topics_learned and topic_choice != '7':
                        review = get_global_valid_input(
                            f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): "
                        )
                        if review == 'no':
                            continue

                    # "All topics" dumps everything in one go
                    if topic_choice == '7':
                        teach_all_string_topics()
                        topics_learned = ['1', '2', '3', '4', '5', '6']
                        print_global_separator()
                        print("🎉 COMPLETE STRINGS GUIDE FINISHED!")
                        print_global_separator()
                        return

                    # Individual sub-topic selection
                    if topic_choice == '1':
                        teach_string_basics()
                        if '1' not in topics_learned:
                            topics_learned.append('1')
                    elif topic_choice == '2':
                        teach_string_indexing()
                        if '2' not in topics_learned:
                            topics_learned.append('2')
                    elif topic_choice == '3':
                        teach_string_operations()
                        if '3' not in topics_learned:
                            topics_learned.append('3')
                    elif topic_choice == '4':
                        teach_string_methods()
                        if '4' not in topics_learned:
                            topics_learned.append('4')
                    elif topic_choice == '5':
                        teach_string_formatting()
                        if '5' not in topics_learned:
                            topics_learned.append('5')
                    elif topic_choice == '6':
                        teach_string_errors()
                        if '6' not in topics_learned:
                            topics_learned.append('6')

                    # Ask if user wants to continue with strings
                    continue_learning = get_global_valid_input(
                        "\n🔹 Want to learn another string topic? (yes/no): "
                    )
                    if continue_learning == 'no':
                        print("\n✅ Exiting strings section...")
                        return

            explain_strings()

            # ---- PRACTICE: STRINGS ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with strings? (yes/no): "
            )
            if practice == 'yes':
                def check_strings_practice(code, output):
                    """Checks if multiple string operations are used"""
                    if '=' not in code:
                        return False, "Create a string variable using '='!"
                    if 'print' not in code:
                        return False, "Use print() to display results!"

                    string_operations = [
                        'upper(', 'lower(', 'strip(', 'replace(', 'split(',
                        'join(', '+', '*', '['
                    ]
                    found_operations = [op for op in string_operations if op in code]

                    if len(found_operations) < 3:
                        return False, (
                            f"Use at least 3 string operations/methods! "
                            f"Found: {len(found_operations)}"
                        )
                    return True, ""

                run_practice_session(
                    topic_name="Strings",
                    instructions="Create a string variable with your name. Use at least 3 string operations (e.g., upper(), lower(), concatenation with +, indexing with [], or slicing). Print each result!",
                    expected_keywords=['=', 'print'],
                    example_code=(
                        "name = 'Python Learner'\n"
                        "print(f'Original: {name}')\n"
                        "print(f'Uppercase: {name.upper()}')\n"
                        "print(f'First letter: {name[0]}')\n"
                        "print(f'First 6 chars: {name[:6]}')\n"
                        "print(f'Reversed: {name[::-1]}')"
                    ),
                    custom_check_function=check_strings_practice,
                )

            print("Excellent! You've learned comprehensive string handling in Python!")

        elif selected_topic == 'Data types in Python':
            # ======================================================
            # TOPIC 11: DATA TYPES IN PYTHON
            # ======================================================
            print_global_separator()
            print("11. Data Types in Python:")

            def explain_data_types():
                print("\n   📊 What are data types?")
                print("\n📊 DATA TYPES: CATEGORIES OF VALUES")
                print_global_separator()

                print("""
                🎯 WHAT ARE THEY?
                Data types classify the kind of value a variable holds.
                They determine what operations can be performed on that value.

                🔧 COMMON DATA TYPES:
                1️⃣ int     → Integer numbers (e.g., 42, -5, 0)
                2️⃣ float   → Decimal numbers (e.g., 3.14, -0.001, 2.0)
                3️⃣ str     → Text/strings (e.g., "Hello", 'Python', "123")
                4️⃣ bool    → Boolean values (True or False)
                5️⃣ list    → Collection of items (e.g., [1, 2, 3])
                6️⃣ tuple   → Immutable collection (e.g., (1, 2, 3))
                7️⃣ dict    → Key-value pairs (e.g., {"name": "Alice"})

                💡 EXAMPLES:
                age = 30              # int
                price = 19.99         # float
                name = "Alice"        # str
                is_student = True     # bool
                scores = [85, 90, 78] # list
                colors = ("red", "blue") # tuple
                person = {"name": "Bob", "age": 25} # dict

                🔑 KEY POINTS:
                • Use type() to check data type
                • Different types support different operations
                • Strings and numbers cannot be directly added
                • Lists are mutable (can change), tuples are immutable
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples of data types? (yes/no): "
                )
                if examples_choice == 'yes':
                    age = 30
                    price = 19.99
                    name = "Alice"
                    is_student = True
                    scores = [85, 90, 78]
                    print(f"\n   age = {age} (Type: {type(age).__name__})")
                    print(f"   price = {price} (Type: {type(price).__name__})")
                    print(f"   name = \"{name}\" (Type: {type(name).__name__})")
                    print(f"   is_student = {is_student} (Type: {type(is_student).__name__})")
                    print(f"   scores = {scores} (Type: {type(scores).__name__})")

            explain_data_types()

            # ---- PRACTICE: DATA TYPES ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with data types? (yes/no): "
            )
            if practice == 'yes':
                def check_datatypes_practice(code, output):
                    """Checks if type() is used and multiple data types are created"""
                    if 'type(' not in code:
                        return False, "Use type() to check the data type of variables!"
                    if '=' not in code:
                        return False, "Create variables with different data types!"
                    if 'print' not in code:
                        return False, "Use print() to display the types!"

                    data_type_keywords = [
                        'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict'
                    ]
                    found_types = [t for t in data_type_keywords if t in code.lower()]

                    if len(found_types) < 3:
                        return False, (
                            f"Create at least 3 different data types! Found: {found_types}"
                        )
                    return True, ""

                run_practice_session(
                    topic_name="Data Types",
                    instructions="Create at least 4 variables of different data types (int, float, str, bool). Use type() to check and print each variable's type!",
                    expected_keywords=['type(', 'print'],
                    example_code=(
                        "age = 25\n"
                        "score = 95.5\n"
                        "name = 'Student'\n"
                        "is_active = True\n"
                        "print(f'age type: {type(age)}')\n"
                        "print(f'score type: {type(score)}')\n"
                        "print(f'name type: {type(name)}')\n"
                        "print(f'is_active type: {type(is_active)}')"
                    ),
                    custom_check_function=check_datatypes_practice,
                )

            print("Great! You've learned about different data types in Python!")

        elif selected_topic == 'Conditional statements':
            # ======================================================
            # TOPIC 12: CONDITIONAL STATEMENTS
            # ======================================================
            print_global_separator()
            print("12. Conditional Statements in Python:")

            # ----------------------------------------------------------
            # Sub-topic 1: Basic IF statements
            # ----------------------------------------------------------
            def teach_conditionals_basics():
                """Teach conditional statements basics"""
                print_global_separator()
                print("📘 PART 1: IF Statements - The Basics")
                print_global_separator()

                print("""
            🤔 WHAT ARE CONDITIONAL STATEMENTS?
            Conditional statements are Python's DECISION-MAKERS! They allow
            your program to choose different paths based on conditions.

            🎯 THE 'if' STATEMENT (The Gatekeeper):
            syntax:
            if condition:
                # Code block executes ONLY if condition is True

            💡 EXAMPLE:
            temperature = 30

            if temperature > 25:
                print("It's hot outside!")
            # Output: "It's hot outside!" (since 30 > 25)

            🔑 KEY POINTS:
            • Conditions evaluate to True or False
            • Indentation (4 spaces) is MANDATORY
            • Code runs ONLY when condition is True
            • Think of it as: "IF this is true, THEN do this"
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see more if examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 IF STATEMENT EXAMPLES:")
                    print("   # Check if user is old enough to drive")
                    print("   age = 18")
                    print("   if age >= 16:")
                    print("       print('You can get a driver\\'s license!')")
                    print("   # Output: You can get a driver's license!")
                    print()
                    print("   # Check if a number is positive")
                    print("   number = 5")
                    print("   if number > 0:")
                    print("       print(f'{number} is positive')")
                    print("   # Output: 5 is positive")

            # ----------------------------------------------------------
            # Sub-topic 2: If-Else statements
            # ----------------------------------------------------------
            def teach_if_else():
                """Teach if-else statements"""
                print_global_separator()
                print("📘 PART 2: If-Else Statements - Two Paths")
                print_global_separator()

                print("""
            🎯 THE 'if-else' STATEMENT (The Fork in the Road):
            syntax:
            if condition:
                # Code block if condition is True
            else:
                # Code block if condition is False

            💡 REAL-LIFE ANALOGY:
            Like a coin flip: HEADS → do this, TAILS → do that!

            🔧 EXAMPLE:
            password = "python123"

            if password == "python123":
                print("Access granted! ✅")
            else:
                print("Access denied! ❌")

            🎮 PRACTICAL USE:
            # Check voting eligibility
            age = 17

            if age >= 18:
                print("You can vote in elections!")
            else:
                print(f"Wait {18 - age} more years to vote.")
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see if-else examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 IF-ELSE EXAMPLES:")
                    print("   # Check if number is even or odd")
                    print("   num = 7")
                    print("   if num % 2 == 0:")
                    print("       print(f'{num} is even')")
                    print("   else:")
                    print("       print(f'{num} is odd')")
                    print("   # Output: 7 is odd")
                    print()
                    print("   # Temperature check")
                    print("   temp = 15")
                    print("   if temp > 20:")
                    print("       print('Wear shorts! 🩳')")
                    print("   else:")
                    print("       print('Wear a jacket! 🧥')")
                    print("   # Output: Wear a jacket! 🧥")

            # ----------------------------------------------------------
            # Sub-topic 3: Elif (else if) statements
            # ----------------------------------------------------------
            def teach_elif():
                """Teach elif statements"""
                print_global_separator()
                print("📘 PART 3: Elif Statements - Multiple Paths")
                print_global_separator()

                print("""
            🎯 THE 'if-elif-else' STATEMENT (The Menu):
            syntax:
            if condition1:
                # Code for condition1
            elif condition2:
                # Code for condition2
            elif condition3:
                # Code for condition3
            else:
                # Code if none are True

            💡 REAL-LIFE ANALOGY:
            Like a RESTAURANT MENU:
            • IF you want pizza → order pizza
            • ELIF you want burger → order burger
            • ELIF you want salad → order salad
            • ELSE → order water 😢

            🔧 IMPORTANT:
            • Python checks conditions IN ORDER
            • Stops at the FIRST True condition
            • 'elif' can be used multiple times
            • 'else' is optional

            🎮 EXAMPLE:
            score = 85

            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'

            print(f"Score: {score}, Grade: {grade}")  # Score: 85, Grade: B
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see elif examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 ELIF EXAMPLES:")
                    print("   # Traffic light system")
                    print("   light = 'yellow'")
                    print("   if light == 'red':")
                    print("       print('STOP! 🛑')")
                    print("   elif light == 'yellow':")
                    print("       print('SLOW DOWN! ⚠️')")
                    print("   elif light == 'green':")
                    print("       print('GO! 🟢')")
                    print("   else:")
                    print("       print('Invalid light color')")
                    print("   # Output: SLOW DOWN! ⚠️")
                    print()
                    print("   # Day of week check")
                    print("   day = 'Saturday'")
                    print("   if day == 'Saturday' or day == 'Sunday':")
                    print("       print('It\\'s the weekend! 🎉')")
                    print("   elif day == 'Friday':")
                    print("       print('TGIF! Almost weekend! 📅')")
                    print("   else:")
                    print("       print('Time to work! 💼')")
                    print("   # Output: It's the weekend! 🎉")

            # ----------------------------------------------------------
            # Sub-topic 4: Nested conditionals
            # ----------------------------------------------------------
            def teach_nested_conditionals():
                """Teach nested conditional statements"""
                print_global_separator()
                print("📘 PART 4: Nested Conditionals - Decisions Within Decisions")
                print_global_separator()

                print("""
            🎯 NESTED CONDITIONALS:
            Putting if statements INSIDE other if statements.

            💡 REAL-LIFE ANALOGY:
            Like applying for a job:
            • IF you have degree
                • IF you have experience → Get senior position
                • ELSE → Get junior position
            • ELSE → No interview 😢

            🔧 EXAMPLE:
            age = 25
            has_license = True

            if age >= 18:
                print("You are old enough!")
                if has_license:
                    print("You can drive a car! 🚗")
                else:
                    print("Get your license first! 📝")
            else:
                print(f"Wait {18 - age} years to drive.")

            ⚠️ IMPORTANT:
            • Keep nesting levels LIMITED (3-4 max)
            • Deep nesting = Hard to read code
            • Consider using logical operators (and/or) instead
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see nested conditionals examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 NESTED CONDITIONALS EXAMPLES:")
                    print("   # Restaurant ordering system")
                    print("   hungry = True")
                    print("   has_money = True")
                    print("   ")
                    print("   if hungry:")
                    print("       print('Looking for food... 🍽️')")
                    print("       if has_money:")
                    print("           print('Going to a restaurant! 🍜')")
                    print("       else:")
                    print("           print('Cooking at home! 🏠')")
                    print("   else:")
                    print("       print('Not hungry, maybe later! 😴')")
                    print()
                    print("   # Login system")
                    print("   username = 'student'")
                    print("   password = 'python123'")
                    print("   ")
                    print("   if username == 'student':")
                    print("       print('Username correct! ✓')")
                    print("       if password == 'python123':")
                    print("           print('Access granted! Welcome! 🎉')")
                    print("       else:")
                    print("           print('Wrong password! ❌')")
                    print("   else:")
                    print("       print('Username not found! ❌')")

            # ----------------------------------------------------------
            # Sub-topic 5: Combining conditions with AND, OR, NOT
            # ----------------------------------------------------------
            def teach_conditional_operators():
                """Teach combining conditions with logical operators"""
                print_global_separator()
                print("📘 PART 5: Combining Conditions - AND, OR, NOT")
                print_global_separator()

                print("""
            🎯 COMBINING MULTIPLE CONDITIONS:
            Use logical operators to check multiple conditions at once.

            🔧 LOGICAL OPERATORS IN CONDITIONALS:

            and → ALL conditions must be True
            if age >= 18 and has_id:
                print("Can enter club")

            or → AT LEAST ONE condition must be True
            if day == 'Saturday' or day == 'Sunday':
                print("Weekend! 🎉")

            not → REVERSES the condition
            if not is_raining:
                print("Go for a walk! ☀️")

            💡 REAL EXAMPLES:
            # Scholarship eligibility
            gpa = 3.5
            family_income = 40000
            is_first_gen = True

            if gpa >= 3.0 and family_income < 50000:
                print("Eligible for need-based scholarship!")

            if is_first_gen or gpa >= 3.8:
                print("Eligible for merit scholarship!")

            # Weekend shopping
            is_weekend = True
            has_coupon = False

            if is_weekend or has_coupon:
                print("Let's go shopping! 🛍️")
            else:
                print("Wait for weekend or coupon! ⏰")
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see combined conditions examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 COMBINED CONDITIONS EXAMPLES:")
                    print("   # Movie ticket pricing")
                    print("   age = 12")
                    print("   is_student = True")
                    print("   ")
                    print("   if age < 5:")
                    print("       price = 'Free'")
                    print("   elif age < 18 or is_student:")
                    print("       price = 'Discounted ($8)'")
                    print("   else:")
                    print("       price = 'Regular ($12)'")
                    print("   print(f'Price: {price}')")
                    print("   # Output: Price: Discounted ($8)")
                    print()
                    print("   # Weather decision maker")
                    print("   is_raining = False")
                    print("   is_sunny = True")
                    print("   temperature = 25")
                    print("   ")
                    print("   if not is_raining and temperature > 20:")
                    print("       print('Perfect day for outdoor activities! ☀️')")
                    print("   elif is_raining or temperature < 10:")
                    print("       print('Better stay indoors! 🏠')")
                    print("   else:")
                    print("       print('Maybe a light jacket is enough 🧥')")

            # ----------------------------------------------------------
            # Sub-topic 6: Common mistakes & best practices
            # ----------------------------------------------------------
            def teach_common_mistakes():
                """Teach common mistakes with conditional statements"""
                print_global_separator()
                print("📘 PART 6: Common Mistakes & Best Practices")
                print_global_separator()

                print("""
            ⚠️ COMMON MISTAKES:

            1️⃣ INDENTATION ERRORS:
            # WRONG ❌
            if age >= 18:
            print("Adult")  # Indentation error!

            # CORRECT ✓
            if age >= 18:
                print("Adult")

            2️⃣ USING = INSTEAD OF ==:
            # WRONG ❌ (Assignment, not comparison)
            if age = 18:
                print("You are 18")

            # CORRECT ✓
            if age == 18:
                print("You are 18")

            3️⃣ FORGETTING COLON:
            # WRONG ❌
            if age >= 18
                print("Adult")

            # CORRECT ✓
            if age >= 18:
                print("Adult")

            4️⃣ WRONG INDENTATION LEVEL:
            # WRONG ❌ (Mixing spaces and tabs)
            if condition:
              print("4 spaces")
             print("Mixed spaces")  # Inconsistent!

            5️⃣ LOGICAL OPERATOR CONFUSION:
            # WRONG ❌ (This is always True!)
            if age == 18 or 21:
                print("Age is 18 or 21")

            # CORRECT ✓
            if age == 18 or age == 21:
                print("Age is 18 or 21")

            💡 BEST PRACTICES:
            1. Always use 4 spaces for indentation
            2. Keep conditions simple and readable
            3. Use parentheses for complex conditions
            4. Limit nesting depth (max 3-4 levels)
            5. Use elif for mutually exclusive conditions
            6. Consider using dictionaries for many conditions
            7. Write conditions that read like English
                """)

                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see examples of best practices? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 BEST PRACTICE EXAMPLES:")
                    print("   # Good: Readable condition")
                    print("   is_eligible = age >= 18 and has_license and not is_suspended")
                    print("   if is_eligible:")
                    print("       print('Can drive')\n")
                    print("   # Better: Using parentheses for clarity")
                    print("   if (age >= 18) and (has_license) and (not is_suspended):")
                    print("       print('Can drive')\n")
                    print("   # Using dictionary instead of many elifs")
                    print("   day = 'Monday'")
                    print("   schedules = {")
                    print("       'Monday': 'Meeting at 10 AM',")
                    print("       'Tuesday': 'Workshop at 2 PM',")
                    print("       'Wednesday': 'No events'")
                    print("   }")
                    print("   print(schedules.get(day, 'No schedule found'))")

            # --- Run all conditional sub-topics sequentially ---
            def teach_all_conditional_topics():
                """Teach all conditional topics in sequence"""
                teach_conditionals_basics()
                teach_if_else()
                teach_elif()
                teach_nested_conditionals()
                teach_conditional_operators()
                teach_common_mistakes()

            # --- Main entry point for the Conditionals chapter ---
            def explain_conditional_statements():
                """Comprehensive guide to conditional statements"""
                print("\n   🤔 What are conditional statements?")
                print("\n🤔 CONDITIONAL STATEMENTS: CODE'S DECISION-MAKERS")
                print_global_separator()

                print("""
            🎯 WHAT ARE THEY?
            Conditional statements allow your code to MAKE DECISIONS
            and execute different blocks of code based on conditions.

            🔧 THE DECISION-MAKING TOOLKIT:
            if     → Executes block if condition is True
            elif   → Checks another condition if previous was False
            else   → Executes block if all previous conditions were False

            🔑 IMPORTANT NOTE:
            Indentation is CRUCIAL in Python to define code blocks!
                """)

                topics_learned = []

                while True:
                    # Display the conditionals sub-menu
                    print("\n📚 CONDITIONAL STATEMENTS TOPIC MENU:")
                    print("   1. IF Statements - The Basics")
                    print("   2. If-Else Statements - Two Paths")
                    print("   3. Elif Statements - Multiple Paths")
                    print("   4. Nested Conditionals - Decisions Within Decisions")
                    print("   5. Combining Conditions - AND, OR, NOT")
                    print("   6. Common Mistakes & Best Practices")
                    print("   7. All topics (Complete guide)")
                    print("   8. I'm done with conditionals (exit)")

                    topic_choice = get_global_menu_choice(
                        "\n🔹 Which conditional topic would you like to learn? (1-8/exit): ", 1, 8
                    )

                    if topic_choice == 'exit':
                        print("\n✅ Returning to main menu...")
                        return

                    if topic_choice == '8':
                        print("\n✅ Exiting conditional statements section...")
                        return

                    if topic_choice in topics_learned and topic_choice != '7':
                        review = get_global_valid_input(
                            f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): "
                        )
                        if review == 'no':
                            continue

                    if topic_choice == '7':
                        teach_all_conditional_topics()
                        topics_learned = ['1', '2', '3', '4', '5', '6']
                        print_global_separator()
                        print("🎉 COMPLETE CONDITIONAL STATEMENTS GUIDE FINISHED!")
                        print_global_separator()
                        return

                    if topic_choice == '1':
                        teach_conditionals_basics()
                        if '1' not in topics_learned:
                            topics_learned.append('1')
                    elif topic_choice == '2':
                        teach_if_else()
                        if '2' not in topics_learned:
                            topics_learned.append('2')
                    elif topic_choice == '3':
                        teach_elif()
                        if '3' not in topics_learned:
                            topics_learned.append('3')
                    elif topic_choice == '4':
                        teach_nested_conditionals()
                        if '4' not in topics_learned:
                            topics_learned.append('4')
                    elif topic_choice == '5':
                        teach_conditional_operators()
                        if '5' not in topics_learned:
                            topics_learned.append('5')
                    elif topic_choice == '6':
                        teach_common_mistakes()
                        if '6' not in topics_learned:
                            topics_learned.append('6')

                    continue_learning = get_global_valid_input(
                        "\n🔹 Want to learn another conditional topic? (yes/no): "
                    )
                    if continue_learning == 'no':
                        print("\n✅ Exiting conditional statements section...")
                        return

            explain_conditional_statements()

            # ---- PRACTICE: CONDITIONAL STATEMENTS ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with conditional statements? (yes/no): "
            )
            if practice == 'yes':
                def check_conditionals_practice(code, output):
                    """Checks if if-elif-else structure and indentation are correct"""
                    if 'if ' not in code:
                        return False, "You need an 'if' statement!"
                    if 'else' not in code:
                        return False, "Use an 'else' block as well!"
                    if 'print(' not in code:
                        return False, "Use print() in your conditional blocks!"

                    lines = code.split('\n')
                    indented_lines = [
                        l for l in lines if l.startswith('    ') or l.startswith('\t')
                    ]
                    if len(indented_lines) < 2:
                        return False, "Make sure to indent the code inside if/else blocks (4 spaces)!"
                    return True, ""

                run_practice_session(
                    topic_name="Conditional Statements",
                    instructions="Write a program that checks if a number is positive, negative, or zero. Use if-elif-else statements and print the result!",
                    expected_keywords=['if', 'elif', 'else', 'print'],
                    example_code=(
                        "num = 10\n"
                        "if num > 0:\n"
                        "    print('Positive number')\n"
                        "elif num < 0:\n"
                        "    print('Negative number')\n"
                        "else:\n"
                        "    print('Zero')"
                    ),
                    custom_check_function=check_conditionals_practice,
                )

            print("Excellent! You've learned comprehensive conditional statements in Python!")

        elif selected_topic == 'Lists in Python':
            # ======================================================
            # TOPIC 13: LISTS IN PYTHON
            # ======================================================
            print_global_separator()
            print("13. Lists in Python:")

            # ----------------------------------------------------------
            # Sub-topic 1: List Basics & Creation
            # ----------------------------------------------------------
            def teach_list_basics():
                """Teach what lists are and how to create them"""
                print_global_separator()
                print("📘 PART 1: List Basics & Creation")
                print_global_separator()
                print("""
            📦 WHAT IS A LIST?
            A list is a COLLECTION that can hold multiple items in a single variable.
            Lists are ORDERED, CHANGEABLE (mutable), and allow DUPLICATE values.

            🎯 CREATING LISTS:
            empty_list = []                     # Empty list
            numbers = [1, 2, 3, 4, 5]           # List of integers
            fruits = ["apple", "banana", "cherry"] # List of strings
            mixed = [10, "hello", 3.14, True]   # Mixed data types

            🔑 KEY PROPERTIES:
            • Ordered – items have a defined order (index 0,1,2...)
            • Mutable – you can change, add, or remove items
            • Indexed – each item can be accessed by its position
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see list examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 LIST EXAMPLES:")
                    numbers = [1, 2, 3, 4, 5]
                    fruits = ["apple", "banana", "cherry"]
                    mixed = [10, "hello", 3.14, True]
                    print(f"   numbers = {numbers}")
                    print(f"   fruits = {fruits}")
                    print(f"   mixed = {mixed}")
                    print(f"   Type of numbers: {type(numbers).__name__}")

            # ----------------------------------------------------------
            # Sub-topic 2: Accessing Items (Indexing)
            # ----------------------------------------------------------
            def teach_list_indexing():
                """Teach how to access list elements using indices"""
                print_global_separator()
                print("📘 PART 2: Accessing Items – Indexing")
                print_global_separator()
                print("""
            🔢 INDEXING (Zero-based):
            List:      ["apple", "banana", "cherry", "date"]
            Index:       0        1         2        3
            Negative:   -4       -3        -2       -1

            🎯 ACCESSING ELEMENTS:
            fruits = ["apple", "banana", "cherry"]
            first = fruits[0]      # "apple"
            last = fruits[-1]      # "cherry"
            second = fruits[1]     # "banana"

            💡 REMEMBER: Index starts at 0, not 1!
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see indexing examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    fruits = ["apple", "banana", "cherry", "date"]
                    print(f"\n   fruits = {fruits}")
                    print(f"   fruits[0] → '{fruits[0]}'")
                    print(f"   fruits[2] → '{fruits[2]}'")
                    print(f"   fruits[-1] → '{fruits[-1]}'")
                    print(f"   fruits[-3] → '{fruits[-3]}'")

            # ----------------------------------------------------------
            # Sub-topic 3: Slicing Lists
            # ----------------------------------------------------------
            def teach_list_slicing():
                """Teach how to extract sublists using slicing"""
                print_global_separator()
                print("📘 PART 3: Slicing Lists")
                print_global_separator()
                print("""
            🔪 SLICING SYNTAX:
            list[start:end:step]
            • start – index to begin (inclusive)
            • end   – index to stop (exclusive)
            • step  – interval (optional)

            🎯 EXAMPLES:
            numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            numbers[2:5]   → [2, 3, 4]     # indices 2,3,4
            numbers[:4]    → [0, 1, 2, 3]  # from start to index 4 (exclusive)
            numbers[6:]    → [6, 7, 8, 9]  # from index 6 to end
            numbers[::2]   → [0, 2, 4, 6, 8]  # every 2nd element
            numbers[::-1]  → [9,8,7,6,5,4,3,2,1,0]  # reverse
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see slicing examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    print(f"\n   numbers = {numbers}")
                    print(f"   numbers[2:5] → {numbers[2:5]}")
                    print(f"   numbers[:4] → {numbers[:4]}")
                    print(f"   numbers[6:] → {numbers[6:]}")
                    print(f"   numbers[::2] → {numbers[::2]}")
                    print(f"   numbers[::-1] → {numbers[::-1]}")

            # ----------------------------------------------------------
            # Sub-topic 4: List Methods (append, extend, insert, remove, pop)
            # ----------------------------------------------------------
            def teach_list_methods():
                """Teach common list methods"""
                print_global_separator()
                print("📘 PART 4: Common List Methods")
                print_global_separator()
                print("""
            🛠️ MUTATING METHODS (change the list):

            1. append(item)   – Adds an item to the END
            fruits = ["apple", "banana"]
            fruits.append("cherry")
            # fruits → ["apple", "banana", "cherry"]

            2. extend(iterable) – Adds multiple items from another list
            fruits.extend(["date", "elderberry"])
            # fruits → ["apple", "banana", "cherry", "date", "elderberry"]

            3. insert(index, item) – Inserts at a specific position
            fruits.insert(1, "blueberry")
            # fruits → ["apple", "blueberry", "banana", ...]

            4. remove(item)   – Removes the FIRST occurrence of an item
            fruits.remove("banana")
            # removes "banana"

            5. pop(index)     – Removes and returns item at index (default last)
            last = fruits.pop()        # removes and returns last item
            second = fruits.pop(1)     # removes item at index 1

            6. clear()        – Removes all items
            fruits.clear()    # []

            📊 OTHER USEFUL METHODS:
            • index(item) – returns the index of first occurrence
            • count(item) – counts how many times item appears
            • sort()      – sorts the list in place
            • reverse()   – reverses the list in place
            • copy()      – returns a shallow copy
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see list methods in action? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 METHOD EXAMPLES:")
                    fruits = ["apple", "banana", "cherry"]
                    print(f"   Initial: {fruits}")
                    fruits.append("date")
                    print(f"   After append('date'): {fruits}")
                    fruits.insert(1, "blueberry")
                    print(f"   After insert(1, 'blueberry'): {fruits}")
                    fruits.remove("banana")
                    print(f"   After remove('banana'): {fruits}")
                    popped = fruits.pop()
                    print(f"   After pop(): {fruits} (removed '{popped}')")
                    fruits.sort()
                    print(f"   After sort(): {fruits}")

            # ----------------------------------------------------------
            # Sub-topic 5: List Operations (concatenation, repetition, membership)
            # ----------------------------------------------------------
            def teach_list_operations():
                """Teach operations on lists: +, *, in, not in"""
                print_global_separator()
                print("📘 PART 5: List Operations")
                print_global_separator()
                print("""
            ⚙️ CONCATENATION (+):
            list1 = [1, 2, 3]
            list2 = [4, 5, 6]
            combined = list1 + list2   # [1, 2, 3, 4, 5, 6]

            🔁 REPETITION (*):
            zeros = [0] * 5            # [0, 0, 0, 0, 0]
            pattern = [1, 2] * 3       # [1, 2, 1, 2, 1, 2]

            🔍 MEMBERSHIP (in / not in):
            fruits = ["apple", "banana", "cherry"]
            has_apple = "apple" in fruits      # True
            has_grape = "grape" in fruits      # False
            no_banana = "banana" not in fruits # False

            📏 LENGTH:
            length = len(fruits)       # number of items
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see list operation examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    a = [1, 2, 3]
                    b = [4, 5, 6]
                    print(f"   a = {a}, b = {b}")
                    print(f"   a + b = {a + b}")
                    print(f"   [0] * 5 = {[0] * 5}")
                    fruits = ["apple", "banana", "cherry"]
                    print(f"   fruits = {fruits}")
                    print(f"   'banana' in fruits → {'banana' in fruits}")
                    print(f"   'grape' not in fruits → {'grape' not in fruits}")
                    print(f"   len(fruits) = {len(fruits)}")

            # ----------------------------------------------------------
            # Sub-topic 6: Looping Through Lists
            # ----------------------------------------------------------
            def teach_list_looping():
                """Teach how to iterate over lists using for loops"""
                print_global_separator()
                print("📘 PART 6: Looping Through Lists")
                print_global_separator()
                print("""
            🔁 ITERATING OVER LISTS:

            1. Loop through items directly:
            fruits = ["apple", "banana", "cherry"]
            for fruit in fruits:
                print(fruit)

            2. Loop with index using range() and len():
            for i in range(len(fruits)):
                print(f"{i}: {fruits[i]}")

            3. Loop with enumerate() (gives both index and value):
            for i, fruit in enumerate(fruits):
                print(f"{i}: {fruit}")

            🎯 EXAMPLE:
            numbers = [10, 20, 30, 40]
            total = 0
            for num in numbers:
                total += num
            print(f"Sum: {total}")   # Sum: 100
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see looping examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    fruits = ["apple", "banana", "cherry"]
                    print("\n📝 LOOPING EXAMPLES:")
                    print("   # Simple for loop:")
                    for fruit in fruits:
                        print(f"      {fruit}")
                    print("   # With enumerate:")
                    for i, fruit in enumerate(fruits):
                        print(f"      Index {i}: {fruit}")

            # ----------------------------------------------------------
            # Sub-topic 7: List Comprehension (bonus)
            # ----------------------------------------------------------
            def teach_list_comprehension():
                """Teach list comprehension for concise list creation"""
                print_global_separator()
                print("📘 PART 7: List Comprehension (Concise List Creation)")
                print_global_separator()
                print("""
            ✨ LIST COMPREHENSION – A Python superpower!
            Creates a new list by applying an expression to each item in an iterable.

            🔧 SYNTAX:
            new_list = [expression for item in iterable if condition]

            🎯 EXAMPLES:
            # Square numbers 0-9
            squares = [x**2 for x in range(10)]
            # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

            # Even numbers from 0-9
            evens = [x for x in range(10) if x % 2 == 0]
            # [0, 2, 4, 6, 8]

            # Uppercase each fruit
            fruits = ["apple", "banana", "cherry"]
            upper_fruits = [fruit.upper() for fruit in fruits]
            # ["APPLE", "BANANA", "CHERRY"]

            # With condition
            numbers = [1, 2, 3, 4, 5]
            parity = ["even" if n % 2 == 0 else "odd" for n in numbers]
            # ["odd", "even", "odd", "even", "odd"]
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see list comprehension examples? (yes/no): "
                )
                if examples_choice == 'yes':
                    squares = [x**2 for x in range(5)]
                    evens = [x for x in range(10) if x % 2 == 0]
                    fruits = ["apple", "banana", "cherry"]
                    upper_fruits = [fruit.upper() for fruit in fruits]
                    print(f"\n   [x**2 for x in range(5)] → {squares}")
                    print(f"   [x for x in range(10) if x % 2 == 0] → {evens}")
                    print(f"   [fruit.upper() for fruit in {fruits}] → {upper_fruits}")

            # ----------------------------------------------------------
            # Sub-topic 8: Common Errors & Best Practices
            # ----------------------------------------------------------
            def teach_list_errors():
                """Teach common mistakes when working with lists"""
                print_global_separator()
                print("📘 PART 8: Common Errors & Best Practices")
                print_global_separator()
                print("""
            ⚠️ COMMON MISTAKES:

            1️⃣ IndexError – accessing index that doesn't exist
            fruits = ["apple", "banana"]
            # print(fruits[2])  ❌ IndexError: list index out of range

            2️⃣ Modifying list while iterating (can skip items)
            # WRONG ❌
            for fruit in fruits:
                if fruit == "banana":
                    fruits.remove(fruit)   # Dangerous!

            # CORRECT ✓
            fruits = [f for f in fruits if f != "banana"]

            3️⃣ Using '=' to copy a list (creates reference, not copy)
            original = [1, 2, 3]
            copy = original       # Both point to same list!
            copy.append(4)
            # original now also [1,2,3,4]   😲

            # Use copy() or slicing for a true copy:
            proper_copy = original.copy()
            proper_copy = original[:]

            4️⃣ Forgetting that list methods modify in-place
            fruits = ["apple", "banana"]
            result = fruits.append("cherry")   # result is None! append returns None
            print(result)   # None
            # fruits is modified: ["apple", "banana", "cherry"]

            💡 BEST PRACTICES:
            • Use meaningful variable names (student_grades, not lst)
            • Prefer list comprehension for simple transformations
            • Use .append() and .extend() to add items
            • Use .pop() to remove by index, .remove() by value
            • Copy lists explicitly when you need independence
                """)
                examples_choice = get_global_examples_valid_input(
                    "\n🔹 Want to see common errors demonstrated? (yes/no): "
                )
                if examples_choice == 'yes':
                    print("\n📝 COPY EXAMPLE:")
                    original = [1, 2, 3]
                    wrong_copy = original
                    right_copy = original.copy()
                    wrong_copy.append(4)
                    print(f"   original after wrong_copy.append(4): {original}")
                    print(f"   right_copy after original.copy(): {right_copy}")

            # --- Run all list sub-topics sequentially ---
            def teach_all_list_topics():
                """Teach all list topics in sequence"""
                teach_list_basics()
                teach_list_indexing()
                teach_list_slicing()
                teach_list_methods()
                teach_list_operations()
                teach_list_looping()
                teach_list_comprehension()
                teach_list_errors()

            # --- Main entry point for the Lists chapter ---
            def explain_lists():
                """Comprehensive guide to Python lists"""
                print("\n   📋 What are lists?")
                print("\n📋 LISTS: POWERFUL COLLECTIONS IN PYTHON")
                print_global_separator()
                print("""
            🎯 WHAT ARE LISTS?
            Lists are ordered, mutable collections that can hold any data type.
            They are one of Python's most versatile and commonly used data structures.

            🔑 KEY FEATURES:
            • Ordered – items keep their position
            • Mutable – you can change, add, remove items
            • Indexable – access by position (0,1,2...)
            • Slicable – extract portions
            • Iterable – loop through items
            • Heterogeneous – can mix types
                """)

                topics_learned = []

                while True:
                    # Display the lists sub-menu
                    print("\n📚 LISTS TOPIC MENU:")
                    print("   1. List Basics & Creation")
                    print("   2. Accessing Items (Indexing)")
                    print("   3. Slicing Lists")
                    print("   4. List Methods (append, extend, insert, remove, pop)")
                    print("   5. List Operations (concatenation, repetition, membership)")
                    print("   6. Looping Through Lists")
                    print("   7. List Comprehension (bonus)")
                    print("   8. Common Errors & Best Practices")
                    print("   9. All topics (Complete guide)")
                    print("   10. I'm done with lists (exit)")

                    topic_choice = get_global_menu_choice(
                        "\n🔹 Which list topic would you like to learn? (1-10/exit): ", 1, 10
                    )

                    if topic_choice == 'exit':
                        print("\n✅ Returning to main menu...")
                        return

                    if topic_choice == '10':
                        print("\n✅ Exiting lists section...")
                        return

                    if topic_choice in topics_learned and topic_choice != '9':
                        review = get_global_valid_input(
                            f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): "
                        )
                        if review == 'no':
                            continue

                    if topic_choice == '9':
                        teach_all_list_topics()
                        topics_learned = ['1', '2', '3', '4', '5', '6', '7', '8']
                        print_global_separator()
                        print("🎉 COMPLETE LISTS GUIDE FINISHED!")
                        print_global_separator()
                        return

                    if topic_choice == '1':
                        teach_list_basics()
                        if '1' not in topics_learned:
                            topics_learned.append('1')
                    elif topic_choice == '2':
                        teach_list_indexing()
                        if '2' not in topics_learned:
                            topics_learned.append('2')
                    elif topic_choice == '3':
                        teach_list_slicing()
                        if '3' not in topics_learned:
                            topics_learned.append('3')
                    elif topic_choice == '4':
                        teach_list_methods()
                        if '4' not in topics_learned:
                            topics_learned.append('4')
                    elif topic_choice == '5':
                        teach_list_operations()
                        if '5' not in topics_learned:
                            topics_learned.append('5')
                    elif topic_choice == '6':
                        teach_list_looping()
                        if '6' not in topics_learned:
                            topics_learned.append('6')
                    elif topic_choice == '7':
                        teach_list_comprehension()
                        if '7' not in topics_learned:
                            topics_learned.append('7')
                    elif topic_choice == '8':
                        teach_list_errors()
                        if '8' not in topics_learned:
                            topics_learned.append('8')

                    continue_learning = get_global_valid_input(
                        "\n🔹 Want to learn another list topic? (yes/no): "
                    )
                    if continue_learning == 'no':
                        print("\n✅ Exiting lists section...")
                        return

            explain_lists()

            # ---- PRACTICE: LISTS ----
            practice = get_global_valid_input(
                "\n🔹 Want to practice with lists? (yes/no): "
            )
            if practice == 'yes':
                def check_lists_practice(code, output):
                    """Checks if list operations are used properly"""
                    
                    if '= [' not in code:
                        return False, "Remember to put spaces around the = operator! Use: colors = ['red', 'blue']"
                    if 'print' not in code:
                        return False, "Use print() to display results!"
                    list_methods = ['.append(', '.extend(', '.insert(', '.remove(', '.pop(', '.sort(', '.reverse(']
                    method_used = any(m in code for m in list_methods)
                    if not method_used:
                        return False, "Use at least one list method (e.g., .append(), .remove(), .sort())!"
                    if 'for' in code or 'while' in code:
                        # looping is fine, but not required
                        pass
                    return True, ""

                run_practice_session(
                    topic_name="Lists",
                    instructions="Create a list of your favorite colors. Add a new color using append(), remove one color, and sort the list. Print the list after each operation!",
                    expected_keywords=['=', 'print'],
                    example_code=(
                        "colors = ['red', 'blue', 'green']\n"
                        "print(f'Original: {colors}')\n"
                        "colors.append('yellow')\n"
                        "print(f'After append: {colors}')\n"
                        "colors.remove('blue')\n"
                        "print(f'After remove: {colors}')\n"
                        "colors.sort()\n"
                        "print(f'After sort: {colors}')"
                    ),
                    custom_check_function=check_lists_practice
                )

            print("Excellent! You've learned how to work with lists in Python!")

        # ========== SECTION 7: CONTINUE OR EXIT ==========
        print_global_separator()
        learn_more = get_global_valid_input(
            "\n🔹 Would you like to learn another topic? (yes/no/exit): "
        )

        if learn_more == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break
        elif learn_more == 'no':
            break

        # Show menu for next topic
        topic_choice = show_topic_menu(TOPICS, "Which topic would you like to learn next?")
        if topic_choice == 'exit':
            print("\n👋 Goodbye! Come back whenever you need me")
            break

    # ========== FINAL MESSAGE ==========
    print_global_separator()
    print("Congratulations! You've completed the Python basics tutorial 🐍 You learned what you wanted!")
    print("Keep practicing to enhance your skills. 🥷")
    print_global_separator()

except (KeyboardInterrupt, EOFError):
    print("\n👋 Sorry, the program got interrupted or ended, it's not your fault restart again the assistant, Goodbye!")
    sys.exit(0)
