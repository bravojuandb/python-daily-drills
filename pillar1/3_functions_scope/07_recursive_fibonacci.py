"""
Drill 07 - Recursive Fibonacci

Write a function:
    fibonacci(n: int) -> int

Requirements:
1. Use recursion only.
2. Return `0` if `n == 0`.
3. Return `1` if `n == 1`.
4. Otherwise, return `fibonacci(n - 1) + fibonacci(n - 2)`.
5. If `n` is negative, raise `ValueError`.

Example:
>>> fibonacci(7)
13
>>> fibonacci(1)
1

Thinking goal:
This drill is about tracing two recursive branches while still respecting a clear boundary case.
"""
