# Pillar 3 — Applied Data Engineering Drills (Automation & Integration)


## 1. File & Data Handling

-   Parse CSV Files → `csv` / `pandas.read_csv()`
-   Read & Write JSON → `json.load()` / `json.dump()`
-   Work with YAML Configs → `yaml.safe_load()`
-   Save as Parquet → `pandas.to_parquet()`
-   Handle Compressed Files → `gzip`, `.zipfile`

---

## 2. Configs & CLI Tools

-   Add CLI arguments → `argparse`
-   Load parameters from YAML
-   Read secrets from `.env` → `os.getenv`
-   Combine CLI + config for flexible scripts
-   Create usage examples in README

---

## 3. Logging & Error Handling

-   Implement logging → `logging.basicConfig()`
-   Use structured JSON logs
-   Raise custom exceptions → `class DataError(Exception)`
-   Wrap ETL steps in `try/except`
-   Write logs to file and console

---

## 4. Testing & Validation

-   Set up `pytest` in `tests/`
-   Write unit tests for parsing/cleaning
-   Test error cases with `pytest.raises`
-   Validate small datasets (row counts, columns)
-   Automate tests via GitHub Actions

---

## 5. Local ETL Pattern

-   Build `extract.py` / `transform.py` / `load.py`
-   Use config for input/output folders
-   Chain steps via main script
-   Log each stage result
-   Produce clean output in `/data_clean/`

---

## 6. Mini Warehouse & SQL

-   Load cleaned data into SQLite or Postgres
-   Define schema via DDL
-   Insert or upsert transformed rows
-   Run analytical queries (aggregations)
-   Export query results to CSV/Parquet

---

## 7. Cloud Storage Basics

-   Connect to AWS S3 via `boto3`
-   Upload raw → clean → warehouse files
-   Manage credentials securely
-   Implement download utility
-   Verify integrity after transfer

---

## 8. Lightweight Orchestration

-   Automate ETL run via `cron` or Makefile
-   Add simple dependency handling
-   Integrate with GitHub Actions CI
-   Store logs of last run
-   Document schedule and run command

