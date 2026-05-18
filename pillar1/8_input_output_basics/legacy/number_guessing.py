"""
Write a program `guess_number()` that:

1. Picks a secret number (e.g. 7).
2. Asks the user to guess with input("Guess a number: ").
3. Converts the guess to an integer with int().
4. If the guess is correct → print "Correct!".
5. If the guess is too low → print "Too low!".
6. If the guess is too high → print "Too high!".

⚡ Task:
- Implement the function.
- Test it by guessing wrong once, then correct.

Be quick! 🚀
"""
import random

def guess_number() -> str:
    secret_num = random.randint(0, 30)
    while True:
        try:
            number = int(input("Guess a number from 0 to 30: "))
        except ValueError:
            print(" Invalid input! Please enter a number.")
            continue

        if number < 0 or number > 30:
            print("Out of range! Must be between 0 and 30. Try again!")
            continue

        if number == secret_num:
            print(f"Correct! You just won {secret_num} Bitcoins!!!")
            break
        elif number < secret_num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


    return "Game over"

print(guess_number())