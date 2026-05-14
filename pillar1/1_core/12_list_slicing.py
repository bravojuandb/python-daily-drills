"""
Drill 12 - List Slicing

Write a function:
    slice_temperatures(values: list[int]) -> tuple[list[int], list[int], list[int]]

Requirements:
1. Return a tuple with:
   - every second value starting from the first
   - the last two values
   - the list reversed, taking every second value
2. Use slicing only.
3. Do not use loops.

Example:
>>> slice_temperatures([15, 17, 20, 22, 18, 19, 21, 23])
([15, 20, 18, 21], [21, 23], [23, 19, 22, 17])

Thinking goal:
This drill strengthens your ability to read and write slice expressions without trial and error.
"""

def slice_temperatures(
        values: list[int]) -> tuple[list[int], list[int], list[int]]:
    every_second = values[::2]
    last_two = values[-2:]
    reversed_vals = values[::-2]

    return every_second, last_two, reversed_vals


if __name__ == "__main__":
    print(slice_temperatures([15, 17, 20, 22, 18, 19, 21, 23]))