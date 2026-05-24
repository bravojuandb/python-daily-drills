"""
Drill 10 - First Matching Task

Write a function:
    first_ready_task(tasks: list[dict[str, object]]) -> str

Each task dictionary has:
- `"name"`: a string
- `"blocked"`: a boolean
- `"priority"`: an integer

Requirements:
1. Loop through the tasks in order.
2. Ignore blocked tasks.
3. A task is ready only if it is unblocked and its priority is at least `3`.
4. Return the name of the first ready task.
5. If nothing is ready, return `"No task ready"`.
6. Use `continue` and `break`.

Example:
>>> first_ready_task([
...     {"name": "docs", "blocked": True, "priority": 5},
...     {"name": "tests", "blocked": False, "priority": 2},
...     {"name": "deploy", "blocked": False, "priority": 4},
... ])
'deploy'

Thinking goal:
This drill is about combining a skip rule with a match rule and stopping exactly when the first real answer appears.
"""

def first_ready_task(tasks: list[dict[str, object]]) -> str:

    result = "No task ready"

    for task in tasks:
        
        if task["blocked"]:
            continue

        if task["priority"] >= 3:
            result = task["name"]
            break
    
    return result
        

if __name__ == "__main__":

    tasks = [
    {"name": "write_docs", "blocked": True, "priority": 5},
    {"name": "fix_typo", "blocked": False, "priority": 1},
    {"name": "add_tests", "blocked": False, "priority": 2},
    {"name": "clean_data", "blocked": True, "priority": 4},
    {"name": "build_pipeline", "blocked": False, "priority": 3},
    {"name": "review_code", "blocked": False, "priority": 5},
    {"name": "update_readme", "blocked": True, "priority": 2},
    {"name": "run_linter", "blocked": False, "priority": 2},
    {"name": "deploy_app", "blocked": False, "priority": 4},
    {"name": "backup_files", "blocked": True, "priority": 3},
    ]

    print(first_ready_task(tasks))

