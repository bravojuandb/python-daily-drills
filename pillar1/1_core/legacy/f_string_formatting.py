"""
f-String Formatting Drill

Problem:
Write a function format_report(name: str, items: int, price: float) 
that returns a neatly formatted string using f-strings.  

Requirements:  
1. Show the name capitalized.  
2. Show the number of items padded with leading zeros (width 3).  
3. Show the total cost (`items * price`) with 2 decimal places and a € sign at the end.  
4. All fields should be joined into one string like:  
   "Customer: Alice | Items: 007 | Total: 123.45€"

Example:
```python
>>> format_report("alice", 7, 17.635)
"Customer: Alice | Items: 007 | Total: 123.45€"

"""

def format_report(name: str, items: int, price:float) -> str:
    f_name = f"Customer: {name.title()}"
    f_items = f"Items: {items:03}"
    total = items * price
    f_total = f"Total: {total:.2f}€"
    return f"{f_name} | {f_items} | {f_total}"

print(format_report("alice", 5, 234.50))