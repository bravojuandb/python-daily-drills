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

def classify_number(n: int) -> str:
    if n == 0:
        return "Zero"
    elif n > 0:
        if n % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    else:
        if abs(n) > 10:
            return "Negative Large"
        elif abs(n) == 10:
            return "Negative Ten"
        else:
            return "Negative Small"


if __name__ == "__main__":
    numbers = [-12, 10, -10, 49, -49]
    for num in numbers:
        print(num, classify_number(num))