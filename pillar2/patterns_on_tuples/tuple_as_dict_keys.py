"""
Challenge: Tuple as Dictionary Keys (Coordinates and Pairs)

You are asked to build a small grid tracker for delivery checkpoints.  
Each checkpoint has **coordinates (x, y)** that must uniquely identify a location.

Since lists are unhashable, you must use **tuples as dictionary keys**.

Example:
    checkpoints = {
        (40.4168, -3.7038): "Madrid Center",
        (41.3874,  2.1686): "Barcelona Downtown",
    }

Write a function `add_checkpoint(map_: dict[tuple[float, float], str], coords: tuple[float, float], name: str) -> dict[tuple[float, float], str]`
that adds a new coordinate-name pair to the map.

Rules:
- Use tuples `(x, y)` as keys — no lists allowed.
- If the coordinate already exists, update the name.
- Demonstrate that using a **list as a key** raises a `TypeError`.
- Print all checkpoint names in sorted order by latitude (x).

⚡️ Be quick and precise: code the function, add two entries, 
and show what happens if you try to use a list `[40.0, -3.7]` as a key.
"""

def add_checkpoint(
    map_: dict[tuple[float, float], str],
    coords: tuple[float, float],
    name: str
) -> dict[tuple[float, float], str]:
    try:
        map_[coords] = name 
    
    except TypeError as e:
        print(f"The coordinates must be inserted as a tuple, not {type(coords).__name__}.")
        print("Error details:", e)
        return map_
        
    print("\nCurrent checkpoints sorted by latitude:\n")
    for c in sorted(map_.keys(), key= lambda x: x[0]):
        print(f"{c[0]:.4f}, {c[1]:.4f} ----> {map_[c]}")
    print("\n")
    return map_


checkpoints = {
    (40.4168, -3.7038): "Madrid Center",
    (41.3874,  2.1686): "Barcelona Downtown",
}
new_point = (50.0540, 19.9357)
place = "Wawel Cathedral"

print(add_checkpoint(checkpoints, (50.0540, 19.9357), place))