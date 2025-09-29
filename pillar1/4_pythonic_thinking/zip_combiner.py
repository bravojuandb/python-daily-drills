"""
You are given two lists:
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

1. Use `zip()` to combine them into pairs (tuples).
2. Convert the zipped result into a dictionary where names are keys and scores are values.

Expected:
- Zipped → [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
- Dict   → {'Alice': 85, 'Bob': 92, 'Charlie': 78}
"""

# Direct
def combine_convert(l1: list[str], l2: list[int]) -> dict:
    combined = zip(l1, l2)
    return dict(combined)

# Expanded
def combine_convert(l1: list[str], l2: list[int]) -> dict:
    combined = zip(l1, l2)
    result = {}
    for k, v in combined:
        result[k] = v
    return result

# List comprehension
def combine_convert(l1: list[str], l2: list[int]) -> dict:
    combined = zip(l1, l2)
    return {k : v for k, v in combined}



names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(combine_convert(names, scores))
