"""
Quick challenge — Merge Two Lists Alternately

You’re given two lists:
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]

Task:
1. Create a new list where elements from both lists are merged *alternately*.
   Expected pattern: ["Alice", 85, "Bob", 92, "Charlie", 78]
2. The function must handle lists of *different lengths* gracefully 
   (remaining elements from the longer list should be added at the end).
3. Return the merged list.

⚡️ Be quick and precise — this drill tests your mastery of iteration and indexing logic.
"""

names = ["Alice", "Bob", "Charlie", "juan"]
scores = [85, 92, 78]

from typing import Any

names = ["Alice", "Bob", "Charlie", "juan"]
scores = [85, 92, 78]

def merge_lists(keys: list[str], vals: list[int]) -> list[Any]:
    if len(keys) != len(vals):
        print("Lists have different lengths!")

    result = []
    for i in range(max(len(keys), len(vals))):
        if i < len(keys):
            result.append(keys[i])
        if i < len(vals):
            result.append(vals[i])
    return result

if __name__ == "__main__":
    merged = merge_lists(names, scores)
    print("Merged result:", merged)

