"""
Drill 04 - Validate References Containing Digits and Letters

Goal: distinguish validation from normalization.
Prerequisites: text Series, missing values, and Boolean masks.

Contract:
- A valid reference is one or more ASCII digits (0-9), optionally followed
  by one ASCII letter (A-Z or a-z). The whole value must match.
- Return a Series of dtype "bool": True for valid references, False for all
  others, including empty text and missing values. Never return missing flags.
- Leading zeros are valid. Signs, spaces, decimal points, extra letters,
  and non-ASCII digits are invalid; do not clean them before validation.
- Keep the index and name. Do not modify values or remove rows.
  The shared rules in ../README.md apply.

Examples (Series values -> validity flags):
["12", "003b", "A12", pd.NA] -> [True, True, False, False]
["12AB", " 12", "12.0", "", "１２"] -> [False, False, False, False, False]
[] -> [] with dtype "bool"

Tools: pandas; regex or standard-library string checks are allowed.
Cost check: account for examining characters and returning one flag per row.
Thinking goal: how would silently trimming first change this contract?
"""

import pandas as pd


def validate_mixed_text_values(values: pd.Series) -> pd.Series:
    pattern = r"[0-9]+[A-Za-z]?"
    flags = values.str.fullmatch(pattern)
    flags = flags.fillna(False)
    flags = flags.astype("bool")

    return flags

if __name__ == "__main__":

    examples = [
        (["12", "003b", "A12", pd.NA], [True, True, False, False]),
        (["12AB", " 12", "12.0", "", "１２"], [False, False, False, False, False]),
        ([], []),
    ]

    for raw, expected_list in examples:
        index = [10, 20, 30, 40, 50][: len(raw)]
        values = pd.Series(raw, dtype="string", name="ref", index=index)
        original = values.copy()

        result = validate_mixed_text_values(values)
        expected = pd.Series(expected_list, dtype="bool", name="ref", index=index)

        # Checks flags, dtype "bool", index and name in one go
        pd.testing.assert_series_equal(result, expected)
        # Input must be unchanged
        pd.testing.assert_series_equal(values, original)

    print("All examples pass")


