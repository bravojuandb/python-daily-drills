"""
Drill 06 - Fix an UnboundLocalError

You are given this broken function:

    counter = 0

    def broken_increment() -> int:
        counter += 1
        return counter

Write:
    counter = 0

Then write one function:
    increment() -> int

Requirements:
1. `increment()` must increase the global `counter` by `1`.
2. `increment()` must return the new value.
3. Use the `global` keyword intentionally.
4. Add a short comment explaining why the broken version raises `UnboundLocalError`.

Example:
>>> increment()
1
>>> increment()
2

Thinking goal:
This drill is about Python's rule that assigning to a name inside a function makes it local
unless you explicitly declare otherwise.
"""
