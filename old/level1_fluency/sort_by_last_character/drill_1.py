"""
Drill Name: sort_by_last_char.py
Pillar: 1 – Fluency & Logic
Subcategory: Sorting & lambda
Level: Easy

Description:
Write a function that takes a list of strings and returns a new list sorted 
in ascending order based on the last character of each string. 
If two strings have the same last character, maintain their original relative order.

Function Signature:
    def sort_by_last_char(words: list[str]) -> list[str]:
        pass

Example:
    >>> sort_by_last_char(["apple", "banana", "pear", "grape"])
    ['banana', 'apple', 'grape', 'pear']

Explanation:
    Last letters:
        "banana" → 'a'
        "apple"  → 'e'
        "grape"  → 'e'
        "pear"   → 'r'
    Sorted by last letter:
        'a' → banana
        'e' → apple, grape
        'r' → pear

Constraints:
    - Must use sorted() with a lambda as the key.
    - Do NOT use list slicing in the key — extract the last character cleanly.
    - Input list will have at least one element; strings will be non-empty.
    - Preserve stability (same last char keeps original order).

Turing-style note:
    You’ll be tested for clean syntax, correctness, and time-to-first-solution speed.
    Aim for under 3 minutes.
"""

def sort_by_last_char(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: word[len(word) -1])

print(sort_by_last_char(["apple", "z", "banana", "pear", "grape"]))

