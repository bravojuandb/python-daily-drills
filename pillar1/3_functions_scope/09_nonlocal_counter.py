"""
Challenge 02 - Nonlocal Counter

Write a function:
    make_counter(start: int = 0)

Inside it, write and return an inner function:
    increment() -> int

Requirements:
1. `make_counter()` must store the current count in a local variable named `count`.
2. `increment()` must increase `count` by `1`.
3. `increment()` must return the new value.
4. Use `nonlocal` intentionally.
5. Two counters created by `make_counter()` must not share state.

Example:
>>> counter_a = make_counter()
>>> counter_b = make_counter(10)
>>> counter_a()
1
>>> counter_a()
2
>>> counter_b()
11

Thinking goal:
This challenge is about modifying a variable from an enclosing function scope without using a global.
"""
