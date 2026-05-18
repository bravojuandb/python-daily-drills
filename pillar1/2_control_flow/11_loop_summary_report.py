"""
Challenge 03 - Loop Summary Report

Write a function:
    summarize_temperatures(values: list[int]) -> dict[str, int]

Requirements:
1. Loop through the list once.
2. Count how many values are below `0`.
3. Count how many values are from `0` to `20` inclusive.
4. Count how many values are above `20`.
5. Return a dictionary with keys `"cold"`, `"mild"`, and `"hot"`.

Example:
>>> summarize_temperatures([-2, 0, 15, 21, 30])
{'cold': 1, 'mild': 2, 'hot': 2}

Thinking goal:
This challenge is about maintaining several related counts while reading each value only once.
"""
