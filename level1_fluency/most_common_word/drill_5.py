"""
Problem Statement: most_frequent_word_basic.py

Pillar 1 – Fluency & Logic
Subcategory: Loops & Flow Control
Level: Easy

Prompt:
You are given a short string containing words separated by spaces. 
Your task is to return the most frequent word. 

- Do not worry about punctuation. 
- Do not worry about uppercase vs lowercase (assume all words are lowercase). 
- There is no banned list. 
- The answer will always exist. 

Function Signature:
def most_frequent_word(text: str) -> str:

Input:
- text: A string of lowercase words separated by spaces. 

Output:
- A single string: the word that appears the most times. 

Example:
text = "dog cat dog fish cat dog"
Output: "dog"

Restrictions:
❌ Do NOT use:
- collections.Counter
- max(..., key=...)
- Any library function that does frequency counting or finding maximums

✅ Do use:
- For-loops
- Dictionaries
"""

def most_frequent_word(text: str) -> str:

    counts = {}
   
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1 
    
    max_count = 0
    candidate = ""
    for key, val in counts.items():
        if val > max_count:
            max_count = val
            candidate = key
    return candidate


sentence = "push harder push sharper push stronger consistency wins consistency wins"


print(most_frequent_word(sentence))