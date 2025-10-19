"""
Challenge: Swap Values Between Dictionary Keys via Tuple Unpacking

You are given a dictionary `student_scores` where each key is a student's name 
and each value is their score.

Example:
    student_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78
    }

Write a function `swap_scores(data: dict[str, int], key1: str, key2: str) -> dict[str, int]`
that swaps the scores of the two given students **using tuple unpacking** — no temporary variable allowed.

Example:
    swap_scores(student_scores, "Alice", "Bob")
    # → {"Alice": 92, "Bob": 85, "Charlie": 78}

Rules:
- Don’t use `temp`, `copy()`, or any helper dict.
- Modify the existing dict in place and return it.
- Be ready for potential missing keys (decide what to do).

⚡️ Be quick and precise: write the cleanest, most Pythonic version possible.
Then explain what happens under the hood when tuple unpacking runs on dictionary values.
"""

def swap_scores(data: dict[str, int], key1: str, key2: str) -> dict[str, int]:
    if key1 not in data or key2 not in data:
        raise KeyError("One or both keys not found in the dictionary")
    data[key1], data[key2] = data[key2], data[key1]
    return data

student_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78
}

print(swap_scores(student_scores, "Alice", "Bob"))