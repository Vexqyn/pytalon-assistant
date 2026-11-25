"""Application identity and topic catalog (static data)."""

NAME = "Pytalon"
VERSION = "2.3"
CATEGORY = "Major Release (Stable Version)"
DESCRIPTION = (
    """I'm a fully customizable, plugin-powered Python terminal assistant built to adapt to you.\n
   - Extend, configure, and shape it your way. Dependency-free & rule-based. 
   - Transparent, and local-first & Non-AI, no cloud, no black boxes & MIT-licensed. 
   - Learn Python through hands-on practice tailored to your pace and learning style as plugin."""
)

TOPICS = {
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
    '12': 'Conditional statements',
    '13': 'Lists in Python',
}

# Reverse lookup: topic name -> number
TOPIC_NAME_TO_NUMBER = {topic_name: number for number, topic_name in TOPICS.items()}
