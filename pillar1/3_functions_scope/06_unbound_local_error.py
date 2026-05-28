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

counter = 0

def increment() -> int:
    """
    Intentionally increment by 1 the global variable counter. 
    """
    global counter
    counter += 1
    return counter

# The broken version raises UnboundLocalError because assigning to counter
# inside the function makes Python treat counter as local unless global is used.

if __name__ == "__main__":
    print(increment())
    print(increment())