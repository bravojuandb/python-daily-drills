"""
Drill 02 - Running Total

Goal: accumulate each value's amount, extending Drill 01's count updates.
Prerequisites: Drill 01 and integer addition.

Contract:
- Given an integer list, return one integer: the sum of all its elements.
  Include repeated values; return only the final total.
- Return 0 for an empty list.
- Do not modify the input. The shared rules in README.md apply.

Examples:
running_total([4, 4]) -> 8
running_total([7, -4, 0, -1]) -> 2
running_total([]) -> 0

Technique: one explicit for loop and an accumulator; perform the additions
in your loop rather than using sum().

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What must the accumulator represent after processing any prefix of the list?
"""


def running_total(numbers: list[int]) -> int:
    raise NotImplementedError("Implement this drill.")
