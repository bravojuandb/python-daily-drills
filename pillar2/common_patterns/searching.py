"""
Problem — Searching (efficient lookup)

You’re given a **sorted list of IDs** (integers), for example:

ids = [3, 7, 9, 12, 18, 21, 25, 30, 44, 57, 60]

Task:
1️⃣ Implement **linear_search(ids, target)**:
    - Scan from left to right.
    - Return the index if found, otherwise -1.
    - O(n) time.

2️⃣ Implement **binary_search(ids, target)**:
    - Use left, right, and mid indexes.
    - Repeatedly halve the search range.
    - Return the index if found, otherwise -1.
    - O(log n) time.

3️⃣ For both functions, print:
       Found at index X
       or
       Not found

Bonus:
- Count and print how many steps each algorithm took.
- Show the performance difference for random targets.
- Raise a TypeError if `ids` is not sorted (optional).

Reminder:
- Linear search → brute force (check each item).
- Binary search → divide the list in half repeatedly.

"""

def linear_search(nums: list[int], target: int) -> int:
    """
    Scan a list of integers from left to right
    Return the index if found, otherwise  -1

    """
    if not isinstance(target, int):
        raise TypeError("xtarget must be an integer")
    elif not isinstance(nums, list):
        raise TypeError("nums must be a list of integers")
    
    for i, num in enumerate(nums):
        if num == target:
            print(f"found at index: {i}")
            return i
        
    print("target not found")
    return -1



def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = nums[mid]

        if mid_value == target:
            print("Found the target")
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print("target not found")
    return -1



ids = [3, 7, 9, 12, 18, 21, 25, 30, 44, 57, 60]

print(binary_search(ids, 18))