"""
Challenge: Store Immutable Records using Tuples

You are building a small data log for temperature readings.  
Each reading must be **immutable** — once recorded, it can’t be changed —  
so you decide to store each entry as a tuple.

Example of one record:
    ("Madrid", 24.6, "2025-10-16 06:00")

Write a function `add_reading(log: list[tuple[str, float, str]], city: str, temp: float, timestamp: str) -> list[tuple[str, float, str]]`
that adds a new record to a list called `log`.

Rules:
- Use tuples to store each record (no lists inside).  
- Demonstrate that modifying one element of a tuple raises an error.  
- Show how you can safely *replace* a record (by creating a new tuple).  

⚡️ Be quick and precise: code the function and test it with two readings, 
then try to mutate one tuple element to confirm immutability.
"""

temperatures = [
    ("Barcelona", 23.1, "2025-10-16 08:00"),
    ("Seville", 26.3, "2025-10-16 12:00"),
]

def add_reading(
        log: list[tuple[str, float, str]], 
        city: str, 
        temp: float, 
        timestamp: str
) -> list[tuple[str, float, str]]:
    
    log.append((city, temp, timestamp))
    return log

# ("Madrid", 24.6, "2025-10-16 06:00")
print(add_reading(temperatures, "Madrid", 24.6, "2025-10-16 06:00"))
print(add_reading(temperatures, "Pamplona", 18, "2025-10-15 10:00"))

# Trying to modify a tuple raises a TypeError
temperatures[0][0] = "Alicante"

print(temperatures)