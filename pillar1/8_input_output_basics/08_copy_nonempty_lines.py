"""
Drill 08 - Copy Nonempty Lines

Write a function:
    copy_nonempty_lines(source: str, target: str) -> None

Requirements:
1. Read the source file line by line.
2. Copy only nonempty lines to the target file.
3. Preserve the original order of copied lines.
4. Write the target file from scratch.

Example:
If the source file contains:
alpha

beta

gamma

Then the target file should contain:
alpha
beta
gamma

Thinking goal:
This drill is about combining file reading, filtering, and writing in one small pipeline.
"""


from pathlib import Path

def copy_nonempty_lines(source: str | Path, target: str | Path) -> None:
    """
    Open a file and write valid lines one by one to a new file on one pass
    """
    with open(source, "r") as source_file, open(target, "w") as target_file:
        for line in source_file:
            cleaned_line = line.rstrip("\n")
            if cleaned_line.strip():
                target_file.write(cleaned_line + "\n")


if __name__ == "__main__":

    base_dir = Path(__file__).parent
    source_file = base_dir / "ethics.txt"
    target_file = base_dir / "ethics_new.txt"

    copy_nonempty_lines(source_file, target_file)

    if target_file.exists() and target_file.stat().st_size > 0:
        print("success")

