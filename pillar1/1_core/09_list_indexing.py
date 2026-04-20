"""
Drill 09 - List Indexing

Write a function:
    inspect_positions(nums: list[int]) -> tuple[int, int, int, int]

Requirements:
1. Return a tuple with:
   - the first element
   - the last element
   - the third element
   - the second-to-last element
2. If the list has fewer than 3 elements, raise `ValueError`.

Example:
>>> inspect_positions([10, 20, 30, 40, 50])
(10, 50, 30, 40)

Thinking goal:
This drill is about making positive and negative indexing feel immediate and reliable.
"""

def inspect_positions(nums: list[int]) -> tuple[int, int, int, int]:
    if len(nums) < 3:
        raise ValueError("List must have at least 3 elements")

    return (
        nums[0],   # first
        nums[-1],  # last
        nums[2],   # third
        nums[-2]   # second-to-last
    )
if __name__ == "__main__":
    print(inspect_positions([10, 20, 30, 40, 50]))
