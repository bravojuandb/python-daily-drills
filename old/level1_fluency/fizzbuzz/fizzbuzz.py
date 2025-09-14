"""
Problem: FizzBuzz with a Twist (Medium)

Write a function `fizzbuzz_range(start: int, end: int) -> List[str]` 
that returns a list of strings representing the numbers from `start` to `end` (inclusive), 
but with the following rules:

- For multiples of 3, insert "Fizz" instead of the number.
- For multiples of 5, insert "Buzz" instead of the number.
- For numbers which are multiples of both 3 and 5, insert "FizzBuzz".
- For numbers that are **prime**, insert "Prime" instead of the number.
    (Note: Prime override has highest priority — do not show Fizz/Buzz for primes.)

Examples:
>>> fizzbuzz_range(1, 15)
['1', 'Prime', 'Fizz', '4', 'Buzz', 'Fizz', 'Prime', '8', 'Fizz', 'Buzz', 'Prime', 'Fizz', 'Prime', '14', 'FizzBuzz']

Requirements:
- Use a helper function `is_prime(n: int) -> bool` to detect primes.
- Handle edge cases where start > end (return an empty list).
- Do not use external libraries.
"""

def fizzbuzz_range(start: int, end: int) -> list[str]:

    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
    

    pass

