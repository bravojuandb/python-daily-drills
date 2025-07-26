"""
Repetition. If there's a tie, this version returns the first ord in alphabetical order.
"""

import re

def most_common_word(paragraph: str, banned: list[str]) -> str:


    words = re.findall(r"\b\w+\b", paragraph.lower())
    counts = {}

    for word in words:
        if word not in banned:
            counts[word] = counts.get(word, 0) + 1

    max_count = 0
    for word in counts:
        if counts[word] > max_count:
            max_count = counts[word]

    most_common = []
    for word in counts:
        if counts[word] == max_count:
            most_common.append(word)

    return min(most_common)

    """Or: Track best word manually (alphabetical first among most common)
        best_word = ""
        for word in counts:
            if counts[word] == max_count:
                if best_word == "" or word < best_word:
                    best_word = word"""



paragraph = "While the trees are trees, the trees will be trees, not bees, not bees, not bees"
banned = ["trees"]

print(most_common_word(paragraph, banned))

