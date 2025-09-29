"""
Problem:
You have a list of integers: nums = [2, -3, 5, 0, -8, 7].

1. Transform it into a new list that contains:
   - each positive number squared
   - skip zeros
   - replace each negative number with its absolute value

Use **one list comprehension**.

Expected result for nums = [2, -3, 5, 0, -8, 7]:
[4, 3, 25, 8, 49]
"""

def transform_list(nums: list[int]) -> list[int]:
    return [
        (x**2 if x > 0 else abs(x))
        for x in nums
        if x != 0]


nums = [2, -3, 5, 0, -8, 7]

print(transform_list(nums))