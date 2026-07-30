"""
Drill 05 - Group Records

Write group_by_department(employees) -> dict[str, list[dict]]. Group records by
their "department" value. Preserve first department appearance and record order
inside each group. Do not mutate records; complete grouping in one pass.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: grouping maps one key to a growing collection of matching items.
"""


def group_by_department(employees: list[dict]) -> dict[str, list[dict]]:
    result = {}

    for record in employees:
        group_key = record["department"]

        if group_key not in result:
            result[group_key] = []

        result[group_key].append(record)

    return result


# Time: O(n), because every employee record is processed once, with
# average O(1) dictionary lookup and list append operations.

# Extra space: O(n + k), which simplifies to O(n), where n is the number
# of employee references stored in the lists and k is the number of
# distinct department keys.