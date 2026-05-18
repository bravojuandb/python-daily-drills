"""
Drill 06 - Validation Entrypoint

Write:
    class InvalidScoreError(Exception): ...

Then write a function:
    grade_label(score: int) -> str

Requirements:
1. If `score` is below `0` or above `100`, raise `InvalidScoreError`.
2. Return `"pass"` if `score >= 60`.
3. Return `"fail"` otherwise.
4. Keep validation separate from the grading rule in your reasoning.

Example:
>>> grade_label(75)
'pass'
>>> grade_label(20)
'fail'
>>> grade_label(120)
raises InvalidScoreError

Thinking goal:
This drill is about validating the domain first so the normal logic can stay simple.
"""
