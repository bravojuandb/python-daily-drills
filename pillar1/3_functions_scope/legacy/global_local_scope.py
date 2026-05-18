"""
You are asked to simulate a simple counter with global and local scope.

Rules:
1. Create a global variable `counter` starting at 0.
2. Write a function `increment()` that:
   - Uses the global `counter`
   - Increases it by 1 each time it’s called
   - Returns the new value
3. Write another function `shadow_increment()` that:
   - Creates a **local variable** also called `counter`
   - Starts it at 100
   - Increases it by 1 and returns it
   - Does NOT affect the global `counter`

Example expected behavior:
counter = 0
print(increment())        → 1
print(increment())        → 2
print(shadow_increment()) → 101
print(counter)            → 2   (still global counter, unchanged by shadow_increment)

⚡ Be fast — solve this under 2 minutes and watch out for the `global` keyword vs shadowing!
"""

counter = 0

def increment():
    global counter
    counter += 1
    return counter

def shadow_increment():
    counter = 100
    return counter + 1

print(counter)
print(increment())
print(increment())
print(shadow_increment())
print(counter)