"""
Challenge 03 - Recursive Entrypoint

Write two functions:
    factorial_checked(n: int) -> int
    factorial_recursive(n: int) -> int

Requirements:
1. `factorial_checked()` should validate the input.
2. If `n` is negative, `factorial_checked()` must raise `ValueError`.
3. Otherwise, `factorial_checked()` should call `factorial_recursive(n)`.
4. `factorial_recursive()` should use recursion only.
5. `factorial_recursive()` should handle the base cases for `0` and `1`.

Example:
>>> factorial_checked(4)
24

Thinking goal:
This challenge is about separating validation from recursion so each function has one clear job.
"""
