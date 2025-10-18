"""
You receive a list of (category, item) tuples, e.g.:

[
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "kiwi"),
    ("vegetable", "onion")
]

Write a function `group_items_by_category(pairs: list[tuple[str, str]]) -> dict[str, list[str]]`
that returns a dictionary grouping all items under their category:

{
    "fruit": ["apple", "banana", "kiwi"],
    "vegetable": ["carrot", "onion"]
}

Rules:
- Preserve the order of insertion (Python 3.7+ dicts do).
- Use `.setdefault()` or `defaultdict(list)` to make it efficient.
- Avoid multiple passes over the list.
- Don’t import pandas or any external libraries.

Be quick and precise — this pattern appears constantly in data aggregation and ETL logic.
"""

# Using .setdefault(dict)
def group_items_by_category(l: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Group items by category using dict.setdefault().

    The method works like this:
    1. Check if the key (category) exists in the dictionary.
    2. If it doesn’t, insert it and create an empty list for that category.
    3. Return the list corresponding to the key, allowing direct appending of the item.
    """
    group = {}
    for cat, item in l:
        group.setdefault(cat, []).append(item)
    return group

# Using defaultdict(list)

def group_items_by_category_defaultdict(l: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Group items by category using collections.defaultdict(list).

    This approach automatically initializes an empty list for any new category,
    so you can append items directly without checking for key existence.
    """
    from collections import defaultdict

    group = defaultdict(list)
    for cat, item in l:
        group[cat].append(item)
    return dict(group)


print(group_items_by_category([
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "kiwi"),
    ("vegetable", "onion")
]))