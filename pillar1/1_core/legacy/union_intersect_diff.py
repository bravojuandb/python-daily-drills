"""
You are given two SETS of students:

class_A = {"Alice", "Bob", "Charlie", "Diana"}
class_B = {"Charlie", "Eve", "Frank", "Alice"}

1. Find the union of students (all unique names).
2. Find the intersection (students in both classes).
3. Find the difference (students in class_A but not in class_B).

Return them as a tuple of three sets, in the order (union, intersection, difference).

Example:
expected = (
    {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"},
    {"Alice", "Charlie"},
    {"Bob", "Diana"}
)
"""

# Option A

def find_union(set_a: set, set_b:set) -> set:
    return set_a.union(set_b)

def find_intersection(set_a: set, set_b:set) -> set:
    return set_a.intersection(set_b)

def find_difference(set_a: set, set_b:set) -> set:
    return set_a.difference(set_b)

class_A = {"Alice", "Bob", "Charlie", "Diana"}
class_B = {"Charlie", "Eve", "Frank", "Alice"}

print(find_union(class_A, class_B))
print(find_intersection(class_A, class_B))
print(find_difference(class_A, class_B))

# Option B

union = class_A | class_B
intersection = class_A & class_B
difference = class_A - class_B

print(union)
print(intersection)
print(difference)