"""
Drill Name: sort_by_last_char.py
Pillar: 1 – Fluency & Logic
Subcategory: Sorting & lambda
Level: Medium

Description:
Write a function that takes a list of strings and 
returns a new list sorted primarily by the last character of each string. 
If two or more strings share the same last character, sort them secondarily 
by string length (shorter first). If they still tie (same last char and length), 
maintain their original relative order.

Example:
    >>> sort_by_last_char(["apple", "banana", "pear", "grape", "pie"])
    ['banana', 'pie', 'apple', 'grape', 'pear']

Explanation:
    Last letters:
        "banana" → 'a' (len=6)
        "apple"  → 'e' (len=5)
        "grape"  → 'e' (len=5)
        "pear"   → 'r' (len=4)
        "pie"    → 'e' (len=3)

    Sorted by:
        'a' → banana
        'e' → pie (len 3), apple (len 5), grape (len 5, comes after apple since stable)
        'r' → pear

Constraints:
    - Must use sorted() with a lambda as the key.
    - Must combine multiple sort keys into the lambda.
    - Do NOT sort multiple times (must be one sorted() call).
    - Input list will have at least one element; strings will be non-empty.
    - Preserve stability for exact ties (same last char + same length).
"""

def sort_by_last_char(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: (word[-1], len(word)))

print(sort_by_last_char(["apple", "banana", "pear", "grape", "pie"]))