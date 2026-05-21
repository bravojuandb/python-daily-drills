"""
Drill 07 - Ternary Operator

Write a function:
    movement_label(change: int) -> str

Requirements:
1. Return `"down"` if the value is below `0`.
2. Return `"flat"` if the value is exactly `0`.
3. Return `"up"` otherwise.
4. Use only nested ternary expressions.

Example:
>>> movement_label(7)
'up'
>>> movement_label(0)
'flat'

Thinking goal:
This drill is about writing a compact three-way decision without falling back to a full `if` block.
"""

import random

def movement_label(change: int) -> str:
    return "flat" if change == 0 else "up" if change > 0 else "down"

if __name__ == "__main__":

    values = [random.randint(-30, 30) for _ in range(10)]

    print([(value, movement_label(value)) for value in values])