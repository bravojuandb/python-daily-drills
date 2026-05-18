"""
Write a function `sum_of_squares(n: int) -> int`.

Rules:
- Use a `for i in range()` loop.
- Compute and return the sum of the squares of numbers from 1 to n (inclusive).

Example:
sum_of_squares(5) → 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55

Can you code it in under 90 seconds?
"""

def sum_of_squares(n: int) -> int:
    return sum([ x**2 for x in range(1, n + 1)])

print(sum_of_squares(30))