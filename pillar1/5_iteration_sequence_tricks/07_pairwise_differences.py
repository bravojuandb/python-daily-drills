"""
Drill 07 - Pairwise Differences

Write a function:
    pairwise_differences(nums: list[int]) -> list[int]

Requirements:
1. Compare each number with the one immediately after it.
2. Return the differences `next - current`.
3. Preserve the original order of comparisons.
4. If the input has fewer than `2` items, return an empty list.

Example:
>>> pairwise_differences([10, 13, 9, 15])
[3, -4, 6]

Thinking goal:
This drill is about traversing a sequence by relationship, not just by individual value.
"""

def pairwise_differences(nums: list[int]) -> list[int]:
    result = []

    for i in range(len(nums) - 1):
        current = nums[i]
        next_number = nums[i + 1]
        result.append(next_number - current)

    return result

if __name__ == "__main__":
    nums = [i**2 for i in range(20)]
    print(nums)
    print(pairwise_differences(nums))