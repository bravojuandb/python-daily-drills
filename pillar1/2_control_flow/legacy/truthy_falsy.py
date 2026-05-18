"""
Truthy/Falsy Drill ⚡

Write a function that takes a value and returns:
- "truthy" if the value evaluates to True
- "falsy" if the value evaluates to False

Hint: Use bool() or Python’s implicit truthiness.

Examples:
check(0)        → "falsy"
check("")       → "falsy"
check([1, 2])   → "truthy"
check("hello")  → "truthy"
check([])       → "falsy"
"""

def check(value) -> str:
    return "truthy" if value else "falsy"

assert check(0) == "falsy"
assert check("") == "falsy"
assert check([1, 2]) == "truthy"
assert check("hello") == "truthy"
assert check([]) == "falsy"