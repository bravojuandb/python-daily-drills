"""
Drill — Benchmark List vs Set Lookup

Measure how long it takes to check membership in a list vs a set using time.perf_counter().

Goal:
Show empirically that `in` lookups are O(n) for lists, but O(1) for sets (on average).
"""

import time

items = list(range(1_000_000))
items_set = set(items)

# how many times we'll repeat the membership test
N = 1_000_000

start = time.perf_counter()
for _ in range(N):
    999 in items
list_time = time.perf_counter() - start
print("List lookup total:", list_time)

start = time.perf_counter()
for _ in range(N):
    999 in items_set
set_time = time.perf_counter() - start
print("Set lookup total:", set_time)

print("Ratio (list / set):", list_time / set_time)


"""
Concept Summary — O(n) vs O(1)

In Python:
- 'in' for lists → O(n)
- 'in' for sets  → O(1) average case

Explanation:
O(n) means linear time — the operation gets slower as the list grows.
Python must scan each element one by one until it finds a match (or reaches the end).

O(1) means constant time — the operation takes roughly the same time regardless of size.
Sets (and dicts) use a hash table:
    - The value is hashed to find its "bucket"
    - Python jumps directly to that bucket and checks membership
    - No full scan needed

Why it matters:
For small collections, the difference is invisible.
For millions of items, O(1) lookups (sets) are hundreds of times faster than O(n) lookups (lists).

Memory tip:
O(n): “I must check everything.”
O(1): “I jump straight to it.”
"""