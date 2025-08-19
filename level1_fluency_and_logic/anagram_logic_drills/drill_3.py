"""
Group Words by Anagram Class

Level: Easy+
Category: Word grouping, dictionaries
Skills: defaultdict, sorting, tuple keys

Given a list of words, return a list of groups — each group containing words that are anagrams of one another.
	•	The result can be in any order.
	•	Each group must contain at least one word.
	•	Words are case-insensitive, but the output should preserve original case.

"""
import unicodedata
from collections import defaultdict


def normalize(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if c.isalpha()
    ).lower()


def group_anagrams(words: list[str]) -> list[list[str]]:

    anagram_groups = defaultdict(list)

    for word in words:
        normalized = normalize(word)
        key = tuple(sorted(normalized))
        anagram_groups[key].append(word)

    for key, group in anagram_groups.items():
        print(f"Key: {''.join(key)} → Group: {group}")
              
    return list(anagram_groups.values())


print(group_anagrams(["listen", "silent", "enlist", "rat", "tar", "art", "hello"]))