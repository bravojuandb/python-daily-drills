# Pillar 3 — Applied Data Processing & Integration

Read, clean, combine, validate, and deliver data with Python.
Start with pandas; file concepts are introduced when needed.

## Study order

Chapter and subchapter letters follow the learning sequence.

| Chapter | Focus |
| --- | --- |
| [A — Pandas Foundations & Cleaning](a_pandas_foundations_and_cleaning/README.md) | DataFrames, CSV, missing values, text, types, identifiers |
| B — Tabular Transformations & Excel | Aggregation, joins, dates, duplicates, workbooks |
| C — Reliable Scripts & Validation | Tests, environments, JSON, CLI, errors, Pandera |
| D — API Ingestion | HTTP requests, pagination, retries, saved responses |
| E — Python Database Integration | Psycopg, transactions, SQLAlchemy, pandas transfers |
| F — Parquet & Local Processing Costs | Schemas, memory, chunking, optional DuckDB |
| G — Data Services & Object Storage | FastAPI, Pydantic, S3 with boto3 |
| H — PySpark & Distributed Processing | DataFrames, execution plans, partitions, local tests |

Prioritize A–F, then extend with G–H. Subprocess (C) and DuckDB (F) are optional.
Files & Formats is a separate support block, used as needed.
Practise checks from the first drill; C formalizes testing and reproducibility.

## Status and scope

The plan contains **115 drills in A–H and 9 supporting drills**. Chapter A has
**13 unsolved templates**; the other chapters remain planned. Previous work
remains locally in the Git-ignored `archive/pillar3/`.

Introduce dependencies per block; the root `requirements.txt` only includes
pytest and Ruff. Deeper SQL belongs in the separate SQL repository; deployment
and complete data systems belong in [Pillar 4](../pillar4/README.md).
