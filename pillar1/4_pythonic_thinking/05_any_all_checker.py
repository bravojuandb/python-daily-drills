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

def check_numbers(nums: list[int]) -> tuple[bool, bool]:
    has_negative = any(num < 0 for num in nums)
    all_even = all(num % 2 == 0 for num in nums)
    return has_negative, all_even

if __name__ == "__main__":
    nums = [2, 4, -6, 8, 10]
    print(check_numbers(nums))
