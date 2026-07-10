"""
Drill 01 - User Input Echo

Write a function:
    echo_input() -> None

Requirements:
1. Ask the user to type something with `input()`.
2. Immediately print back what the user typed.
3. Do not transform the text.

Example:
If the user types:
Hello world

Output:
Hello world

Thinking goal:
This drill is about building the smallest possible loop between external input and visible output.
"""

def echo_input() -> None:
    text = input("Type anything:")
    print(text)
    return None

echo_input()