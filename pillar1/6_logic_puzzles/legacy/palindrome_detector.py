"""
Write a function is_palindrome(text: str) -> bool:

Rules:
- A palindrome reads the same forward and backward.
- Ignore case (e.g., "Racecar" → True).
- Ignore spaces (e.g., "nurses run" → True).
- Use slicing [::-1] for the reversal check.

Examples:
is_palindrome("Racecar") → True
is_palindrome("hello") → False
is_palindrome("nurses run") → True
"""

# According to the problem statement:
def is_palinndrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# SOlution using pointers and while loop
def is_palinndrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    left, right = 0, len(cleaned) -1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palinndrome("racecar"))
print(is_palinndrome("nurses run"))
print(is_palinndrome("hello"))