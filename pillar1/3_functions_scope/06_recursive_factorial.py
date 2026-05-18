"""
Drill 06 - Recursive Factorial

Write a function:
    factorial(n: int) -> int

Requirements:
1. Use recursion only.
2. If `n` is `0` or `1`, return `1`.
3. Otherwise, return `n * factorial(n - 1)`.
4. If `n` is negative, raise `ValueError`.

Example:
>>> factorial(5)
120
>>> factorial(0)
1

Thinking goal:
This drill is about pairing a recursive pattern with one explicit invalid-input rule.
"""
