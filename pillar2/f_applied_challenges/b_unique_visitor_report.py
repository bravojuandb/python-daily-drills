"""
Drill 02 - Unique Visitor Report

Write unique_visitor_report(lines) returning {"unique": int, "repeat": int}.
Each nonblank line is an IP visit. unique is the number of distinct IPs; repeat
counts visits after an IP's first appearance. Process any iterable in one pass.

Example: ["a", "b", "a", ""] returns {"unique": 2, "repeat": 1}.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: use set membership while tracking two related metrics.
"""

from collections.abc import Iterable


def unique_visitor_report(lines: Iterable[str]) -> dict[str, int]:
    pass
