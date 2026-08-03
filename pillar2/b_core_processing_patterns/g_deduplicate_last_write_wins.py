"""
Drill 07 - Deduplicate with Last-Write-Wins

Write deduplicate_users(records) -> list[dict]. Email is the unique key and must
be compared case-insensitively. The last record for an email wins, but the email
keeps the position where it first appeared. Missing or blank emails are skipped.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: deduplication requires both an identity rule and a conflict rule.
"""


def deduplicate_users(records: list[dict]) -> list[dict]:
    result = []
    email_to_position = {}

    for record in records:
        email = record.get("email", "").strip().lower()

        if not email:
            continue

        if email in email_to_position:
            position = email_to_position[email]
            result[position] = record
        else: 
            email_to_position[email] = len(result)
            result.append(record)

    return result


# Time complexity: O(n) on average, where n is the number of input records.
# Each record is processed once, and dictionary operations plus list updates
# take O(1) average time.
# Extra-space complexity: O(n), because the result list and position mapping
# may grow with the number of distinct valid email addresses.
