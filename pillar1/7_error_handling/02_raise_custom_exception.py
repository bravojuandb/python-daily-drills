"""
Drill 02 - Raise Custom Exception

Write:
    class InsufficientFundsError(Exception): ...

Then write a function:
    withdraw(balance: float, amount: float) -> float

Requirements:
1. If `amount` is greater than `balance`, raise `InsufficientFundsError`.
2. Otherwise, subtract `amount` from `balance` and return the new balance.
3. Do not catch the custom exception inside `withdraw()`.

Example:
>>> withdraw(100, 30)
70
>>> withdraw(50, 80)
raises InsufficientFundsError

Thinking goal:
This drill is about signaling a rule violation clearly instead of silently returning a fake result.
"""

class InsufficientFundsError(Exception):
    pass

def withdraw(balance: float, amount: float) -> float:
    
    if amount > balance:
        raise InsufficientFundsError ("Error: not enough funds")
    
    return balance - amount

if __name__ == "__main__":
    print(withdraw(3, 1))
    print(withdraw(0, 4))