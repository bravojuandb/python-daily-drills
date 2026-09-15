"""
Drill 01 - Two-Pointer Pair Sum

Write has_pair_with_sum(numbers, target) -> bool for an ascending sorted list.
Use one pointer at each end and move exactly one based on the current sum. Do
not use a set or nested loops. A value cannot pair with itself at one index.

Target complexity: O(n) time and O(1) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: discard impossible ranges while preserving the search invariant.
"""


def has_pair_with_sum(numbers: list[int], target: int) -> bool:
    left_index = 0
    right_index = len(numbers) - 1

    while left_index < right_index:
        current_sum = numbers[left_index] + numbers[right_index]

        if current_sum == target:
            return True

        if current_sum > target:
            right_index -= 1
        else:
            left_index += 1

    return False


# Time: O(n) because each pointer moves toward the other at most once per item.
# Extra space: O(1) because the function stores only two indices and one sum.
