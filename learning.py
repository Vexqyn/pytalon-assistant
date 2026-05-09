# HEADER COMMENT

"""
Pytalon — Your Python Tutor Companion (formely known as Python Teaching Assistant)
Created by: M Qasim Farooqi
Role: BS IT Student | Python Developer · AI Prompt Strategist · Digital Creator & Game Systems Analyst | I build, analyze & create
Version: 1.0.3
Category: Preview
Purpose: Learn Python basics through interactive teaching with 12 comprehensive topics

"""

# ========== SECTION 1: INTRO & SETUP ==========

# Assistant introducing himself:
name = "Pytalon"
version = "1.0.3"
category = "Preview"
Description = "A Tutor Companion Assistant developed to guide you with Python programming and learning."

def introduce():
    return f"Hello! I am {name}, version {version}, category, {category}. \n{Description}"

print(introduce())

# ========== SMART INPUT VALIDATION FUNCTIONS ==========

# ----- RESPONSE CATEGORIES (Constants for better readability) -----
YES_RESPONSES = ['yes', 'y', 'teach me this topic', 'i want to learn this topic',
                 'wanted to learn more', 'of course! Lets learn this new topic', 'yeah! Teach me man', 'fr! Let\'s do it!',
                 'ngl! I am excited to learn this topic', 'tbh! I want to learn this topic', 'lock in bro! I want to learn']

NO_RESPONSES = ['no', 'n', 'move on to next topic', 'skip', 'skip the topic', 'I dont have plans to learn this topic',
                'nah! I am not going to continue further', 'I am fine, dont want to learn today', 'I dont want to learn anything',
                'nuh uh! I am good for now', 'I\'ll pass', 'no way! I dont want to learn', 'Not on my watch today! no learning today']

EXIT_RESPONSES = ['exit', 'e', 'exit the session', 'i want to exit', 'nah! I dont want to study', 'nuh uh! No more, I am quiting', 
                  'I am taking a relaxing break', 'dipping out for now', 'clear out for today! No learning',
                  'I\'m gonna bounce, so bye for now', 'sorry! But I do not want to learn anything', 'I am out right now, maybe later']

YES_EXAMPLES_RESPONSES = ['yes', 'y', 'show me examples', 'i want to see examples', 'give me some examples','of course! I want to see the example',
                          'yeah! Show me more examples', 'OK! I want to see more examples', 'yup! show me some examples!',
                          'fr! I want to see examples', 'ngl! I am excited to see examples', 'tbh! I want to see examples']

NO_EXAMPLES_RESPONSES = ['no', 'n', 'skip examples', 'no examples', 'skip showing examples', 'skip this particular example',
                         'nah! I dont want to see examples', 'nuh uh! I am fine without examples', 'I am good, dont show me examples',
                         'bruh! I dont want to see examples', 'I am straight, nuh uh! I am good without examples', 'I am good, nah!']

YES_QUESTION_RESPONSES = [
    'yes', 'y', 
    'i have a question', 'ask a question', 'i want to ask a question',
    'can you teach', 'can you help me', 'i need help', 
    'i wanted to ask you something', 'yeah! can you help me', 
    'yeah! I have a question'
]

NO_QUESTION_RESPONSES = [
    'no', 'n',
    'no questions', 'i do not have a question', 'skip questions',
    'no! I do not have a question', 'nah! I do not want to ask a question',
    'nuh ! I do not have any questions', 'nuh uh! I do not want to ask anything'
]

EXIT_QUESTION_RESPONSES = [
    'exit', 'e', 'exit the session', 'i want to exit', 'i want to leave',
    'Nuh uh! I want to exit', 'nah! I want to exit', 'no! I want to exit',
    'i want to leave now', 'Nah! I am fine',
    'sorry! But I do not want to learn anything', 'i am good for now'
]

SIMPLE_RESPONSES = ['yes', 'y', 'no', 'n', 'ok', 'okay', 'exit', 'e']

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

# ----- Global Input Validation Functions -----

def get_global_valid_input(prompt):
    """Get and validate user input for yes/no/exit"""
    valid_options = YES_RESPONSES + NO_RESPONSES + EXIT_RESPONSES
    
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no/exit)")
            continue
        
        # ----- EXACT MATCHES FIRST -----
        if user_input in valid_options:
            if user_input in YES_RESPONSES:
                return 'yes'
            elif user_input in NO_RESPONSES:
                return 'no'
            elif user_input in EXIT_RESPONSES:
                return 'exit'
            else:
                return user_input
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif user_input.startswith('e'):
            return 'exit'
        elif user_input.startswith('s'):
            return 'no'  # skip
        elif 'teach' in user_input or 'learn' in user_input:
            return 'yes'
        
        print("⚠️  Please enter a valid response (yes/no/exit)")

# ----- Global Question-Specific Input Validation Function -----        

def get_global_user_question_valid_input(prompt):
    """Get and validate user input for questions"""
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no/exit)")
            continue
        
        # ----- EXACT MATCHES -----
        if user_input in YES_QUESTION_RESPONSES:
            return 'yes'
        elif user_input in NO_QUESTION_RESPONSES:
            return 'no'
        elif user_input in EXIT_QUESTION_RESPONSES:
            return 'exit'
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif user_input.startswith('e'):
            return 'exit'
        elif 'question' in user_input or 'ask' in user_input:
            return 'yes'
        elif 'skip' in user_input or 'nah' in user_input or 'nuh' in user_input:
            return 'no'
        elif 'leave' in user_input or 'exit' in user_input:
            return 'exit'
        
        print("⚠️  Please enter a valid response (yes/no/exit)")

#  ----- Global Menu Choice Functions -----

def get_global_menu_choice(prompt, min_val=1, max_val=12):
    """Get and validate user input for menu choice"""
    while True:
        choice = input(prompt).strip().lower()
        
        # ----- EXIT CHECK -----
        if choice == 'exit':
            return 'exit'
        
        # ----- EMPTY INPUT CHECK -----
        if not choice:
            print(f"⚠️  Please enter a number between {min_val} and {max_val}, or 'exit'")
            continue

        # ----- VALID NUMBER CHECK -----
        if choice.isdigit() and min_val <= int(choice) <= max_val:
            return choice

        print(f"⚠️  Please enter a number between {min_val} and {max_val}, or 'exit'")

# ----- Global Examples-Specific Input Validation Function -----        

def get_global_examples_valid_input(prompt):
    """Get and validate user input for examples"""
    while True:
        user_input = input(prompt).strip().lower()
        
        # ----- EMPTY INPUT CHECK -----
        if not user_input:
            print("⚠️  Please enter a valid response (yes/no)")
            continue
        
        # ----- EXACT MATCHES -----
        if user_input in YES_EXAMPLES_RESPONSES:
            return 'yes'
        elif user_input in NO_EXAMPLES_RESPONSES:
            return 'no'
        
        # ----- PARTIAL MATCHES -----
        if user_input.startswith('y'):
            return 'yes'
        elif user_input.startswith('n'):
            return 'no'
        elif 'example' in user_input or 'show' in user_input:
            return 'yes'
        elif 'skip' in user_input:
            return 'no'
        
        print("⚠️  Please enter a valid response (yes/no)")

# ----- Global Question Content Validation Function -----       

def get_global_question_content_input(prompt):
    """Get and validate the actual question content (not yes/no/exit)"""
    
    # ----- HELPER FUNCTIONS -----
    def is_simple_response(text):
        """Check if input is just yes/no/exit"""
        return text in SIMPLE_RESPONSES
    
    def is_full_question(text):
        """Check if input is a complete question (has enough words)"""
        words = text.split()
        
        # Any question with at least 4 words is likely complete
        return len(words) >= 4
    
    def print_helpful_feedback():
        """Print helpful examples"""
        print("\n❌ Please ask a complete question (at least 4 words).")
        print("\n📝 Examples:")
        print("   • 'Can you teach me Python?'")
        print("   • 'How do I learn variables?'")
        print("   • 'What is a function?'")
        print("   • 'Can you explain loops?'")
        print()
    
    # ----- MAIN VALIDATION LOOP -----
    while True:
        question = input(prompt).strip()
        
        # ----- EMPTY INPUT CHECK -----
        if not question:
            print("⚠️  Please enter a valid question.")
            continue
        
        question_lower = question.lower()
        
        # ----- SIMPLE RESPONSE CHECK -----
        if is_simple_response(question_lower):
            print("⚠️  Please ask an actual Python question, not just 'yes' or 'no'.")
            continue
        
        # ----- CHECK IF IT'S A FULL QUESTION -----
        if is_full_question(question):
            return question
        
        # ----- HELPFUL FEEDBACK -----
        print_helpful_feedback()

# ========== SECTION 2: HELPER FUNCTIONS FOR INPUT VALIDATION & CODE READABILITY ==========

# Global Seperator Function
def print_global_separator():
    global_separator = "\n" + "="*50
    print(global_separator)


# ========== SECTION 3: MAIN PROGRAM & USER QUESTIONS ==========

# Start of the conservation
print("\nHow can I assist you with Python programming today?")

# Ask if user has a specific question
user_question = get_global_user_question_valid_input("\n🔹 Do you have any specific questions about Python? (yes/no/exit): ")

# Handle user's question if they have one
user_python_question = ""
if user_question == 'yes':
    print("\n🔹 Please ask your Python question:")
    user_python_question = get_global_question_content_input("💬 Your Question: ") 
    print(f"\n🤖 Thank you for your question: '{user_python_question}'")
    
    user_input = get_global_valid_input("\n🔹 Would you like to learn Python topics? (yes/no/exit): ")
    
    # If user chooses 'exit' after asking question, end the session
    if user_input == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()         
    # If user chooses 'no' after asking question, proceed to topics menu
    elif user_input == 'no':
        print("\n🔹 Okay, we will do it later")
        exit()    

elif user_question == 'no':
    print("\n🔹 No problem! We can proceed to Python topics anytime you want.")
    user_input = get_global_valid_input("\n🔹 Would you like to learn Python topics after break now? (yes/no/exit): ")
    
    if user_input == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()
    elif user_input == 'no':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        exit()
    # If user says 'yes', continue to topics menu
    
elif user_question == 'exit':
    print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
    exit()

# ========= MAIN TOPICS LOOP ==========
while True:
    # ========= TOPICS MENU ==========        
    print_global_separator()
    Assistant_Response = "I can teach you Python basics! Here are the available topics:\n" \
                         "📚 Topics Menu:\n" \
                         "1. Hello World\n" \
                         "2. Functions\n" \
                         "3. Variables\n" \
                         "4. Relational operators\n" \
                         "5. Assignment operators\n" \
                         "6. Logical operators\n" \
                         "7. Type conversion\n" \
                         "8. Input function\n" \
                         "9. Comments in Python\n" \
                         "10. Strings in Python\n" \
                         "11. Data types in Python\n" \
                         "12. Conditional statements\n"

    print(Assistant_Response)
    print_global_separator()

    # Get topic choice
    Assistant_Ask = "\n🔹 Which topic would you like to start with? (1-12/exit): "
    topic_choice = get_global_menu_choice(Assistant_Ask, 1, 12)

    if topic_choice == 'exit':
        print("\n👋 Ok, goodbye! No class today, come back whenever you need me")
        break

    # Map topic numbers to names
    topics = {
        '1': 'Hello World',
        '2': 'Functions',
        '3': 'Variables',
        '4': 'Relational operators',
        '5': 'Assignment operators',
        '6': 'Logical operators',
        '7': 'Type conversion',
        '8': 'Input function',
        '9': 'Comments in Python',
        '10': 'Strings in Python',
        '11': 'Data types in Python',
        '12': 'Conditional statements'
    }

    selected_topic = topics[topic_choice]
    print(f"\n🎯 Excellent choice! You selected: {selected_topic}")

    # Ask if they want to learn this topic
    learn_topic = get_global_valid_input(f"\n🔹 Would you like me to teach you about {selected_topic}? (yes/no/exit): ")

    if learn_topic == 'exit':
        print("\n👋 Goodbye! Come back whenever you need me")
        break
    elif learn_topic == 'no':
        print(f"\n🔹 Okay, skipping {selected_topic}.")
        print("\n🔹 You can select another topic from the menu.")
        continue
    
    print(f"\n📖 Teaching {selected_topic}...")

    # ========== SECTION 4: TOPICS 1-6 ==========
    
    # TEACH THE SELECTED TOPIC BASED ON USER'S CHOICE
    if selected_topic == 'Hello World':
        # ========== TOPIC 1: HELLO WORLD ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with Hello World? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE HELLO WORLD PRACTICE")
            print_global_separator()
            
            user_name = input("Enter your name to greet: ").strip()
            
            if user_name:
                print(f"\n📊 YOUR CUSTOM GREETING:")
                print(f"   print(\"Hello, {user_name}!\")")
                print(f"   Output: Hello, {user_name}!")
                print(f"\n   You can also try:")
                print(f"   print('Welcome to Python, {user_name}!')")
                print(f"   print(f'Hi {{user_name}}, let\\'s learn Python!')")
                print("\n✅ Practice complete! You've created your first custom print statement!")
            else:
                print("⚠️  No name entered for practice.")
        
        Assistant_Response = "Awesome! You've learned how to print text in Python."
        print(Assistant_Response)
    
    elif selected_topic == 'Functions':
        # ========== TOPIC 2: FUNCTIONS ==========
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
            
            print("\n" + "💡 REMEMBER: If you do something MORE THAN ONCE,")
            print("             make it a FUNCTION!")
            
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with functions? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE FUNCTIONS PRACTICE")
            print_global_separator()
            
            user_input = input("Enter a skill you want to learn (e.g., Python, Coding): ").strip()
            
            if user_input:
                print(f"\n📊 FUNCTION ANALYSIS FOR: {user_input}")
                print(f"   # Function definition")
                print(f"   def learn_{user_input.lower()}():")
                print(f"       print('Learning {user_input} is fun!')")
                print(f"       return 'I mastered {user_input}!'")
                print(f"\n   # Using the function")
                print(f"   learn_{user_input.lower()}()")
                print(f"   result = learn_{user_input.lower()}()")
                print(f"   print(result)")
                print("\n✅ Practice complete! You've created a custom function!")
            else:
                print("⚠️  No skill entered for practice.")
        
        Assistant_Response = "Awesome! You've learned about functions and how to create and use them."
        print(Assistant_Response)
    
    elif selected_topic == 'Variables':
        # ========== TOPIC 3: VARIABLES ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with variables? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE VARIABLES PRACTICE")
            print_global_separator()
            
            print("Let's create variables with your information!")
            user_name = input("Enter your name: ").strip()
            user_age = input("Enter your age: ").strip()
            user_hobby = input("Enter your hobby: ").strip()
            
            if user_name and user_age and user_hobby:
                print(f"\n📊 VARIABLE ANALYSIS FOR: {user_name}")
                print(f"   name = '{user_name}'           # String variable")
                print(f"   age = {user_age}                # Integer variable")
                print(f"   hobby = '{user_hobby}'         # String variable")
                print(f"   is_student = True               # Boolean variable")
                print(f"\n   # Using your variables:")
                print(f"   print(f'My name is {{name}}')")
                print(f"   print(f'I am {{age}} years old')")
                print(f"   print(f'I love {{hobby}}')")
                print(f"\n   # Type checking:")
                print(f"   print(type(name))   # <class 'str'>")
                print(f"   print(type(age))    # <class 'str'> (input always returns string)")
                print(f"   # To use age as number: age = int('{user_age}')")
                print("\n✅ Practice complete! You've created and used variables!")
            else:
                print("⚠️  Missing information for practice.")
        
        Assistant_Response = "Great job! You've learned about variables and their types."
        print(Assistant_Response)
    
    elif selected_topic == 'Relational operators':
        # ========== TOPIC 4: RELATIONAL OPERATORS ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with relational operators? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE RELATIONAL OPERATORS PRACTICE")
            print_global_separator()
            
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            
            if num1 and num2:
                try:
                    a = float(num1)
                    b = float(num2)
                    
                    print(f"\n📊 COMPARING {a} AND {b}:")
                    print(f"   {a} == {b}  → {a == b}   (Equal to)")
                    print(f"   {a} != {b}  → {a != b}   (Not equal to)")
                    print(f"   {a} >  {b}  → {a > b}    (Greater than)")
                    print(f"   {a} <  {b}  → {a < b}    (Less than)")
                    print(f"   {a} >= {b}  → {a >= b}   (Greater than or equal)")
                    print(f"   {a} <= {b}  → {a <= b}   (Less than or equal)")
                    
                    if a > b:
                        print(f"\n   💡 {a} is GREATER than {b}")
                    elif a < b:
                        print(f"\n   💡 {a} is LESS than {b}")
                    else:
                        print(f"\n   💡 {a} is EQUAL to {b}")
                    
                    print("\n✅ Practice complete! You've used relational operators!")
                except ValueError:
                    print("⚠️  Please enter valid numbers next time!")
            else:
                print("⚠️  No numbers entered for practice.")
        
        Assistant_Response = "Great! You've learned about relational operators and how to compare values."
        print(Assistant_Response)
    
    elif selected_topic == 'Assignment operators':
        # ========= TOPIC 5: Assignment Operators ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with assignment operators? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE ASSIGNMENT OPERATORS PRACTICE")
            print_global_separator()
            
            start_value = input("Enter a starting number: ").strip()
            
            if start_value:
                try:
                    x = float(start_value)
                    
                    print(f"\n📊 STARTING WITH x = {x}")
                    print(f"\n   Operation    |  Code        |  Result")
                    print(f"   {x} + 5        |  x += 5      |  {x + 5}")
                    print(f"   {x} - 3        |  x -= 3      |  {x - 3}")
                    print(f"   {x} * 2        |  x *= 2      |  {x * 2}")
                    print(f"   {x} / 4        |  x /= 4      |  {x / 4}")
                    print(f"   {x} ** 2       |  x **= 2     |  {x ** 2}")
                    
                    print(f"\n   # Example with multiple operations:")
                    print(f"   x = {x}")
                    print(f"   x += 5   # x = {x} + 5 = {x + 5}")
                    print(f"   x *= 2   # x = {x + 5} * 2 = {(x + 5) * 2}")
                    
                    print("\n✅ Practice complete! You've used assignment operators!")
                except ValueError:
                    print("⚠️  Please enter a valid number next time!")
            else:
                print("⚠️  No number entered for practice.")
        
        Assistant_Response = "Great! You learned about assignment operators!"
        print(Assistant_Response)
    
    elif selected_topic == 'Logical operators':
        # ========= TOPIC 6: LOGICAL OPERATORS ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with logical operators? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE LOGICAL OPERATORS PRACTICE")
            print_global_separator()
            
            print("Answer these questions with True/False:")
            has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()
            has_car = input("Do you own a car? (yes/no): ").strip().lower()
            age = input("Enter your age: ").strip()
            
            if has_license and has_car and age:
                license_bool = has_license in ['yes', 'y', 'true']
                car_bool = has_car in ['yes', 'y', 'true']
                
                try:
                    user_age = int(age)
                    
                    print(f"\n📊 LOGICAL ANALYSIS:")
                    print(f"   has_license = {license_bool}")
                    print(f"   has_car = {car_bool}")
                    print(f"   age = {user_age}")
                    print(f"   age >= 18 = {user_age >= 18}")
                    
                    print(f"\n   🔧 LOGICAL OPERATOR RESULTS:")
                    print(f"   has_license and has_car = {license_bool and car_bool}  (Both true?)")
                    print(f"   has_license or has_car = {license_bool or car_bool}   (At least one true?)")
                    print(f"   not has_license = {not license_bool}           (Opposite of license)")
                    
                    can_drive = (user_age >= 18) and license_bool
                    print(f"\n   Can drive? (age >= 18 and has_license) = {can_drive}")
                    
                    can_borrow = (user_age >= 18) and car_bool
                    print(f"   Can borrow car? (age >= 18 and has_car) = {can_borrow}")
                    
                    print("\n✅ Practice complete! You've used logical operators!")
                except ValueError:
                    print("⚠️  Please enter a valid age number next time!")
            else:
                print("⚠️  Missing information for practice.")
        
        Assistant_Response = "Great! You learned about logical operators!"
        print(Assistant_Response)

        # ========== SECTION 5: TOPICS 7-12 ==========
    
    elif selected_topic == 'Type conversion':
        # ==== TOPIC 7: TYPE CONVERSION ===========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with type conversion? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE TYPE CONVERSION PRACTICE")
            print_global_separator()
            
            user_input = input("Enter a number (can be integer or decimal): ").strip()
            
            if user_input:
                print(f"\n📊 TYPE CONVERSION ANALYSIS FOR: '{user_input}'")
                print(f"   Original type: {type(user_input).__name__}")
                
                try:
                    # Convert to different types
                    to_int = int(float(user_input))
                    to_float = float(user_input)
                    to_str = str(user_input)
                    to_bool = bool(user_input)
                    
                    print(f"\n   🔧 CONVERSION RESULTS:")
                    print(f"   int()   → {to_int}     (Type: {type(to_int).__name__})")
                    print(f"   float() → {to_float}   (Type: {type(to_float).__name__})")
                    print(f"   str()   → '{to_str}'   (Type: {type(to_str).__name__})")
                    print(f"   bool()  → {to_bool}    (Type: {type(to_bool).__name__})")
                    
                    print(f"\n   💡 PRACTICAL EXAMPLES:")
                    print(f"   '{user_input}' + '5' = '{user_input}5' (String concatenation)")
                    print(f"   {to_float} + 5 = {to_float + 5} (Numeric addition)")
                    
                    if '.' in user_input:
                        print(f"\n   ⚠️  Note: int('{user_input}') would cause an error!")
                        print(f"   Always use float() first: int(float('{user_input}')) = {to_int}")
                    
                    print("\n✅ Practice complete! You've converted data types!")
                except ValueError:
                    print("⚠️  Cannot convert to number! Please enter a valid number next time!")
            else:
                print("⚠️  No input entered for practice.")
        
        Assistant_Response = "Great! You learned about type conversion!"
        print(Assistant_Response)
    
    elif selected_topic == 'Input function':
        # ========= TOPIC 8: INPUT FUNCTION ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with input function? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE INPUT FUNCTION PRACTICE")
            print_global_separator()
            
            print("Let's create an interactive program!")
            fav_color = input("What's your favorite color? ").strip()
            fav_number = input("What's your favorite number? ").strip()
            
            if fav_color and fav_number:
                print(f"\n📊 YOUR INTERACTIVE PROGRAM:")
                print(f"   # Get user input")
                print(f"   color = input('What\\'s your favorite color? ')")
                print(f"   number = input('What\\'s your favorite number? ')\n")
                
                print(f"   # Your inputs:")
                print(f"   color = '{fav_color}'")
                print(f"   number = '{fav_number}'\n")
                
                print(f"   # Using the inputs:")
                print(f"   print(f'Your favorite color is {{color}}')")
                print(f"   print(f'Your favorite number is {{number}}')\n")
                
                try:
                    num_int = int(fav_number)
                    print(f"   # Converting to number for calculations:")
                    print(f"   number_int = int('{fav_number}')  # {num_int}")
                    print(f"   doubled = number_int * 2          # {num_int * 2}")
                except ValueError:
                    print(f"   # To use '{fav_number}' as number: int('{fav_number}') would need a valid integer")
                
                print("\n✅ Practice complete! You've used the input function!")
            else:
                print("⚠️  Missing information for practice.")
        
        Assistant_Response = "Great! You learned about the input function!"
        print(Assistant_Response)
    
    elif selected_topic == 'Comments in Python':
        # ======== TOPIC 9: COMMENTS IN PYTHON ==========
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with comments? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE COMMENTS PRACTICE")
            print_global_separator()
            
            user_explanation = input("Explain what you learned about comments in your own words: ").strip()
            
            if user_explanation:
                print(f"\n📊 YOUR CODE WITH COMMENTS:")
                print(f"\n   # {user_explanation}")
                print(f"   # This is a single-line comment explaining the code")
                print(f"   \n   '''")
                print(f"   This is a multi-line comment")
                print(f"   It can span multiple lines")
                print(f"   Useful for longer explanations")
                print(f"   '''")
                print(f"   \n   print('Comments make code readable!')  # Inline comment")
                
                print(f"\n   💡 COMMENT TYPES YOU USED:")
                print(f"   • Single-line comment: # {user_explanation[:50]}...")
                print(f"   • Multi-line comment: ''' ... '''")
                print(f"   • Inline comment: after code on same line")
                
                print(f"\n   🔑 WHY COMMENTS ARE IMPORTANT:")
                print(f"   • Explain complex logic")
                print(f"   • Help other developers understand your code")
                print(f"   • Remind yourself what the code does")
                print(f"   • Temporarily disable code for debugging")
                
                print("\n✅ Practice complete! You've learned to write comments!")
            else:
                print("⚠️  No explanation entered for practice.")
        
        Assistant_Response = "Great! You learned about comments!"
        print(Assistant_Response)
    
    elif selected_topic == 'Strings in Python':
        # ======== TOPIC 10: STRINGS IN PYTHON ==========
        print_global_separator()
        print("10. Strings in Python:")

        # Define all helper functions FIRST before they are called
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "Python Programming"
                print(f"\n   text = \"{text}\"")
                print(f"   Length: {len(text)} characters")
                print(f"   Type: {type(text)}")
                print(f"   Uppercase: {text.upper()}")
                print(f"   Lowercase: {text.lower()}")

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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "PythonProgramming"
                print(f"\n   text = \"{text}\"")
                print(f"   text[0] = '{text[0]}'           # First character")
                print(f"   text[-1] = '{text[-1]}'         # Last character")
                print(f"   text[0:6] = \"{text[0:6]}\"     # Characters 0 to 5")
                print(f"   text[6:] = \"{text[6:]}\"       # From index 6 to end")
                print(f"   text[::-1] = \"{text[::-1]}\"   # Reversed string")

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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                str1 = "Hello"
                str2 = "World"
                print(f"\n   str1 = \"{str1}\"")
                print(f"   str2 = \"{str2}\"")
                print(f"   Concatenation: str1 + ' ' + str2 = \"{str1 + ' ' + str2}\"")
                print(f"   Replication: 'ha' * 3 = \"{'ha' * 3}\"")
                print(f"   Membership: 'Python' in 'Python Programming' = {'Python' in 'Python Programming'}")

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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                text = "   Python Programming   "
                print(f"\n   text = \"{text}\"")
                print(f"   strip(): \"{text.strip()}\"")
                print(f"   upper(): \"{text.upper()}\"")
                print(f"   lower(): \"{text.lower()}\"")
                print(f"   replace('Python', 'Java'): \"{text.replace('Python', 'Java')}\"")
                print(f"   split(): {text.strip().split()}")

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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples? (yes/no): ")
            if examples_choice == 'yes':
                name = "Alice"
                age = 25
                price = 49.9999
                print(f"\n   name = \"{name}\", age = {age}, price = {price}")
                print(f"   f-string: f'Name: {name}, Age: {age}' = \"{f'Name: {name}, Age: {age}'}\"")
                print("   format(): 'Name: {}, Age: {}' = \"" + 'Name: {}, Age: {}'.format(name, age) + "\"")
                print(f"   Number formatting: f'Price: ${price:.2f}' = \"{f'Price: ${price:.2f}'}\"")

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

        def teach_all_string_topics():
            """Teach all string topics in sequence"""
            teach_string_basics()
            teach_string_indexing()
            teach_string_operations()
            teach_string_methods()
            teach_string_formatting()
            teach_string_errors()

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
            
            # Track which topics have been learned
            topics_learned = []
            
            while True:
                # Display menu
                print("\n📚 STRINGS TOPIC MENU:")
                print("   1. String Basics & Creation")
                print("   2. Indexing & Slicing")
                print("   3. String Operations")
                print("   4. String Methods")
                print("   5. String Formatting")
                print("   6. Common Errors & Best Practices")
                print("   7. All topics (Complete guide)")
                print("   8. I'm done with strings (exit strings)")
                
                topic_choice = get_global_menu_choice("\n🔹 Which string topic would you like to learn? (1-8/exit): ", 1, 8)
                
                # Handle exit
                if topic_choice == 'exit':
                    print("\n👋 Session ended. Goodbye!")
                    exit()
                
                # Handle return to main menu
                if topic_choice == '8':
                    print("\n✅ Exiting strings section...")
                    break
                
                # Check if topic was already learned (skip for "All topics")
                if topic_choice in topics_learned and topic_choice != '7':
                    review = get_global_valid_input(f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): ")
                    if review == 'no':
                        continue
                
                # Handle "All topics" selection
                if topic_choice == '7':
                    teach_all_string_topics()
                    topics_learned = ['1', '2', '3', '4', '5', '6']
                    print_global_separator()
                    print("🎉 COMPLETE STRINGS GUIDE FINISHED!")
                    print_global_separator()
                    break
                
                # Teach individual topic based on choice
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
                continue_learning = get_global_valid_input("\n🔹 Want to learn another string topic? (yes/no): ")
                if continue_learning == 'no':
                    print("\n✅ Exiting strings section...")
                    break

        # Now call explain_strings()
        explain_strings()

        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with a string example? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE STRING PRACTICE")
            print_global_separator()
            
            user_text = input("Enter a text to practice with: ").strip()
            
            if user_text:
                print(f"\n📊 ANALYSIS OF YOUR TEXT: \"{user_text}\"")
                print(f"   Length: {len(user_text)} characters")
                print(f"   First character: '{user_text[0]}'")
                print(f"   Last character: '{user_text[-1]}'")
                print(f"   Uppercase: {user_text.upper()}")
                print(f"   Lowercase: {user_text.lower()}")
                print(f"   Title case: {user_text.title()}")
                
                if len(user_text) >= 3:
                    print(f"   First 3 characters: '{user_text[:3]}'")
                    print(f"   Last 3 characters: '{user_text[-3:]}'")
                    print(f"   Middle section: '{user_text[1:-1]}'")
                
                vowels = "aeiouAEIOU"
                vowel_count = sum(1 for char in user_text if char in vowels)
                print(f"   Vowel count: {vowel_count}")
                
                print("\n✅ Practice complete! You've applied string operations!")
            else:
                print("⚠️  No text entered for practice.")
        
        Assistant_Response = "Excellent! You've learned comprehensive string handling in Python!"
        print(Assistant_Response)

    elif selected_topic == 'Data types in Python':
        # ========== TOPIC 11: DATA TYPES IN PYTHON ==========
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples of data types? (yes/no): ")
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
        
        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with data types? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE DATA TYPES PRACTICE")
            print_global_separator()
            
            user_input = input("Enter a value to analyze its data type: ").strip()
            
            if user_input:
                print(f"\n📊 DATA TYPE ANALYSIS FOR: '{user_input}'")
                print(f"   Original value: {user_input}")
                print(f"   Data type: {type(user_input).__name__}")
                
                # Try to detect if it can be converted
                print(f"\n   🔧 TYPE DETECTION:")
                if user_input.isdigit():
                    print(f"   ✓ Can be converted to int: {int(user_input)}")
                    print(f"   ✓ Can be converted to float: {float(user_input)}")
                elif user_input.replace('.', '', 1).isdigit() and user_input.count('.') <= 1:
                    try:
                        float_val = float(user_input)
                        print(f"   ✓ Can be converted to float: {float_val}")
                        print(f"   ✓ Can be converted to int: {int(float_val)}")
                    except:
                        print(f"   ✗ Cannot convert to number")
                elif user_input.lower() in ['true', 'false']:
                    print(f"   ✓ Can be converted to bool: {user_input.lower() == 'true'}")
                else:
                    print(f"   → String value (text)")
                    print(f"   → Length: {len(user_input)} characters")
                
                print(f"\n   💡 PRACTICAL EXAMPLES:")
                print(f"   type('{user_input}') → {type(user_input).__name__}")
                
                print("\n✅ Practice complete! You've learned about data types!")
            else:
                print("⚠️  No input entered for practice.")
        
        Assistant_Response = "Great! You've learned about different data types in Python!"
        print(Assistant_Response)

    elif selected_topic == 'Conditional statements':
        # ========== TOPIC 12: CONDITIONAL STATEMENTS ==========
        print_global_separator()
        print("12. Conditional Statements in Python:")
 
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
 
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see more if examples? (yes/no): ")
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see if-else examples? (yes/no): ")
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see elif examples? (yes/no): ")
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see nested conditionals examples? (yes/no): ")
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see combined conditions examples? (yes/no): ")
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
            
            examples_choice = get_global_examples_valid_input("\n🔹 Want to see examples of best practices? (yes/no): ")
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
 
        def teach_all_conditional_topics():
            """Teach all conditional topics in sequence"""
            teach_conditionals_basics()
            teach_if_else()
            teach_elif()
            teach_nested_conditionals()
            teach_conditional_operators()
            teach_common_mistakes()
 
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
            
            # Track which topics have been learned
            topics_learned = []
            
            while True:
                # Display menu
                print("\n📚 CONDITIONAL STATEMENTS TOPIC MENU:")
                print("   1. IF Statements - The Basics")
                print("   2. If-Else Statements - Two Paths")
                print("   3. Elif Statements - Multiple Paths")
                print("   4. Nested Conditionals - Decisions Within Decisions")
                print("   5. Combining Conditions - AND, OR, NOT")
                print("   6. Common Mistakes & Best Practices")
                print("   7. All topics (Complete guide)")
                print("   8. I'm done with conditionals (exit)")
                
                topic_choice = get_global_menu_choice("\n🔹 Which conditional topic would you like to learn? (1-8/exit): ", 1, 8)
                
                # Handle exit
                if topic_choice == 'exit':
                    print("\n👋 Session ended. Goodbye!")
                    exit()
                
                # Handle return to main menu
                if topic_choice == '8':
                    print("\n✅ Exiting conditional statements section...")
                    break
                
                # Check if topic was already learned (skip for "All topics")
                if topic_choice in topics_learned and topic_choice != '7':
                    review = get_global_valid_input(f"\n🔹 You've already learned topic {topic_choice}. Review it again? (yes/no): ")
                    if review == 'no':
                        continue
                
                # Handle "All topics" selection
                if topic_choice == '7':
                    teach_all_conditional_topics()
                    topics_learned = ['1', '2', '3', '4', '5', '6']
                    print_global_separator()
                    print("🎉 COMPLETE CONDITIONAL STATEMENTS GUIDE FINISHED!")
                    print_global_separator()
                    break
                
                # Teach individual topic based on choice
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
                
                # Ask if user wants to continue with conditionals
                continue_learning = get_global_valid_input("\n🔹 Want to learn another conditional topic? (yes/no): ")
                if continue_learning == 'no':
                    print("\n✅ Exiting conditional statements section...")
                    break
 
        # Now call explain_conditional_statements()
        explain_conditional_statements()

        # Practice section
        practice = get_global_valid_input("\n🔹 Want to practice with conditional statements? (yes/no): ")
        if practice == 'yes':
            print_global_separator()
            print("🧪 INTERACTIVE CONDITIONAL STATEMENTS PRACTICE")
            print_global_separator()
            
            print("Let's practice with conditional statements! 📊")
            print("\nEnter a number and I'll analyze it using if-elif-else:")
            
            user_number = input("Enter a number: ").strip()
            
            if user_number:
                try:
                    num = float(user_number)
                    
                    print(f"\n📊 ANALYZING YOUR NUMBER: {num}")
                    
                    # Let the user see conditional logic in action
                    if num > 0:
                        print(f"   ✅ {num} is POSITIVE")
                        if num > 100:
                            print(f"   🚀 {num} is a BIG positive number!")
                        elif num > 50:
                            print(f"   👍 {num} is a medium positive number")
                        else:
                            print(f"   👌 {num} is a small positive number")
                    elif num < 0:
                        print(f"   ❌ {num} is NEGATIVE")
                        if num < -100:
                            print(f"   🧊 {num} is very negative!")
                        elif num < -50:
                            print(f"   📉 {num} is moderately negative")
                        else:
                            print(f"   📌 {num} is slightly negative")
                    else:
                        print(f"   ⚖️ {num} is ZERO")
                        print("   🔄 Zero is neither positive nor negative")
                    
                    # Check if integer or decimal
                    if num == int(num):
                        print(f"   🔢 {num} is an INTEGER")
                    else:
                        print(f"   💫 {num} is a DECIMAL/FLOAT")
                    
                    # Even or odd (only for positive integers)
                    if num == int(num) and num > 0:
                        if int(num) % 2 == 0:
                            print(f"   🟢 {int(num)} is EVEN")
                        else:
                            print(f"   🟡 {int(num)} is ODD")
                    
                    print("\n✅ Practice complete! You've seen conditional statements in action!")
                    
                except ValueError:
                    print("⚠️  Please enter a valid number next time!")
            else:
                print("⚠️  No number entered for practice.")
 
        Assistant_Response = "Excellent! You've learned comprehensive conditional statements in Python!"
        print(Assistant_Response)
 
    # ========== SECTION 6: ASK TO LEARN ANOTHER TOPIC ==========
    # Ask if user wants to learn another topic
    print_global_separator()
    learn_more = get_global_valid_input("\n🔹 Would you like to learn another topic? (yes/no/exit): ")
 
    if learn_more == 'exit':
        print("\n👋 Goodbye! Come back whenever you need me")
        exit()
    elif learn_more == 'no':
        break
    # If yes, the loop continues
 
# ========== FINAL MESSAGE ==========
print_global_separator()
Assistant_Response = "Congratulations! You've completed the Python basics tutorial 🐍 You learned what you wanted!"
print(Assistant_Response)
print("Keep practicing to enhance your skills. 🥷")
print_global_separator()
