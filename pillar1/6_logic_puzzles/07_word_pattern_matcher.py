"""
Drill 07 - Word Pattern Matcher

Write a function:
    matches_pattern(pattern: str, words: str) -> bool

Requirements:
1. `pattern` is a string like `"abba"`.
2. `words` is a space-separated string like `"dog cat cat dog"`.
3. Return `True` only if each pattern character maps to exactly one word, and each word maps back to exactly one character.
4. If the lengths do not match, return `False`.
5. Repeated spaces in `words` should not create empty words.

Example:
>>> matches_pattern("abba", "dog cat cat dog")
True
>>> matches_pattern("abba", "dog cat cat fish")
False
>>> matches_pattern("aaaa", "dog cat cat dog")
False
>>> matches_pattern("abba", "dog dog dog dog")
False
>>> matches_pattern("", "")
True

Challenge bar:
- Checking only `pattern -> word` is not enough.
- Keep the two directions consistent throughout the scan.

Thinking goal:
This drill is about detecting when two sequences have the same shape, not just the same length.
"""

def matches_pattern(pattern: str, words: str) -> bool:

    word_list = words.split()

    if len(pattern) != len(word_list):
        return False

    word_to_char = {}
    char_to_word = {}
        
    for char, word in zip(pattern, word_list):
        if char in char_to_word and char_to_word[char] != word:
            return False

        if word in word_to_char and word_to_char[word] != char:
            return False

        char_to_word[char] = word
        word_to_char[word] = char

    return True

if __name__ == "__main__":

    print(matches_pattern("abba", "dog cat cat dog"))
    print(matches_pattern("abba", "dog cat cat fish"))
    print(matches_pattern("aaaa", "dog cat cat dog"))
    print(matches_pattern("abba", "dog dog dog dog"))
    print(matches_pattern("", ""))                          

