"""
Drill 02 - Palindrome Detector

Write a function:
    is_palindrome(text: str) -> bool

Requirements:
1. Ignore case.
2. Ignore spaces.
3. Use slicing `[::-1]` for the reversal check.
4. Return `True` if the cleaned text reads the same forward and backward.

Example:
>>> is_palindrome("Racecar")
True
>>> is_palindrome("nurses run")
True
>>> is_palindrome("hello")
False

Thinking goal:
This drill is about spotting that normalization is part of the puzzle, not a side detail.
"""
