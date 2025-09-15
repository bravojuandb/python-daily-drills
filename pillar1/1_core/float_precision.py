# Float Precision & Rounding

import math

def float_drill():
    x = 0.1 + 0.2
    y = round(2.675, 2)
    z1 = round(7.5)
    z2 = round(8.5)
    f1 = math.floor(-3.7)
    f2 = math.ceil(-3.7)

    return x, y, z1, z2, f1, f2


# Run the drill
print(float_drill())