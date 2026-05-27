"""
Drill 05 - Reading vs Writing Globals

You are building a small status banner.

Write:
    app_name = "Daily Drills"

Then write two functions:
    get_banner() -> str
    preview_rename(new_name: str) -> str

Requirements:
1. `get_banner()` must read the global `app_name` and return `"Welcome to {app_name}!"`.
2. `preview_rename()` must create a local variable named `app_name` using `new_name`.
3. `preview_rename()` must return `"Preview: {app_name}"`.
4. Calling `preview_rename()` must not change the global `app_name`.

Example:
>>> get_banner()
'Welcome to Daily Drills!'
>>> preview_rename("Python Gym")
'Preview: Python Gym'
>>> get_banner()
'Welcome to Daily Drills!'

Thinking goal:
This drill is about the difference between reading a global name and assigning a local name.
"""

app_name = "Daily Drills"

def get_banner() -> str:
    return f"Welcome to {app_name}!"

def preview_rename(new_name: str) -> str:
    app_name = new_name
    return f"Preview: {app_name}"


if __name__ == "__main__":
    print(get_banner())
    print(preview_rename("Python Gym"))
    print(app_name)