"""
Drill 01 - Pure Function

Write a function:
    normalize_title(text: str) -> str

Requirements:
1. Return a new string without mutating external state.
2. Remove leading and trailing spaces.
3. Collapse repeated internal spaces to a single space.
4. Convert the result to title case.
5. If the cleaned text is empty, return `"Untitled"`.

Example:
>>> normalize_title("  the   odyssey ")
'The Odyssey'
>>> normalize_title("   ")
'Untitled'

Thinking goal:
This drill is about making a function deterministic while applying a small sequence of transformations.
"""
