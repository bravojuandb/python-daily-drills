"""
Drill 02 - Step-Sized Slicing

Write a function:
    step_slice(nums: list[int]) -> tuple[list[int], list[int]]

Requirements:
1. First slice the list to take every second element starting from index `0`.
2. Then slice the list to take every third element, but stop before the last item.
3. Return both slices as a tuple.
4. Use slicing directly.

Example:
>>> step_slice([10, 20, 30, 40, 50, 60, 70])
([10, 30, 50, 70], [10, 40])

Thinking goal:
This drill is about reading slice boundaries and step sizes without trial and error.
"""


def step_slice(nums: list[int]) -> tuple[list[int], list[int]]:
    return nums[::2], nums[:-1:3]


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70]
    print(step_slice(numbers))