"""
Find the First Duplicate with Index

Write a function first_duplicate_with_index(lst) that:
	•	Returns the first element that appears twice, along with its second index.
	•	If no duplicate is found, return None.

>>> first_duplicate_with_index([1, 2, 3, 2, 1])
(2, 3)      # 2 is the first duplicate; second appearance is at index 3

>>> first_duplicate_with_index(["a", "b", "c", "a"])
('a', 3)

>>> first_duplicate_with_index([1, 2, 3])
None

	•	Return a tuple: (duplicate_value, index_of_second_occurrence)
	•	Use set for tracking
	•	Must be linear time O(n)
	•	No imports

"""

def first_duplicate_with_index(l:list) -> tuple:

    seen = set()

    for i, val in enumerate(l):
        if val in seen:
            return (val, i)
        seen.add(val)

    return None

print(first_duplicate_with_index([1, 2, 3, 2, 1]))

