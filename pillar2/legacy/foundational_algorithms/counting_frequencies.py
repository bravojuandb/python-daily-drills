"""
Problem: Counting Frequencies

You are given a list of values (could be strings, numbers, or any hashable type).  
Write a function `count_frequencies(items)` that returns a dictionary-like object  
showing how many times each distinct element appears.

Rules:
- Use `collections.Counter` for clarity and performance.
- The function must return the Counter object (or dict equivalent).
- Do not manually loop with nested conditions.

Example:
    Input:
        ["apple", "banana", "apple", "orange", "banana", "apple"]
    Output:
        {"apple": 3, "banana": 2, "orange": 1}

Be quick and precise — counting frequency is the foundation of grouping, aggregation, and analytics.
"""

from collections import Counter

def count_frequencies(items: list) -> dict:
    return dict(Counter(items))


fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_frequencies(fruits))


# Manual version
"""
freq = {}
for i in items:
    freq[i] = freq.get(i, 0) + 1
"""

count = {}
for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1
print(count)
