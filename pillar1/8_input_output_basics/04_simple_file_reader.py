"""
Drill 04 - Simple File Reader

Write a function:
    read_notes(path: str) -> list[str]

Requirements:
1. Open the file in read mode.
2. Read all lines with `.readlines()`.
3. Strip the trailing newline from each line.
4. Return strings in the form `"Line 1: Hello world"`.

Example:
If the file contains:
Hello world
Python drills

Then return:
['Line 1: Hello world', 'Line 2: Python drills']

Thinking goal:
This drill is about turning raw file input into a slightly more useful structure.
"""

from pathlib import Path

def read_notes(path: str) -> list[str]:

    with open(path, "r") as file:
        lines = file.readlines()

        result = []

        for i, line in enumerate(lines, start=1):
            line = line.rstrip("\n")
            result.append(f"line {i}: {line}")
    
    return result


if __name__ == "__main__":

    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / "demo.txt"

    print(read_notes(file_path))