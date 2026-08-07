"""
Drill 01 - Linear Search

Write linear_search(items, target) -> int. Return the index of the first matching
integer or -1 when absent. Do not use `in`, `.index()`, or sorting.

Examples: linear_search([8, 3, 8], 8) returns 0; searching for 2 returns -1.
Target complexity: O(n) time and O(1) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: define exactly what a search returns when duplicates exist.
"""


def linear_search(items: list[int], target: int) -> int:
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

# Time: O(n) in the worst case because every element may need to be examined.
# Space: O(1) because the algorithm uses only a constant amount of extra memory.
# enumerate() does not create a copy of the list, so the auxiliary space remains constant.

