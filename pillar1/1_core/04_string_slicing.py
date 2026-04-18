"""
Drill 04 - String Slicing

Write a function:
    slice_code(token: str) -> dict[str, str]

Scenario:
You receive a compact identifier and need to inspect different parts of it quickly.

Requirements:
1. Return a dictionary with these keys:
   - "prefix": first 4 characters
   - "suffix": last 3 characters
   - "middle": all characters except the first and last
   - "every_second": every second character starting from index 0
   - "reversed": the full string reversed
2. Do not use loops.
3. Use slicing for every derived value.

Example:
>>> slice_code("DataEngineer")
{
    "prefix": "Data",
    "suffix": "eer",
    "middle": "ataEnginee",
    "every_second": "DtEgne",
    "reversed": "reenignEataD",
}

Thinking goal:
The drill is simple on purpose, but it should make slicing feel automatic and precise.
"""

def slice_code(token: str) -> dict[str, str]:

    return {
        "prefix": token[:4],
        "suffix": token[-3:],
        "middle": token[1:-1],
        "every_second": token[::2],
        "reversed": token[::-1],
    }

if __name__ == "__main__":
    assert slice_code("DataEngineer") == {
        "prefix": "Data",
        "suffix": "eer",
        "middle": "ataEnginee",
        "every_second": "DtEgne",
        "reversed": "reenignEataD",
    }
