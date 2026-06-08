"""
Drill 11 - Generator Pipeline

Write a function:
    total_error_message_lengths(messages: list[str]) -> int

Requirements:
1. Use a generator expression, not a list comprehension.
2. After stripping surrounding whitespace, consider only messages that start with `"ERROR:"`.
3. Measure the lengths of those cleaned messages.
4. Sum the lengths with `sum()`.
5. Return the final total.

Example:
>>> total_error_message_lengths(["INFO: ok", " ERROR: disk full ", "ERROR: timeout", "WARN: retrying"])
30

Thinking goal:
This drill is about building a small lazy pipeline and finishing with one 
focused built-in.
"""

def total_error_message_lengths(messages: list[str]) -> int:
    cleaned_messages = (message.strip() for message in messages)
    total = sum(
        len(message)
        for message in cleaned_messages
        if message.startswith("ERROR:")
    )
    return total

def total_error_for_loop(messages: list[str]) -> int:
    total = 0
    for message in messages:
        clean_message = message.strip()
        if clean_message.startswith("ERROR:"):
            total += len(clean_message)
    return total

def total_error_comprehension(messages: list[str]) -> list[int]:
    "Intentionally returns the list of lengths for each valid string"
    return [
        len(message.strip()) 
        for message in messages 
        if message.strip().startswith("ERROR:")
    ]

if __name__ == "__main__":
    messages = ["INFO: ok", " ERROR: disk full ", "ERROR: timeout", "WARN: retrying"]
    print(f"this is the canonical solution: {total_error_message_lengths(messages)}")

    print(f"This is the for loop solution: {total_error_for_loop(messages)}")

    print(f"This is the list of lengths: {total_error_comprehension(messages)}")