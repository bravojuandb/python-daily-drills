"""
Ignore Spaces and Punctuation

Problem

Again: 
each key is a character, 
and each value is the number of times it appears in the string.

Extend your character frequency counter so that:
	•	It ignores spaces, punctuation, and digits.
	•	It treats uppercase and lowercase letters as the same (i.e., case-insensitive).

	•	Use a dictionary.
	•	Convert all characters to lowercase.
	•	Only include alphabetic characters: char.isalpha() should be True.
	•	No imports needed.

"""

def count_clean_char_frequencies(s: str) -> dict:
    freq = {}
    for char in s:
        char = char.lower()
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    print(f"This is the clean count:{freq}")
    print(f"This is the sorted count: {dict(sorted(freq.items()))}")
    print(f"This is the list of tuples sorted by freq: {sorted(freq.items(), key=lambda x: x[1])} ")
    
    return freq



count_clean_char_frequencies("Hello, World!123")