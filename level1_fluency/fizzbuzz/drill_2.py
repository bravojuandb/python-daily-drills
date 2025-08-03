"""
Problem: Basic FizzBuzz (Easy–Medium)

Write a function `fizzbuzz_range(start: int, end: int) -> List[str]` 
that returns a list of strings representing the numbers 
from `start` to `end` (inclusive), with the following rules:

- For multiples of 3, insert "Fizz" instead of the number.
- For multiples of 5, insert "Buzz" instead of the number.
- For numbers which are multiples of both 3 and 5, insert "FizzBuzz".
- For all other numbers, insert the number itself as a string.

Examples:
>>> fizzbuzz_range(1, 5)
['1', '2', 'Fizz', '4', 'Buzz']

>>> fizzbuzz_range(14, 16)
['14', 'FizzBuzz', '16']

Requirements:
- Use conditionals (if / elif / else) effectively.
- Handle edge cases where `start > end` by returning an empty list.
"""

def fizzbuzz_range(start: int, end: int) -> list[str]:
    if start > end:
        return []

    def mult_3(n: int) -> bool:
        return n % 3 == 0

    def mult_5(n: int) -> bool:
        return n % 5 == 0

    result = []

    for num in range(start, end + 1):
        if mult_3(num) and mult_5(num):
            result.append('FizzBuzz')
        elif mult_3(num):
            result.append('Fizz')
        elif mult_5(num):
            result.append('Buzz')
        else:
            result.append(str(num))
    return result


print(fizzbuzz_range(1,5))