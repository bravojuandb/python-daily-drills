"""
🧠 list_diff.py

Write a function `list_diff(list1, list2)` that returns a list containing all the elements that are in
`list1` but not in `list2`, **preserving the original order** and **excluding duplicates** in the output.

The function should:
- Only consider items that are not in list2.
- Keep the original order from list1.
- Ensure the returned list has no repeated elements.

Examples:
>>> list_diff([1, 2, 2, 3, 4], [2, 4, 5])
[1, 3]

>>> list_diff(['apple', 'banana', 'apple', 'cherry'], ['banana'])
['apple', 'cherry']

>>> list_diff([], [1, 2])
[]

>>> list_diff([1, 2, 3], [])
[1, 2, 3]

Constraints:
- Don't use `set` to solve the entire problem — order matters.
- You may use set() to track duplicates *in the result*, not to filter list1 directly.
"""

def list_diff(list1:list, list2:list) -> list:

    seen = set()
    elements = []
    for item in list1:
        if item not in list2 and item not in seen:
            elements.append(item)
            seen.add(item)

    return elements

print(list_diff(['apple', 'banana', 'apple', 'cherry'], ['banana']))

