
"""
Description:
Given a dictionary where keys are strings and values are integers,
return a sorted list of all values that appear exactly once.

If no values are unique, return an empty list.

Input / Output Examples:

>>> unique_values({"a": 3, "b": 4, "c": 3, "d": 5})
[4, 5]

>>> unique_values({"x": 10, "y": 10, "z": 10})
[]

>>> unique_values({})
[]

Constraints:
- Input is a dictionary with string keys and integer values.
- Output must be a list of integers sorted in ascending order.
- Your solution should use only one pass to count and one to collect results.
- Avoid nested loops.

Python tools to focus on:
- Dictionary iteration
- `collections.Counter`
- Sorting lists

Optional extension:
Write a test file using `pytest` to cover:
    - typical use
    - all values repeated
    - all values unique
    - empty dictionary
"""
# Implement your solution here:

def unique_values(d: dict[str, int]) -> list[int]:
    from collections import Counter
    counts = Counter(d.values())

    unique = []
    for i, j in counts.items():
        if j == 1:
            unique.append(i)
    return sorted(unique)


print(unique_values({"a": 3, "b": 4, "c": 3, "d": 5}))
