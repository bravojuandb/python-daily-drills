"""
Drill 06 - Break and Continue Maze

Write a function:
    first_affordable(price_tags: list[int], budget: int) -> int

Requirements:
1. Loop through the prices in order.
2. If a price is negative, skip it with `continue`.
3. Find the first price that is less than or equal to `budget`.
4. Use `break` for the early stop behavior.
5. If no valid affordable price is found, return `-1`.

Example:
>>> first_affordable([-5, 120, 80, 150], 100)
80

Thinking goal:
This drill is about tracing which values should be ignored, which should stop the search, and which should be skipped.
"""
