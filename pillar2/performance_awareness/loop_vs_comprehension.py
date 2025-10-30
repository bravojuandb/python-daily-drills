"""
Drill — Compare Loop vs Comprehension Runtime

You want to test how much faster a list comprehension is compared to
a regular for-loop when building a new list from a large dataset.

Task:
1. Generate a list of one million integers:
       data = list(range(1_000_000))

2. Build a new list containing the square of each number in two different ways:
   A) Using a for-loop with .append()
   B) Using a list comprehension

3. Measure the runtime of each method using time.perf_counter().

Expected outcome:
- Both produce the same result, but one is significantly faster.
- Think about *why* the comprehension might outperform the loop.

Your function should print both runtimes and the ratio.
Be quick, be precise — timing experiments are about structure, not syntax.
"""

import time

data = list(range(1_000_000))

# Loop -------------------------------
start = time.perf_counter()
result = []
for x in data:
    result.append(x * x)
loop_time = time.perf_counter() - start

print("\n loop time:", loop_time)


# Comprehension ----------------------
start = time.perf_counter()
result = [x * x for x in data]
comprehension_time = time.perf_counter() - start

ratio = loop_time / comprehension_time
print(f"\nLoop time: {loop_time:.6f}")
print(f"Comprehension time: {comprehension_time:.6f}")
print(f"\nThis loop is {ratio:.2f}× slower than comprehension.")
print(f"This comprehension is {ratio:.2f}× faster than the loop.\n")