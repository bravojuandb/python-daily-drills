"""
⚡ List Indexing Drill

Problem:  
Write a function `pick_elements(nums: list[int]) -> tuple` that returns:  
1. The **first element**.  
2. The **last element**.  
3. The **third element** (index 2).  
4. The **second-to-last element** (index -2).  

Example:
>>> pick_elements([10, 20, 30, 40, 50])
(10, 50, 30, 40)

⏱️ Challenge: solve it in under 1 minute using only list indexing.
"""

def pick_elements(nums: list[int]) -> tuple:
    first = nums[0]
    last = nums[-1]
    third = nums[2]
    second_to_last = nums[-2]

    return first, last, third, second_to_last

print(pick_elements([10, 20, 30, 40, 50]))


