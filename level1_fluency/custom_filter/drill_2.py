"""
🎯 CHALLENGE PROPOSITION

Write a function `custom_filter(predicate, values)` that mimics the behavior of Python’s built-in `filter`,
but with the following custom rules:

1. `predicate` is a function that receives a single argument and returns True or False.
2. `values` is a list of mixed values (strings, ints, floats, bools, etc.).
3. The function should return a **new list** containing only the elements for which `predicate(element)` returns True.
4. Do **not** use the built-in `filter()` function or list comprehensions.
5. Use only basic control structures: `for`, `if`, function calls.
6. Your implementation must not mutate the original list.

Additionally:

- You must support **anonymous functions (lambdas)** as `predicate` inputs.
- You must validate that `predicate` is callable and raise a `TypeError` if not.
- If `values` is not iterable, raise a `TypeError`.

📥 INPUT EXAMPLES:

    def is_str(x): return isinstance(x, str)
    
    custom_filter(is_str, [1, "a", True, "b", 3.14]) → ["a", "b"]

    custom_filter(lambda x: x > 10, [5, 15, 3, 22]) → [15, 22]

🧠 CONSTRAINTS:
    - Do not use list comprehensions or built-in filter().
    - Only basic loops and conditionals.
    - Code must be wrapped in a clean, testable function.

🧪 BONUS:
    Write 2–3 test cases using `assert` to confirm behavior.
"""