"""
Challenge 01 - Enclosing Scope

Write a function:
    make_prefixer(prefix: str)

Inside it, write and return an inner function:
    add_prefix(text: str) -> str

Requirements:
1. `make_prefixer()` must return the inner `add_prefix()` function.
2. `add_prefix()` must return `"{prefix}: {text}"`.
3. `add_prefix()` must read `prefix` from the enclosing function scope.
4. Strip leading and trailing spaces from `text` before using it.
5. If the stripped text is empty, use `"Untitled"`.

Example:
>>> label_error = make_prefixer("ERROR")
>>> label_error("  file missing ")
'ERROR: file missing'
>>> label_error("   ")
'ERROR: Untitled'

Thinking goal:
This challenge is about an inner function remembering a name from its enclosing scope.
"""
