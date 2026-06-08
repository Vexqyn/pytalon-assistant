# topics_basic.py
"""Teaching functions for basic Python topics (1-6)."""

from utils import print_global_separator, run_practice_session
from validators import get_global_valid_input, get_global_examples_valid_input

# ------ Topic 1: Hello World ------
def teach_hello_world():
    """Topic 1: Hello World"""
    print_global_separator()
    print("1. Hello World Example:")
    print('   print("Hello, World!")')

    def explain_hello_world():
        print_global_separator()
        print("🖨️ THE 'HELLO WORLD' PROGRAM")
        print("""
            🌍 WHAT IS HELLO WORLD?
            This is the TRADITIONAL first program everyone writes
            when learning a new programming language.
            
            ✨ WHY DO WE START WITH IT?
            • It's SIMPLE: Just one line of code
            • It's EXCITING: You see immediate results
            • It's FOUNDATIONAL: Teaches the most basic command
            
            🔧 BREAKDOWN:
            print() = Your CODE'S MOUTH that speaks to the screen
            "Hello, World!" = The WORDS you want to say
            Parentheses () = Holds what you want to print
            
            💡 THINK OF IT AS:
            Your computer is a QUIET ROBOT 🤖
            print() is the SPEAKER 🔊 you install
            "Hello, World!" is its FIRST WORDS 👶
            
            🎬 THE MAGIC MOMENT:
            When you run this, your silent computer 
            suddenly SPEAKS to you for the first time!
            """)
        
        # Example breakdown for Hello World
        see_example = get_global_examples_valid_input("\nWant to see the code breakdown? (yes/no): ")
        if see_example == 'yes':
            print("\n📝 CODE EXAMPLE:")
            print('   print("Hello, World!")')
            print("   ↑         ↑")
            print("   Command   Message")
        else:
            print("Skipping code breakdown...")
        print_global_separator()
        print("You can try it whenever you want! Just type: print('Your Name Here')")
        print_global_separator()

    explain_hello_world()

    # practice session for Hello World
    practice = get_global_valid_input("\n🔹 Want to practice with Hello World? (yes/no): ")
    if practice == 'yes':
        run_practice_session(
            topic_name="Hello World",
            instructions="Write a Python program that prints 'Hello, World!'",
            expected_keywords=['print', 'Hello'],
            example_code="print('Hello, World!')"
        )

    print("Awesome! You've learned how to print text in Python.")

# ------ Topic 2: Functions ------
def teach_functions():
    """Topic 2: Functions"""
    print_global_separator()
    print("2. Functions in Python:")

    def explain_functions():
        print("\n   📦 What are functions?")
        print("\n🤖 FUNCTIONS = YOUR CODING ASSISTANTS")
        print_global_separator()
        print("""
            🎯 WHAT ARE FUNCTIONS?
            Functions are like TRAINED ASSISTANTS in your code. They are:
            - BLOCKS OF CODE that do a SPECIFIC JOB
            - REUSABLE: Call them anytime you need to do a specific task
            - PARAMETERIZED: They can take INPUTS to work with
            - RETURN VALUES: They can GIVE BACK OUTPUTS after processing
            
            • ONE-TIME TRAINING: Teach them a skill once
            • LIFETIME SERVICE: Use that skill forever
            • TIME TRAVEL: Save hours of repeating work
            
            🍞 REAL-LIFE EXAMPLE: TOASTER
            1. You BUY a toaster (create function)
            2. You PUT in bread (give input)
            3. Toaster DOES its magic (process inside)
            4. You GET toast (receive output)
            
            🔧 IN PROGRAMMING:
            - CREATE function once with 'def'
            - GIVE it data to work with (parameters)
            - GET back results (return value)
            - USE it anytime, anywhere!
            """)
        print("\n💡 REMEMBER: If you do something MORE THAN ONCE,")
        print("             make it a FUNCTION!")

        # Example function definition and usage
        see_example = get_global_examples_valid_input("\nWant to see a function example? (yes/no): ")
        if see_example == 'yes':
            print("\n   🔧 Function Example:")
            print("   def greet(name):")
            print("       return f'Hello, {name}!'")
            print("   ")
            print("   # Using the function:")
            print("   print(greet('Alice'))")
            print("   # Output: Hello, Alice!")
        else:
            print("Skipping example...")

    explain_functions()

    # practice session for functions
    practice = get_global_valid_input("\n🔹 Want to practice with functions? (yes/no): ")
    if practice == 'yes':
        def check_function_practice(code, output):
            """Checks if the code has proper function structure"""
            if 'def ' not in code:
                return False, "You need to define a function using 'def' keyword!"
            if 'print' not in code:
                return False, "You should use print() to show the result!"
            if 'return' not in code:
                return False, "Remember to use 'return' to send back a value!"
            if 'greet' not in code:
                return False, "Make sure your function is named 'greet'!"
            
            # Check only the def line for empty parentheses
            def_line = None
            for line in code.split('\n'):
                if line.strip().startswith('def '):
                    def_line = line.strip()
                    break
            if def_line and '()' in def_line:
                return False, "Your function should have parameters in the parentheses!"
            
            return True, ""

        run_practice_session(
            topic_name="Functions",
            instructions="Create a function called 'greet' that takes a 'name' parameter and returns a greeting message. Then call it with your name!",
            expected_keywords=['def', 'greet', 'return'],
            example_code="def greet(name):\n    return f'Hello, {name}!'\n    \nprint(greet('YourName'))",
            custom_check_function=check_function_practice
        )

    print("Awesome! You've learned about functions and how to create and use them.")

# ------ Topic 3: Variables ------
def teach_variables():
    """Topic 3: Variables"""
    print_global_separator()
    print("3. Variables in Python:")

    def explain_variables():
        print("\n   🏷️ What are variables?")
        print("\n📦 VARIABLES: YOUR CODE'S STORAGE BOXES")
        print_global_separator()
        print("""
            🎯 WHAT ARE VARIABLES?
            Variables are like LABELED STORAGE BOXES 📦
            You put things in them, give them a NAME TAG,
            and find them later using the name!
            
            🏪 REAL-LIFE EXAMPLE: SUPERMARKET LOCKERS
            1. You put your bag in a locker (STORE value)
            2. You get a ticket with number 42 (VARIABLE name)
            3. Later, show ticket 42 (USE variable)
            4. Get your bag back (RETRIEVE value)
            
            🔑 KEY IDEA: 
            The LOCKER NUMBER is the VARIABLE NAME (age, name, score)
            The BAG INSIDE is the VARIABLE VALUE (18, "Ali", 95.5)
            
            📊 TYPES OF BOXES (DATA TYPES):
            • 📝 STRING BOX: For text → name = "Qasim"
            • 🔢 INTEGER BOX: For whole numbers → age = 18  
            • 📐 FLOAT BOX: For decimals → height = 5.9
            • ✅ BOOLEAN BOX: For True/False → is_student = True
            
            💡 WHY USE VARIABLES?
            1. REUSE DATA: Store once, use many times
            2. CLARITY: Descriptive names explain themselves
            3. FLEXIBILITY: Change value in one place
            4. ORGANIZATION: Keeps your code tidy
            """)
        
        # Example usage of variables
        see_examples = get_global_examples_valid_input("\nWant to see variable examples? (yes/no): ")
        if see_examples == 'yes':
            print("\n📝 REAL EXAMPLE:")
            print("   name = 'Muhammad Qasim'   ← STRING variable")
            print("   age = 18                   ← INTEGER variable")
            print("   score = 95.5               ← FLOAT variable")
            print("   passed = True              ← BOOLEAN variable")
        else:
            print("Skipping examples...")
        print_global_separator()
        print("ALWAYS REMEMBER VARIABLES SO, YOU DON'T HAVE TO!")
        print_global_separator()

    explain_variables()

    # Practice session for variables
    practice = get_global_valid_input("\n🔹 Want to practice with variables? (yes/no): ")
    if practice == 'yes':
        def check_variables_practice(code, output):
            """Checks if the code has proper variable structure"""
            if '=' not in code:
                return False, "You need to use the assignment operator '=' to create variables!"
            if 'name' not in code.lower():
                return False, "Create a variable called 'name'!"
            if 'age' not in code.lower():
                return False, "Create a variable called 'age'!"
            if 'print' not in code:
                return False, "Use print() to display your variables!"
            return True, ""

        run_practice_session(
            topic_name="Variables",
            instructions="Create three variables: 'name' (your name as string), 'age' (your age as number), and 'hobby' (your hobby as string). Then print all of them!",
            expected_keywords=['name', 'age', 'hobby', 'print'],
            example_code="name = 'John'\nage = 20\nhobby = 'Coding'\nprint(f'Name: {name}, Age: {age}, Hobby: {hobby}')",
            custom_check_function=check_variables_practice
        )

    print("Great job! You've learned about variables and their types.")

# ------ Topic 4: Relational Operators ------
def teach_relational_operators():
    """Topic 4: Relational Operators"""
    print_global_separator()
    print("4. Relational Operators in Python:")

    def explain_relational_operators():
        print("\n   🔍 What are relational operators?")
        print("\n🔍 RELATIONAL OPERATORS: CODE'S COMPARISON TOOLS")
        print_global_separator()
        print("""
            🎯 WHAT ARE THEY?
            These are CODE'S QUESTION WORKS that compare values
            and answer with TRUE 👍 or FALSE 👎
            
            👨🏫 THINK LIKE A TEACHER GRADING PAPERS:
            • Is score1 EQUAL TO score2? (==)
            • Is Ali's height GREATER THAN Sara's? (>)
            • Is age1 LESS THAN age2? (<)
            
            🔧 THE COMPARISON TOOLKIT:
            ==  EQUAL TO           → "Are these TWINS?" 👯
            !=  NOT EQUAL TO       → "Are they DIFFERENT?" 🚫
            >   GREATER THAN       → "Who is TALLER?" 📏
            <   LESS THAN          → "Who is YOUNGER?" 👶
            >=  GREATER OR EQUAL   → "Passing grade OR higher?" 🎓
            <=  LESS OR EQUAL      → "Child ticket age limit?" 🎫
            
            🎮 REAL-LIFE DECISIONS:
            • CAN YOU VOTE? → age >= 18
            • IS THE DOOR LOCKED? → door_status == "locked"
            • IS THE CUP FULL? → water_level >= cup_capacity
            
            💡 SECRET: Computers are DUMB at thinking
            but SMART at COMPARING! These operators 
            give computers DECISION-MAKING POWER!
            """)
        
        # Example usage of relational operators
        see_examples = get_global_examples_valid_input("\nWant to see practical examples? (yes/no): ")
        if see_examples == 'yes':
            print("\n📝 PRACTICAL EXAMPLES:")
            print("   age = 18")
            print("   can_vote = age >= 18      # True ✓")
            print("   is_minor = age < 18       # False ✗")
            print("   is_teenager = age >= 13 and age <= 19  # True ✓")
        else:
            print("Skipping examples...")
        print_global_separator()
        print("EVERY 'IF' DECISION USES THESE OPERATORS!")
        print_global_separator()

    explain_relational_operators()

    # practice session for relational operators
    practice = get_global_valid_input("\n🔹 Want to practice with relational operators? (yes/no): ")
    if practice == 'yes':
        def check_relational_practice(code, output):
            """Checks if at least 2 different comparison operators are used"""
            all_operators = ['==', '!=', '>', '<', '>=', '<=']
            found_operators = [op for op in all_operators if op in code]
            if len(found_operators) < 2:
                return False, f"Use at least 2 different relational operators! Found: {found_operators if found_operators else 'none'}"
            if 'print' not in code:
                return False, "Use print() to display the comparison results!"
            return True, ""

        run_practice_session(
            topic_name="Relational Operators",
            instructions="Create two number variables (a and b) and use at least 2 different relational operators (==, !=, >, <, >=, <=) to compare them. Print each comparison result!",
            expected_keywords=['=', 'print'],
            example_code="a = 10\nb = 5\nprint(f'a > b: {a > b}')\nprint(f'a == b: {a == b}')\nprint(f'a >= b: {a >= b}')",
            custom_check_function=check_relational_practice
        )

    print("Great! You've learned about relational operators and how to compare values.")

# ------ Topic 5: Assignment Operators ------
def teach_assignment_operators():
    """Topic 5: Assignment Operators"""
    print_global_separator()
    print("5. Assignment Operators in Python:")

    def explain_assignment_operators():
        print("\n   📝 What are assignment operators?")
        print("\n📝 ASSIGNMENT OPERATORS: CODE'S VALUE ASSIGNERS")
        print_global_separator()
        print("""
            🎯 WHAT ARE THEY?
            Assignment operators are used to ASSIGN VALUES
            to VARIABLES in your code.
            
            🔧 THE ASSIGNMENT TOOLKIT:
            =    SIMPLE ASSIGNMENT       → x = 5          # Assigns 5 to x
            +=   ADD AND ASSIGN          → x += 3         # x = x + 3
            -=   SUBTRACT AND ASSIGN     → x -= 2         # x = x - 2
            *=   MULTIPLY AND ASSIGN     → x *= 4         # x = x * 4
            /=   DIVIDE AND ASSIGN       → x /= 2         # x = x / 2
            %=   MODULUS AND ASSIGN      → x %= 3         # x = x % 3
            //=  FLOOR DIVIDE AND ASSIGN → x //= 2        # x = x // 2
            **=  EXPONENTIATE AND ASSIGN → x **= 3        # x = x ** 3
            
            💡 EXAMPLE USAGE:
            x = 10
            x += 5    # Now x = 15
            x *= 2    # Now x = 30
            print(x)  # Output: 30
            
            🔑 SIMPLE RULE:
            These are SHORTCUTS for updating variables!
            """)
        print_global_separator()
        print("Assignment operators make your code SHORTER!")
        print_global_separator()

    explain_assignment_operators()

    # Practice session for assignment operators
    practice = get_global_valid_input("\n🔹 Want to practice with assignment operators? (yes/no): ")
    if practice == 'yes':
        def check_assignment_practice(code, output):
            """Checks if at least 2 compound assignment operators are used"""
            compound_operators = ['+=', '-=', '*=', '/=', '%=', '//=', '**=']
            found_operators = [op for op in compound_operators if op in code]
            if len(found_operators) < 2:
                return False, f"Use at least 2 compound assignment operators! Found: {found_operators if found_operators else 'none'}"
            if 'print' not in code:
                return False, "Use print() to show the results!"
            return True, ""

        run_practice_session(
            topic_name="Assignment Operators",
            instructions="Create a variable x with an initial value. Then use at least 2 compound assignment operators (+=, -=, *=, /=, etc.) and print x after each operation!",
            expected_keywords=['x', '=', 'print'],
            example_code="x = 10\nprint(f'Initial x: {x}')\nx += 5\nprint(f'After x += 5: {x}')\nx *= 2\nprint(f'After x *= 2: {x}')",
            custom_check_function=check_assignment_practice
        )

    print("Great! You learned about assignment operators!")

# ------ Topic 6: Logical Operators ------
def teach_logical_operators():
    """Topic 6: Logical Operators"""
    print_global_separator()
    print("6. Logical Operators in Python:")

    def explain_logical_operators():
        print("\n   🤔 What are logical operators?")
        print("\n🤔 LOGICAL OPERATORS: CODE'S THINKING TOOLS")
        print_global_separator()
        print("""
            🎯 WHAT ARE THEY?
            Logical operators help your code MAKE DECISIONS
            by combining multiple conditions.
            
            🔧 THE LOGICAL TOOLKIT:
            and  LOGICAL AND       → True if BOTH conditions are True
            or   LOGICAL OR        → True if AT LEAST ONE condition is True
            not  LOGICAL NOT       → Inverts the truth value
            
            💡 EXAMPLE USAGE:
            age = 20
            has_id = True
            
            # Check if eligible to enter club
            can_enter = (age >= 18) and has_id   # True ✓
            
            # Check if eligible for discount
            is_student = False
            eligible_discount = (age < 18) or is_student  # False ✗
            
            # Invert a condition
            is_not_adult = not (age >= 18)  # False ✗
            
            🔑 SIMPLE RULE:
            Use logical operators to COMBINE CONDITIONS!
            """)
        print_global_separator()
        print("Logical operators help your code THINK SMARTER!")
        print_global_separator()

    explain_logical_operators()

    # Practice session for logical operators
    practice = get_global_valid_input("\n🔹 Want to practice with logical operators? (yes/no): ")
    if practice == 'yes':
        def check_logical_practice(code, output):
            """Checks if at least one logical operator is used"""
            logical_operators = ['and', 'or', 'not']
            found_operators = [op for op in logical_operators if op in code]
            if len(found_operators) < 1:
                return False, "Use at least one logical operator (and/or/not)!"
            if 'print' not in code:
                return False, "Use print() to show the results!"
            if '=' not in code:
                return False, "Create variables with values!"
            return True, ""

        run_practice_session(
            topic_name="Logical Operators",
            instructions="Create two boolean variables (e.g., is_raining, has_umbrella). Use logical operators (and/or/not) to make decisions and print the results!",
            expected_keywords=['=', 'print'],
            example_code="is_raining = True\nhas_umbrella = False\nprint(f'Should I go out? {not is_raining or has_umbrella}')",
            custom_check_function=check_logical_practice
        )

    print("Great! You learned about logical operators!")


# Map topic names to functions
BASIC_TOPICS = {
    'Hello World': teach_hello_world,
    'Functions': teach_functions,
    'Variables': teach_variables,
    'Relational operators': teach_relational_operators,
    'Assignment operators': teach_assignment_operators,
    'Logical operators': teach_logical_operators,
}