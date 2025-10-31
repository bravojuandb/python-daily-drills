# Pillar 4 — Data Engineering Systems (Project-Style Drills)


## 1. Pipeline Design & Structure
-   Draw a minimal pipeline architecture (raw → clean → warehouse)
-   Create a standard folder layout (`src/`, `data_raw/`, `data_clean/`, `tests/`)
-   Add `.env.example` and `config.yaml` for environment isolation
-   Draft a run order (`extract` → `transform` → `load`) with dependency comments
-   Document the structure in a 10-line Markdown summary

---

## 2. Parameterization & Configuration
-   Convert hard-coded values to YAML parameters
-   Load configs dynamically → `yaml.safe_load()`
-   Switch environments (dev/prod) via CLI flag
-   Validate missing keys and raise errors
-   Log the loaded configuration on startup

---

## 3. Data Quality & Validation
-   Implement a quick row-count check before and after transform
-   Verify column schema using `pandas.dtypes`
-   Write a `pytest` that fails on nulls or duplicates
-   Generate a small quality report (`pass / fail / % valid`)
-   Store validation logs in `/reports/`

---

## 4. Error Handling & Recovery
-   Wrap ETL step in `try/except` with descriptive messages
-   Add a retry mechanism with `time.sleep()` backoff
-   Log errors to a dedicated `error.log`
-   Simulate a failing input file and test graceful exit
-   Summarize all failed files at the end of run

---

## 5. Scheduling & Orchestration Basics
-   Run your ETL script via `cron` (local)
-   Add a Makefile command `make run_etl`
-   Simulate dependency ordering using timestamps
-   Create a lightweight DAG dictionary (`{task: [dependencies]}`)
-   Record start/end time of each task in log

---

## 6. Monitoring & Logging Enhancements
-   Add log rotation (`RotatingFileHandler`)
-   Include runtime duration per step
-   Tag logs with pipeline name + run ID
-   Count warnings and errors
-   Output summary metrics at the end (rows processed, time taken)

---

## 7. Testing for Reliability
-   Add integration test that runs a mini ETL end-to-end
-   Use fixtures with sample data in `/tests/resources`
-   Assert that output files exist and contain expected rows
-   Mock a database connection (`sqlite3.connect(':memory:')`)
-   Include a `pytest.ini` with logging level settings

---

## 8. SQL & Warehouse Operations
-   Write SQL DDL for a simple staging schema
-   Run basic analytics query (TOP N, SUM, AVG)
-   Parameterize SQL with placeholders
-   Export query results as Parquet
-   Log query execution time

---

## 9. Cloud Interaction (Playground Level)
-   Upload one file to S3 via `boto3`
-   List bucket contents programmatically
-   Download file and confirm checksum
-   Handle missing credentials gracefully
-   Clean up test files automatically

---

## 10. Documentation & CI Simulation
-   Write a 20-line `README.md` explaining one drill
-   Generate a simple Mermaid diagram of your ETL
-   Create a `.github/workflows/test.yml` to run `pytest`
-   Add a status badge placeholder to README
-   Commit and push with clear message (`docs(ci): add pipeline test workflow`)
