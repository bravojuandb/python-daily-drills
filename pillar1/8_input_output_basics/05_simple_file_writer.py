"""
Drill 05 - Simple File Writer

Write a function:
    save_notes(path: str, lines: list[str]) -> None

Requirements:
1. Open the file in write mode with a `with` block.
2. Write each string on its own line.
3. Overwrite any existing content in the file.
4. Do not add extra blank lines.

Example:
If `lines` is:
["Learning Python", "Practicing drills", "Becoming fluent!"]

Then the file should contain exactly those three lines.

Thinking goal:
This drill is about writing visible output carefully so the file ends up exactly as intended.
"""


from pathlib import Path

def save_notes(path: str | Path, lines: list[str]) -> None:

    with open(path, mode="w") as file:
        file.write("\n".join(lines))



if __name__ == "__main__":

    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / "notes.txt"

    notes = [
        "Learning Python", 
        "Practicing drills", 
        "Becoming fluent!"
    ]

    save_notes(file_path, notes)