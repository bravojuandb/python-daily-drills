"""
Drill 03 - Find Maximum

Goal: maintain a candidate, updating it only when a value improves it.
Prerequisites: Drills 01-02, comparisons, and None for an absent result.

Contract:
- Given an integer list, return its greatest value, not its index.
- Return None for an empty list. A one-element list returns that element.
- Repeated maxima and all-negative lists are valid.
- Do not modify the input. The shared rules in README.md apply.

Examples:
find_maximum([3, 9, 2, 9]) -> 9
find_maximum([-7, -2, -5]) -> -2
find_maximum([]) -> None

Technique: one explicit for loop and a candidate variable. Select the
candidate yourself; do not use max() or sorting.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What must the candidate represent after a nonempty prefix, and how does your
initialization handle an all-negative list?
"""


def find_maximum(numbers: list[int]) -> int | None:
    raise NotImplementedError("Implement this drill.")
