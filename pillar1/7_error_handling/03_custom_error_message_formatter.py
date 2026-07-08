"""
Drill 03 - Custom Error Message Formatter

Write a function:
    check_age(age: int) -> str

Requirements:
1. If `age < 0`, raise `ValueError("Age cannot be negative")`.
2. If `age < 18`, raise `ValueError("User must be at least 18 years old")`.
3. Otherwise, return `"Access granted"`.

Example:
>>> check_age(21)
'Access granted'
>>> check_age(-3)
raises ValueError("Age cannot be negative")

Thinking goal:
This drill is about making invalid cases precise enough that the caller learns something useful.
1. Reject invalid input with raise
2. Use specific error messages
3. Order validations correctly
4. Separate validations from the successful return path
"""


def check_age(age: int) -> str:

    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("User must be at least 18 years old")
    
    return "Access granted"
    

if __name__ == "__main__":

    print(check_age(18))