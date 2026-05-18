"""
Drill 01 - If/Else Classifier

Write a function:
    classify_temperature(temp: int) -> str

Requirements:
1. Return `"Freezing"` if `temp` is below `0`.
2. Return `"Cold"` if `temp` is from `0` to `15` inclusive.
3. Return `"Mild"` if `temp` is from `16` to `25` inclusive.
4. Return `"Hot"` if `temp` is above `25`.
5. Return `"Perfect"` if `temp` is exactly `21`.
6. Use `if` / `elif` / `else`.
7. Make sure the exact-match case does not get swallowed by a wider range.

Example:
>>> classify_temperature(20)
'Mild'
>>> classify_temperature(21)
'Perfect'

Thinking goal:
This drill is about ordering conditions carefully when one special case overlaps a broader range.
"""
