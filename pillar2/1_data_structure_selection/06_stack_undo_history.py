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
        pass

    def record(self, action: str) -> None:
        pass

    def undo(self) -> str | None:
        pass

    def peek(self) -> str | None:
        pass

    def is_empty(self) -> bool:
        pass
