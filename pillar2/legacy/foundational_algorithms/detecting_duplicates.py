"""
# Pillar 2 — Foundational Algorithms
## Detecting Duplicates → sets

You are given a list of items:
items = ["apple", "banana", "orange", "apple", "kiwi", "banana"]

TASK:
1. Detect whether the list contains any duplicates.
2. Return:
   - True if duplicates exist
   - False otherwise

HINT:
Use the property that sets cannot contain duplicate elements.

Example:
Output → True  (because "apple" and "banana" repeat)

⏱️ Be quick and precise. Focus on how `len()` behaves with sets.
"""

def detect_duplicates_simple(l: list[str]) -> bool:
    items = set(l)
    if len(items) != len(l):
        return True
    else:
        return False



# Using a for loop

from typing import TypeVar

T = TypeVar("T", bound=hash)

def detect_duplicates(l: list[T]) -> bool:
    seen = set()
    for i in l:
        if i in seen:
            return True
        seen.add(i)
    return False

items = ["apple", "banana", "orange", "apple", "kiwi", "banana"]

print(detect_duplicates(items))
