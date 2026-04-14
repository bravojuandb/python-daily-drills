"""
Drill 05 - String Reversal

Write a function:
    analyze_word(text: str) -> tuple[str, bool, str]

Requirements:
1. Return a tuple containing:
   - the reversed string
   - `True` if the original string is a palindrome, otherwise `False`
   - the middle character(s) of the reversed string
2. If the length is odd, return 1 middle character.
3. If the length is even, return the 2 middle characters.
4. Do not import anything.

Examples:
>>> analyze_word("radar")
("radar", True, "d")

>>> analyze_word("python")
("nohtyp", False, "ht")

Thinking goal:
This drill mixes reversal, comparison, and index reasoning in one small function.
"""
