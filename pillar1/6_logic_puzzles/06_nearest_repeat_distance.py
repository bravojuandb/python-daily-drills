"""
Drill 06 - Nearest Repeat Distance

Write a function:
    nearest_repeat_distance(nums: list[int]) -> int

Requirements:
1. Return the smallest distance between two equal values.
2. Distance means the difference between their indexes.
3. If no value repeats, return `-1`.
4. Repeats may happen more than twice; use the nearest pair, not the first pair.
5. Aim for one pass through the list.

Example:
>>> nearest_repeat_distance([7, 1, 3, 4, 1, 7])
3
>>> nearest_repeat_distance([5, 2, 5, 2, 5])
2
>>> nearest_repeat_distance([1, 2, 3])
-1

Challenge bar:
- Do not compare every pair of indexes.
- Track only the most useful previous position for each number.

Thinking goal:
This drill is about updating the best answer when a repeat appears, while keeping only necessary state.
"""

def nearest_repeat_distance(nums: list[int]) -> int:

    last_seen = {}
    min_distance = len(nums)

    for index, val in enumerate(nums):
        if val in last_seen:
            distance = index - last_seen[val]
            min_distance = min(min_distance, distance)

        last_seen[val] = index

    if min_distance == len(nums):
        return -1

    return min_distance


if __name__ == "__main__":

    print(nearest_repeat_distance([7, 1, 3, 4, 1, 7]))