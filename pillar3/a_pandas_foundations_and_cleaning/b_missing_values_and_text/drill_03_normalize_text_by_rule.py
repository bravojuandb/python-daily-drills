"""
Drill 03 - Normalize Status Labels by Rule

Goal: turn different spellings of a status into a consistent label.
Prerequisites: Drill 01 and replacing exact values from Drill 02.

Contract:
- Given a string Series, trim outer whitespace and lowercase nonmissing text.
- After that normalization, replace exactly "wip" with "pending" and "done"
  with "closed". Leave other nonempty labels as their normalized text.
- Turn blank text into pd.NA and preserve existing missing values.
- Preserve internal whitespace and punctuation; this drill does not reject
  unknown labels. Return dtype "string" with the original index and name.
- Do not modify the input. The shared rules in ../README.md apply.

Examples (Series values):
[" WIP ", "Done", "OPEN"] -> ["pending", "closed", "open"]
["  On  Hold  ", "done!", pd.NA] -> ["on  hold", "done!", pd.NA]
[" ", "NA"] -> [pd.NA, "na"]

Tools: pandas text operations and replacement; optional README hints apply.
Cost check: account for multiple passes over the text and temporary results.
Thinking goal: why do aliases apply after trimming and changing case?
"""

import pandas as pd


def normalize_status(values: pd.Series) -> pd.Series:

    values = values.str.strip()
    values = values.str.lower()
    values = values.replace({"wip": "pending", "done": "closed"})

    # Left outside the dictionary, it's a different rule
    values = values.replace("", pd.NA)

    return values



if __name__ == "__main__":

    examples = [
        ([" WIP ", "Done", "OPEN"], ["pending", "closed", "open"]),
        (["  On  Hold  ", "done!", pd.NA], ["on  hold", "done!", pd.NA]),
        ([" ", "NA"], [pd.NA, "na"]),
    ]

    for raw, expected_list in examples:
        values = pd.Series(raw, dtype="string", name="status", index=[10, 20, 30][: len(raw)])
        original = values.copy()

        result = normalize_status(values)
        expected = pd.Series(expected_list, dtype="string", name="status", index=values.index)

        # Checks values, missing values, dtype, index and name in one go
        pd.testing.assert_series_equal(result, expected)
        # Input must be unchanged
        pd.testing.assert_series_equal(values, original)

    print("All examples pass")