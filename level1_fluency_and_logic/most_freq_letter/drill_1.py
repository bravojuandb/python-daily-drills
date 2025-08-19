"""
Most Frequent Letter

Given a string text, 
return the letter (a-z, case-insensitive) 
that occurs most frequently.

Ignore spaces, digits, punctuation, etc.

If there are multiple letters with the same max frequency,
return the one that appears first alphabetically.
Return the letter in lowercase.

most_frequent_letter("Hello World!")         ➞ 'l'
most_frequent_letter("The quick brown fox")  ➞ 'o'
most_frequent_letter("aabbccddeeffgg")       ➞ 'a'
most_frequent_letter("123!@#")               ➞ ''  # no letters

Use a dictionary to count frequencies.
Use .isalpha() to filter letters.
Normalize with .lower().
Use max() with a custom key for tie-breaking (alphabetical).

"""
def most_frequent_letter(text: str) -> str:

    counts = {}

    for item in text:
        if item.isalpha():
            item = item.lower()
            counts[item] = counts.get(item, 0) + 1
        if not counts:
            return ''
        
    max_freq = max(counts.values())

    candidates = [item for item, freq in counts.items() if freq == max_freq]


    return min(candidates)

sentence = "Non nobis solum nati sumus."

print(most_frequent_letter(sentence))
