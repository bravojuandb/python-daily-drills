"""
**Print Formatting Challenge**

You’re given three variables:
name = "Alice"
age = 29
balance = 1345.6789

Write ONE print statement using an f-string that produces this exact output:

Customer: Alice | Age: 29 | Balance: €1,345.68

💡 Requirements:
- Use f-string formatting (not concatenation)
- Round balance to two decimals
- Include the euro sign (€) and thousand separator (,)

Be quick — you should be able to solve this in under 60 seconds!
"""
def print_with_format(name: str, age: int, balance: float) -> str:
    return f"Customer: {name} | Age: {age} | Balance: €{balance:,.2f}"

name = "Alice"
age = 29
balance = 1345.6789

print(print_with_format(name, age, balance))