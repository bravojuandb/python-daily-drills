
"""
CHALLENGE PROPOSITION

Implement a function `sum_even_numbers(start: int, end: int) -> int` that returns the sum of all **even numbers**
between `start` and `end` (inclusive). 

Rules:

1. If `start > end`, return 0.
2. If either `start` or `end` is negative, raise a `ValueError` with the message: "Only non-negative integers allowed".
3. Your solution **must use a function** and should not rely on built-in `sum()` or list comprehensions.
4. Use a `while` or `for` loop to calculate the sum.
5. You may assume `start` and `end` are integers.

INPUT EXAMPLES:

    sum_even_numbers(2, 10)   → 30   # 2 + 4 + 6 + 8 + 10
    sum_even_numbers(3, 3)    → 0    # no even number
    sum_even_numbers(4, 4)    → 4
    sum_even_numbers(10, 2)   → 0    # invalid range

CONSTRAINTS:
    - Use a loop, not `sum()`.
    - Input validation is required.
    - Return 0 if range is invalid.

BONUS:
    - Try writing a second version that uses recursion instead of a loop.

"""

def sum_even_numbers(start: int, end: int) -> int:

    def is_even(num: int) -> bool:
        return num % 2 == 0
    
    if start > end:
        return 0
    if start < 0 or end < 0:
        raise ValueError ("Only non-negative integers allowed")
    
    result = 0
    for i in range(start, end+1):
        if is_even(i):
            result += i
    return result

print(sum_even_numbers(2, 10))