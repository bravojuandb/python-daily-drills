"""
Drill 04 - Find Minimum

Goal: transfer Drill 03's candidate selection to the opposite ordering.
Prerequisites: Drill 03, comparisons, and None for an absent result.

Contract:
- Given an integer list, return its smallest value, not its index.
- Return None for an empty list. A one-element list returns that element.
- Repeated minima, all-positive lists, and all-negative lists are valid.
- Do not modify the input. The shared rules in README.md apply.

Examples:
find_minimum([8, 3, 6, 3]) -> 3
find_minimum([-7, -2, -5]) -> -7
find_minimum([]) -> None

Technique: one explicit for loop and a candidate variable. Select the
candidate yourself; do not use min() or call the maximum drill.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What does the candidate represent after a nonempty prefix, and which
comparison changes from Drill 03?
"""


def find_minimum(numbers: list[int]) -> int | None:
    raise NotImplementedError("Implement this drill.")
