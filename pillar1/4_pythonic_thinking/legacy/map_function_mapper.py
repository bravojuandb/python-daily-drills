"""
You are given a list of words.
1. Use `map()` with `str.upper` to convert all words to uppercase.
2. Use `map()` with a `lambda` to get the length of each word.

words = ["python", "rocks", "map", "function"]

Expected:
- Uppercase → ['PYTHON', 'ROCKS', 'MAP', 'FUNCTION']
- Lengths  → [6, 5, 3, 8]
"""

words = ["python", "rocks", "map", "function"]


def mapped_upper(words: list[str]) -> list:
    return [*map(str.upper , words)]

# using lambda + len is redundant
def mapped_lengths(words: list[str]) -> list:
    return [*map(lambda x: len(x), words)]

# len alone would be enough:
def mapped_lengths(words: list[str]) -> list:
    return [*map(len, words)]

# pure lambda function with loop:
def mapped_lengths(words: list[str]) -> list:
    return [*map(lambda x: sum(1 for _ in x), words)]

print(mapped_upper(words))
print(mapped_lengths(words))