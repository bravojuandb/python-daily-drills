"""
Basic Anagram Check

given two strings, write a function are_anagrams that returns 
True is word1 and word 2 are anagrams.
Otherwise return False.

	•	Ignore spaces, punctuation, and case
	•	Anagrams must have the same letters in any order
	•	Empty strings count as anagrams of each other

are_anagrams("listen", "silent")      ➞ True
are_anagrams("Astronomer", "Moon starer") ➞ True
are_anagrams("hello", "world")        ➞ False
are_anagrams("Dormitory", "dirty room") ➞ True
are_anagrams("a", "A")                ➞ True
are_anagrams("", "")                  ➞ True

	•	Use .lower() to normalize case
	•	Use .isalpha() to remove punctuation and spaces
	•	Use sorted() to compare the cleaned letter sequences
"""

def are_anagrams(word1: str, word2: str) -> bool:

    """
    Return True is word1 and word2 are anagrams. Otherwise return False.
    """
    counts1 = {}
    counts2 = {}

    for char1 in word1.lower():
        if char1.isalpha():
            counts1[char1] = counts1.get(char1, 0) + 1

    for char2 in word2.lower():
        if char2.isalpha():
            counts2[char2] = counts2.get(char2, 0) + 1

    return counts1 == counts2
        

print(are_anagrams("listen", "silent"))