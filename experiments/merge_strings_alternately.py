"""
Leetcode string merging problem.

Features:

Wrapping the simple script into a function
"""


def strings_merger (word1, word2):
    
    result = []

    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return ''.join(result)

print(strings_merger("socrates", "aristoteles"))