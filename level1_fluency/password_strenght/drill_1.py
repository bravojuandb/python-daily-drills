"""
💡 Drill: Password Strength Checker

Write a function called `check_password_strength(password: str) -> str` 
that evaluates the strength of a password and returns one of three levels:
- "Weak"
- "Moderate"
- "Strong"

The password is rated based on the following criteria:

1. "Weak":
   - Length is less than 8 characters
   OR
   - Contains only letters or only digits

2. "Moderate":
   - Length is at least 8
   - Contains both letters and digits
   - Does NOT contain special characters

3. "Strong":
   - Length is at least 10
   - Contains letters, digits, and at least one special character (e.g., !@#$%^&*()_+-=)

Special characters can be any of the following: `!@#$%^&*()_+-=`

Examples:
check_password_strength("pass123")           ➞ "Weak"
check_password_strength("pass1234")          ➞ "Moderate"
check_password_strength("Pass1234!")         ➞ "Strong"
check_password_strength("1234567890")        ➞ "Weak"
check_password_strength("MyPassword2024")    ➞ "Moderate"

⚠️ Constraints:
- Do not use any external libraries (e.g., `re`).
- Use only built-in Python tools.
"""


def check_password_strength(password: str) -> str:
    only_letters = password.isalpha()
    only_digits = password.isdigit()
    specials = '`!@#$%^&*()_+-='
    has_letters = any(char.isalpha() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_specials = any(char in specials for char in password)
    length = len(password)

    if length < 8 or only_digits or only_letters:
        return "Weak"
    elif length >= 10 and has_letters and has_digits and has_specials:
        return "Strong"
    elif length >= 8 and has_letters and has_digits and not has_specials:
        return "Moderate"
    else:
        return "Weak"