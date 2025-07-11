"""
Return All Duplicates in a List (Ordered, No Repeats)

Write a function get_duplicates(lst) that returns a list 
of all elements that appear more than once, 
in the order of their first duplicate appearance. 
Each duplicate should appear only once in the result.

>>> get_duplicates([1, 2, 3, 2, 1, 4])
[2, 1]

>>> get_duplicates(["a", "b", "a", "c", "b"])
['a', 'b']

>>> get_duplicates([1, 2, 3])
[]

	•	Maintain the order of first appearance of the duplicates.
	•	Only return each duplicate once.
	•	Use no imports.
	•	Optimize for clarity and performance (avoid nested loops).

"""

def get_duplicates(l:list) -> list:

    seen = set() 
    duplicates = []
    added = set() # Prevents repeated characters to be added to the list

    for char in l:
        if char in seen and char not in added:
            duplicates.append(char)
            added.add(char)
        else:
            seen.add(char)
    return duplicates


assert get_duplicates([1, 2, 3, 2, 1, 4]) == [2, 1], "Failed on [1, 2, 3, 2, 1, 4]"
assert get_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"], "Failed on ['a', 'b', 'a', 'c', 'b']"
assert get_duplicates([1, 2, 3]) == [], "Failed on [1, 2, 3]"
assert get_duplicates([]) == [], "Failed on empty list"
assert get_duplicates(["a", "a", "a", "a"]) == ["a"], "Failed on ['a', 'a', 'a', 'a']"
assert get_duplicates(["x", "y", "z", "x", "z", "x"]) == ["x", "z"], "Failed on ['x', 'y', 'z', 'x', 'z', 'x']"