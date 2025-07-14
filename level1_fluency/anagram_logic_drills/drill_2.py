"""
Unicode-Aware Anagram Check

Level: Easy+
Category: String normalization, Unicode
Skills: unicodedata, Counter, filtering

Return True if the two words are anagrams, 
even if they contain accented or Unicode letters (ñ, á, ö, etc.).

	•	Case-insensitive
	•	Ignore spaces and punctuation
	•	Normalize accents (treat á as a, ñ as n, etc.)
	•	You may assume only alphabetic characters (no emoji or complex scripts)

are_anagrams_unicode("niño", "ño in")     ➞ True
are_anagrams_unicode("café", "face")      ➞ True
are_anagrams_unicode("árbol", "lobar")    ➞ True
are_anagrams_unicode("niño", "nino")      ➞ True
are_anagrams_unicode("años", "sano")      ➞ True


Use this to normalize accented characters:

import unicodedata

Use this to normalize accented characters:
def normalize(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if c.isalpha()
    ).lower()

"""

import unicodedata
from collections import Counter

def normalize(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if c.isalpha()
    ).lower()

def are_anagrams_unicode(word1: str, word2: str) -> bool:
    return Counter(normalize(word1)) == Counter(normalize(word2))


print(are_anagrams_unicode("árbol", "lobar"))