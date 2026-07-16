"""
Write a function `test_slice_copy_vs_reference()` that demonstrates
the difference between **copying a list by slicing** and **creating a reference**.

Steps:
1. Create a list `a = [1, 2, 3, 4]`.
2. Assign `b = a` (reference) and `c = a[:]` (slice copy).
3. Modify one element in `a` (for example, `a[0] = 99`).
4. Print all three lists and observe which ones changed.

Expected insight:
- `b` will reflect the change because it references the same object.
- `c` will not change because slicing creates a shallow copy.

Be quick and precise — the goal is to *see* Python’s memory behavior.
"""

def test_slice_copy_vs_reference():
    a = [x for x in range(10)] 
    b = a          # a reference, a new name pointing to the same object
    c = a[:]       # shallow copy

    a[0] = 99      # mutate the original list

    print("a:", a)
    print("b:", b, "<-- same object")
    print("c:", c, "<-- independent copy")

    print(a is b)  # True — same object
    print(a is c)  # False — new object



print(test_slice_copy_vs_reference())

"""
Conclusions:

•	Timing: When you do a[:], the copy happens at that exact moment — it takes a snapshot of the current elements.
•	Mutations afterward don’t affect the copy.
•	References (b = a) always stay tied to whatever object they point to.

"""