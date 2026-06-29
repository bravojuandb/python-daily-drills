"""
Drill 03 - Duplicate Finder

Write a function:
    find_duplicates(nums: list[int]) -> set[int]

Requirements:
1. Return a set of all numbers that appear more than once.
2. Do not return the same duplicate twice.
3. Preserve negative numbers and `0` exactly like any other value.
4. Do not use explicit `for` or `while` loops.
5. Solve it with either `collections.Counter` or a set/list method.

Example:
>>> find_duplicates([4, 5, 6, 7, 4, 5, 8, 9, 5])
{4, 5}
>>> find_duplicates([0, -1, -1, 2, 2, 2, 3])
{-1, 2}
>>> find_duplicates([])
set()

Challenge bar:
- Avoid returning counts; return only the repeated values.
- Try to keep the solution to one expression after any import.

Thinking goal:
This drill is about choosing a structure that makes repetition visible without manual bookkeeping.
"""


from collections import Counter

def find_duplicates(nums: list[int]) -> set[int]:
    return {num for num, count in Counter(nums).items() if count > 1}


if __name__ == "__main__":
    print(find_duplicates([4, 5, 6, 7, 4, 5, 8, 9, 5]))