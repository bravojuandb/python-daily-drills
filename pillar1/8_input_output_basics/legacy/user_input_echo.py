"""
Write a function `echo_input()` that:
1. Asks the user to type something (use input()).
2. Immediately prints back what the user typed.

⚡ Task:
- Implement the function.
- Run it once with "Hello world".
- Run it again with "42".

Be quick, don’t overthink! 🚀
"""

# Barebones version:
def echo_input():
    return input("Type something:")

# With logging and .strip()and .upper()

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def echo_input() -> str:

    message = input("Type something:")
    logging.info(f"User typed: {message}")

    processed = message.strip().upper()
    logging.info(f"Processed: {processed.split()}")

    return processed

print(echo_input())