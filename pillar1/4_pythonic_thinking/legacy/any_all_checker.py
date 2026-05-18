"""
You are given a list of numbers.
1. Use `any()` with a generator expression to check if **any number is negative**.
2. Use `all()` with a generator expression to check if **all numbers are even**.

nums = [2, 4, -6, 8, 10]

Expected:
- any(...) → True   (because -6 is negative)
- all(...) → False  (because -6 is negative oddness aside)
"""

nums = [2, 4, -6, 8, 5, 10]

# Generators of booleans:
negatives_check = (x < 0 for x in nums)
even_check = (x % 3 == 0 for x in nums)

# Generators of values:
negatives = (x for x in nums if x % 2 == 0)
even = (x for x in nums if x % 3 == 0)

print(any(negatives_check))
print(all(even_check))
