"""
Drill 08 — Remove exact duplicate rows

Goal:
Remove fully duplicated records while preserving data meaning.

Rules:
- Use pandas `df.drop_duplicates()` with default behavior
- Do NOT specify subsets or fuzzy logic
- Do NOT attempt to reconcile near-duplicates
- Preserve the first occurrence of each exact row

Validation:
- Log row count before deduplication
- Log row count after deduplication
- Assert that the number of rows does not increase

Rationale:
Exact duplicates indicate ingestion or source duplication.
Removing them is safe and non-destructive, unlike heuristic deduplication.

Completion:
- Deduplication is deterministic
- No column-level logic is applied
- No semantic assumptions are introduced
"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values
from .fix_cnae_cols import fix_cnae_columns
from .fix_portalt_col import fix_portalt_column
from .cast_year_to_int import enforce_year_to_integer
from .preserve_codes_as_strings import preserve_identifiers
from .handle_free_text_fields import ensure_string_columns

def remove_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows using default pandas behavior.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Row count before deduplication: {before}")
    print(f"Row count after deduplication:  {after}")

    return df

def assert_duplicate_rows(df: pd.DataFrame) -> None:
    dup_count = int(df.duplicated().sum())
    return dup_count == 0, f"Duplicate rows detected: {dup_count}"


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    text_cols = [
        "nombre",
        "callet",
        "nombre_cmun",
        "cnae09_descrip_ppal",
        "cnae09_descrip_local",
        "denominacion_entidad",
    ]
        
    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)
    df = fix_cnae_columns(df)
    df = fix_portalt_column(df)
    df = enforce_year_to_integer(df)
    df = preserve_identifiers(df, verbose=False)
    df = ensure_string_columns(df, text_cols)
    df = remove_duplicate_rows(df)

    assert_duplicate_rows(df)
