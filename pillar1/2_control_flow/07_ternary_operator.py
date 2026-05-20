"""
Drill 07 - Ternary Operator

Write a function:
    movement_label(change: int) -> str

Requirements:
1. Return `"down"` if the value is below `0`.
2. Return `"flat"` if the value is exactly `0`.
3. Return `"up"` otherwise.
4. Use only nested ternary expressions.

Example:
>>> movement_label(7)
'up'
>>> movement_label(0)
'flat'

Thinking goal:
This drill is about writing a compact three-way decision without falling back to a full `if` block.
"""
