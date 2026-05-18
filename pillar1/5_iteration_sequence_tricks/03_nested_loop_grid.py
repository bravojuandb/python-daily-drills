"""
Drill 03 - Nested Loop Grid

Write a function:
    build_grid(rows: int, cols: int) -> list[str]

Requirements:
1. Return a list of exactly `rows` strings.
2. Each string must have length `cols`.
3. Use two nested `for` loops to build the grid character by character.
4. Border cells must be `"#"`.
5. Inner cells must form a checkerboard:
   - use `"A"` when `(row + col)` is even
   - use `"B"` when `(row + col)` is odd

Example:
>>> build_grid(4, 7)
['#######', '#ABABA#', '#BABAB#', '#######']

Thinking goal:
This drill is about keeping track of two dimensions and one repeating pattern at the same time.
"""
