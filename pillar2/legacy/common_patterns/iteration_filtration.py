"""
Turing-style problem — Iteration & Conditional Filtering (Advanced)

You’re given a CSV file named `customers.csv` with the following headers:  
`id,name,email,country,status,spend`

Example:
1,Anna,anna@example.com,Spain,active,120.50  
2,Bob,bob@example.com,Germany,inactive,80.00  
3,Cara,cara@example.com,Spain,active,300.00  
4,Dan,dan@example.com,Italy,active,50.00  
5,Eve,eve@example.com,Spain,inactive,0  

Task:
Write a Python script that:
1. Reads the CSV using the **csv.DictReader**.
2. Filters **only active customers from Spain**.
3. Keeps only those with a **spend greater than 100**.
4. Prints them in the format:  
   `Anna (Spain) — €120.50`

Bonus:
Sort the output by spend (descending order).

Hints:
- You may use `float(row["spend"])` to compare spend.
- Use list comprehension or a filtered loop.

Time target: 7–8 minutes.
"""


from typing import Iterable
from pathlib import Path
import csv


def filter_csv(rows: Iterable[dict[str, str]]) -> None:
    """
    Filters data by status, country, and spend greater than €100.

    Args:
        rows (Iterable[dict[str, str]]): Sequence of rows from a CSV file.
    Returns:
        None
    """
    for row in rows:
        name = row["name"]
        country = row["country"]
        spend = float(row["spend"])
        status = row["status"]
        if status == "active" and country == "Spain" and spend > 100:
            print(f"{name}({country}) - €{spend}")
        else:
            continue


def filter_and_sort_csv(rows: Iterable[dict[str, str]]) -> None:
    """
    Same as filter_csv but sorts by spend descending
    """
    results = [
        (row["name"], row["country"], float(row["spend"]))
        for row in rows
        if row["status"] == "active"
        and row["country"] == "Spain"
        and float(row["spend"]) > 100
    ]
    for name, country, spend in sorted(results, key=lambda x: x[2], reverse=True):
        print(f"{name} ({country}) — €{spend:.2f}")


if __name__ == "__main__":
    BASE_PATH = Path(__file__).parent
    FILE_PATH = BASE_PATH / "customers.csv"

    with open(FILE_PATH, newline="") as f:
        reader = csv.DictReader(f)
        print("\nThis is the filtered result from filter_csv:\n")
        filter_csv(reader)
        
        print("\nThis is the result from filter_and_sort_csv:\n")
    with open(FILE_PATH, newline="") as f:
        filter_and_sort_csv(csv.DictReader(f))