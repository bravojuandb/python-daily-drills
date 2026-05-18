"""
You receive a list of integers.  
Your task: return a set of all numbers that appear more than once.

Rules:
- You may not use loops explicitly (`for`, `while`).
- You must use either `set()` operations or `collections.Counter`.
- Input: [4, 5, 6, 7, 4, 5, 8, 9, 5]
- Output: {4, 5}

Write the function `find_duplicates(nums: list[int]) -> set[int]`.
"""

# Using a for loop 
def find_duplicates(nums: list[int]) -> set[int]:
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen: 
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

# Using collections.Counter and set comprehension
from collections import Counter
def find_duplicates(nums: list[int]) -> set[int]:
    return {num for num, count in Counter(nums).items() if count > 1}

# Using set comprehension with set.count() 
# Efficiency is O(n ** 2) because it scans the list every time
def find_duplicates(nums: list[int]) -> set[int]:
    return {n for n in set(nums) if nums.count(n) > 1}


input = [4, 5, 6, 7, 4, 5, 8, 9, 5]

print(find_duplicates(input))