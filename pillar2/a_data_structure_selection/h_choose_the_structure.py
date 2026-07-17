"""
Drill 08 - Choose the Structure

Write classify_requirements(order_matters, unique_only, keyed_lookup, fifo)
returning one of: "list", "set", "dict", or "deque".

Rules: fifo has highest priority, then keyed_lookup, then unique_only, otherwise
choose list. Raise ValueError if fifo and keyed_lookup are both True because the
requirements conflict for this simplified exercise.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: translate required operations into an explicit structure choice.
"""


def classify_requirements(
    *, order_matters: bool, unique_only: bool, keyed_lookup: bool, fifo: bool
) -> str:
    pass
