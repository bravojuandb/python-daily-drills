"""
Problem: Binary Search Implementation

You are given a sorted list of integers `nums` and a target value `x`.  
Write a function `binary_search(nums, x)` that returns the **index** of `x` in `nums`,  
or `-1` if `x` is not found.

Rules:
- Use a `while low <= high` loop (no recursion).
- Update `low` and `high` correctly depending on comparisons.
- Midpoint formula: `mid = (low + high) // 2`
- Do NOT use `in`, `.index()`, or any helper libraries.

Example:
    Input:
        nums = [1, 3, 5, 7, 9, 11]
        x = 7
    Output:
        3

Be quick and precise — off-by-one errors lurk everywhere in binary search.
"""

def binary_search(nums: list[int], x: int) -> int:
    """
    Principles:
    1. If x is in the array it is within the closest interval [low, high]
    2. Binary search works only in sorted data in ascendin order.
    2. Compute mid, compare, discard half, repeat
    """
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11]
target = 5

print(binary_search(numbers, target))
"""
1. low = 0 high = 6 mid = 3 / high = 2
2. low = 0 high = 2 mid = 1 / low = 2
3. low = 2 high = 2 mid = 2 / end

"""