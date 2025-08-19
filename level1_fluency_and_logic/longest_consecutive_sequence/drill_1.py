"""
Problem Statement: longest_consecutive_sequence.py

Pillar 1 – Fluency & Logic
Subcategory: Set Logic & Scanning
Level: Medium

Prompt:
You are given an unsorted list of integers. Your task is to return the length of the longest 
sequence of consecutive numbers (in any order). The sequence must consist of numbers that 
appear in the input list, and the algorithm must run in linear time O(n).

You may NOT sort the list.

Function Signature:
def longest_consecutive(nums: List[int]) -> int:

Input:
- nums: List[int] — a list of integers (may include duplicates and negative numbers)

Output:
- An integer representing the length of the longest consecutive sequence

Example:
nums = [100, 4, 200, 1, 3, 2]
Output: 4
# The sequence [1, 2, 3, 4] has 4 elements.

Constraints:
- 0 ≤ len(nums) ≤ 10^5
- -10^9 ≤ nums[i] ≤ 10^9

Restrictions:
Do NOT use:
- sort()
- sorted()

Do use:
- A set for O(1) lookups
- Loops and flow control to detect and grow sequences
- Manual logic to skip redundant checks

Turing Hints:
- Convert the list to a set to remove duplicates and allow fast membership testing.
- Only start a sequence if the previous number (n - 1) is NOT in the set.
- Use a while-loop to scan forward and count the length of the sequence.
"""

def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest

# Example test
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4


def longest_consecutive_sequence(nums: list[int]) -> list[int]:
    if not nums:
        return []

    num_set = set(nums)
    longest_seq = []

    for num in num_set:
        # Start only at the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            current_seq = [current]

            while current + 1 in num_set:
                current += 1
                current_seq.append(current)

            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq

    return longest_seq

# Example usage
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: [1, 2, 3, 4]