"""
Write a function `classify_number(n: int) -> str`.

Rules:
1. First check if the number is positive, negative, or zero.
   - If zero → return "Zero".
   - If positive:
        * If it's even → return "Positive Even".
        * If it's odd → return "Positive Odd".
   - If negative:
        * If its absolute value is greater than 10 → return "Negative Large".
        * Otherwise → return "Negative Small".

You MUST use nested if statements (an if inside another if).
Be quick — can you solve it in under 2 minutes?
"""

def classify_number(n: int) -> str:
    if n == 0: 
        return "Zero"
    elif n > 0:
        if n % 2 == 0:
            return "Positive Even"
        else:  # n % 2 != 0
            return "Positive Odd"
    else:
        if abs(n) > 10:
            return "Negative Large"
        else:
            return "Negative Small"
        
nums = [x for x in range(-20,50,3)]

for num in nums:
    print(f"{num}", classify_number(num))