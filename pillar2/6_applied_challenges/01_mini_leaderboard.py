"""
Drill 01 - Mini Leaderboard

Each event contains "player" and integer "points". Normalize names with strip
and lowercase, skip blank names, aggregate totals, and return (player, total)
ranked by total descending then player ascending. Do not mutate events.

Example events for Alice 10, alice 5, Bob 15 produce
[("alice", 15), ("bob", 15)].

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: compose normalization, validation, aggregation, and ranking.
"""


def build_leaderboard(events: list[dict]) -> list[tuple[str, int]]:
    pass
