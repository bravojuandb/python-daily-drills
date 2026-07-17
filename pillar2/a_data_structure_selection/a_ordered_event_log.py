"""
Drill 01 - Ordered Event Log

Write append_event(events, event) -> list[str]. Return a new list containing the
existing events followed by event. Do not mutate the input.

Example: append_event(["login", "view"], "logout") returns
["login", "view", "logout"]. An empty input list is valid.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: choose a list when order and repeated values both matter.
"""


def append_event(events: list[str], event: str) -> list[str]:
    events_copy = events.copy()
    events_copy.append(event)
    return events_copy
    
# Worst case is .copy() which is O(n) time and O(n) extra space, since the copied list is n elemnts long.
# Main cost is copying the list, since it creates another list in memory.
# A list is the best choice because it keeps the order, and keeps duplicate values.
