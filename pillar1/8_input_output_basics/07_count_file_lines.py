"""
Drill 07 - Count File Lines

Write a function:
    count_nonempty_lines(path: str) -> int

Requirements:
1. Open the file in read mode.
2. Count only lines that are not blank after stripping spaces.
3. Return the count.

Example:
If the file contains:
one

two
  three

Then return:
3

Thinking goal:
This drill is about reading outside data and deciding which parts should count.
"""


from pathlib import Path


def count_nonempty_lines(path: str | Path) -> int:
    count = 0
    
    with open(path, "r") as file:
        for line in file:
            if line.strip():
                count += 1

    return count
    

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    file_path = base_dir / "ethics.txt"

    print(count_nonempty_lines(file_path))