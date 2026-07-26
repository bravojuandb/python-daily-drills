"""
Drill 01 - Classify Growth Rates

For each function below, write its worst-case time and auxiliary-space complexity
as comments: scan a list; binary search; copy a list; nested pair comparison;
build a set; sort a list. Use O(1), O(log n), O(n), O(n log n), or O(n²).

Then write one sentence explaining which operation dominates each result.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: derive complexity from executed work, not from function names.
"""


def scan(items: list[int], target: int) -> bool:
    return any(item == target for item in items)


def copy_items(items: list[int]) -> list[int]:
    return items[:]


def compare_pairs(items: list[int]) -> int:
    return sum(1 for left in items for right in items if left == right)


def ordered(items: list[int]) -> list[int]:
    return sorted(items)


# Write your complexity analysis below.
