"""
Drill 07 - Map Function Mapper

Write a function:
    normalize_usernames(usernames: list[str]) -> tuple[list[str], list[str]]

Requirements:
1. Use `map()` with `str.strip` to remove surrounding whitespace from each username.
2. Use `map()` again to create a lowercase version of the stripped usernames.
3. Return `(stripped_usernames, lowercased_usernames)`.

Example:
>>> normalize_usernames(["  Alice  ", "BOB", "  Carla"])
(['Alice', 'BOB', 'Carla'], ['alice', 'bob', 'carla'])

Thinking goal:
This drill is about noticing when an existing function is clearer than writing a fresh loop.
"""


def normalize_usernames(usernames: list[str]) -> tuple[list[str], list[str]]:

    stripped = list(map(str.strip, usernames))
    lowercased = list(map(str.lower, stripped))

    return stripped, lowercased


if __name__ == "__main__":
    names = ["  Alice  ", "BOB", "  Carla"]
    print(normalize_usernames(names))