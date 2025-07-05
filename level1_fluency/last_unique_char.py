"""
Write a function that returns the index of the last unique character
in the string s that appears only once
Retur -1 if no such character exists

last_unique_char("leetcode")       # ➞ 7  ('e')
last_unique_char("loveleetcode")   # ➞ 7  ('d')
last_unique_char("aabbcc")         # ➞ -1

Use collections.Counter or dict.
	•	Loop through the string in reverse order, while keeping access to original indices.
	•	Time complexity should be O(n).

"""

# Using collections.Counter

from collections import Counter

def last_unique_char(s:str) -> int:
    counts = Counter(s)
    for index in reversed(range(len(s))):
        character = s[index]
        if counts[s[index]]  == 1:
            return index
    return -1

# Returning a uple (index, character) Using collections.Counter

from collections import Counter

def last_unique_char(s:str) -> tuple:
    counts = Counter(s)
    for index in reversed(range(len(s))):
        character = s[index]
        if counts[s[index]]  == 1:
            return index, character
    return -1


# Using collections.Counter

def last_unique_char(s: str) -> int:
    counts = {}
    # First pass: count characters
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Second pass: reverse loop to find last unique
    for index in reversed(range(len(s))):
        if counts[s[index]] == 1:
            return index

    print(counts)

last_unique_char("leetcode")