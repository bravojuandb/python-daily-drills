"""
Drill 02 - Dict Comprehension Builder

Write a function:
    build_inventory(keys: list[str], values: list[int]) -> dict[str, int]

Requirements:
1. Use one dictionary comprehension.
2. Pair each key with the value at the same position.
3. Include only items whose value is greater than `2`.
4. Convert each key to uppercase.
5. If the input lists have different lengths, raise `ValueError`.

Example:
>>> build_inventory(["apple", "banana", "orange", "pear"], [5, 0, 3, 8])
{'APPLE': 5, 'ORANGE': 3, 'PEAR': 8}

Thinking goal:
This drill is about deciding when a comprehension can stay concise even with a filter and a validation rule.
"""
