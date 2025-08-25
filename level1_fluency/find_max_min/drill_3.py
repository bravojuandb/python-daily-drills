"""
Drill Name: second_largest.py
Pillar: Pillar 1 – Fluency & Logic
Level: Medium

Problem Statement:

Write a function `second_largest(nums: list[int]) -> int`
that returns the **second largest unique value** in a list of integers.

Constraints:

- You **may not use** Python built-in sorting (`sorted()`, `.sort()`).
- You **may not use** `max()` more than once.
- You must handle duplicates by considering **unique values only**.
- If no second largest exists (e.g., fewer than 2 unique values),
  raise a `ValueError`.

Example:

    nums = [4, 2, 7, 2, 9, 4]
    result = second_largest(nums)
    print(result)

    Expected Output:
    7

    # Explanation:
    # Unique values: [2, 4, 7, 9]
    # 2nd largest = 7

Edge Cases:
- Empty list → raise `ValueError("Empty list")`
- Single unique value → raise `ValueError("Not enough unique values")`

⏱ Target Time: 10 minutes
"""

def second_largest(nums:list[int]) -> int:
    if not nums:
        raise ValueError("Empty list")
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        raise ValueError('Not enough unique values')
    
    largest = second = float("-inf")
    for num in unique_nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second

print(second_largest([2, 4, 7, 9]))