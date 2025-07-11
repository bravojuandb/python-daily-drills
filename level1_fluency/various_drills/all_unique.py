"""
Write a function that takes a list of integers,
and returns True if all elements are unique (i.e., no duplicates),
and False otherwise.
"""

def all_unique (l:list[int]) -> bool:
    """Returns True if all numbers in the list are unique, 
    otherwise returns False
    """
    return len(set(l)) == len(l)

list = [1,2,3,4,5,5,6,7]

result = all_unique(list)

print(result)