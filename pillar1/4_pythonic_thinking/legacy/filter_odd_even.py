"""
You are given a list of numbers.
1. Use `filter()` with a `lambda` to extract only the even numbers.
2. Use `filter()` with a `lambda` to extract only the odd numbers.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected:
- Evens → [2, 4, 6, 8, 10]
- Odds  → [1, 3, 5, 7, 9]
"""

nums = [x for x in range(1, 11)]

evens = filter(lambda x: x % 2 == 0, nums)

odds = filter(lambda x: x % 2 != 0, nums)

print([*evens])
print([*odds])