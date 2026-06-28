"""
Drill 02 - Palindrome Detector

Write a function:
    is_palindrome(text: str) -> bool

Requirements:
1. Ignore case.
2. Ignore spaces and punctuation, not just plain spaces.
3. Treat digits as meaningful characters.
4. Return `True` only if the cleaned text reads the same forward and backward.
5. An empty cleaned string should return `True`.

Example:
>>> is_palindrome("Racecar")
True
>>> is_palindrome("nurses run")
True
>>> is_palindrome("A man, a plan, a canal: Panama!")
True
>>> is_palindrome("No lemon, no melon 123")
False
>>> is_palindrome("hello")
False

Challenge bar:
- Build the cleaned text deliberately before checking it.
- Use slicing `[::-1]` for the final reversal check.

Thinking goal:
This drill is about defining exactly what counts as signal before checking symmetry.

"""


def is_palindrome(text: str) -> bool:

    cleaned = ""
    
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    text_inverted = cleaned[::-1]

    return cleaned == text_inverted


if __name__ == "__main__":

    texts = [
    "       Racecar",
    "nurses run",
    "A man, a plan, a canal: Panama!",
    "No lemon, no melon 123",
    "hello",
    "Was it a car or a cat I saw?",
    "12321",
    "12345",
    "Madam, I'm Adam.",
    "",
    ]
    for text in texts:
        solved = is_palindrome(text)

        print(f"{repr(text)} --> is palindrome? :  {solved}")
