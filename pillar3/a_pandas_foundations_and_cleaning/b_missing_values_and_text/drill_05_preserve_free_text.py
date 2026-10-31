"""
Drill 05 - Clean a Status While Preserving Free Text

Goal: transfer a known cleaning rule to a table without changing other fields.
Prerequisites: Drill 03 and DataFrame column selection.

Contract:
- frame contains string columns "status" and "note"; each row is a support
  record. Additional columns may exist.
- Normalize only status using Drill 03's rule: trim, lowercase, map "wip"
  to "pending" and "done" to "closed", and turn blanks into pd.NA.
- Keep note and every other column exactly as supplied, including whitespace,
  capitalization, blank strings, literal markers, missing values, and dtypes.
- Return the same rows, index, column order, and dtypes. Do not modify frame.
  The shared rules in ../README.md apply.

Examples (DataFrame columns):
{"status": [" DONE "], "note": ["  Keep CASE!  "]}
    -> {"status": ["closed"], "note": ["  Keep CASE!  "]}
{"status": [" ", pd.NA], "note": ["NA", ""]}
    -> {"status": [pd.NA, pd.NA], "note": ["NA", ""]}

Tools: pandas; you may reuse your solved normalize_status helper.
Cost check: distinguish transformed text from any copied table data.
Thinking goal: what check proves that cleaning did not alter the notes?
"""

import pandas as pd


def clean_status_preserve_notes(frame: pd.DataFrame) -> pd.DataFrame:
    frame_copy = frame.copy()

    status = frame_copy["status"]
    status = status.str.strip()
    status = status.str.lower()
    status = status.replace({"wip": "pending", "done": "closed"})
    status = status.replace("", pd.NA)

    frame_copy["status"] = status

    return frame_copy


if __name__ == "__main__":

    examples = [
        ({"status": [" DONE "], "note": ["  Keep CASE!  "]},
         {"status": ["closed"], "note": ["  Keep CASE!  "]}),
        ({"status": [" ", pd.NA], "note": ["NA", ""]},
         {"status": [pd.NA, pd.NA], "note": ["NA", ""]})
    ]

    for input, output in examples:
        corrupt = pd.DataFrame(input, dtype="string")
        expected = pd.DataFrame(output, dtype="string")
        original = corrupt.copy()

        result = clean_status_preserve_notes(corrupt)
        pd.testing.assert_frame_equal(result, expected)
        # Input must be unchanged
        pd.testing.assert_frame_equal(corrupt, original)

    # Extra column of another dtype and a custom index must survive
    text_dtypes = {"status": "string", "note": "string"}
    corrupt = pd.DataFrame(
        {"status": [" WIP ", "done"], "note": [" a ", ""], "qty": [3, 5]},
        index=[10, 20],
    ).astype(text_dtypes)
    expected = pd.DataFrame(
        {"status": ["pending", "closed"], "note": [" a ", ""], "qty": [3, 5]},
        index=[10, 20],
    ).astype(text_dtypes)

    pd.testing.assert_frame_equal(clean_status_preserve_notes(corrupt), expected)

    print("All examples pass")