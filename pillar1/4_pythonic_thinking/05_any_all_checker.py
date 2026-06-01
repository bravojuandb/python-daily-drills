"""
Drill 05 - Any and All Checker

Write a function:
    review_scores(scores: list[int]) -> tuple[bool, bool]

Requirements:
1. Use `any()` with a generator expression to check whether any score is below `50`.
2. Use `all()` with a generator expression to check whether all scores are at most `100`.
3. Return the results as `(has_failing_score, all_valid)`.

Example:
>>> review_scores([72, 88, 49, 100])
(True, True)

Thinking goal:
This drill is about asking direct yes-or-no questions without building extra lists.
"""
