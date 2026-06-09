"""
Drill 01 - Forward and Backward Iteration

Write a function:
    mirror_iter(words: list[str]) -> list[str]

Requirements:
1. First iterate forward through the list and collect all elements.
2. Then iterate backward through the same list and collect them again.
3. Return the combined list.

Example:
>>> mirror_iter(["sun", "moon", "stars"])
['sun', 'moon', 'stars', 'stars', 'moon', 'sun']

Thinking goal:
This drill is about noticing that direction is part of the logic, not just a loop detail.
"""


def mirror_iter(words: list[str]) -> list[str]:
    mirrored_words = []

    for word in words:
        mirrored_words.append(word)

    for word in words[::-1]:
        mirrored_words.append(word)
        
    return mirrored_words


if __name__ == "__main__":
    words = ["sun", "moon", "stars"]
    print(mirror_iter(words))