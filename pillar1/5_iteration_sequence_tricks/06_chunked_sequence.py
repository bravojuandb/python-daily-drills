"""
Drill 06 - Chunked Sequence

Write a function:
    chunk_items(items: list[int], size: int) -> list[list[int]]

Requirements:
1. Split the input into consecutive chunks of length `size`.
2. If the final chunk is shorter, keep it.
3. Preserve the original order.
4. You may use slicing inside a loop.
5. If `size` is less than `1`, raise `ValueError`.

Example:
>>> chunk_items([1, 2, 3, 4, 5], 2)
[[1, 2], [3, 4], [5]]

Thinking goal:
This drill is about stepping through a sequence in controlled jumps without dropping leftovers.
"""
