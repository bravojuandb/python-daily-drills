"""
Drill 03 - Loop Counting with Range

Write a function:
    sum_even_squares(n: int) -> int

Requirements:
1. Use a `for` loop with `range()`.
2. Consider the numbers from `1` to `n` inclusive.
3. Add the square of a number only if the number itself is even.
4. Return the final total.
5. Do not use `sum()` on a comprehension.

Example:
>>> sum_even_squares(6)
56

Thinking goal:
This drill is about tracing a loop and deciding which values should affect the accumulator.
"""


def sum_even_squares(n: int) -> int:
    result = 0
    for i in range(2, n+1, 2):
        result += i * i
    return result

if __name__ == "__main__":
    print(sum_even_squares(6))