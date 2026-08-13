"""
Drill 03 - Manual Min and Max

Write min_max(numbers) -> tuple[int, int]. Find both values in one pass without
using min, max, or sorting. Raise ValueError for an empty list.

Example: min_max([4, -2, 9, 9]) returns (-2, 9).
Target complexity: O(n) time and O(1) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: initialize state from valid data rather than arbitrary sentinels.
"""


def min_max(numbers: list[int]) -> tuple[int, int]:

    if not numbers:
        raise ValueError("numbers cannot be empty")

    min_number = numbers[0]
    max_number = numbers[0]

    for index in range(1, len(numbers)):
        number = numbers[index]

        if number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number

    return min_number, max_number


# Worst-case time is O(n) because the loop examines every item once.
# Auxiliary space is O(1) because the function stores only the current
# minimum and maximum, regardless of the input size.