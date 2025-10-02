"""
Write a function `is_prime(n: int) -> bool` that checks if a number is prime.

Rules:
- Use a loop and the modulo operator `%` to test divisibility.
- Return True if `n` is prime, False otherwise.
- Handle edge cases: numbers less than 2 are not prime.

"A prime number 
is an integer greater than 1
that has no positive divisors 
other than 1 and itself."

Examples:
- is_prime(2) → True
- is_prime(17) → True
- is_prime(18) → False
- is_prime(1) → False
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
print(is_prime(17))