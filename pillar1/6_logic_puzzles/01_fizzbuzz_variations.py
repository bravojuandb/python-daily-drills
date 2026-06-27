"""
Drill 01 - FizzBuzz Variations

Write a function:
    fizzbuzz_variation(n: int) -> list[str]

Rules:
1. For every number from `1` through `n`, apply all matching labels:
   - divisible by `3` adds `"Fizz"`
   - divisible by `5` adds `"Buzz"`
   - divisible by `7` adds `"Bazz"`
2. When several rules match, combine the labels in 3, 5, 7 order.
   Examples: `15 -> "FizzBuzz"`, `21 -> "FizzBazz"`,
   `35 -> "BuzzBazz"`, `105 -> "FizzBuzzBazz"`.
3. If no rule matches, use the number as a string.
4. If `n < 1`, return an empty list.

Example:
>>> fizzbuzz_variation(21)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Bazz', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', 'Bazz', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'FizzBazz']

Challenge bar:
- Do not hard-code special cases for combined numbers.
- The same logic should still work if another divisor/label pair were added.

Thinking goal:
This drill is about accumulating all matching rules for one value before deciding what to append.
"""


def fizzbuzz_variation(n: int) -> list[str]:

    result = []

    if n < 1:
        return result

    for num in range(1,n + 1):
        word = ""
        if num % 3 == 0:
            word += "Fizz"
        if num % 5 == 0:
            word += "Buzz"
        if num % 7 == 0:
            word += "Bazz"
        result.append(word if word else str(num))

    return result

if __name__ == "__main__":
    print(fizzbuzz_variation(30))
