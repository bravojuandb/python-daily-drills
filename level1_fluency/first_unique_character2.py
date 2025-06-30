"""
Write a function that returns the first character in a string that does not repeat.
	•	Be case-sensitive (e ≠ E)
	•	Ignore spaces
	•	Use dict, Counter, or your own logic
	•	Aim for O(n) time — no nested loops
"""

from collections import Counter

# Looping over counts.items() — which reflects character frequency,
# but not the original string order 
# (especially if the input includes spaces or reordered letters)

def first_unique_char(s: str) -> str | None:
    
    counts = Counter(s)
    for i,j in counts.items():
        if j == 1:
            return i
        return None


# Returns the first non-repeating character in original order.
def first_unique_char(s: str) -> str | None:
    counts = Counter(s)
    for char in s:
        if char != " " and counts[char] == 1:
            return char
        return None

print(first_unique_char("azabbcddex"))