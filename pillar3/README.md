# Pillar 3 — Applied Data Processing & Integration

Build small Python tasks that read, clean, combine, validate, and deliver data.
The aim is to explain decisions, check results, and handle failures with tools
that solve concrete problems.

## Current status

The curriculum is planned: **8 chapters and 124 drills**, including 3 optional
DuckDB drills. The chapter directories, prompts, and implementations have not
been created. Prepare one selected block at a time; this count measures planned
coverage, not completed work or mastery.

On 3 October 2026, the previous Pillar 3 exercises, CSV dataset, README files,
and local notes moved to `archive/pillar3/`. The archive is ignored by Git and
is not included in new clones. It remains local reference material and is
excluded from automatic pytest discovery.

## Planned chapters

| Chapter | Focus | Planned drills |
| --- | --- | --- |
| A — Files & Formats | Paths, text, CSV, JSON, JSON Lines, gzip | 11 |
| B — Pandas Foundations & Cleaning | DataFrames, missing values, text, identifiers, types, Excel I/O | 18 |
| C — Tabular Transformations | Derived columns, aggregation, joins, dates, reshaping, duplicates | 15 |
| D — Reliable Scripts & Validation | CLI, configuration, errors, logs, tests, subprocess, reproducible environments, Pandera | 21 |
| E — HTTP APIs & Object Storage | HTTP ingestion, pagination, retries, FastAPI endpoints, S3 | 21 |
| F — Python Database Integration | Psycopg, parameters, transactions, SQLAlchemy, pandas transfers | 12 |
| G — Parquet & Local Processing Costs | Schema preservation, memory, chunking, optional DuckDB comparison | 10 |
| H — PySpark & Distributed Processing | Local DataFrames, execution, partitions, plans, outputs, tests | 16 |

Each chapter follows **chapter → subchapter → drill**. The planned chapter
directories are:

```text
pillar3/
├── a_files_and_formats/
├── b_pandas_foundations_and_cleaning/
├── c_tabular_transformations/
├── d_reliable_scripts_and_validation/
├── e_http_apis_and_object_storage/
├── f_python_database_integration/
├── g_parquet_and_local_processing_costs/
└── h_pyspark_and_distributed_processing/
```

For example, a future drill path is
`pillar3/c_tabular_transformations/b_joins/drill_02_left_join.py`.
These paths describe the target structure, not existing modules to run.

## Recommended learning route

Chapter letters organize topics; the learning route revisits them as needed.
There is no requirement to finish Pillar 2 before starting here.

1. **Start with paths, an environment, and small tests.** Combine A's path/text
   basics with D's dependency declarations and first function/file tests.
2. **Learn files and pandas cleaning.** Work through CSV/JSON and B's DataFrame,
   missing-value, text, and type exercises. Check identifiers, schema, and counts.
3. **Transform and deliver tables.** Study C, then B's Excel subchapter. Practise
   dates before selecting the latest record; justify join cardinality and totals.
4. **Make the script repeatable.** Use D's CLI, configuration, error handling,
   logs, and tests. Recreate its environment and verify repeated execution.
5. **Integrate data sources and outputs.** Study E's HTTP client exercises,
   F's database integration, and G's Parquet exercises. F can precede HTTP when
   the chosen task uses a database.
6. **Consolidate quality and processing costs.** Apply Pandera and memory/chunking
   exercises to transformations already understood.
7. **Choose extensions for a concrete task.** Add FastAPI, S3, subprocess, or
   optional DuckDB as useful. Start PySpark after understanding schemas, joins,
   aggregation, and Parquet; it does not require the other extensions first.

Tests accompany every stage. Core practice takes priority over collecting
libraries. A drill a day is a possible pace, not a deadline; review, corrections,
and new variations also count as practice.

## How drills build understanding

Prompts state a short, explicit contract before technique hints. Each introductory
drill adds one main idea; closing drills combine familiar ideas with new data.
Useful checks include:

- Preserving identifiers and explaining missing or invalid values.
- Detecting a join that multiplies records and reconciling aggregate totals.
- Consolidating daily sheets with an explicit schema policy, then reopening
  the output to verify it.
- Repeating a load without unintended duplicates and verifying rollback after
  an intermediate failure.

Use small synthetic inputs and temporary output paths. Documentation is allowed.
Progress means choosing an approach, implementing it, explaining it, and checking
a new case or failure; those are separate pieces of evidence.

## Scope and dependencies

Start with the standard library. Introduce pandas/openpyxl, pytest/Pandera,
Requests, Psycopg/SQLAlchemy, PyArrow, and the extension tools only for their
selected exercises. uv and `pyproject.toml` support reproducible environments;
FastAPI introduces Pydantic models and HTTPX-backed tests.

The root `requirements.txt` currently installs pytest and Ruff, not this full
curriculum. No new Pillar 3 environment or run commands are established yet.
CI lint currently covers Pillars 1 and 2; a green CI run does not verify the
planned Pillar 3 exercises.

Keep deeper SQL queries and modelling in the separate MySQL/PostgreSQL study
repository, reusing known SQL here. Dedicated Bash study is outside this
curriculum, while basic terminal use remains part of running Python tools.
Deployment, scheduling, orchestration, and operating complete data systems
belong in [Pillar 4](../pillar4/README.md).
