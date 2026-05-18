"""
**Simple File Reader Challenge**

You’re given a file called `notes.txt` containing several lines of text.

Write a function `read_notes()` that:
1. Opens the file in read mode (`"r"`)
2. Reads all lines using `.readlines()`
3. Prints each line **without extra newline characters**

Example expected output if the file contains:
Hello world
Python drills
Keep going!

Output:
Line 1: Hello world
Line 2: Python drills
Line 3: Keep going!

⏱️ Try to code it in under 90 seconds!
"""

with open("notes.txt", "w") as f:
    f.write("Hello world\n")
    f.write("Python drills\n")
    f.write("Keep going!\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Answer:
def read_notes(filename: str):
    with open('notes.txt', "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start= 1):
            print(f"Line {i}: {line.strip()}")


read_notes("notes.txt")