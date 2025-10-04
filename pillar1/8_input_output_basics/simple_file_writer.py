"""
**Simple File Writer Challenge**

Write a function `save_notes()` that:
1. Opens a file called `output.txt` in **write mode** (`"w"`)
2. Writes three lines of your choice into it using `.write()`
3. Closes automatically (using a `with` block)

Then, open and print the file contents to verify your write worked!

Expected console output example:
File written successfully.
--- output.txt ---
Learning Python
Practicing drills
Becoming fluent!

Hints:
- Each `.write()` call needs a `\n` at the end for line breaks.
- Use `with open("output.txt", "w") as f:` to manage the file safely.

Try to solve this in under 90 seconds!
"""

def save_notes():
    with open('ethics.txt', "w") as file:
        file.write(
            "We are what we repeatedly do. Excellence, then, is not an act, but a habit.\n")
        file.write(
            "The good for man is an activity of the soul in conformity with virtue.\n")
        file.write("Pleasure in the job puts perfection in the work.\n")
    print("File written succesfully.")

def read_notes():
    with open("ethics.txt", "r") as f:
        content = f.read()
    print("--- ethics.txt ---")
    print(content)

save_notes()
read_notes()