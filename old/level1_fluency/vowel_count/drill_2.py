"""
Drill Name: count_vowels.py

Pillar: Fluency & Logic
Level: Easy

Problem Statement:
Write a function count_vowels(text: str) -> int that takes a string and returns 
the total number of vowels (a, e, i, o, u) it contains.

	•	The function should ignore case (count both uppercase and lowercase vowels).
	•	If the string is empty, return 0.

Example:
text = "Hello, world!"
result = count_vowels(text)
print(result)   # Expected output: 3
"""

from collections import Counter

def count_vowels(text:str) -> int:

    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = Counter(text.lower())
    result = 0
    for element in counts:
        if element in vowels:
            result += counts[element]

    return result

print(count_vowels("“Llegó con tres heridas: la del amor, la de la muerte, la de la vida.”"))