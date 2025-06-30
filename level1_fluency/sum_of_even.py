"""

Write a function that takes a list of integers 
and return the sum of all even numbers in it.

"""

def sum_even(nums: list[int]) -> int:
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total
 
print(sum_even([1,3,4,2,5,6,7,4,5,1]))