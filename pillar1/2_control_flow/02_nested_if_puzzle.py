"""
Drill 02 - Nested If Puzzle

Write a function:
    classify_number(n: int) -> str

Requirements:
1. If `n` is `0`, return `"Zero"`.
2. If `n` is positive:
   - return `"Positive Even"` if it is even
   - return `"Positive Odd"` if it is odd
3. If `n` is negative:
   - return `"Negative Large"` if `abs(n) > 10`
   - return `"Negative Ten"` if `abs(n) == 10`
   - return `"Negative Small"` otherwise
4. You must use nested `if` statements.

Example:
>>> classify_number(-12)
'Negative Large'
>>> classify_number(-10)
'Negative Ten'

Thinking goal:
This drill is about handling one decision inside another while keeping boundary cases straight.
"""
