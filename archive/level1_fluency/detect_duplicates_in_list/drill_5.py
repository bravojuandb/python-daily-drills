"""
Write a function count_all_duplicates(lst) that returns a dictionary with:
	•	Keys: the elements that appear more than once
	•	Values: the number of times they occur

    >>> count_all_duplicates([1, 2, 2, 3, 1, 1])
{1: 3, 2: 2}

>>> count_all_duplicates(["a", "b", "a", "c", "b", "b"])
{'a': 2, 'b': 3}

>>> count_all_duplicates(["x", "y", "z"])
{}

	•	Return only elements that appear 2 or more times
	•	Dictionary format: {element: count}
	•	Don’t use collections.Counter (this is Pillar 1 — core logic practice)
	•	Must run in O(n) time

"""

def count_all_duplicates(l:list) -> dict:

    counts = {}

    for item in l:
        counts[item] = counts.get(item, 0) + 1

    duplicates = {k: v for k, v in counts.items() if v > 1}
    return duplicates

print(count_all_duplicates(["a", "b", "a", "c", "b", "b"]))
{'a': 2, 'b': 3}

