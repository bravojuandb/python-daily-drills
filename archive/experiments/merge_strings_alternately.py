"""
Leetcode string merging problem.

Features:

Wrapping the simple script into a function
"""

class Solution:

    def mergeAlternately (self, word1: str, word2: str) -> str:
        
        result = []

        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        return ''.join(result)

sol = Solution() # Create the sol object

# Call the mergeAlternately method on that sol object.
result = sol.mergeAlternately("euclides", "aristofanes") 

print(result)