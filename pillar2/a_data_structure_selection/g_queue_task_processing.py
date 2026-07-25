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
        self.tasks = deque()

    def enqueue(self, task: str) -> None:
        if not isinstance(task, str):
            raise TypeError("task must be a string")
        if not task.strip():
            raise ValueError("task must not be empty")

        self.tasks.append(task)

    def dequeue(self) -> str | None:
        if not self.tasks:
            return None
        
        return self.tasks.popleft()

    def peek(self) -> str | None:
        if not self.tasks:
            return None
        
        return self.tasks[0]

    def size(self) -> int:
        return len(self.tasks)


# Worst-case time: O(1) for enqueue(), dequeue(), peek() and size()
# Worst-case extra space: O(n) for storing n tasks
# collections.deque() fits FIFO processing because append() and popleft()
# operate at opposite ends in O(1) time.