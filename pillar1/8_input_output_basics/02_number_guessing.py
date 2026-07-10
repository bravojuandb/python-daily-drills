"""
Drill 02 - Number Guessing

Write a program:
    guess_number() -> None

Requirements:
1. Pick a secret number such as `7`.
2. Ask the user for a guess with `input()`.
3. Convert the guess with `int()`.
4. Print `"Correct!"` if the guess matches.
5. Print `"Too low!"` or `"Too high!"` otherwise.
6. Keep the first version simple; one guess is enough.

Example:
If the secret is `7` and the user types `5`, print:
Too low!

Thinking goal:
This drill is about connecting input, conversion, and comparison in one tiny interactive flow.
"""


def guess_number() -> None:
    secret_number = 7
    guess = int(input("Guess a number: "))

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct!")


if __name__ == "__main__":
    guess_number()