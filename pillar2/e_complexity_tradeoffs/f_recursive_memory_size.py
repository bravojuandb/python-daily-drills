"""
Drill 06 - Shallow versus Recursive Memory

Write deep_size(value) -> int using sys.getsizeof. Recursively include contents
of dicts, lists, tuples, sets, and frozensets. Track object IDs so shared objects
and cycles are counted once. Strings and bytes are terminal values.

Compare deep_size with sys.getsizeof on a nested example.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: container size alone does not measure the entire object graph.
"""


def deep_size(value: object) -> int:
    pass
