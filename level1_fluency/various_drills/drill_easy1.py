"""
“First Unique Character”

Write a function that returns the index of the first 
non-repeating character in a string s. 
If there is no unique character, return -1.

first_unique_char("leetcode")      # ➞ 0
first_unique_char("loveleetcode")  # ➞ 2
first_unique_char("aabb")          # ➞ -1

You must not use external libraries.
	•	Must run in O(n) time.
	•	Use built-in Python tools where appropriate (collections, dict, set, etc.).
"""

from collections import Counter

def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for i, j in enumerate(s):
        if counts[j] == 1:
            return i
    return -1


# Test your function on:
long_string = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
print(first_unique_char(long_string))  # ➞ 50 (index of 'z')

