"""
Find top n letters from a string.

Given a string text, return a list of the n most frequent alphabetic characters 
(case-insensitive), sorted by frequency (descending), and alpahbetically for ties.

	•	Ignore non-letter characters (digits, punctuation, etc.)
	•	Compare letters case-insensitively ('A' = 'a')
	•	In case of frequency tie, sort alphabetically (e.g., ['a', 'b', 'c'])

find_top_n_letters("Hello World!")  # ➞ ['l', 'o', 'd']
find_top_n_letters("Mississippi river", n=2)  # ➞ ['i', 's']
find_top_n_letters("1234567890", n=5)  # ➞ []
find_top_n_letters("AaAaBbCc!", n=2)  # ➞ ['a', 'b']
find_top_n_letters("", n=3)  # ➞ []

	•	Time complexity: Aim for O(N) with a dictionary or collections.Counter
	•	Only letters from a to z and A to Z should be considered
	•	n will always be a positive integer
	•	You may assume text is a valid string

"""

def find_top_n_letters(text: str, n: int = 3) -> list[str]:

    counts = {}
    # Creating a counting dictionary with loop
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1

    # Sort letters by frequency (highest first), then alphabetically for ties.
    # item[1] = count, item[0] = letter
    counts_sorted = sorted(counts.items(), key= lambda item: (-item[1], item[0]))
  
    # Return the top n letter only, not their counts
    return [char for char, count in counts_sorted[:n]]


print(find_top_n_letters("El Señor es mi Pastor", 3))