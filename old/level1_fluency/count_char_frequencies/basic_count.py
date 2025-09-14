"""
Count Character Frequencies (Basic)


Write a function count_char_frequencies(text) that 
takes a string and returns a dictionary where each key 
is a character and each value 
is the number of times it appears in the string.

	•	Use a dictionary to store counts.
	•	Be case-sensitive.
	•	Include all characters (including punctuation, spaces, etc.).
	•	No imports needed.

"""

def count_char_frequencies(s:str) -> dict:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(count_char_frequencies("esternocleidomastoideo"))