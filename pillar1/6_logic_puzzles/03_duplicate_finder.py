"""
Drill 03 - Duplicate Finder

Write a function:
    find_duplicates(nums: list[int]) -> set[int]

Requirements:
1. Return a set of all numbers that appear more than once.
2. Do not return the same duplicate twice.
3. Do not use explicit `for` or `while` loops.
4. Use either `collections.Counter` or a set-based approach.

Example:
>>> find_duplicates([4, 5, 6, 7, 4, 5, 8, 9, 5])
{4, 5}

Thinking goal:
This drill is about choosing a data structure that does the counting or deduplication work for you.
"""
