
# works with the formula a % b = a - b * floor(a / b)
# % keeps the sign of the divisor

def modulo_madness():
    a = 13 % 5
    b = -13 % 5
    c = 13 % -5
    d = -13 % -5
    e = 20 % 7
    f = -20 % 7
    g = 20 % -7
    h = -20 % -7

    return a, b, c, d, e, f, g, h

print(modulo_madness())
