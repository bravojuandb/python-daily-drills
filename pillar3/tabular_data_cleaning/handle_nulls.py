"""
Drill 03 — Replace placeholder values with nulls

Make missing data explicit without guessing meaning.

- Identify placeholder tokens (e.g. `"."`, `"--"`, `"0"`)
- Empty strings (missing values) were handled in drill 2
- Replace them with `pd.NA`
- Apply replacements only to columns where the placeholder truly means “missing”
- Do not touch identifiers or free-text fields

NOTE:
Your job in pipelines is to normalize everything to pd.NA before loading, 
so it maps cleanly to SQL NULL.

"""

from pathlib import Path
import pandas as pd
from .read_csv import read_registry
from .normalize_csv import normalize_registry

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace placeholder tokens with pd.NA.
    Only whole-token replacements; do not edit valid values.
    """

    placeholders_by_col: dict[str, dict[str, object]] = {
        # Contains the tokens that truly mean missing
        "portalt": {
            "0": pd.NA,
            "0.0": pd.NA,
        },
        "restot": {
            ".": pd.NA,
            ". .": pd.NA,
            "--": pd.NA,
            "-": pd.NA,
            "- -": pd.NA,
            "99": pd.NA,
        }
    }

    for col, mapping in placeholders_by_col.items():
        if col in df.columns:
            df[col] = df[col].replace(mapping)

    return df

def assert_no_placeholders(df: pd.DataFrame, col: str, tokens: list[str]) -> None:
    """Assert none of the placeholder tokens remain in the given column."""
    remaining = df[col].isin(tokens).sum()
    assert remaining == 0, f"Found {remaining} placeholder tokens still present in '{col}'"


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"


if __name__ == "__main__":

    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)
    assert_no_placeholders(df, "restot", [".", ". .", "--", "-", "- -", "99"])
    assert_no_placeholders(df, "portalt", ["0", "0.0"])
    print("passed: placeholder tokens replaced with pd.NA ")