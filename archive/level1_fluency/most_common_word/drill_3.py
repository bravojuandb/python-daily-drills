"""
Fluency & Logic

Level: Hard
Subcategory: Loops & Flow Control

Problem Statement: most_common_word.py

You are given a paragraph of text and a list of banned words.
Your task is to find and return the most common word that is NOT in the banned list.

Rules:
	•	Ignore punctuation.
	•	Treat words case-insensitively.
	•	Return the most frequent valid word.

You may NOT use built-in helpers like collections.Counter or max(dictionary, key=...).
This drill is about manual control using loops and conditionals.

Input:
	•	paragraph: A string of English words, possibly with punctuation and mixed case.
	•	banned: A list of lowercase strings representing words to ignore.

Output:
	•	A single lowercase string: the most frequent word that is not banned.

Example: 
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
output "ball"

Constraints:
	•	1 ≤ len(paragraph) ≤ 1000
	•	0 ≤ len(banned) ≤ 100
	•	All strings in banned are lowercase.
	•	The answer will always exist.

"""

# THIS IS A SIMPLE WORD COUNTER
import re
def word_counter(paragraph=str) -> dict:
 
    words_unclean = paragraph.lower().split() # simple split
    words_clean = re.findall(r'\b\w+\b', paragraph.lower())
    counts = {}
    for word in words_clean:
        counts[word] = counts.get(word, 0) + 1

    return counts


def most_common_word(paragraph=str, banned=list[str]) -> str:

    # Logic for cleaning each word from puctuation and spaces
    words = re.findall(r'\b\w+\b', paragraph.lower())

    # Logic for counting all non-banned words
    counts = {}
    for word in words:
        if word not in banned:
            counts[word] = counts.get(word, 0) + 1

    # Logic for finding the word with the maximum count

    most_common = ""
    max_count = 0

    for word in counts:
        if counts[word] > max_count:
            most_common = word
            max_count = counts[word]

    return most_common


words = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_common_word(words, banned))