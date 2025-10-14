"""
Given a list of integers `nums` and an integer `k`, implement a function
that rotates the elements of the list to the **right** by `k` steps.

For example:
nums = [10, 20, 30, 40, 50], k = 2
→ result: [40, 50, 10, 20, 30]

Constraints:
- Do NOT use `collections.deque.rotate()`.
- Aim for a solution that works in-place or with minimal extra space.
- Handle cases where `k` > len(nums) gracefully.

Be quick and precise. 
Once done, paste your solution here for review.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s'
)
def rotate_to_the_right(nums: list[int], step: int) -> list[int]:
    logging.info(f"Starting rotation to the right by {step} steps")
    try:

        if not isinstance(nums, list):
            raise TypeError("Input must be a list")
        if not isinstance(step, int):
            raise TypeError("Step must be an integer")
        if not nums:
            return []
        
        step = step % len(nums) # Handles step > len(nums)
        if step == 0:
            return nums
        
        return nums[-step:] + nums[:-step]
    
    except Exception as e:
        logging.error(f"Rotation failed: {e}")
        return []


nums = [10, 20, 30, 40, 50]

print(rotate_to_the_right(nums, 10))

