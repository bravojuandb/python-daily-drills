"""
⚡ Replace Characters Drill

Problem:  
Write a function `mask_vowels(text: str) -> str` that:  
1. Replaces all vowels (`a, e, i, o, u`) with `*`.  
2. Keeps consonants and other characters unchanged.  
3. Returns the masked string.

Example:
>>> mask_vowels("Hello World")
"H*ll* W*rld"

⏱️ Challenge: solve it in under 2 minutes using only `.replace()` (chaining or looping).
"""

def musk_vowels(text: str) -> str:

    vowels = "aeiouAEIOU"
    musked_text = []

    for char in text:
        if char in vowels:
            musked_text.append("musk")
        else:
            musked_text.append(char)
        
    return "".join(musked_text)

print(musk_vowels("Hello World"))
    
