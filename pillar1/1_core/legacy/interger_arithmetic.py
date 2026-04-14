# aritmetic operators

def operations(a: int, b: int) -> tuple[float, ...]:
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    modulo = a % b
    compound = (a + b) * (a - b)
    power1 = a ** b
    power2 = b ** a

    return add, subtract, multiply, divide, modulo, compound, power1, power2


print(operations(-7, -3))