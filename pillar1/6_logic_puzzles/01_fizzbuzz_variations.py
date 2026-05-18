"""
Drill 01 - FizzBuzz Variations

Write a function:
    fizzbuzz_variation(n: int) -> list[str]

Rules:
1. For numbers from `1` to `n`:
   - if divisible by `3`, include `"Fizz"`
   - if divisible by `5`, include `"Buzz"`
   - if divisible by `7`, include `"Bazz"`
2. If more than one rule matches, combine the words in that order.
3. If no rule matches, use the number as a string.

Example:
>>> fizzbuzz_variation(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Bazz', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', 'Bazz', 'FizzBuzz']

Thinking goal:
This drill is about building one answer from overlapping rules instead of writing a fragile chain of special cases.
"""
