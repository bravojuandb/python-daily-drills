"""
Drill 07 - Map Function Mapper

Write a function:
    map_words(words: list[str]) -> tuple[list[str], list[int]]

Requirements:
1. Use `map()` with `str.upper` to create an uppercase version of the words.
2. Use `map()` again to create a list of word lengths.
3. Return `(uppercase_words, word_lengths)`.

Example:
>>> map_words(["python", "rocks", "map", "function"])
(['PYTHON', 'ROCKS', 'MAP', 'FUNCTION'], [6, 5, 3, 8])

Thinking goal:
This drill is about noticing when an existing function is clearer than writing a fresh loop.
"""
