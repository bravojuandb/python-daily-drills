"""
You are given a list of daily temperatures: [15, 17, 20, 22, 18, 19, 21, 23].

1. Slice the list to get every 2nd day’s temperature (starting from the first element).
2. Slice the list to get the temperatures of the weekend (last two values).
3. Slice the list in reverse order, but only every second element.

⚡ Be quick — use slicing with steps only, no loops.
"""

temperatures = [15, 17, 20, 22, 18, 19, 21, 23]

def every_second(degrees):
    return degrees[::2]

def weekend(degrees):
    return degrees[-2:]

def reverse_step2(degrees):
    return degrees[::-2]

print(every_second(temperatures))
print(weekend(temperatures))
print(reverse_step2(temperatures))