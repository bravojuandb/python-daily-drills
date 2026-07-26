"""
Drill 08 - Reliable Microbenchmark

Write benchmark_membership(size, repeats) -> dict[str, float]. Build equivalent
list and set data before timing. Use time.perf_counter to time repeated absent
membership checks. Return seconds under "list" and "set".

Validate positive arguments, avoid printing inside timed loops, run the same
number of checks, and explain why several runs are more trustworthy than one.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: a benchmark must isolate the operation it claims to compare.
"""


def benchmark_membership(size: int, repeats: int) -> dict[str, float]:
    pass
