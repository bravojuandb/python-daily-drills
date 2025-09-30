"""
Write a function `indexed_pairs(words: list[str]) -> list[str]`.

Rules:
- Use `enumerate()` to loop through the list with both index and word.
- For each word, return a string in the format: "index: word".
- Collect them all in a list and return it.

Example:
words = ["sun", "moon", "stars"]
indexed_pairs(words) = ["0: sun", "1: moon", "2: stars"]

Try to solve it in under 2 minutes!
"""

def indexed_pairs(words: list[str]) -> list[str]:
    return [f"{i}: {word}" for i, word in enumerate(words)]

words = ["sun", "moon", "stars"]

print(indexed_pairs(words))