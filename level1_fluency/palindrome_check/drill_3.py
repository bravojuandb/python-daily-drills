"""
Pillar 1 Drill: palindrome_check.py
Level: Medium
Subcategory: Strings and Loops

Problem:
Implement a function that checks if a given string is a **valid palindrome**.

A string is considered a palindrome if:
- It reads the same forward and backward,
- It **ignores case** and **non-alphanumeric characters**.

Your function should:
1. Return True if the cleaned string is a palindrome.
2. Return False otherwise.

Examples:

>>> is_valid_palindrome("A man, a plan, a canal: Panama")
True

>>> is_valid_palindrome("race a car")
False

>>> is_valid_palindrome("No 'x' in Nixon")
True

>>> is_valid_palindrome("")
True

>>> is_valid_palindrome(".,,,")
True

Requirements:
- Use loops (not slicing or built-in reversed).
- Convert all characters to lowercase.
- Only consider alphanumeric characters.
- Do **not** use `re` or `filter` or `reversed()` or slicing (`[::-1]`).
- Write your own loop to compare characters from both ends.

Constraints:
- Input: A string `s` of length ≤ 100,000.
- You must achieve O(n) time and O(1) extra space (excluding the input).

"""

def is_valid_palindrome(s:str) -> bool:
    """This approach an intuitive solution: 
    clean -> reverse -> compare, 
    but it is O(n) extra space.
    """

    cleaned = ""
    for i in s.lower().strip():
        if i.isalnum():
            cleaned += i

    # Since (cleaned == cleaned[::-1]) is not allowed, then:
    reversed = ""
    for char in cleaned:
        reversed = char + reversed

    return reversed == cleaned


def is_valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer until alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer until alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare chars (lowercased)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


print(is_valid_palindrome("A man, a plan, a canal: Panama"))