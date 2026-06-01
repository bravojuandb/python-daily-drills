"""
Drill 09 - Zip Combiner

Write a function:
    combine_scores(usernames: list[str], scores: list[int]) -> dict[str, int]

Requirements:
1. Use `zip()` to combine the lists.
2. Convert the result into a dictionary.
3. Normalize each username by stripping surrounding whitespace.
4. If the input lists have different lengths, raise `ValueError`.

Example:
>>> combine_scores([" Alice ", "Bob", " Carla"], [85, 92, 78])
{'Alice': 85, 'Bob': 92, 'Carla': 78}

Thinking goal:
This drill is about pairing aligned data cleanly while still guarding against silent mismatch.
"""
