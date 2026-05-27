"""
Challenge 03 - LEGB Name Lookup

You are modeling how Python searches for names.

Write:
    label = "global"

Then write one function:
    describe_lookup(prefix: str = "enclosing") -> tuple[str, str, str, int]

Requirements:
1. Use the `prefix` parameter as the enclosing-scope value for the inner function.
2. Inside `describe_lookup()`, create an inner function named `read_names()`.
3. Inside `read_names()`, create a local variable named `local_label` with the value `"local"`.
4. `read_names()` must return `(local_label, prefix, label, len("abc"))`.
5. `describe_lookup()` must return the result of calling `read_names()`.
6. Do not shadow the built-in name `len`.

Example:
>>> describe_lookup()
('local', 'enclosing', 'global', 3)
>>> describe_lookup("custom")
('local', 'custom', 'global', 3)

Thinking goal:
This challenge is about tracing Local, Enclosing, Global, and Built-in name lookup in a small example.
"""
