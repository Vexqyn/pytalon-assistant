"""Practice task specifications (static data).

Each entry tells the practice engine what to show the learner and what
kind of observable output to look for. The engine never enforces a coding
style: any safe code that produces real output passes.
"""

PRACTICE_SPECS = {
    "Hello World": {
        "instructions": "Write a Python program that prints 'Hello, World!'",
        "example": "print('Hello, World!')",
        "hints": ["use print()", "put the text inside quotes"],
        "output": {"kind": "any_stdout"},
    },
    "Functions": {
        "instructions": "Create a function called 'greet' that takes a 'name' parameter and returns a greeting message. Then call it with your name!",
        "example": "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('YourName'))",
        "hints": ["define the function with def", "use return", "call the function"],
        "output": {"kind": "function_return", "name": "greet", "inputs": ["Ali"]},
    },
    "Variables": {
        "instructions": "Create three variables: 'name' (your name as string), 'age' (your age as number), and 'hobby' (your hobby as string). Then print all of them!",
        "example": "name = 'John'\nage = 20\nhobby = 'Coding'\nprint(f'Name: {name}, Age: {age}, Hobby: {hobby}')",
        "hints": ["use = to assign", "use print()"],
        "output": {"kind": "any_stdout"},
    },
    "Relational operators": {
        "instructions": "Create two number variables (a and b) and use at least 2 different relational operators (==, !=, >, <, >=, <=) to compare them. Print each comparison result!",
        "example": "a = 10\nb = 5\nprint(f'a > b: {a > b}')\nprint(f'a == b: {a == b}')\nprint(f'a >= b: {a >= b}')",
        "hints": ["assign two numbers", "compare them", "print the results"],
        "output": {"kind": "any_stdout"},
    },
    "Assignment operators": {
        "instructions": "Create a variable x with an initial value. Then use at least 2 compound assignment operators (+=, -=, *=, /=, etc.) and print x after each operation!",
        "example": "x = 10\nprint(f'Initial x: {x}')\nx += 5\nprint(f'After x += 5: {x}')\nx *= 2\nprint(f'After x *= 2: {x}')",
        "hints": ["start with a value", "use += or *=, then print"],
        "output": {"kind": "any_stdout"},
    },
    "Logical operators": {
        "instructions": "Create two boolean variables (e.g., is_raining, has_umbrella). Use logical operators (and/or/not) to make decisions and print the results!",
        "example": "is_raining = True\nhas_umbrella = False\nprint(f'Should I go out? {not is_raining or has_umbrella}')",
        "hints": ["assign True/False", "combine with and/or/not", "print"],
        "output": {"kind": "any_stdout"},
    },
    "Type conversion": {
        "instructions": "Create a string variable 'num_str' with a number value. Convert it to int and float. Print the type before and after each conversion!",
        "example": "num_str = '42'\nprint(f'Original type: {type(num_str)}')\nnum_int = int(num_str)\nprint(f'After int(): {num_int}, Type: {type(num_int)}')\nnum_float = float(num_str)\nprint(f'After float(): {num_float}, Type: {type(num_float)}')",
        "hints": ["use int() and float()", "print type() to check"],
        "output": {"kind": "any_stdout"},
    },
    "Input function": {
        "instructions": "Write a program that asks for a user's name and age using input(). Then print a message using both values!",
        "example": "name = input('Enter your name: ')\nage = input('Enter your age: ')\nprint(f'Hello {name}, you are {age} years old!')",
        "hints": ["use input()", "store the result", "print a message"],
        "output": {"kind": "any_stdout"},
    },
    "Comments in Python": {
        "instructions": "Write a small Python program with at least 3 lines of code. Add comments explaining what each part does! Use both single-line (#) and inline comments.",
        "example": "# This program greets the user\nname = 'Student'  # Store the name\n# Print the greeting\nprint(f'Hello, {name}!')",
        "hints": ["start a comment with #", "put code and comments together", "print something"],
        "output": {"kind": "any_stdout"},
    },
    "Strings in Python": {
        "instructions": "Create a string variable with your name. Use at least 3 string operations (e.g., upper(), lower(), concatenation with +, indexing with [], or slicing). Print each result!",
        "example": "name = 'Python Learner'\nprint(f'Original: {name}')\nprint(f'Uppercase: {name.upper()}')\nprint(f'First letter: {name[0]}')\nprint(f'First 6 chars: {name[:6]}')\nprint(f'Reversed: {name[::-1]}')",
        "hints": ["assign a string", "try .upper() or slicing", "print each result"],
        "output": {"kind": "any_stdout"},
    },
    "Data types in Python": {
        "instructions": "Create at least 4 variables of different data types (int, float, str, bool). Use type() to check and print each variable's type!",
        "example": "age = 25\nscore = 95.5\nname = 'Student'\nis_active = True\nprint(f'age type: {type(age)}')\nprint(f'score type: {type(score)}')\nprint(f'name type: {type(name)}')\nprint(f'is_active type: {type(is_active)}')",
        "hints": ["assign int, float, str, bool", "print type() of each"],
        "output": {"kind": "any_stdout"},
    },
    "Conditional statements": {
        "instructions": "Write a program that checks if a number is positive, negative, or zero. Use if-elif-else statements and print the result!",
        "example": "num = 10\nif num > 0:\n    print('Positive number')\nelif num < 0:\n    print('Negative number')\nelse:\n    print('Zero')",
        "hints": ["use if / elif / else", "indent the blocks", "print the result"],
        "output": {"kind": "any_stdout"},
    },
    "Lists in Python": {
        "instructions": "Create a list of your favorite colors. Add a new color using append(), remove one color, and sort the list. Print the list after each operation!",
        "example": "colors = ['red', 'blue', 'green']\nprint(f'Original: {colors}')\ncolors.append('yellow')\nprint(f'After append: {colors}')\ncolors.remove('blue')\nprint(f'After remove: {colors}')\ncolors.sort()\nprint(f'After sort: {colors}')",
        "hints": ["create a list with []", "use .append() and .remove()", "print the list"],
        "output": {"kind": "any_stdout"},
    },
}
