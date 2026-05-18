"""
Write a function `first_even(nums: list[int]) -> int`.

Rules:
- Use a `for` loop to go through the numbers.
- If you find an even number, return it immediately (use `break`).
- If the number is negative, skip it (use `continue`).
- If no even number is found, return -1.

Example:
nums = [-3, -2, 7, 9, 12] → first_even(nums) = 12
nums = [-5, -7, -9] → first_even(nums) = -1

Try to solve it fast — under 2 minutes!
"""

def first_even(nums: list[int]) -> int:
    first = -1  # default return value
    for num in nums:
        if num < 0:
            continue          # skip negatives
        if num % 2 == 0:
            first = num       # store the first even
            break             # exit loop immediately
    return first


# examples
print(first_even([-3, -2, 7, 9, 12]))
print(first_even([-5, -7, -9])) 