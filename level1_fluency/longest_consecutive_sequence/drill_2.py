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

def longest_consecutive(nums: list[int], debug: bool = False) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    # Debug helper to avoid scattered prints
    def log(msg: str):
        if debug:
            print(msg)

    for num in num_set:
        if (num - 1) not in num_set:
            current_num = num
            current_length = 1
            log(f"Start run at {current_num} (no {current_num - 1} in set); length={current_length}")

            while (current_num + 1) in num_set:
                current_num += 1
                current_length += 1
                log(f"Extend run to {current_num}; length={current_length}")

            if current_length > max_length:
                log(f"New max run found: start={num}, end={current_num}, length={current_length}")
            max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":

    # Edge cases
    assert longest_consecutive([]) == 0
    assert longest_consecutive([7]) == 1
    assert longest_consecutive([5, 5, 5]) == 1

    # Core logic checks
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([-3, -2, -1, 0, 10]) == 4
    assert longest_consecutive([1, 9, 3, 10, 2, 20, 4, 30, 5]) == 5
    assert longest_consecutive([10, 12, 11, 50, -1, 13, 14, 0]) == 5
    assert longest_consecutive([1, 2, 4, 5, 7, 8, 9]) == 3

    print("✅ All tests passed")