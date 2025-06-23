"""
First Unique Character, difficulty: easy

Write a function that receives a lowercase string and returns the index of
the first non-repeating character. If there's no unique character, treturn -1.

"""

from collections import Counter

def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1

print(first_unique_char("loveleetcode"))