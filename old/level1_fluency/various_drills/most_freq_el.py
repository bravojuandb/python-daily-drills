"""
Most Frequent Element:
Given a list of integers, 
return the number that appears most frequently.
If there is a tie,
return the smallest number
among those with the highest frequency.
"""
from collections import Counter

def most_frequent (nums:list[int]) -> int:
    counts = Counter(nums)
    max_freq = max(counts.values())
    most_common = [num for num, freq in counts.items() if freq == max_freq]
    return min(most_common)

result = most_frequent([1,2,2,3,3,4,-1,-3,-3])

print(result)