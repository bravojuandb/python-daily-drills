"""
Given a list of integers and a target number,
determine if any two distinct elements in the list add up to the target.
Return True if such a pair exists, else return False.

"""

def sum_of_two(l: list[int], t: int) -> bool:
    checked = set()
    # 'checked' is a set used to store numbers we've already seen in the list.
    # It helps us check in constant time if the complement of the current number exists.
    for num in l:
        complement = t - num
        if complement in checked:
            # If the complement is found in 'checked', it means we have found two numbers that add up to 't'.
            return True
        checked.add(num)
        # Add the current number to 'checked' for future checks.
    return False
    # If we finish the loop without finding any pair, return False.
