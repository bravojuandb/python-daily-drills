"""
Problem Statement: most_frequent_word_normalized.py

Pillar 1 – Fluency & Logic
Subcategory: Loops & Flow Control
Level: Medium

Prompt:
Given a string with words that may include punctuation and mixed case,
return the most frequent word after normalizing:
- Treat words case-insensitively (compare in lowercase).
- Ignore punctuation (letters and digits only).

If there is a tie for highest frequency, return the word whose FIRST occurrence
appears earliest in the original text (after normalization).

Function Signature:
def most_frequent_word_normalized(text: str) -> str:

Input:
- text: A string possibly containing punctuation and mixed case.

Output:
- A single lowercase string: the normalized most frequent word,
  with tie broken by earliest first occurrence.

Examples:
1)
text = "Bob hit a ball, the hit BALL flew far after it was hit."
Output: "hit"

2)
text = "Alpha, beta! alpha? BETA; beta."
# 'alpha' -> 2 times (positions 0, 2), 'beta' -> 3 times (positions 1, 3, 4)
Output: "beta"

3)
text = "Tie tie! TIE? win."
# 'tie' -> 3 times (first at index 0), 'win' -> 1 time
Output: "tie"

Constraints:
- 1 ≤ len(text) ≤ 1000
- The answer will always exist

Restrictions:
❌ Do NOT use:
- collections.Counter
- max(..., key=...)
- Any library function that does frequency counting or argmax

✅ Do use:
- For-loops
- Dictionaries
- Simple indexing to record the first position a word appears

Notes:
- You may use regex or manual character checks to extract alphanumeric tokens.
- Keep a dict for counts (word -> int) and another (or combine logic) for first index (word -> first_position).
- When scanning to find the winner, compare by (count DESC, first_position ASC).
"""
def most_frequent_word_normalized(text: str) -> str:


    text = text.lower()
    counts = {}
    for raw_word in text.split():
        word = "".join(char for char in raw_word if char.isalnum())
        if word.isalnum():
            counts[word] = counts.get(word, 0) + 1

    max_count = 0
    candidate = ""
    for key, val in counts.items():
        if val > max_count:
            candidate = key
            max_count = val
    
    return candidate


text = "tree, tree, tree, rock, rock, rock, bird"

print(most_frequent_word_normalized(text))


## Perfect solution with tie breaking
def most_frequent_word_normalized(text: str) -> str:
    text = text.lower()
    counts = {}
    first_index = {}

    # tokenize and normalize
    words = []
    for raw_word in text.split():
        word = "".join(char for char in raw_word if char.isalnum())
        if word:
            words.append(word)

    # count frequencies and record first occurrence
    for idx, word in enumerate(words):
        counts[word] = counts.get(word, 0) + 1
        if word not in first_index:
            first_index[word] = idx  # record first time we see this word

    # manual max with tie-breaker
    max_count = 0
    candidate = ""
    min_index = float("inf")

    for word, freq in counts.items():
        if freq > max_count or (freq == max_count and first_index[word] < min_index):
            max_count = freq
            candidate = word
            min_index = first_index[word]

    return candidate