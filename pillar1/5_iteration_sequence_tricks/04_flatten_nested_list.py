"""
Drill 04 - Flatten Nested List

Write a function:
    flatten_list(nested: list[list[int]]) -> list[int]

Requirements:
1. Input is a list of lists of integers.
2. Use a list comprehension with two `for` clauses.
3. Return the flat list in the original left-to-right order.

Example:
>>> flatten_list([[1, 2], [3, 4, 5], [6]])
[1, 2, 3, 4, 5, 6]

Thinking goal:
This drill is about seeing a nested traversal as one readable sequence expression.
"""

def flatten_list(nested: list[list[int]]) -> list[int]:
    return [num for inner in nested for num in inner]


if __name__ == "__main__":
    nested = [[1, 2], [3, 4, 5], [6]]
    print(flatten_list(nested))