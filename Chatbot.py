
# PROJECT 1: RULE-BASED AI CHATBOT
# DecodeLabs - Artificial Intelligence Engineer Track


def sanitize_input(user_text):
    """Normalize user input."""
    return user_text.lower().strip()


def get_response(user_input):
    """Process intent using dictionary lookup."""

    knowledge_base = {

    # Greetings
    "hello": "🤖 Hello! Nice to meet you.",
    "hi": "🤖 Hi there!",
    "hey": "🤖 Hey! Ready to chat?",

    # Personal Information
    "what is your name": "🤖 My name is DecodeBot.",
    "who are you": "🤖 I am DecodeBot, a Rule-Based AI Chatbot.",

    # AI Questions
    "what is ai": "🤖 AI stands for Artificial Intelligence. It enables machines to simulate human intelligence.",

    "what is artificial intelligence":
    "🤖 Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",

    "who created you":
    "🤖 I was created as part of the DecodeLabs AI Internship Project.",

    "what can you do":
    "🤖 I can answer predefined questions and demonstrate rule-based decision making.",

    # Small Talk
    "how are you":
    "🤖 I am functioning perfectly. Thanks for asking!",

    "good morning":
    "🤖 Good morning! Hope you have a productive day.",

    "good afternoon":
    "🤖 Good afternoon! How can I help you?",

    "good evening":
    "🤖 Good evening! Nice to see you.",

    "thank you":
    "🤖 You're welcome!",

    "thanks":
    "🤖 Happy to help!",

    # Help
    "help": """
🤖 Available Commands:

• hello
• hi
• hey
• how are you
• what is your name
• who are you
• what is ai
• what is artificial intelligence
• who created you
• what can you do
• good morning
• good afternoon
• good evening
• thank you
• bye
• exit
• quit
"""
}
    

    return knowledge_base.get(
        user_input,
        "🤖 Sorry, I don't understand that command."
    )


def display_welcome():
    print("=" * 60)
    print("🤖 DECODEBOT - RULE BASED AI CHATBOT")
    print("=" * 60)
    print("Type 'help' to see available commands.")
    print("Type 'exit' to terminate the chatbot.")
    print("=" * 60)


def is_exit_command(user_input):
    """Check exit conditions."""
    exit_commands = {"bye", "exit", "quit"}
    return user_input in exit_commands


# MAIN PROGRAM

display_welcome()

while True:

    # INPUT
    raw_input_text = input("\nYou: ")

    # SANITIZATION
    user_input = sanitize_input(raw_input_text)

    # EXIT STRATEGY
    if is_exit_command(user_input):
        print("🤖 Goodbye! Have a great day.")
        break

    # PROCESS
    response = get_response(user_input)

    # OUTPUT
    print(response)

print("\n✅ Program Terminated Successfully.")