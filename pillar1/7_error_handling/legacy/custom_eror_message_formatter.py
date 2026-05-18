"""
You are writing a function `check_age(age: int)` that must validate a user’s age.

Rules:
- If `age < 0`, raise an Exception with the message: "Age cannot be negative"
- If `age < 18`, raise an Exception with the message: "User must be at least 18 years old"
- Otherwise, return "Access granted"

⚡ Task:
Implement this function and test it with:
- age = -3
- age = 15
- age = 21

Be quick! 🚀
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

class ExceptionAgeNegative(Exception):
    pass
class ExceptionNotYetAdult(Exception):
    pass

def check_age(age: int):
    try:
        if age < 0:
            raise ExceptionAgeNegative ("Age cannot be negative")
        elif age < 18:
            raise ExceptionNotYetAdult ("User must be at least 18 years old")
        else:
            return "Access granted"
    except Exception as e:
        logging.error(f"Input error: {e}")
        return None

    
print(check_age(-3))
print(check_age(15))
print(check_age(21))