"""
Drill Name: vowel_count.py
Pillar: Pillar 1 – Fluency & Logic
Level: Medium++

Problem Statement:

Write a function `count_vowels_by_word(text: str) -> dict` 
that takes a sentence as input and returns a dictionary 
where each **word** in the sentence is a **key**, 
and its **value** is the number of vowels in that word.

- Vowels are: a, e, i, o, u (both lowercase and uppercase).
- Words are separated by one or more spaces or punctuation 
    preserve punctuation in the keys)
- The keys in the returned dictionary 
    should preserve the **original casing and punctuation** 
    of each word as it appeared in the input, 
    but still count vowels **case-insensitively**.

Example:

    text = "Hello, world! This is Python."
    result = count_vowels_by_word(text)
    print(result)

    Expected output:
    {
        "Hello,": 2,
        "world!": 1,
        "This": 1,
        "is": 1,
        "Python.": 1
    }

Constraints & Edge Cases:

- Empty string → return empty dict.
- Multiple spaces or newline characters → ignore as separators.
- Apostrophes (e.g., in "don't") should be treated as part of the word.

Bonus Challenge:

- Modify your function to also return the total number of vowels in the text.

⏱ Target Time:
15–20 minutes
"""

import re

def count_vowels_by_word(text: str) -> dict:

    vowels = "aeiou"    # List or string?
    count = {}
    words = re.findall(r"\S+", text)

    for word in words:
        num = 0
        for char in word:
            if char.lower() in vowels:
                num += 1
        count[word] = count.get(word, num)

    return count


text = "Hello, world! This is Python."
result = count_vowels_by_word(text)
print(result)