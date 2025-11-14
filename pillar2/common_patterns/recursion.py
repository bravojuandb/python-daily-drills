"""
Recursion (self-similar decomposition)

You're given a nested folder structure built from:
- strings  → files
- lists    → contents of a folder
- dicts    → subfolders, where each key maps to a list

Example shape:
{
    "root": [
        "a.txt",
        "b.csv",
        { "images": ["pic1.png", "pic2.png", { "raw": ["img001.raw"] }] },
        { "docs": ["notes.md", { "archive": ["old1.txt", "old2.txt"] }] }
    ]
}

Task:
1) Implement a recursive function:

       count_files(node) -> int

   It must:
   - return 1 if the node is a file (string)
   - explore lists by visiting each element
   - explore dicts by visiting each value
   - return the total number of files found inside `node`
   - **must use recursion**, not loops only

Bonus (still mid-level):
2) Implement:

       list_all_files(node) -> list[str]

   It should collect every filename from every depth into a flat list.

3) Print:
       Total files: X
       All files:
         - file1
         - file2
         ...

⏱ Target: 6–10 minutes.
"""