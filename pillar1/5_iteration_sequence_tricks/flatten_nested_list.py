"""
Write a function `flatten_list(nested: list[list[int]]) -> list[int]`.

Rules:
- Input is a list of lists of integers.
- Use a **list comprehension** with two `for` loops to flatten it.
- Return the flat list.

Example:
nested = [[1, 2], [3, 4, 5], [6]]
flatten_list(nested) = [1, 2, 3, 4, 5, 6]

Solve it under 2 minutes!
"""
# Normal loop
def flatten_list(nested: list[list[int]]) -> list[int]:
    flattened = []
    for sub in nested:
        for num in sub:
            flattened.append(num)
    return flattened

# List comprehension
def flatten_list(nested: list[list[int]]) -> list[int]:
    return [num for sub in nested for num in sub]


nested = [[1, 2], [3, 4, 5], [6]]
print(flatten_list(nested))