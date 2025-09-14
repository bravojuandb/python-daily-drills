"""
Problem: Longest Consecutive Zeros in Binary String
Problem: Given a binary string (only 0s and 1s), 
find the length of the longest consecutive sequence of 0s.

Example:

Input: "1100011000111"
Output: 4 (the sequence "0000" in the middle)

"""

def longest_chain(s: str) -> int:
    max_length = 0
    i = 0 # i is the position counter, or pointer
    
    while i < len(s):
        if s[i] == '0':
            current_length = 0
            while i < len(s) and s[i] == '0':  # Keep going while we see 0s
                current_length += 1
                i += 1  # Move to next position!
            max_length = max(max_length, current_length)
        else:
            i += 1  # Skip the '1'
    
    return max_length


print(longest_chain("1100011000111"))