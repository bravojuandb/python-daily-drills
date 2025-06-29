"""
Write a function that takes alist of integers
and returns a new list with duplicates removed,
preserving the original order of elements.

"""

def remove_duplicates(nums: list[int]) -> list[int]:
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique


def remove_duplicates(nums: list[int]) -> list[int]:
    # Set to keep track of seen elements (for fast O(1) lookups)
    seen = set()
    # List to store the result while preserving original order
    result = []
    
    for num in nums:
        # Only add the number if it hasn't been seen before
        if num not in seen:
            seen.add(num)         # Mark the number as seen
            result.append(num)    # Add it to the result list
            
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))