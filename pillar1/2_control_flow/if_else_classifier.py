"""
You are given a function `classify_temperature(temp: int) -> str`.

Rules:
- If the temperature is below 0 → return "Freezing".
- If the temperature is between 0 and 15 (inclusive) → return "Cold".
- If the temperature is between 16 and 25 (inclusive) → return "Mild".
- If the temperature is above 25 → return "Hot".

Implement the function using if / elif / else.

Be quick! Can you write it correctly in under 90 seconds?
"""

def classify_temperature(temp: int) -> str:
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 15:
        return "Cold"
    elif 16 <= temp <= 25:
        return "Mild"
    else:
        return "Hot"


test_values = [-10, -1, 0, 5, 15, 16, 20, 25, 26, 40]
for val in test_values:
    print(f"{val:>3}°C → {classify_temperature(val)}")