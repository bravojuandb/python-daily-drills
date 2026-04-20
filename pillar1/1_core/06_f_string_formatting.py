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

def format_invoice(name: str, items: int, unit_price: float) -> str:
    customer = name.title()
    items_str = f"{items:03d}"
    total = items * unit_price
    total_str = f"{total:.2f}"
    return f"Customer: {customer} | Items: {items_str} | Total: {total_str} EUR"


if __name__ == "__main__":

    invoices = {
    "INV-001": {"name": "alice", "items": 7,  "unit_price": 17.635},
    "INV-002": {"name": "bob",   "items": 12, "unit_price": 5.5},
    "INV-003": {"name": "carol", "items": 3,  "unit_price": 99.99},
    "INV-004": {"name": "dave",  "items": 25, "unit_price": 2.75},
    "INV-005": {"name": "eve",   "items": 1,  "unit_price": 250.0},
    "INV-006": {"name": "frank", "items": 9,  "unit_price": 13.2},
    "INV-007": {"name": "grace", "items": 15, "unit_price": 7.89},
    "INV-008": {"name": "heidi", "items": 4,  "unit_price": 45.5},
    "INV-009": {"name": "ivan",  "items": 30, "unit_price": 1.99},
    "INV-010": {"name": "judy",  "items": 6,  "unit_price": 18.75},
    }  

    for i, j in invoices.items():
        print(format_invoice(j["name"], j["items"], j["unit_price"]))
        