"""
Drill 07 - Avoid Global State

Write a function:
    increment_counter(current: int) -> int

Requirements:
1. Return `current + 1`.
2. Do not read or write any global variables.
3. If `current` is negative, raise `ValueError`.
4. The function must be pure: the same input should always produce the same output.

Example:
>>> increment_counter(0)
1
>>> increment_counter(10)
11

Thinking goal:
This drill is about replacing hidden global state with explicit input and output.
"""


def increment_counter(current: int) -> int:
    if current < 0:
        raise ValueError("current must not be negative")
    return current + 1
    
if __name__ == "__main__":

    for _ in range(5):
        print(increment_counter(1))

# key idea: state goes in, new state comes out