"""
You are given a list of product prices: [199, 49, 350, 120, 75].

1. Sort the list in ascending order using .sort().
2. Create a new list with the same prices but sorted in descending order using sorted().
3. Return both lists as a tuple (asc, desc).

⚡ Be quick — just code and return the result, no explanations.
"""




def sort_ascending(items:list[int]) -> list[int]:
    items.sort()
    return items

def sort_descending(items:list[int]) -> list[int]:
    return sorted(items, reverse=True)

def sorted_twice(items: list[int]) -> tuple:
    srtd_desc = sorted(items, reverse=True)
    srtd_asc = sorted(items)
    return srtd_asc, srtd_desc


products = [199, 49, 350, 120, 75]

print(sort_ascending(products))
print(sort_descending(products))
print(sorted_twice(products))