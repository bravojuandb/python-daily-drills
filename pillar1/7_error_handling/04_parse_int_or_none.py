"""
Drill 04 - Parse Int or None

Write a function:
    parse_int(text: str) -> int | None

Requirements:
1. Try to convert the text with `int()`.
2. If the conversion works, return the integer.
3. If a `ValueError` occurs, return `None`.
4. Strip surrounding spaces before converting.

Example:
>>> parse_int(" 42 ")
42
>>> parse_int("hello")
None

Thinking goal:
This drill is about separating invalid text input from valid numeric input without overcomplicating the flow.
"""
