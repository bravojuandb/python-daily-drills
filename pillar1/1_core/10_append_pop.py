"""
Drill 10 - Append and Pop

Write a function:
    process_queue() -> list[int]

Scenario:
You are modeling a tiny service queue.

Steps:
1. Start with an empty list called `queue`.
2. Append customer IDs `101`, `102`, and `103`.
3. Serve the first customer by removing them from the front.
4. Append `104` and `105`.
5. Remove the last customer because they leave unexpectedly.
6. Return the final queue.

Expected result:
>>> process_queue()
[102, 103, 104]

Thinking goal:
The drill is about tracking list state over time, not just calling methods.
"""
