"""
Drill — Recursive Directory Walk (simulate folder scan)

You're given a nested dictionary representing a folder structure like the one 
below.

Task:
Implement a function `walk(directory: dict, path: str = "") -> list[str]`
that returns a **flat list** of all file paths found recursively, such as:

[
    "root/docs/readme.txt",
    "root/docs/notes.txt",
    "root/src/main.py",
    "root/src/utils/helpers.py",
    "root/src/utils/config.yaml",
    "root/data/raw/file1.csv",
    "root/data/raw/file2.csv"
]

Rules:
1. If a value is a dictionary → recurse deeper.
2. If a value is `None` → it's a file, include it in the list.
3. The output must include full paths using `'/'`.
4. Don’t use `os.walk()` — simulate recursion manually.

Tip: build up the path incrementally and collect results in a list.
You can use an inner helper function or just recursion itself.

Aim to solve in 10 minutes.  
Be quick, be precise — recursion is all about clarity.
"""

filesystem = {
    "root": {
        "docs": {
            "readme.txt": None,
            "notes.txt": None
        },
        "src": {
            "main.py": None,
            "utils": {
                "helpers.py": None,
                "config.yaml": None
            }
        },
        "data": {
            "raw": {
                "file1.csv": None,
                "file2.csv": None
            },
            "clean": {}
        }
    }
}


def walk(directory: dict, path: str = "") -> list[str]:
    result = []
    for key, val in directory.items():
        new_path = f"{path}/{key}" if path else key

        if isinstance(val, dict):
            result.extend(walk(val, new_path))
        else:
            result.append(new_path)

    return result


for i in walk(filesystem):
    print(i)