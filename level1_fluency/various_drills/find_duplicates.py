"""
+++
Detect Duplicates in a String (introductory to longest unique substring)

Write a function that returns True if any character appears more than once in the string.

"""

def print_seen(s:str):
    """
    Explains how set() don't include repeated characters
    """
    seen = set()
    for char in s:
        seen.add(char)
        print(f"{char} ----> {seen}")

def find_duplicates(s:str) -> bool:
    """
    Returns True if the string contains a duplicate character
    """
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)



print(find_duplicates("abccdef"))