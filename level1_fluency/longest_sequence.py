"""
Longest Sequence Without Repeats (Just Count)

Return the length of the longest substring that contains no repeated characters.
We don't need to return the actual substring (yet!) — just the count.

	•	Input: a string s
	•	Output: an integer
	•	Case-sensitive
	•	You may use:
        •	a set() to track seen characters in the current substring
        •	two pointers to track the current window
"""

def count_longest_seq(s:str) -> int:

    start = 0                # Left side of sliding window
    max_length = 0           # To store the longest length found
    seen = set()             # To store characters in current window

    for end in range(len(s)):  # Loops during as many characters the string has
        print(s[end]) # This is the current character. end is a pointer
        while s[end] in seen:  # 
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length


print(count_longest_seq("abcaaaaabcb"))
