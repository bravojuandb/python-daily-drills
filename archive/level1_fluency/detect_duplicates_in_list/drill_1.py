"""
Problem Statement

Write a function has_duplicates(lst) 
that returns True if the list contains any duplicate elements, 
and False otherwise.

>>> has_duplicates([1, 2, 3, 4])
False

>>> has_duplicates([1, 2, 3, 2])
True

>>> has_duplicates([])
False

>>> has_duplicates(["a", "b", "a"])
True

	•	Use a set to track seen elements (optimal way)
	•	Must run in linear time O(n)
	•	No imports allowed

"""

def has_duplicates(l: list) -> bool:
    seen = set()
    for char in l:
        if char in seen:
            return True
        seen.add(char)
    return False

# Test the function visually
print(has_duplicates([1, 2, 2, 3, 4]))

# Assert tests (will raise errors if they fail)
assert has_duplicates([1, 2, 3, 4]) == False
assert has_duplicates([1, 2, 3, 2]) == True
assert has_duplicates([]) == False
assert has_duplicates(["a", "b", "a"]) == True
assert has_duplicates(["apple", "banana", "apple", "cherry"]) == True