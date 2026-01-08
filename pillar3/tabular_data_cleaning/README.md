# Tabular Data Cleaning

This folder implements a **minimal but real-world tabular data cleaning contract**.

It uses a trimmed subset of a real CSV registry of economic establishments in Navarra, Spain:

- `data/navarra_trimmed.csv`

Each drill corresponds to a Python script that can be executed as a **module**.  
Later drills build on earlier ones. For example, running the script for **Drill 03 (handle_nulls)** will internally reuse logic from **Drill 01 (read_csv)** and **Drill 02 (normalize_csv)**.

## How to run

Activate the virtual environment and move to `pillar3/`:

```bash
source ../venv/bin/activate
cd pillar3
```

Run any script as a module:

```bash
python -m tabular_data_cleaning.normalize_csv
```

### Drill 01 — Read CSV as strings on purpose
**Goal:** Preserve identifiers and avoid numeric surprises.  
- Use `pd.read_csv(..., dtype="string", keep_default_na=False)`
- Verify leading zeros are preserved

---

### Drill 02 — Trim whitespace and standardize empty strings
**Goal:** Normalize trivial missing values.  
- Apply `.str.strip()` to selected string columns  
- Replace empty strings `""` with `pd.NA`

---

### Drill 03 — Replace placeholder values with nulls
**Goal:** Make missing data explicit.  
- Replace placeholders like `"."`, `"--"`, `"0"` with `pd.NA`
- Apply replacements **only where semantically correct**

---

### Drill 04 — Remove trailing `.0` from code-like columns
**Goal:** Fix formatting artifacts from numeric parsing.  
- Clean values like `"6910.0"` → `"6910"`
- Use regex replacement anchored at end of string

---

### Drill 04.1 — Normalize address portal numbers

**Goal:** Enforce domain rules for address portal numbers without affecting free-text values.

- Apply the rule: portal numbers must be integers (no decimals)
- Remove trailing `.0` from numeric portal values (e.g. `"6.0"` → `"6"`)
- Do **not** modify non-numeric tokens (`"PBJ"`, `"BAJO"`, `"ENT"`, etc.)
- Preserve original meaning of address components

---

### Drill 05 — Enforce year as nullable integer
**Goal:** Apply correct numeric typing without data loss.  
- Convert year columns using `pd.to_numeric(errors="coerce")`
- Cast to pandas nullable integer type `Int64`

---

### Drill 06 — Preserve identifiers as strings
**Goal:** Protect codes and identifiers.  
- Ensure columns like `dnici`, `codpost`, `cod_cmun` remain `string`
- Never cast identifiers to numeric
- Apply zero-padding only if explicitly required
- Validate identifiers (e.g. `codpost` must be exactly five digits)

---

### Drill 07 — Minimal cleaning of free-text fields
**Goal:** Avoid corrupting descriptive data.  
- Apply `.str.strip()` only
- No casing changes, no replacements, no normalization

---

### Drill 08 — Remove exact duplicate rows
**Goal:** Deduplicate safely.  
- Use `df.drop_duplicates()`
- No fuzzy matching, no subset logic
- Log before/after row counts

---

## Completion Criteria

These drills are considered complete when:
- You can write them without looking up documentation
- Each script is fully understood line by line
- The process feels mechanical and boring
