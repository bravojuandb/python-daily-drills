"""
Drill 05 - Prime Number Tester

Write a function:
    is_prime(n: int) -> bool

Requirements:
1. Numbers less than `2` are not prime.
2. Use a loop and `%` to test divisibility.
3. Return `False` as soon as you find a divisor.
4. Do not test divisors larger than the square root of `n`.
5. Handle `2` correctly even though it is the only even prime.

Example:
>>> is_prime(2)
True
>>> is_prime(17)
True
>>> is_prime(18)
False
>>> is_prime(1)
False
>>> is_prime(49)
False

Challenge bar:
- Skip unnecessary work after handling small and even numbers.
- The function should still be easy to trace for `n = 2`, `n = 3`, and `n = 4`.

Thinking goal:
This drill is about shrinking the search space without losing the edge cases.
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True

if __name__ == "__main__":

    print(is_prime(49))

