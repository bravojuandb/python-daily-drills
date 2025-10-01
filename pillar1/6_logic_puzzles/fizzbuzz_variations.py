"""
Write a function fizzbuzz_variation(n: int) -> list[str]:

Rules:
- For numbers from 1 to n:
    * If divisible by 3 → "Fizz"
    * If divisible by 5 → "Buzz"
    * If divisible by 7 → "Bazz"
    * If divisible by 3 and 5 → "FizzBuzz"
    * If divisible by 3 and 7 → "FizzBazz"
    * If divisible by 5 and 7 → "BuzzBazz"
    * If divisible by 3, 5, and 7 → "FizzBuzzBazz"
    * Otherwise, return the number as a string.

Example:
n = 21 → 
["1", "2", "Fizz", "4", "Buzz", "Fizz", "Bazz", "8", "Fizz", "Buzz",
 "11", "Fizz", "13", "Bazz", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
 "FizzBazz"]

Your task: implement this as fast as you can!
"""


def fizzbuzz_variations(n: int) -> list[str]:

    result = []
    for num in range(1, n+1):
        word = ""
        if num % 3 == 0:
            word += "Fizz"
        if num % 5 == 0:
            word += "Buzz"
        if num % 7 == 0:
            word += "Bazz"
        result.append(word if word else str(num))
    return result


print(fizzbuzz_variations(15))