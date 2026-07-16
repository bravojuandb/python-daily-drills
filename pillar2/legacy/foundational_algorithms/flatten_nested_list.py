"""
You are given a list of lists containing integers — for example:

    data = [[1, 2, 3], [4, 5], [6, 7, 8]]

Write a function `flatten_nested_list(L)` that returns a single flat list
containing all numbers in order:

Expected output:
    [1, 2, 3, 4, 5, 6, 7, 8]

💡 Constraint:
Do it in *one line* using a comprehension — no external libraries.

Be quick and precise.
"""

def flatten_nested_list(L: list[list[int]]) -> list[int]:
    """
    Flatten a two-level nested list into a single list.
    """
    return [x for sub in L for x in sub]

data = [[1, 2, 3], [4, 5], [6, 7, 8]]

print(flatten_nested_list(data))