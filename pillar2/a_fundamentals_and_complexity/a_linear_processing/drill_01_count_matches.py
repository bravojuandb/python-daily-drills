"""
Drill 01 - Count Matches

Goal: connect loops and conditions to maintaining a count during traversal.
Prerequisites: functions, lists, for loops, comparisons, and variable updates.

Contract:
- Given an integer list and an integer target, return the number of elements
  equal to target. Count every occurrence.
- Return 0 for an empty list or when target is absent.
- Do not modify the input. The shared rules in README.md apply.

Examples:
count_matches([4, 2, 4, 7, 4], 4) -> 3
count_matches([-2, 0, -2], 9) -> 0
count_matches([], 4) -> 0

Technique: one explicit for loop and a counter, so each update is visible.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What must the counter represent after processing any prefix of the list?
"""


def count_matches(numbers: list[int], target: int) -> int:
    counter = 0

    for number in numbers:
        if number == target:
            counter += 1

    return counter


# O(n) time because time grows proportionally to the number of elements in the array.
# this means that the loop takes n steps for n elements in the array.

# O(1) auxiliary space because the size of the counter remains constant.
# the variable counter updates in every coincidence. 
# The algorithm does not accumulate more than one number.
