"""
Drill 06 - Nearest Repeat Distance

Write a function:
    nearest_repeat_distance(nums: list[int]) -> int

Requirements:
1. Return the smallest distance between two equal values.
2. Distance means the difference between their indexes.
3. If no value repeats, return `-1`.
4. Aim for one pass through the list.

Example:
>>> nearest_repeat_distance([7, 1, 3, 4, 1, 7])
3

Thinking goal:
This drill is about tracking just enough state to improve your answer whenever you see a repeat.
"""
