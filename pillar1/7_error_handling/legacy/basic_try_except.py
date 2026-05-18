"""
Write a function `safe_divide(a: int, b: int) -> float | str` that divides `a` by `b`.  

Rules:
- Use `try/except` to catch division errors.
- If division works, return the result.
- If division by zero occurs, return the string "Error: Division by zero".

Examples:
- safe_divide(10, 2) → 5.0
- safe_divide(7, 0) → "Error: Division by zero"
"""


from typing import Union
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def safe_divide(a: Union[int, float], b: Union[int, float]) -> float | None:
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        logging.error(f"Division failed: {e}")
        return None


print(safe_divide(10, 2))
print(safe_divide(7, 0))
print(safe_divide("f", 0))
print(safe_divide(2.4, 5))