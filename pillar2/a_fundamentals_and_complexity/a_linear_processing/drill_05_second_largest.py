"""
Drill 05 - Second Largest Distinct Value

Goal: extend single-candidate selection to two related candidates.
Prerequisites: Drills 03-04, comparisons, and None for an absent candidate.

Contract:
- Given an integer list, return the greatest value strictly below its maximum.
- Duplicates do not create another rank.
- Return None if there are fewer than two distinct values: this includes
  empty lists, one-element lists, and lists whose values are all equal.
- Do not modify the input. The shared rules in README.md apply.

Examples:
second_largest([7, 2, 7, 5]) -> 5
second_largest([-5, -2, -8, -2]) -> -5
second_largest([4, 4]) -> None

Technique: one explicit for loop and at most two candidate variables, plus
its loop variable. Maintain candidates directly; no sorting or repeated scans.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What must each candidate represent after a prefix, including when a new
maximum appears?
"""


def second_largest(numbers: list[int]) -> int | None:
    if not numbers:
        return None

    maior = None
    second_maior = None

    for current in numbers:
        if maior is None or current > maior:
            second_maior = maior
            maior = current
        elif current < maior and (second_maior is None or current > second_maior):
            second_maior = current

    return second_maior


# O(n) time: n is the input length, and each element is visited once.
# O(1) auxiliary space: only two candidates and the loop variable are stored.
