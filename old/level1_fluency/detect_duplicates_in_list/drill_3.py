"""
Check If All Elements Are Unique

Problem

Write a function all_unique(lst) 
that returns True only if all elements in the list are unique, 
and False otherwise.

This is the inverse of has_duplicates() — but let's build it fresh to sharpen fluency.

>>> all_unique([1, 2, 3, 4])
True

>>> all_unique([1, 2, 2, 3])
False

>>> all_unique(["a", "b", "c"])
True

>>> all_unique(["a", "b", "a"])
False

Requirements
	•	Use a set to check for duplicates.
	•	Must run in O(n) time.
	•	No imports.
"""

def all_unique(l:list) -> bool:
    seen = set()

    for char in l:
        if char in seen:
            return False
        seen.add(char)
    return True

print(all_unique(["a", "b", "c"]))

assert all_unique(["a", "b", "c"]) == True