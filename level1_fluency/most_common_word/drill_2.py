"""
🔠 most_common_word.py

Write a function `most_common_word(text: str, banned: list[str]) -> str` that returns
the **most frequent word** in the input `text` that **is not** in the list `banned`.

Rules:
- Words are case-insensitive (i.e., "Ball" and "ball" are the same word).
- Punctuation marks should be ignored — treat `"ball,"` as `"ball"`.
- Return **the most frequent word** that is not in the banned list.
- If there's a tie, return the one that comes **first alphabetically**.
- Assume `text` will contain at least one non-banned word.

Examples:
>>> most_common_word("Ball! Ball. BALL? bat bat", ["ball"])
'bat'

>>> most_common_word("To be, or not to be: that is the question.", ["to", "be"])
'question'

>>> most_common_word("a a a b b c", ["a", "b"])
'c'

Constraints:
- Use a dictionary to count word frequencies.
- Do not use `collections.Counter`.
- You may use `re` for punctuation handling if needed.
- Your solution should run in O(n) time relative to number of words.
"""
import re

def most_common_word(text: str, banned: list[str]) -> str:
    
    words = re.findall(r'\b\w+\b', text.lower() )
    counts = {}
    for word in words:
        if word not in banned:
            counts[word] = counts.get(word, 0) + 1
        
    max_freq = max(counts.values())
    candidates = [word for word, freq in counts.items() if freq == max_freq]

    return min(candidates)


print(most_common_word("To be, or not to be: that is the question.", ["to", "be"]))