"""
You are given a long string representing the content of a text file.

Write a function `count_word_occurrences(text: str) -> dict[str, int]`
that returns a dictionary mapping each *unique word* to the number of times it appears.

Rules:
- Words are case-insensitive ("Python" and "python" are the same).
- Ignore punctuation (.,!?:;).
- Words are separated by spaces or newlines.

Example:
>>> count_word_occurrences("Python is great, and python is fun!")
{'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}

Be quick and precise — avoid unnecessary loops or memory overhead.
"""

def count_word_occurrences(text: str) -> dict[str, int]:
    count = {}
    for word in text.lower().split():
        if word.isalpha():
            count[word] = count.get(word, 0) + 1
    return count

print(count_word_occurrences("Python is great, and python is fun!"))