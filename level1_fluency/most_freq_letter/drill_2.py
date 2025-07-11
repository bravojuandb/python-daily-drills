"""
Count Vowels and Consonants

Write a function count_vowels_and_consonants.

Given a string text, return a dictionary 
with the number of vowels and consonants in the string.

	•	Count letters only (ignore digits, punctuation, etc.).
	•	Count is case-insensitive.
	•	Return a dictionary with this exact format:
        {'vowels': 4, 'consonants': 7}

count_vowels_and_consonants("Hello World!")  
# ➞ {'vowels': 3, 'consonants': 7}

count_vowels_and_consonants("123!@#")        
# ➞ {'vowels': 0, 'consonants': 0}

count_vowels_and_consonants("AEIOUxyz")      
# ➞ {'vowels': 5, 'consonants': 3}

•	Use a set: vowels = {'a', 'e', 'i', 'o', 'u'}
•	Use str.lower() and str.isalpha() to clean the input.
•	Loop through the characters and classify each one.

"""

def count_vowels_and_consonants(text: str) -> dict:

    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {}
    vowel_num = 0
    consonant_num  = 0

    for item in text.lower():
        if item.isalpha():
            counts[item] = counts.get(item, 0) + 1

    for value, freq in counts.items():
        if value in list(vowels):
            vowel_num += 1

        else:
            consonant_num += 1

    return {'vowels': vowel_num, 'consonants': consonant_num}


sentence = """
Quanta enim libido 
in discordiis civilibus, 
quanta audacia, 
quantae calamitates sequantur, 
vel bellorum civilium 
documenta satis ostendunt.
"""

print(count_vowels_and_consonants(sentence))