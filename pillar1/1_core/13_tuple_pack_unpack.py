"""
Drill 13 - Tuple Pack and Unpack

Write a function:
    format_point(x: int, y: int) -> tuple[tuple[int, int], str]

Requirements:
1. Pack `x` and `y` into a tuple called `point`.
2. Unpack that tuple into variables.
3. Return:
   - the tuple itself
   - a formatted string like `"X=5, Y=9"`

Example:
>>> format_point(5, 9)
((5, 9), "X=5, Y=9")

Thinking goal:
The point of this drill is to make tuple packing and unpacking feel deliberate, not decorative.
"""


def format_point(x: int, y: int) -> tuple[tuple[int, int], str]:
    # pack values
    point = x, y
 
    # unpack tuple into variables
    unpacked_x, unpacked_y = point

    return point, f"X={unpacked_x}, Y={unpacked_y}"

if __name__ == "__main__":
    print(format_point(5, 9))