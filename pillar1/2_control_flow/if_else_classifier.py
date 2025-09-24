def classify_temperature(temp: int) -> str:
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 15:
        return "Cold"
    elif 16 <= temp <= 25:
        return "Mild"
    else:
        return "Hot"


# Test harness
test_values = [-10, -1, 0, 5, 15, 16, 20, 25, 26, 40]
for val in test_values:
    print(f"{val:>3}°C → {classify_temperature(val)}")