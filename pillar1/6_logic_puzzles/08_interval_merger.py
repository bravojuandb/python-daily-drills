"""
Drill 08 - Interval Merger

Write a function:
    merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]

Requirements:
1. Each interval is `(start, end)` with `start <= end`.
2. Sort the intervals by start position first.
3. Merge intervals that overlap.
4. Return the merged list in sorted order.

Example:
>>> merge_intervals([(1, 3), (2, 5), (8, 10), (9, 12)])
[(1, 5), (8, 12)]

Thinking goal:
This drill is about maintaining a current best segment and deciding when to extend it versus when to start a new one.
"""
