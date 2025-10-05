"""
Problem: Sorting Dicts by Value

You are given a dictionary of students and their scores.  
Write a function `sort_scores(data)` that returns a list of tuples `(name, score)`  
sorted in **descending order of score**.  
If two students have the same score, sort them **alphabetically by name**.

Example:
    Input:
        {"Alice": 92, "Bob": 85, "Charlie": 92, "Dave": 70}
    Output:
        [("Alice", 92), ("Charlie", 92), ("Bob", 85), ("Dave", 70)]

Rules:
- You must use `sorted(data.items(), key=...)` with a proper key function.
- Do not modify the input dictionary.
- Aim for minimal, expressive code.

Be quick and precise — elegance matters more than length.
"""

def sort_scores(data: dict) -> list:

    return sorted(data.items(), key= lambda item: item[1], reverse= True)

scores = {"Alice": 92, "Bob": 85, "Charlie": 92, "Dave": 70}

print(sort_scores(scores))
