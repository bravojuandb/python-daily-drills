"""
Drill Name: second_smallest.py
Pillar: Pillar 1 – Fluency & Logic
Level: Medium

Problem Statement:

Write a function `second_smallest(nums: list[int]) -> int`
that returns the **second smallest unique value** in a list of integers.

Constraints:

- You **may not use** Python built-in sorting (`sorted()`, `.sort()`).
- You **may not use** `min()` more than once.
- You must handle duplicates by considering **unique values only**.
- If no second smallest exists (e.g., fewer than 2 unique values),
  raise a `ValueError`.

Example:

    nums = [4, 2, 7, 2, 9, 4]
    result = second_smallest(nums)
    print(result)

    Expected Output:
    4

    # Explanation:
    # Unique values: [2, 4, 7, 9]
    # 2nd smallest = 4

Edge Cases:
- Empty list → raise `ValueError("Empty list")`
- Single unique value → raise `ValueError("Not enough unique values")`

⏱ Target Time: 10 minutes
"""

# Inefficient solution
def second_smallest(nums: list[int]) -> int:
    total_nums = set(nums)
    candidate = min(total_nums) + 1
    for num in total_nums:
        if candidate in total_nums:
            sec_sma = candidate
        else:
            candidate += 1
    return sec_sma



# State-of the art solution
# Keep track of two moving targets (the smallest and the second smallest)

def second_smallest(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Empty list")
    
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        raise ValueError("Not enough unique values")

    smallest = second = float("inf")
    for num in unique_nums:
        if num < smallest:
            second = smallest
            smallest = num
        elif smallest < num < second:
            second = num

    return second

print(second_smallest([1, 10000000, 2999999999, 28888888888888]))