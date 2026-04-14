"""
Drill 14 - Union, Intersection, Difference

Write a function:
    compare_groups(group_a: set[str], group_b: set[str]) -> tuple[set[str], set[str], set[str]]

Requirements:
1. Return a tuple with:
   - the union of both groups
   - the intersection of both groups
   - the items that appear in `group_a` but not in `group_b`
2. Use set operations directly.

Example:
>>> compare_groups({"Alice", "Bob"}, {"Bob", "Eve"})
({"Alice", "Bob", "Eve"}, {"Bob"}, {"Alice"})

Thinking goal:
This is about choosing the right data structure and using its strengths directly.
"""
