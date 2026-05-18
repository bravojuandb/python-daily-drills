"""
Write a function `print_fruits(fruits: list[str]) -> None`.

Rules:
- Use `enumerate()` inside a `for` loop.
- For each fruit, print its position (starting at 1) and its name.

Example:
fruits = ["apple", "banana", "cherry"]
Output:
1: apple
2: banana
3: cherry

Can you write it correctly in under 60 seconds?
"""

def print_fruits(fruits: list[str]) -> None:

    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}: {fruit}")
    

fruits = ["apple", "banana", "cherry"]
print_fruits(fruits)