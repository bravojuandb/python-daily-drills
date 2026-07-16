"""
Drill 05 - Prefix-Sum Range Queries

Write range_sums(numbers, queries) -> list[int]. Each inclusive query is
(start, end). Build one prefix-sum array, then answer every query without
resumming its slice. Raise IndexError for invalid bounds.

Example: [2, 4, 1], queries [(0, 1), (1, 2)] returns [6, 5].
Target complexity: O(n + q) time and O(n) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: preprocess once to make repeated range work constant-time.
"""


def range_sums(
    numbers: list[int], queries: list[tuple[int, int]]
) -> list[int]:
    pass
