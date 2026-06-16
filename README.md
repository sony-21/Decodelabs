# 🤖 DecodeBot - Rule-Based AI Chatbot

## Project 1: Rule-Based AI Chatbot

**DecodeLabs - Artificial Intelligence Engineer Internship**

---

## 📌 Project Overview

DecodeBot is a simple rule-based AI chatbot developed using Python. The chatbot simulates basic human interaction by responding to predefined user inputs through deterministic decision-making logic.

Unlike machine learning systems, this chatbot relies entirely on explicit programming rules, making it transparent, predictable, and easy to understand.

---

## 🎯 Objective

The objective of this project is to create a chatbot that:

* Responds to predefined user inputs
* Handles greetings and exit commands
* Uses control flow and decision-making logic
* Runs continuously until the user exits
* Demonstrates foundational AI concepts

---

## ✨ Features

* Greeting recognition
* User input sanitization
* Dictionary-based knowledge base
* Intent matching using hash map lookup
* Continuous conversation loop
* Fallback response for unknown inputs
* Graceful exit handling
* Modular and readable code structure

---

## 🛠 Technologies Used

* Python 3
* Functions
* Dictionaries (Hash Maps)
* Loops
* Conditional Statements
* String Manipulation

---

## 🏗 System Architecture

### IPO Model

Input → Process → Output

1. **Input**

   * Accept user input through the terminal.

2. **Process**

   * Convert input to lowercase.
   * Remove unnecessary spaces.
   * Match the input against predefined intents stored in a dictionary.

3. **Output**

   * Display the corresponding chatbot response.

---

## 🔄 Program Flow

Start

↓

Display Welcome Message

↓

Get User Input

↓

Sanitize Input

↓

Check Exit Command

↓

If Exit → End Program

↓

Else → Search Knowledge Base

↓

Display Response

↓

Repeat

---

## 📚 Supported Commands

| User Input        | Bot Response            |
| ----------------- | ----------------------- |
| hello             | Greeting message        |
| hi                | Greeting message        |
| hey               | Greeting message        |
| who are you       | Bot introduction        |
| what is your name | Bot name                |
| how are you       | Status response         |
| thank you         | Appreciation response   |
| help              | List available commands |
| bye               | Exit chatbot            |
| exit              | Exit chatbot            |
| quit              | Exit chatbot            |

---

## 💻 Sample Output

```text
============================================================
🤖 DECODEBOT - RULE BASED AI CHATBOT
============================================================

You: hello
🤖 Hello! Nice to meet you.

You: who are you
🤖 I am DecodeBot, a rule-based AI chatbot.

You: how are you
🤖 I am functioning perfectly.

You: exit
🤖 Goodbye! Have a great day.

Program Terminated Successfully.
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Control flow implementation
* Decision-making logic using Python
* Dictionary-based intent matching
* Input sanitization techniques
* Continuous program execution using loops
* Fundamental concepts of rule-based AI systems

---

## 🚀 Future Improvements

* Add more conversational intents
* Support partial keyword matching
* Implement sentiment-based responses
* Create a graphical user interface (GUI)
* Integrate machine learning capabilities

---

## 📌 Conclusion

This project demonstrates the core principles of rule-based artificial intelligence using Python. By combining input sanitization, dictionary-based intent matching, and continuous execution, DecodeBot successfully simulates basic conversational behavior and serves as a strong foundation for future AI development.
