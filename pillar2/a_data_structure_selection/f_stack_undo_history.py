"""
Drill 06 - Stack Undo History

Implement UndoHistory with record(action), undo(), peek(), and is_empty(). Store
actions in a list. undo and peek return None when empty. undo must remove the
most recently recorded action.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: recognize last-in, first-out behavior and protect underflow.
"""

from __future__ import annotations


class UndoHistory:
    def __init__(self) -> None:
        self.records = []

    def record(self, action: str) -> None:
        if not isinstance(action, str):
            raise TypeError("action must be a string")
        if not action.strip():
            raise ValueError("action cannot be empty")

        self.records.append(action)

    def undo(self) -> str | None:
        if self.records == []:
            return None
        return self.records.pop()

    def peek(self) -> str | None:
        if self.records == []:
            return None
        return self.records[-1]

    def is_empty(self) -> bool:
        return self.records == []


# Worst-case time: O(1) for each method, but record() is amortized O(1) and worst-case O(n).
# Worst-case extra space: O(n) where n is the number of recorded actions
# The main cost in terms of space comes from storing all recoreded actions
# A list fits this problem because it efficiently implements LIFO beheviour
