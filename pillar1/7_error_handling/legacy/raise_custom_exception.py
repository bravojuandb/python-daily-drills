"""
Write a function `withdraw(balance: float, amount: float) -> float` that simulates withdrawing money.  

Rules:
- If `amount` is greater than `balance`, raise a custom exception `InsufficientFundsError`.
- Otherwise, subtract `amount` from `balance` and return the new balance.
- Define your own exception class using `class InsufficientFundsError(Exception): ...`.

Examples:
- withdraw(100, 30) → 70
- withdraw(50, 80) → raises InsufficientFundsError
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
class InsufficientFundsError(Exception):
    pass

# No try - except block
def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds for this withdrawal")
    else:
        return balance - amount

# With try -except
def withdraw(balance: float, amount: float) -> float | None:
    try:
        if amount > balance:
            # Raise: creates and throws the error at the source.
            raise InsufficientFundsError("Insufficient funds for this withdrawal")
        return balance - amount
    # Except: catches and responds to it somewhere else in the program.
    except InsufficientFundsError as e:
        logging.error(f"Not enough funds: {e}")
        return None


print(withdraw(100, 30))
print(withdraw(50, 80))