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
31

Thinking goal:
This drill is about building a small lazy pipeline and finishing with one focused built-in.
"""
