"""
Drill 02 - Dict Comprehension Builder

Write a function:
    build_inventory(names: list[str], stock_counts: list[int]) -> dict[str, int]

Requirements:
1. Use one dictionary comprehension.
2. Pair each product name with the count at the same position.
3. Include only items whose count is greater than `0`.
4. Normalize each product name to lowercase.
5. If the input lists have different lengths, raise `ValueError`.

Example:
>>> build_inventory([" Apple ", "banana", "PEAR", "Kiwi"], [5, 0, 3, 8])
{'apple': 5, 'pear': 3, 'kiwi': 8}

Thinking goal:
This drill is about deciding when a comprehension can stay concise even with a filter and a validation rule.
"""
