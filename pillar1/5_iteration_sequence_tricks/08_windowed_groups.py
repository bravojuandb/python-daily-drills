"""
Drill 08 - Windowed Groups

Write a function:
    windows(nums: list[int], width: int) -> list[list[int]]

Requirements:
1. Return all consecutive windows of length `width`.
2. Windows should overlap by default.
3. Preserve the original order.
4. If `width` is greater than the list length, return an empty list.
5. If `width` is less than `1`, raise `ValueError`.

Example:
>>> windows([1, 2, 3, 4], 3)
[[1, 2, 3], [2, 3, 4]]

Thinking goal:
This drill is about slicing a sequence by moving viewpoints instead of fixed chunks.
"""
