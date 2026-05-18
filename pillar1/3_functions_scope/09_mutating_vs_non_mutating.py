"""
Challenge 02 - Mutating vs Non-Mutating

Write two functions:
    add_tag_in_place(tags: list[str], new_tag: str) -> None
    add_tag_copy(tags: list[str], new_tag: str) -> list[str]

Requirements:
1. `add_tag_in_place()` must mutate the original list by appending `new_tag`.
2. `add_tag_copy()` must return a new list with `new_tag` added.
3. `add_tag_copy()` must not mutate the original input list.
4. If `new_tag` is already present, neither function should add it again.

Example:
>>> tags = ["python"]
>>> add_tag_copy(tags, "loops")
['python', 'loops']
>>> tags
['python']

Thinking goal:
This challenge is about making mutation decisions explicit instead of accidental.
"""
