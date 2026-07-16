"""
Mid-Easy Version — Clean Text Counter

Write a function `count_words_clean(text: str) -> dict[str, int]`
that counts words case-insensitively, **removing punctuation** before splitting.

Rules:
- Remove common punctuation (.,!?;:’"()-).
- Treat "don't" and "self-taught" as valid single words.
- Ignore empty strings after cleaning.
- Return a dict sorted by descending frequency (not required to print sorted).

Example:
>>> count_words_clean("Python is great, and python is fun!")
{'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}

Expected time: ~10 minutes.
"""

from collections import Counter
import re

def count_words_clean(text: str) -> dict[str, int]:
    text = re.sub(r"[.,!?;:’()-]", " ", text )
    normalized = text.lower().split()
    return dict(sorted(Counter(normalized).items(), key= lambda x: (-x[1], x[0])))

print(count_words_clean("Python is great, and python is fun!"))