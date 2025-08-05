
"""
CHALLENGE PROPOSITION

Write a function `reverse_unique(s: str) -> str` 
that returns the input string **reversed**,
but only after verifying that all characters are unique 
(no duplicates, case-sensitive).

Rules:

1. If the string contains **any duplicate character**, 
    raise a `ValueError` with the message:
   "Duplicate characters not allowed".
2. If the string is empty, return an empty string.
3. The reversal must be manual — do **not** use `reversed()` or slicing (`[::-1]`).
4. You may use a `set` to track seen characters.
5. You must scan the string **only once** (no nested loops).

INPUT EXAMPLES:

    reverse_unique("abcde")   → "edcba"
    reverse_unique("a")       → "a"
    reverse_unique("")        → ""
    reverse_unique("abca")    → ❌ raises ValueError

CONSTRAINTS:
    - Use a single-pass scan with a set for detection.
    - Manual reversal only — use a loop to construct the reversed string.
    - Be precise in exception message and handling.

BONUS:
    - Add assert-based tests for empty string, one-char string, and duplicate detection.
"""
def reverse_unique (s: str) -> str:

    if s == "":
        return ""
    
    seen = set()
    reversed = ""
    for char in s:
        if char in seen:
            return ValueError ("Dupplicate characters not allowed")
        seen.add(char)
        reversed = char + reversed

    return reversed

        
print(reverse_unique("aabcde"))