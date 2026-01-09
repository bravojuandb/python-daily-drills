"""
Drill 06 — Preserve identifiers as strings

Goal:
Protect code-like fields from numeric coercion and formatting loss.

Rules:
- Ensure identifier columns remain pandas string dtype (not numeric):
  - dnici
  - codpost
  - cod_cmun
  - id (or _id, depending on your header)
- Never cast identifiers to numeric types
- Do not remove leading zeros
- Do not add or change zero-padding unless explicitly required by a rule
- This step must NOT coerce invalid identifier values into pd.NA; it should only flag/report invalid and missing values.

Completion criteria:
- Identifier columns have dtype "string"
- Leading zeros are preserved (spot-check dnici, cod_cmun)
"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values
from .fix_cnae_cols import fix_cnae_columns
from .fix_portalt_col import fix_portalt_column
from .cast_year_to_int import enforce_year_to_integer

def preserve_identifiers(df: pd.DataFrame, *, verbose: bool = False) -> pd.DataFrame:

    """
    Keep identifier columns as strings so they are not broken by numeric casting.

    This step:
    - Converts identifier columns (like dnici and codpost) to pandas "string" dtype.
    - Preserves leading zeros.
    - Checks whether codpost and dnici look valid (without changing the data).
    - Counts missing and invalid values for logging.

    This step does NOT:
    - Modify or fix identifier values.
    - Replace invalid values with pd.NA.

    If verbose=True, prints the counts of missing and invalid values.
    """
    # Enforce string dtype for identifier-like columns (preserve leading zeros)
    base_id_cols = ["_id", "id", "dnici", "codpost", "cod_cmun"]
    string_columns = [c for c in base_id_cols if c in df.columns]

    for col in string_columns:
        df[col] = df[col].astype("string")

    # validate codpost format (5 digits for Spanish postal codes) not destructive
    codpost_ok = None
    if "codpost" in df.columns:
        codpost_ok = df["codpost"].str.fullmatch(r"\d{5}", na=False)
        codpost_ok = codpost_ok & (df["codpost"] != "00000")  # Reject 00000

    # Validate dnici format (DNI, NIE, CIF) not destructive
    dnici_ok = None
    if "dnici" in df.columns:
        s = df["dnici"].str.upper()

        dni_ok = s.str.fullmatch(r"\d{8}[A-Z]", na=False)
        nie_ok = s.str.fullmatch(r"[XYZ]\d{7}[A-Z]", na=False)
        cif_ok = s.str.fullmatch(r"[ABCDEFGHJNPQRSUVW]\d{7}[0-9A-Z]", na=False)

        dnici_ok = dni_ok | nie_ok | cif_ok

    # Expose issues (convert counts to Python int for safe logging/serialization)
    missing_codpost = int(df["codpost"].isna().sum()) if "codpost" in df.columns else 0
    missing_dnici = int(df["dnici"].isna().sum()) if "dnici" in df.columns else 0

    invalid_codpost = int((~codpost_ok & df["codpost"].notna()).sum())
    invalid_dnici = int((~dnici_ok & df["dnici"].notna()).sum())


    issues = {
        "invalid_codpost_count": invalid_codpost,
        "missing_codpost_count": missing_codpost,
        "invalid_dnici_count": invalid_dnici,
        "missing_dnici_count": missing_dnici,
    }

    if verbose:
        for issue, count in issues.items():
            print(f"{issue}: {count}")
        
    return df

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)

    df = fix_cnae_columns(df)
    df = fix_portalt_column(df)

    df = enforce_year_to_integer(df)

    df = preserve_identifiers(df, verbose=True)

    # Quick sanity checks
    print("\nDtypes:\n", df.dtypes)
    print("\nSample rows:\n", df.head(5))
