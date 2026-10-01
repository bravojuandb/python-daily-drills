"""
Drill 06 - Longest Streak

Goal: maintain a current run and a best length, adding state that resets.
Prerequisites: Drill 01's counting and Drills 03-05's candidate updates.

Contract:
- Given an integer list and an integer target, return the length of the
  longest run of adjacent elements equal to target in the original order.
- A nonmatch breaks a run. A single matching element has length 1.
- Return 0 for an empty list or when target is absent.
- Do not modify the input. The shared rules in README.md apply.

Examples:
longest_streak([2, 2, 9, 2, 2, 2], 2) -> 3
longest_streak([2, 9, 2, 9, 2], 2) -> 1
longest_streak([], 2) -> 0

Technique: one explicit for loop and two counters, for the current and longest
streaks. Make continuation, reset, and best-length updates explicit.

Complexity check:
For n elements, target O(n) time and O(1) auxiliary space. Justify both.

Thinking goal:
What does each counter represent after a prefix, and why does your approach
also include a streak ending at the last element?
"""


def longest_streak(numbers: list[int], target: int) -> int:
    raise NotImplementedError("Implement this drill.")
