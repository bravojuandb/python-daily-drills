"""
Anagram Check Using Frequency Dictionaries

Level: Easy+
Category: String comparison
Skills: Frequency dicts, filtering, Counter

Return True if the two words are anagrams — but do not use sorting (e.g. sorted(word1) == sorted(word2))
Instead, solve the problem using frequency dictionaries (e.g., collections.Counter).
	•	Case-insensitive
	•	Ignore spaces, punctuation, and accents (e.g. á = a, ñ = n)
	•	Unicode characters should be normalized using unicodedata.normalize

are_anagrams_by_count("Niño", "ñino")        ➞ True
are_anagrams_by_count("árbol", "lobar")      ➞ True
are_anagrams_by_count("rat", "tar")          ➞ True
are_anagrams_by_count("hello", "world")      ➞ False

"""
import unicodedata
from collections import Counter


def normalize(text: str) -> str:
    """Normalize text: remove accents, keep letters, lowercase everything."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if c.isalpha()
    ).lower()


def are_anagrams_by_count(word1: str, word2: str) -> bool:
    """Return True if word1 and word2 are anagrams (using frequency counts)."""

    norm1 = normalize(word1)
    norm2 = normalize(word2)

    return Counter(norm1) == Counter(norm2)

    
print(are_anagrams_by_count("rat", "tar"))