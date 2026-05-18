"""
You are given a list of numbers with duplicates:

nums = [2, 4, 2, 6, 4, 9, 6, 12, 9]

Task:
1. Use a **set comprehension** to extract only the unique values.
2. Only include numbers greater than 5.
3. Transform each number into its square.

Expected result → {36, 81, 144}

Write this in one line using a set comprehension.
"""

def set_builder(nums: list[int]) -> set:
    return {
        x ** 2 for x in nums if x > 5 # No necesary using ... in set(nums)
    }

nums = [2, 4, 2, 6, 4, 9, 6, 12, 9]
print(set_builder(nums))