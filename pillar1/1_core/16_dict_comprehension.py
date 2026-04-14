"""
Drill 16 - Dictionary Comprehension

Write a function:
    build_inventory(products: list[str], quantities: list[int]) -> dict[str, int]

Requirements:
1. Use a dictionary comprehension.
2. Pair each product with the quantity at the same index.
3. If the two lists do not have the same length, raise `ValueError`.

Example:
>>> build_inventory(["apple", "banana", "orange"], [10, 5, 0])
{"apple": 10, "banana": 5, "orange": 0}

Thinking goal:
This drill is about turning aligned inputs into a useful mapping with a concise, readable expression.
"""
