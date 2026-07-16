"""
Challenge — Compare Memory Use Across Data Structures

Task:
1. Import `sys`.
2. Create the following data structures, each containing 100 items:
   - list of integers 0–99
   - tuple of integers 0–99
   - set of integers 0–99
   - dict mapping each integer to its square
   - list of small dicts like {"n": i, "square": i**2}
3. Use `sys.getsizeof()` to measure the memory size (in bytes) of each container.
4. Print a neatly aligned summary sorted from smallest to largest, for example:

   tuple:            904 bytes
   list:             912 bytes
   set:             3240 bytes
   dict:            4728 bytes
   list_of_dicts:   8056 bytes

Remember:
- Measure only the top-level container, not the total recursive size.
- Focus on clarity and precision.
"""

import sys

a = [x for x in range(100)]

b = tuple(x for x in range(100))

c = {x for x in range(100)}

"""
inefficient way:
e = {}
for num in range(100):
    e[num] = e.get(num, 0) + num ** 2
"""

d = {num: num **2 for num in range(100)}

e = [{"n": i, "square": i**2} for i in range(100)]

sizes = {
    "list": sys.getsizeof(a),
    "tuple": sys.getsizeof(b),
    "set": sys.getsizeof(c),
    "dict": sys.getsizeof(d),
    "list_of_dicts": sys.getsizeof(e),
}

# Sort by memory usage and print neatly
for name, size in sorted(sizes.items(), key=lambda x: x[1]):
    print(f"{name:15}: {size} bytes")

