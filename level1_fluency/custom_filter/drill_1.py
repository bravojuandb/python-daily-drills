"""
WARMUP VERSION — CHALLENGE PROPOSITION

Write a function `custom_filter(predicate, values)` 
that mimics the behavior of Python’s built-in `filter`, using only basic Python.

Rules:
1. `predicate` is a function that receives a single argument and returns True or False.
2. `values` is a list of elements.
3. Return a **new list** containing only the elements for which `predicate(element)` returns True.
4. Do **not** use the built-in `filter()` or list comprehensions.
5. Use only `for` loops and `if` statements.
6. You may assume the inputs are valid (no need to check types).

EXAMPLES:

    def is_even(x): return x % 2 == 0
    custom_filter(is_even, [1, 2, 3, 4]) → [2, 4]

    custom_filter(lambda x: x > 0, [-2, 0, 5, 10]) → [5, 10]
"""

def is_even (num:int) -> bool:
        return num % 2 == 0

def custom_filter (predicate:bool, values:list) -> list:
    
    result = []
    for value in values:
        if predicate(value):
            result.append(value)
    return result


print(custom_filter(is_even, [1, 2, 3, 4]))