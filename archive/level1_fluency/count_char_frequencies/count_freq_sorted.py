"""
Return Sorted Frequencies (Descending Count)

Problem

Write a function sorted_char_frequencies(text) that:
	•	Returns a list of tuples (char, frequency)
	•	Sorted by frequency (descending)
	•	If two characters have the same frequency, sort them alphabetically

    >>> sorted_char_frequencies("mississippi")
[('i', 4), ('s', 4), ('p', 2), ('m', 1)]

•	Use dict to count characters.
•	Use sorted() with key= to control order.
•	Keep case-sensitive, and include all characters (don't filter yet — this is a pure logic drill).
"""

def sorted_char_frequencies(s: str) -> list[tuple]:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1 
# (-x[1], x[0]) Sorts by freq descending, then alfabetically
    freq_sorted = sorted(freq.items(), key= lambda x : (-x[1], x[0]))

    return freq_sorted

print(sorted_char_frequencies("mississippi"))