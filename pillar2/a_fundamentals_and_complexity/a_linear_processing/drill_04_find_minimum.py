"""
Drill 04 - Find the First Minimum's Position

Goal: extend Drill 03's candidate selection to track a position and handle ties.
Prerequisites: Drill 03, zero-based indexing, and None for an absent result.

Contract:
- Given an integer list, return the zero-based index of its smallest value.
- If the minimum appears more than once, return its first occurrence's index.
- Return None for an empty list. A one-element list returns 0.
- Do not modify the input. The shared rules in README.md apply.

Examples:
find_minimum([8, 3, 6, 3]) -> 1
find_minimum([-7, -2, -5]) -> 0
find_minimum([]) -> None

Technique: track the position during one explicit for loop; range() and
enumerate() are allowed. Do not use min(), list.index(), or another drill.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What must your stored position represent after a nonempty prefix, including
when a value ties the smallest one already seen?
"""


def find_minimum(numbers: list[int]) -> int | None:
    if not numbers:
        return None

    min_so_far = numbers[0]
    index_minimum = 0

    for i in range(len(numbers)):
        if numbers[i] < min_so_far:
            min_so_far = numbers[i]
            index_minimum = i

    return index_minimum


# O(n) time: each of the n elements is compared with the current minimum once.
# O(1) auxiliary space: min_so_far, index_minimum, and i use fixed storage
# under the drill's integer-cost model; range() does not build a list of indices.
