"""
Challenge: Simple Expression Evaluator

Write a function `evaluate(expr: str) -> int`
that only handles + and - between single-digit numbers.

Rules:
- Expression has only digits 0–9 and + or -
- No spaces, no parentheses, no *, /
- Process strictly left to right
- Return the integer result

Examples:
- "2+3"     ➜ 5
- "7-4+1"   ➜ 4
- "9-2-3"   ➜ 4

Hint:
Start with the first number,
then for each operator, apply it to the next number.
You don’t need stacks yet — just a running total.

This is the step before stacks and precedence.
"""

def evaluate(expr: str) -> int:
    """
    Evaluates expressions containing + or - and digits from 0 to 9.
    Processes the string left to right without operator precedence.
    """
    if not expr or not expr[0].isdigit():
        raise ValueError("Expression must start with a digit.")
    
    total = int(expr[0])  # Take the first number as the starting value
    i = 1

    while i < len(expr):
        op = expr[i]  # Expect an operator (+ or -)
        
        if op not in {"+", "-"}:
            raise ValueError("Only + or - are allowed.")
        
        i += 1
        if i >= len(expr) or not expr[i].isdigit():
            raise ValueError("Operator must be followed by a digit.")
        
        num = int(expr[i])  # Next number after the operator

        if op == "+":
            total += num
        else:
            total -= num

        i += 1

    return total


print(evaluate("9-9"))