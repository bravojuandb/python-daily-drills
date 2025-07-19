"""
This is an improved solution of drill_1.py

"""


def is_valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Move the left pointer to the next alphanumeric
        while left < right and not s[left].isalnum():
            left += 1

        # Move right pointer to prevoious alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True
    

print(is_valid_palindrome("A man, a plan, a canal: Panama"))