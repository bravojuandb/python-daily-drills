"""
Drill 07 - Queue Task Processing

Implement TaskQueue with enqueue(task), dequeue(), peek(), and size(). Use
collections.deque. dequeue and peek return None when empty. Tasks must leave in
the same order they entered.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: recognize first-in, first-out behavior and choose O(1) removal.
"""

from __future__ import annotations

from collections import deque


class TaskQueue:
    def __init__(self) -> None:
        pass

    def enqueue(self, task: str) -> None:
        pass

    def dequeue(self) -> str | None:
        pass

    def peek(self) -> str | None:
        pass

    def size(self) -> int:
        pass
