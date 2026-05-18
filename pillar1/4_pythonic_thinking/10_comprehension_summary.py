"""
Drill 10 - Comprehension Summary

Write a function:
    summarize_words(words: list[str]) -> dict[str, int]

Requirements:
1. Use one dictionary comprehension.
2. Include only words with length at least `4`.
3. Use the lowercase word as the key.
4. Use the word length as the value.
5. If the same word appears with different capitalization, it should collapse to one key naturally.

Example:
>>> summarize_words(["Code", "is", "FUN", "Python", "code"])
{'code': 4, 'python': 6}

Thinking goal:
This drill is about mixing normalization, filtering, and mapping in one readable expression.
"""
