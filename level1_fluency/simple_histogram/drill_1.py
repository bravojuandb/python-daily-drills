"""
Problem: Simple Histogram

You are given a list of strings representing words from a document.

Write a function `build_histogram(words: list[str]) -> dict[str, int]` 
that returns a dictionary representing a frequency histogram of the words.
Each key in the dictionary should be a word from the list (case-sensitive), 
and the value should be the number of times it appears.

Example:
    Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
    Output: {"apple": 3, "banana": 2, "orange": 1}

Constraints:
- Do NOT use collections.Counter.
- Do NOT use external libraries.
- Your solution should run in O(n) time.

Edge Cases:
- An empty list should return an empty dictionary.
- Words may contain punctuation or mixed casing — treat them as distinct.

"""

def build_histogram(words: list[str]) -> dict[str, int]:
    counts = {}
    for word in words:
        print(counts.get(word, 0))
        counts[word] = counts.get(word, 0) + 1
    return counts 

print(build_histogram(["apple", "banana", "apple", "orange", "banana", "apple"]))
