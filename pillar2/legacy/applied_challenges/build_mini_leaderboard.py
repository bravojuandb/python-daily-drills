"""
Drill — Build Mini Leaderboard (sort + dict)

You’re given a list of "score events" from a game.  
Each event is one player earning some amount of points.


Your job:
Write a function leaderboard(events: list[dict]) -> list[tuple[str, int]]
that returns a sorted leaderboard of total points per player,
in DESCENDING order (highest score first).

Expected output for the list above:
[
    ("bob", 25),
    ("alice", 20),
    ("carol", 12)
]

Requirements:
1. First, you must AGGREGATE points per player using a dict:
   {"alice": 20, "bob": 25, "carol": 12}
2. Then you must SORT that dict by total score, highest first.
3. Return the sorted result as a list of (player, total_score) tuples.

Rules / Edge behavior:
- Player names should be treated case-insensitively ("Alice" == "alice"):
  normalize names to lowercase before counting.
- If a player appears only once, they still show up.
- You do NOT need to handle negative points or weird data types here.

Hints you ARE allowed to use:
- To aggregate totals:
    scores[player] = scores.get(player, 0) + points
- To sort by value in descending order:
    sorted(scores.items(), key=lambda x: x[1], reverse=True)

Be quick and precise.
"""

events = [
    {"player": "alice", "points": 10},
    {"player": "bob",   "points": 5},
    {"player": "alice", "points": 7},
    {"player": "carol", "points": 12},
    {"player": "bob",   "points": 20},
    {"player": "alice", "points": 3},
]

def leaderboard(events: list[dict]) -> list[tuple[str, int]]:

    scores = {}
    for event in events:
        player = str(event["player"].lower())
        points = float(event["points"])
        scores[player] = scores.get(player, 0) + points
    return sorted(scores.items(), key= lambda x: x[1], reverse=True)

print(leaderboard(events))