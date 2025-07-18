"""
Problem Statement: most_common_word.py

Pillar 1 – Fluency & Logic
Subcategory: Loops & Flow Control
Level: Medium

Prompt:
You are given a paragraph of text and a list of banned words. 
Your task is to find and return the most common word that is NOT in the banned list.

- Ignore punctuation.
- Treat words case-insensitively.
- Return the most frequent valid word.

You may NOT use built-in helpers like collections.Counter or max(dictionary, key=...).
This drill is about manual control with loops and conditionals.

Function Signature:
def most_common_word(paragraph: str, banned: List[str]) -> str:

Input:
- paragraph: A string of English words, possibly with punctuation and mixed case.
- banned: A list of lowercase strings representing words to ignore.

Output:
- A single lowercase string: the most frequent word that is not banned.

Example:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

Output: "ball"

Constraints:
- 1 ≤ len(paragraph) ≤ 1000
- 0 ≤ len(banned) ≤ 100
- All strings in banned are lowercase
- The answer will always exist

Restrictions:
❌ Do NOT use:
- collections.Counter
- max(..., key=...)
- Any library function that does frequency counting or finding maximums

✅ Do use:
- For-loops
- If-else
- Dictionaries (manually)
"""


def most_common_word(paragraph: str, banned_set= list[str]) -> str:

    # Parsing the text with regex
    import re
    words = re.findall(r'\w+', paragraph.lower())

    # Loop based counting
    freq = {}
    for word in words:
        if word not in banned_set:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    # Manual max lookup
    most_common = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            most_common = word

    return most_common
    
    

print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", "hit"))