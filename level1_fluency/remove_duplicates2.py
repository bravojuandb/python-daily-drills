"""
Write a function that removes duplicates from a list without changing the order of the elements.

	•	Don't use set(nums) — it won't preserve order
	•	Use a loop + a helper structure like a set or another list

"""

from collections import Counter

def remove_duplicates(nums: list[int]) -> list[int]:
    counts = Counter(nums)
    single_nums = []
    dictionary = counts.items()
    for i, j in dictionary:
        single_nums.append(i)
    return single_nums

def remove_duplicates(nums: list[int]) -> list[int]:
    return list(Counter(nums).keys())

def remove_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates([5, 4, 1, 2, 2, 3, 1]))

