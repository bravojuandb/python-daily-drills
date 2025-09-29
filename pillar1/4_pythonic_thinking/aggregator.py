"""
Given a list of temperatures in Celsius, use Python built-ins to compute:

1. The total sum of all temperatures.
2. The minimum temperature.
3. The maximum temperature.

temps = [15, 22, 18, 30, 25, 19, 17]

Expected:
- sum(...) → 146
- min(...) → 15
- max(...) → 30
"""
import timeit

temps = [15, 22, 18, 30, 25, 19, 17]

def analysis(temps: list[int]) -> str:
    return f"Sum: {sum(temps)}, Min: {min(temps)}, Max: {max(temps)}."

print(analysis(temps))

print(timeit.timeit(lambda: analysis(temps), number=10000))

# Optimized function for big data

def analysis(temps: list[int]) -> str:
    total, mn, mx = 0, float("inf"), float("-inf")
    for t in temps:
        total += t
        if t < mn: 
            mn = t
        if t > mx: 
            mx = t
    return f"Sum: {total}, Min: {mn}, Max: {mx}."

print(timeit.timeit(lambda: analysis(temps), number=10000))