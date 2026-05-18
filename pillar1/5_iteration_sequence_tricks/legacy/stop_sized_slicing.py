"""
Write a function `step_slice(nums: list[int]) -> tuple[list[int], list[int]]`.

Rules:
- First slice the list to take every 2nd element starting from index 0.
- Then slice the list to take every 3rd element, but only until the second-to-last item.
- Return both slices as a tuple.

Example:
nums = [10, 20, 30, 40, 50, 60, 70]
step_slice(nums) = ([10, 30, 50, 70], [10, 40])

Solve it fast — under 2 minutes!
"""
# Using slicing shortcut
def step_slice(nums: list[int]) -> tuple[list[int], list[int]]:
    return nums[::2], nums[:-1:3]

# Without slicing
def step_slice(nums: list[int]) -> tuple[list[int], list[int]]:
    
    every_2nd = []
    for i in range(0, len(nums), 2):
        every_2nd.append(nums[i])

    every_3rd = []
    for i in range(0, len(nums) - 1, 3):
        every_3rd.append(nums[i])

    return every_2nd, every_3rd

nums = [10, 20, 30, 40, 50, 60, 70]

print(step_slice(nums))