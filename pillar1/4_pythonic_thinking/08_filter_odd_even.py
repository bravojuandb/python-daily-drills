"""
Drill 08 - Filter Odd and Even

Write a function:
    split_parity(nums: list[int]) -> tuple[list[int], list[int]]

Requirements:
1. Use `filter()` to extract the even numbers.
2. Use `filter()` again to extract the odd numbers.
3. Return `(evens, odds)`.
4. Preserve the original order inside each result.

Example:
>>> split_parity([1, 2, 3, 4, 5, 6])
([2, 4, 6], [1, 3, 5])

Thinking goal:
This drill is about separating a sequence into two views without manually managing indexes.
"""
