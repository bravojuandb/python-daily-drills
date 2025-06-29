"""
This is medium difficulty drill.

Write a functions that returns 
the first character in a string that does not repeat.

•	Ignore spaces
•	Be case-sensitive
•	Use any built-in structures (like dict, collections.Counter, etc.)
•	Aim for O(n) time if possible

"""
from collections import Counter

def first_unique_char(s: str) -> str | None:
    counts = Counter(s)
    unique = []
    for i, j in counts.items():
        if j == 1:
            unique.append(i)
    for char in unique:
        if char in s:
            print("Found the first non repeating character!!!")
        return char
    return None


def first_unique_char_improved (s: str) -> str | None:
    counts = Counter(s)

    for char in s:
        if counts[char] == 1:
            return char
    return None


print(first_unique_char_improved("es.tern oclei domastoideo"))