"""
Drill 05 - Enumerate with Index

Write a function:
    indexed_pairs(words: list[str]) -> list[str]

Requirements:
1. Use `enumerate()` to loop through both index and word.
2. Return strings in the format `"index: word"`.
3. Start indexing at `0`.

Example:
>>> indexed_pairs(["draft", "review", "publish"])
['0: draft', '1: review', '2: publish']

Thinking goal:
Use `enumerate()` when a loop needs both each item's position and its value.
Avoid manually tracking or updating an index variable.
"""

def indexed_pairs(words: list[str]) -> list[str]:
    return [f"{i}: {word}" for i, word in enumerate(words)]

if __name__ == "__main__":
    words = ["draft", "review", "publish"]
    print(indexed_pairs(words))
