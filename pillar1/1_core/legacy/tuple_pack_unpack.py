"""
You are managing coordinates in a 2D grid.

1. Pack the x and y values (5, 9) into a tuple called `point`.
2. Unpack the tuple into variables x and y.
3. Return a string in the format: "X=5, Y=9" using f-strings.

⚡ Be quick — use tuple packing and unpacking directly, no indexing.
"""

point = (5, 9)

def unpacker(coordinates: tuple = (0, 0)) -> str:
    x, y = coordinates
    return f"X={x}, Y={y}"

print(unpacker(point))
