"""
Challenge 02 - First Matching Task

Write a function:
    first_ready_task(tasks: list[dict[str, object]]) -> str

Each task dictionary has:
- `"name"`: a string
- `"blocked"`: a boolean
- `"priority"`: an integer

Requirements:
1. Loop through the tasks in order.
2. Skip tasks whose `"blocked"` value is `True`.
3. Return the `"name"` of the first unblocked task whose priority is at least `3`.
4. If no such task exists, return `"No task ready"`.
5. Use `continue` and `break`.

Example:
>>> first_ready_task([
...     {"name": "docs", "blocked": True, "priority": 5},
...     {"name": "tests", "blocked": False, "priority": 2},
...     {"name": "deploy", "blocked": False, "priority": 4},
... ])
'deploy'

Thinking goal:
This challenge is about tracing multiple conditions while stopping as soon as the right item appears.
"""
