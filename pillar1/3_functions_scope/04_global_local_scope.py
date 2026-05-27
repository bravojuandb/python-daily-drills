"""
Drill 04 - Global and Local Scope

You are modeling a tiny visitor counter.

Write:
    counter = 0

Then write two functions:
    increment() -> int
    preview_increment() -> int

Requirements:
1. `increment()` must use the global `counter`, increase it by `1`, and return the new value.
2. `preview_increment()` must create a local variable also named `counter`, set it to `100`, increase it by `1`, and return it.
3. Calling `preview_increment()` must not change the global `counter`.
4. Add a short comment explaining why the two `counter` names do not refer to the same variable.

Example:
>>> counter = 0
>>> increment()
1
>>> preview_increment()
101
>>> counter
1

Thinking goal:
This drill is about noticing that identical names can still belong to different scopes.
One function changes module-level state; the other only changes its own local name.
"""
