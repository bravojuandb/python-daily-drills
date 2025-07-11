"""
Write a function that returns the largest number in a given list of integers.
If the list is empty, return None.

"""

# Inefficient version O(n log n)

def find_max_naive(nums: list[int]) -> int | None:

    if not nums:
        return None
    
    nums = list(reversed(sorted(nums)))
    return nums[0]

# Efficient version

def find_max(nums: list[int]) -> int | None:

    if not nums:
        return None
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# Pythoniv version

def find_max_efficient(nums: list[int]) -> int | None:
    return max(nums) if nums else None


print(find_max([5,28,45,2,3,-2,-60,5,28,45,2,3,-2,-60,445,34,234,56,14,87,56,787,9876,5453,234]))

import timeit


print(timeit.timeit(
    stmt="find_max_efficient(list(range(1_000_000, 0, -1)))",
    setup="from __main__ import find_max_efficient",
    number=1000  # repeat 1000 times
))