"""
Drill 02 - Binary Search

Write binary_search(items, target) -> int for an ascending sorted list. Return
any matching index or -1. Use a loop with inclusive low and high bounds. Do not
use `in`, `.index()`, recursion, or slicing.

Target complexity: O(log n) time and O(1) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Worst-case time is O(log n) and extra space is O(1) because each iteration
halves the remaining search interval while storing only index variables.

Thinking goal: maintain the invariant that a possible match lies in [low, high].
"""


def binary_search(items: list[int], target: int) -> int:
    # Time: O(log n) — each loop discards half of the remaining search range.
    # Space: O(1) — the algorithm stores only a fixed number of index variables.
    left_index = 0
    right_index = len(items) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = items[middle_index]

        if target == middle_value:
            return middle_index
        elif target > middle_value:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1
