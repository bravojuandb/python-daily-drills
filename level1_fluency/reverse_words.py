"""
Write a function that reverses the order of words in a sentence.
A word is any group of characters separate by spaces.
Preserve the words exactly - don't reverse the letters.

"""

def reverse_words(sentence: str) -> str:
    reversed_words = reversed(sentence.split())
    reversed_string= ' '.join(reversed_words)
    return reversed_string

print(reverse_words("Los dias son largos y las noches interminables"))



