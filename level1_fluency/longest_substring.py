"""
Write a function that returns the length of the longest substring
in a given string without repeating characters.

You must solve it in O(n) time.

"""
from collections import Counter

def longest_unique_substring(s: str) -> int:

    last_seen = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:

        


print(longest_unique_substring("pwwkew"))

    
