"""
Drill 03 - Fixed-Size Sliding Window

Write max_window_sum(numbers, size) -> int. Return the greatest sum of any
contiguous window of exactly size elements. Raise ValueError when size <= 0 or
size exceeds the list length. Do not sum each window from scratch.

Target complexity: O(n) time and O(1) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: update a window by removing one value and adding one value.
"""


def max_window_sum(numbers: list[int], size: int) -> int:
    if size <= 0 or size > len(numbers):
        raise ValueError("size must be greater than zero and smaller that len(list)")

    left_index = 0
    right_index = size

    current_sum = 0
    for index in range(size):
        current_sum += numbers[index]

    greatest = current_sum

    for righ_idex in range(size, len(numbers)):
        current_sum = current_sum - numbers[left_index] + numbers[righ_idex]
        left_index += 1
        right_index += 1

        if current_sum > greatest:
            greatest = current_sum

    return greatest


# Time: O(n), where n is the list length; each window sum is updated in constant time.
# Extra space: O(1), because we keep only indices and sums, without copying the list.
