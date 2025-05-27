"""
Leetcode string merging problem.

Features:

Plain script version
"""
# Define the two words

word1 = "abc"
word2 = "pqrs"

result = []

max_length = max(len(word1), len(word2))

for i in range(max_length):
    if i < len(word1):
        result.append(word1[i])
    if i < len(word2):
        result.append(word2[i])

merged = ''.join(result)

print(merged)