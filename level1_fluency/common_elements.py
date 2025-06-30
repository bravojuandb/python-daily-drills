"""
Write a function that returns the common elements (no duplicates) between two lists of integers.

	•	Preserve order from the first list (a)
	•	No duplicates in the result
	•	Use any Python built-ins (set, in, etc.) but keep time complexity in mind
"""

from collections import Counter

def common_elements(a: list[int], b: list[int]) -> list[int]:
    counter_a = Counter(a)
    counter_b = Counter(b)
    result = []

    for num in a:
        if num in counter_b and num not in result:
            result.append(num)

    return result

def common_elements(a: list[int], b: list[int]) -> list[int]:
    seen = set()
    b_set = set(b)
    result = []
    
    for num in a:
        if num in b_set and num not in seen:
            result.append(num)
            seen.add(num)
            
    return result

a = [1,3,5,7,9,12]

b = [1,2,3,4,5,]

print(common_elements(a, b))