"""
Drill 08 - Replace Characters

Write a function:
    mask_vowels(text: str) -> str

Requirements:
1. Replace every vowel (`a, e, i, o, u`) in either case with `*`.
2. Leave consonants, spaces, digits, and punctuation unchanged.
3. Return the masked string.
4. Solve it using string operations, not regular expressions.

Examples:
>>> mask_vowels("Hello World")
"H*ll* W*rld"

>>> mask_vowels("AEIOU 123")
"***** 123"

Thinking goal:
This is a small transformation drill that tests precision and consistency.
"""
def mask_vowels(text: str) -> str:
    vowels = set("AEIOUaeiou")
    return "".join("*" if char in vowels else char for char in text)

if __name__ == "__main__":
    print(mask_vowels("AEIOU 123"))
