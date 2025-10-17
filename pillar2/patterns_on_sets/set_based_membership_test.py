"""
🚀 Challenge — Set-Based Membership Speed Test

You are analyzing two collections:

    users_list = list(range(1_000_000))
    users_set  = set(users_list)

Write a short script that measures and compares **lookup speed** when checking if
the number `999_999` is present in both the list and the set.

Requirements:
1. Use the `time` or `%timeit` approach to measure the duration of `999_999 in users_list`
   versus `999_999 in users_set`.
2. Print or log both timings clearly.
3. Explain (in a single print statement) *why* the set lookup is faster.

💡 Be quick and precise — focus on *time complexity*, not syntax tricks.
"""


users_list = list(range(1_000_000))
users_set  = set(users_list)

import time

start = time.time()
999_999 in users_list
end = time.time()

print("List lookup time:", end - start)

start = time.time()
999_999 in users_set
end = time.time()

print("Set lookup time:", end - start)

print("Set lookup is faster because it uses O(1) hash table lookups, while list lookup is O(n) linear search.")


import timeit

# Measure lookup times over 100 runs each
list_time = timeit.timeit(lambda: 999_999 in users_list, number=100)
set_time = timeit.timeit(lambda: 999_999 in users_set, number=100)

print("List lookup time:", list_time)
print("Set lookup time:", set_time)
print("Set lookup is faster because it uses O(1) hash table lookups, while list lookup is O(n) linear search.")