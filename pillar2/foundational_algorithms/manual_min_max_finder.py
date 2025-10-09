"""
# Pillar 2 — Foundational Algorithms
## Manual Min/Max Finder → loop

You are given a list of random integers:

nums = [12, 45, 7, 32, 89, 3, 56, 18]

TASK:
1. Without using `min()` or `max()`, write a loop that finds:
   - The smallest number
   - The largest number
2. Return them as a tuple: (min_value, max_value)

Example output:
(3, 89)

⏱️ Be quick and precise. Focus on correct comparisons and initial values.
"""

# Using min() and max()
def min_max_finder(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)


# Manual

def manual_min_max_finder(nums: list[int]) -> tuple[int, int]:
    # Assume the first number is both the smallest and the largest
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest


nums = [12, 45, 7, 32, 89, 3, 56, 18]

print(manual_min_max_finder(nums))

