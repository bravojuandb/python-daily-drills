"""
Drill 06 - f-String Formatting

Write a function:
    format_invoice(name: str, items: int, unit_price: float) -> str

Requirements:
1. Capitalize the customer's name.
2. Show the item count padded to 3 digits.
3. Compute the total as `items * unit_price`.
4. Show the total with exactly 2 decimal places.
5. Return a string in this exact shape:
   "Customer: Alice | Items: 007 | Total: 123.45 EUR"

Example:
>>> format_invoice("alice", 7, 17.635)
"Customer: Alice | Items: 007 | Total: 123.45 EUR"

Thinking goal:
The drill is about combining computation and presentation cleanly in one return value.
"""
