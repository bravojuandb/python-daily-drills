"""
Drill 11 - Loop Summary Report

Write a function:
    summarize_temperatures(values: list[int]) -> dict[str, int]

Requirements:
1. Loop through the list once.
2. Group each value into one of three buckets:
   - `"cold"` for values below `0`
   - `"mild"` for values from `0` to `20` inclusive
   - `"hot"` for values above `20`
3. Return the counts in a dictionary with those three keys.
4. Every value must affect exactly one bucket.

Example:
>>> summarize_temperatures([-2, 0, 15, 21, 30])
{'cold': 1, 'mild': 2, 'hot': 2}

Thinking goal:
This drill is about classifying each input exactly once while maintaining a small running summary.
"""
