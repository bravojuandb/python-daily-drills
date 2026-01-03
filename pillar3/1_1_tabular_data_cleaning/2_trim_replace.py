"""
Drill 02 — Trim whitespace and standardize empty strings

Normalize trivial missing values without changing meaning.

- Apply `.str.strip()` to selected string columns
- Replace empty strings `""` with `pd.NA`
- Do not introduce new nulls beyond true empties
- Keep identifiers and free-text semantics intact
"""

from pathlib import Path
import pandas as pd


def read_registry(file: Path) -> pd.DataFrame:

    df = pd.read_csv(
        file, 
        dtype="string", 
        keep_default_na=False
    ) 
    return df


def normalize_registry(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trim leading/trailing whitespace from all string columns
    and convert empty strings to pd.NA.
    """
    text_cols = df.columns

    df[text_cols] = df[text_cols].apply(lambda s: s.str.strip())
    df[text_cols] = df[text_cols].replace("", pd.NA)

    return df


def assert_no_leading_trailing_whitespace(df: pd.DataFrame) -> None:
    mask = df.apply(lambda s: s.str.contains(r"^\s|\s$", regex=True, na=False))
    assert not mask.any().any(), "Leading/trailing whitespace found"


def assert_no_empty_strings(df: pd.DataFrame) -> None:
    assert (df == "").sum().sum() == 0, "Empty strings still present"


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

df = read_registry(FILE_PATH)
df = normalize_registry(df)

assert_no_leading_trailing_whitespace(df)
assert_no_empty_strings(df)

print("passed: no leading/trailing whitespaces, and no empty strings.")