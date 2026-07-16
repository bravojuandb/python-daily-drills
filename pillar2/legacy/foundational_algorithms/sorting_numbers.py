"""
Problem: Sorting Numbers

You are given a list of integers that may include both positive and negative values.
Write a function `sort_by_abs(nums)` that returns a new list sorted by absolute value,
but if two numbers have the same absolute value, the negative one should appear first.

Example:
    Input:  [3, -1, -4, 2, 0, -2, 4, 1]
    Output: [0, -1, 1, -2, 2, -3, -4, 4]

Rules:
- Use only `sorted()` with a custom `key` (no loops).
- The function must return a new list (not modify the input).
- Aim for clean, minimal code.
"""

def sort_by_abs(nums: list[int]) -> list[int]:
    return sorted(nums, key= lambda x: (abs(x), x))


nums = [3, -1, -4, 2, 0, -2, 4, 1]

print(sort_by_abs(nums))