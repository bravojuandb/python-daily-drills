"""
Drill 08 - Graph Reachability

Write can_reach(graph, start, target) -> bool for a directed adjacency-list
graph. Use DFS or BFS plus a visited set. Missing nodes have no outgoing edges.
Return True immediately when start == target and terminate safely on cycles.

Target complexity: O(V + E) time and O(V) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: visited state prevents cycles and duplicate work.
"""


def can_reach(
    graph: dict[str, list[str]], start: str, target: str
) -> bool:
    pass
