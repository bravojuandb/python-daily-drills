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
