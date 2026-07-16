"""
Challenge: Compare Unique Items Across Lists

You are given two lists of city names representing travel destinations 
from two different years. Some destinations may repeat.

Example:
    cities_2024 = ["Madrid", "Paris", "Berlin", "Rome", "Paris"]
    cities_2025 = ["Lisbon", "Berlin", "Paris", "Warsaw"]

Your task:
1. Use **sets** to compare which cities are unique to each year.  
2. Print:
      - Cities only in 2024
      - Cities only in 2025
      - Cities common to both
3. Ensure each printed list is alphabetically sorted for readability.

Bonus:
- Use symmetric difference (`^`) to get cities that appear in only one of the two lists.

⚡️ Be quick and precise:
Write a function `compare_unique(a: list[str], b: list[str]) -> None`
that prints all three groups clearly labeled.
"""

cities_2024 = ["Madrid", "Paris", "Berlin", "Rome", "Paris"]
cities_2025 = ["Lisbon", "Berlin", "Paris", "Warsaw"]

def compare_unique(a: list[str], b: list[str]) -> None:
    print(f"Elements only in the first list:")
    print(set(a) - set(b))
    print(f"Elements only in the second list:")
    print(set(b) - set(a))
    print(f"Elements common to both lists:")
    print(set(a) & set(b))
    print(f"Elements appearing only in one list:")
    print(set(a) ^ set(b))

compare_unique(cities_2024, cities_2025)