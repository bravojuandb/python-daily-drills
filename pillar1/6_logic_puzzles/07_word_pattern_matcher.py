"""
Drill 07 - Word Pattern Matcher

Write a function:
    matches_pattern(pattern: str, words: str) -> bool

Requirements:
1. `pattern` is a string like `"abba"`.
2. `words` is a space-separated string like `"dog cat cat dog"`.
3. Return `True` only if each pattern character maps to exactly one word, and each word maps back to exactly one character.
4. If the lengths do not match, return `False`.

Example:
>>> matches_pattern("abba", "dog cat cat dog")
True
>>> matches_pattern("abba", "dog cat cat fish")
False
>>> matches_pattern("aaaa", "dog cat cat dog")
False

Thinking goal:
This drill is about enforcing consistency in both directions instead of checking only half the rule.
"""
