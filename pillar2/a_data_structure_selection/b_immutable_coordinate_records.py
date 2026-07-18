"""
Drill 02 - Immutable Coordinate Records

Write make_coordinate(x, y, label) -> tuple[int, int, str]. Then write
move_coordinate(record, dx, dy) which returns a new record with the same label.
Do not modify or convert the original tuple.

Example: move_coordinate((2, 3, "A"), -1, 4) returns (1, 7, "A").

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: represent a fixed-shape record whose values should not mutate.
"""


def make_coordinate(x: int, y: int, label: str) -> tuple[int, int, str]:
    return x, y, label


def move_coordinate(
    record: tuple[int, int, str], dx: int, dy: int
) -> tuple[int, int, str]:
    x, y, label = record
    return x + dx, y + dy, label


if __name__ == "__main__":
    point = make_coordinate(1, 1, "B")
    print(move_coordinate(point, 1, 1))


# Worst-case time: O(1)
# Worst-case extra space: O(1)
# The record always contains three values, so unpacking, updating values, and creating
# the new tuple are constant-time operations. Returning a new tuple preserves
# the original record unchanged.