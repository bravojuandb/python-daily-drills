"""
Drill 04 - Loop with Enumerate

Write a function:
    label_long_fruits(fruits: list[str]) -> list[str]

Requirements:
1. Use `enumerate()` in a `for` loop.
2. Number the fruits starting at `1`.
3. Include only fruit names whose length is at least `6`.
4. Return strings like `"2: banana"`, where the number is the original position.

Example:
>>> label_long_fruits(["apple", "banana", "fig", "cherry"])
['2: banana', '4: cherry']

Thinking goal:
This drill is about separating an item's position from whether it passes a filter.
"""
