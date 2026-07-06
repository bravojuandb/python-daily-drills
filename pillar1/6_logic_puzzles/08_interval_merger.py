"""
Drill 08 - Interval Merger

Write a function:
    merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]

Requirements:
1. Each interval is `(start, end)` with `start <= end`.
2. Sort the intervals by start position first.
3. Merge intervals that overlap or touch at an endpoint.
4. Preserve negative ranges correctly.
5. Return the merged list in sorted order.
6. An empty input should return an empty list.

Example:
>>> merge_intervals([(1, 3), (2, 5), (8, 10), (9, 12)])
[(1, 5), (8, 12)]
>>> merge_intervals([(5, 7), (1, 2), (2, 4), (-3, -1)])
[(-3, -1), (1, 4), (5, 7)]
>>> merge_intervals([])
[]

Challenge bar:
- Sort first, then solve with a single scan.
- Be precise about the difference between extending the current interval and starting a new one.

Thinking goal:
This drill is about turning many local overlaps into the fewest correct final ranges.
"""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if intervals == []:
        return []

    sorted_intervals = sorted(intervals)
    merged = []

    current_start, current_end = sorted_intervals[0]

    for next_start, next_end in sorted_intervals[1:]:
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged.append((current_start, current_end))

    return merged


if __name__ == "__main__":
    print(merge_intervals([(1, 3), (2, 5), (8, 10), (9, 12)]))
    print(merge_intervals([(5, 7), (1, 2), (2, 4), (-3, -1)]))
    print(merge_intervals([]))