"""
Drill 01 - Basic Try/Except

Write a function:
    safe_divide(a: int, b: int) -> float | str

Requirements:
1. Use `try` / `except`.
2. Return the result of `a / b` if division works.
3. If division by zero occurs, return `"Error: Division by zero"`.
4. Catch only the error this drill is about.

Example:
>>> safe_divide(10, 2)
5.0
>>> safe_divide(7, 0)
'Error: Division by zero'

Thinking goal:
This drill is about catching one specific failure without hiding unrelated mistakes.
"""


def safe_divide(a: int, b: int) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    

if __name__ == "__main__":
    print(safe_divide(19, 2))
    print(safe_divide(10, 0))