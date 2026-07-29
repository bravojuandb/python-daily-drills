"""
Drill 04 - Count Frequencies

Write count_frequencies(items) -> dict[str, int] manually using a dictionary.
Preserve the order in which distinct strings first appear. Empty input returns
an empty dictionary. Process the list once.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: counting is dictionary accumulation with a zero default.
"""


def count_frequencies(items: list[str]) -> dict[str, int]:
    result = {}

    for item in items:
        result[item] = result.get(item, 0) + 1

    return result


# Time: O(n), because each item is processed once. O(1) inside the loop * n times
# Extra space: O(k), where k is the number of distinct items.
# Updating an existing key requires no additional dictionary entry O(1),
# while each new key adds one entry O(n) being n the total number of items.
# A dictionary provides average O(1) lookup and update per item.