"""
You are given this function:

    def contains_duplicate(items: list[int]) -> bool:
        seen = set()
        for x in items:
            if x in seen:
                return True
            seen.add(x)
        return False

Estimate its **time complexity (Big-O)** and **space complexity** 
without running the code.

Then justify your reasoning in one line.

Be quick and precise — aim to reason it mentally like an engineer in an interview.
"""


"""
I'm asked to reason about the time complexity of this function.

There is only one loop, which tells me the function is not very complex.
This means the function iterates through the list only once.
Checking for the presence of an element in a set does not make it slower,
since set lookups are O(1) on average.
Therefore, the time complexity is O(n), meaning the runtime grows
directly in proportion to the number of elements.

"""