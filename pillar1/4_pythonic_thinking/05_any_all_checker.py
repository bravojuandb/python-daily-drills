"""
Drill 05 - Any and All Checker

Write a function:
    check_numbers(nums: list[int]) -> tuple[bool, bool]

Requirements:
1. Use `any()` with a generator expression to check whether any number is negative.
2. Use `all()` with a generator expression to check whether all numbers are even.
3. Return the results as `(has_negative, all_even)`.

Example:
>>> check_numbers([2, 4, -6, 8, 10])
(True, True)

Thinking goal:
This drill is about asking direct yes-or-no questions without building extra lists.
"""
