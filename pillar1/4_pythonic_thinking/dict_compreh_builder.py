"""
You are given two lists:

keys = ["apple", "banana", "orange", "pear"]
values = [5, 0, 3, 8]

Task:
1. Build a dictionary using **dict comprehension** where:
   - Each key comes from `keys`.
   - Each value comes from `values`.
   - Only include items where the value is greater than 2.
   - Transform the key into UPPERCASE.

Example:
Expected result → {"APPLE": 5, "ORANGE": 3, "PEAR": 8}

Write this in one line using a dict comprehension.
"""

def dictionary_builder(keys: list[str], values: list[int]) -> dict:
    return {
        keys[i].upper() : values[i]
        for i in range(len(keys))
        if values[i] > 2
    }

# Using zip()
def dictionary_builder(keys: list[str], values: list[int]) -> dict:
    return {
        k.upper(): v
        for k, v in zip(keys, values) 
        if v > 2
        }


keys = ["apple", "banana", "orange", "pear"]
values = [5, 0, 3, 8]

print(dictionary_builder(keys, values))