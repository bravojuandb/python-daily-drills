"""
Write a function that counts how many vowels (a,e,i,o,u)
are in a given string.
Count both uppercase and lowercase vowels.

"""

def count_vowels(s: str) -> int:

    vowels = ["a","e","i","o","u"]
    vowel_num = 0
    for char in s:
        if char in vowels:
            vowel_num += 1

    return vowel_num

print(count_vowels("murcielago"))