"""
First Repeated Character

Write a function that returns the first character in a string that appears more than once.
If there's no repetition, return None.

"""

def first_repeated_character(s:str) -> None:
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_repeated_character("advfr"))