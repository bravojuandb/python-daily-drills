"""
Quick challenge — Append/Extend & In-Place Sort

You’re given two lists:
    nums1 = [3, 1, 4]
    nums2 = [5, 9, 2]

Your task:
1. Append one number (7) to nums1.
2. Extend nums1 with all elements from nums2.
3. Sort nums1 *in-place* (do NOT create a new list).
4. Return the modified nums1.

⚡️ Be quick and precise — it’s about knowing when Python mutates the list vs when it creates a new one.
"""


nums1 = [3, 1, 4]
nums2 = [5, 9, 2]


# Verbose version for educational purposes

def transform_list(l1: list[int], l2: list[int], num: int) -> list[int]:
    """
    Demonstrate mutation in-place vs creation of a new object.
    All names refer tothe same list: l1, they are not new lists.
    """

    def append_to_list(l1: list[int], num: int) -> list[int]:
        l1.append(num) # Mutates the existing list
        appended = l1  # Creates a new alias to the same object in memory
        return appended

    def extend_list(l1: list[int], l2: list[int]) -> list[int]:
        l1.extend(l2)
        extended = l1
        return extended

    def sort_list(l1: list[int]) -> list[int]:
        l1.sort()
        sorted_in_place = l1
        return sorted_in_place
    
    appended = append_to_list(l1, num)
    extended = extend_list(appended, l2)
    result = sort_list(extended)

    return result


print(transform_list(nums1, nums2, 7))


# Simplified version 

def transform_list(l1: list[int], l2: list[int], num: int) -> list[int]:
    l1.append(num)
    l1.extend(l2)
    l1.sort()
    return l1