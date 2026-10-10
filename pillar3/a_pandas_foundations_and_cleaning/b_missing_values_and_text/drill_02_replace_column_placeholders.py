"""
Drill 02 - Replace Placeholders by Column

Goal: apply missing-value rules only where they are defined.
Prerequisites: Drill 01, dictionaries, sets, and column selection.

Contract:
- markers maps existing column names to sets of placeholder strings.
  Each mapped column has dtype "string".
- Replace exact matches in that column with pd.NA. Matching is case-sensitive;
  do not trim text, match substrings, or interpret regex patterns.
- Preserve existing missing values, unmatched values, and unmapped columns.
- Return a DataFrame with the original shape, index, columns, and dtypes.
  Empty marker sets or an empty mapping make no value changes.
- Do not modify inputs. The shared rules in ../README.md apply.

Examples, with frame = {"zone": ["NA", " NA "], "note": ["NA", "ok"]}:
markers={"zone": {"NA"}}
    -> {"zone": [pd.NA, " NA "], "note": ["NA", "ok"]}
markers={} -> the original values

Tools: pandas and standard-library helpers; see optional README hints.
Cost check: include targeted columns, marker sets, and any copied columns.
Thinking goal: what would a table-wide replacement of "NA" get wrong?
"""

import pandas as pd


def replace_column_placeholders(
    frame: pd.DataFrame, markers: dict[str, set[str]]
) -> pd.DataFrame:
    
    frame_copy = frame.copy()

    for column, placeholders in markers.items():
        frame_copy[column] = frame[column].replace(placeholders, pd.NA)

    return frame_copy



if __name__ == "__main__":
    
    frame = pd.DataFrame(
        {
            "zone": ["North", "NA", " NA ", "unknown", pd.NA],
            "phone": ["555-1234", "N/A", "", "555-9876", pd.NA],
            "note": ["NA", "Keep this", "", "unknown", "ok"],
        },
        dtype="string",
        index=[10, 20, 30, 40, 50],
    )

    markers = {
        "zone": {"NA", "unknown"},
        "phone": {"N/A", ""},
    }

    print(replace_column_placeholders(frame, markers))