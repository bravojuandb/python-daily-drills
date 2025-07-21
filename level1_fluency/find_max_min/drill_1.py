"""
Drill Name: find_max_min.py
Pillar: Pillar 1 – Fluency & Logic
Level: Hard

Problem Statement:

Write a function `find_second_min_max(nums: list[int]) -> tuple[int, int]`  
that returns a tuple with the **second smallest** 
and **second largest** values in a list of integers.

But here's the twist:

- You **may not use** Python built-in sorting functions (`sorted()`, `.sort()`).
- You **may not use** `min()` or `max()` more than once each.
- You must **filter manually** using loops or comprehensions.
- The input list may contain **duplicates**, 
	which must be ignored in determining second smallest/largest.
- If no second min/max exists (e.g., all values are the same or 
	only one unique element), raise a `ValueError`.

Example:

    nums = [5, 3, 9, 1, 9, 5, 3, 1]
    result = find_second_min_max(nums)
    print(result)

    Expected Output:
    (3, 5)

    # Explanation:
    # Unique values: [1, 3, 5, 9]
    # 2nd smallest = 3
    # 2nd largest = 5

Constraints & Edge Cases:

- Empty list → raise `ValueError("Empty list")`
- Less than 2 unique elements → raise `ValueError("Not enough unique values")`
- Input list may be very large → avoid O(n²) solutions

Bonus Challenge:

Use only **one full pass** to compute `min` and `max`, 
then **one additional pass** to compute the second min/max via filtering.

⏱ Target Time:
20–25 minutes
"""

def find_second_min_max(nums: list[int]) -> tuple[int, int]:
    if not nums:
        raise ValueError("Empty list")
    
    unique = set(nums)
    if len(unique) < 2:
        raise ValueError("Not enough unique values")

    # One pass to find min and max
    iterator = iter(unique)
    first = next(iterator)
    min_val = max_val = first

    for num in unique:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # One pass to find second min and second max
    second_min = second_max = None

    for num in unique:
        if num != min_val:
            if second_min is None or num < second_min:
                second_min = num
        if num != max_val:
            if second_max is None or num > second_max:
                second_max = num

    if second_min is None or second_max is None:
        raise ValueError("Not enough unique values")

    return (second_min, second_max)

    


nums = [5, 3, 9, 1, 9, 5, 3, 1]
result = find_second_min_max(nums)
print(result)