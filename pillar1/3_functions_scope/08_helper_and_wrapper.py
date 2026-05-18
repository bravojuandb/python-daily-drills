"""
Challenge 01 - Helper and Wrapper

Write two functions:
    normalize_name(name: str) -> str
    build_username(name: str) -> str

Requirements:
1. `normalize_name()` must be pure.
2. `normalize_name()` should strip spaces, collapse repeated spaces, and lowercase the text.
3. `build_username()` should call `normalize_name()`.
4. `build_username()` should replace spaces with underscores.
5. If the normalized name is empty, `build_username()` should return `"anonymous"`.

Example:
>>> build_username("  Ada   Lovelace ")
'ada_lovelace'
>>> build_username("   ")
'anonymous'

Thinking goal:
This challenge is about splitting one small job into a reusable helper and a thin wrapper.
"""
