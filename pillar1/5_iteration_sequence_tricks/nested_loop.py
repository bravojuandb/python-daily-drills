"""
Nested Loop Grid Builder — GO FAST ⚡

Write a function `build_grid(rows: int, cols: int) -> list[str]`.

Rules:
- Return a list of exactly `rows` strings, each string length exactly `cols`.
- Use two nested `for` loops (row, col) to construct the grid **character by character**.
- Border cells (top row, bottom row, leftmost col, rightmost col) must be '#'.
- Inner cells form a checkerboard that starts with 'A' at position (1,1):
    - If (row + col) is even -> 'A'
    - If (row + col) is odd  -> 'B'

Example:
rows = 4, cols = 7
build_grid(4, 7) ->
[
  "#######",
  "#ABABA#",
  "#BABAB#",
  "#######",
]

Solve it quickly — under 3 minutes!
"""

def build_grid(rows: int, cols: int) -> list[str]:
    result = []
    for r in range(rows):
        row = ""
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                row += "#"
            else:
                if (r + c) % 2 == 0:
                    row += "A"
                else:
                    row += "B"
        result.append(row)
    return result

print(build_grid(4, 7))



# Starter version
def simple_grid(rows: int, cols: int) -> list[str]:
    result = []
    for r in range(rows):
        row = ""
        for c in range(cols):
            row += "#"
        result.append(row)
    return result

print("\n".join(simple_grid(3, 5)))