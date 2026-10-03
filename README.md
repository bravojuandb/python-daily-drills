# Python Daily Drills 

[![Tests and lint](https://github.com/bravojuandb/python-daily-drills/actions/workflows/quality.yml/badge.svg)](https://github.com/bravojuandb/python-daily-drills/actions/workflows/quality.yml)

A structured collection of Python exercises focused on data manipulation, problem-solving, automation, and data systems.

The exercises are organized into four foundational areas, which I call pillars:

- Pillar 1: Fluency & Logic
- Pillar 2: Data Structures & Problem Solving
- Pillar 3: Applied Data Processing & Integration
- Pillar 4: Project-like Drills & Systems

## Current repository status

Pillar 1 is established. Pillar 2's new curriculum begins with
[Linear Processing](pillar2/a_fundamentals_and_complexity/a_linear_processing/README.md)
under Fundamentals & Complexity. The remaining curriculum is planned.

Pillar 3 intends covering files, pandas, reliable scripts, APIs,
databases, Parquet, and PySpark. Its chapter directories and drills are planned.
See the [Pillar 3 guide](pillar3/README.md) for priorities and progression.

Pillar 4 remains a roadmap for integrated data systems.

Pillar 1 uses numbered chapters. Pillar 2 uses three curricular layers:
algorithmic family, pattern, and progressive drills. Pillar 3's planned structure
uses chapter, subchapter, and progressive drills. Families and patterns
have letter prefixes; drills use local numbering. For example:
`pillar2/a_fundamentals_and_complexity/a_linear_processing/drill_01_count_matches.py`.
The names preserve order while remaining valid as importable Python modules.

Each smaller group consists of exercises—called drills—that follow this structure:

```
"""
Drill n - Demo Prompt

Prompt description, requirements, goal, constraints.

Example: input vs. output

Complexity check: Define big O notation for time and space

Thinking goal: desired takeaway.
"""

Function signature and learner implementation (or an unsolved template)

```


## Repository structure

### Pillar 1: Fluency & Logic
Think in Python without stumbling on syntax.  
- **What it covers:** Core data types, loops, functions, comprehensions, error handling, I/O basics.  
- [Contents](pillar1/README.md)


### Pillar 2: Data Structures & Problem Solving
Develop algorithmic thinking by selecting appropriate data structures, recognizing reusable processing patterns, and evaluating solution tradeoffs.  
- **What it covers:** Data-structure selection, filtering and aggregation, searching and ranking, sequence and graph traversal, recursion, complexity analysis, performance tradeoffs, and applied data-processing challenges.  
- **Available now:** Six Linear Processing drills: count matches, running total, maximum, first minimum's position, second largest distinct value, and longest streak.
- **Planned progression:** Fundamentals & Complexity → Searching & Sorting → Hashing & Lookup → Sequence Patterns → Stacks & Queues → Recursion → Divide & Conquer → Dynamic Programming → Node-Based Structures → Graphs.
- [Contents](pillar2/README.md)


### Pillar 3: Applied Data Processing & Integration
Read, clean, combine, validate, and deliver data through reproducible Python tasks.

- **Core:** CSV/JSON, pandas and Excel, joins and aggregation, testing, reliable
  scripts, HTTP ingestion, PostgreSQL integration, and Parquet.
- **Extensions:** Pandera, local processing costs, FastAPI, S3, optional DuckDB,
  and PySpark after its prerequisites.
- **Available now:** The curriculum and recommended learning route. The new
  exercise files have not been created.
- **Scope:** Deeper SQL practice belongs in a separate SQL repository;
  deployment, orchestration, and operating complete systems belong in Pillar 4.
- [Contents](pillar3/README.md)


### Pillar 4: Project-like Drills & Systems (Incomplete—Under Review)
End-to-end pipeline-like systems.  
- **What it covers:**  
  - Full ETL/ELT pipelines  
  - Scheduling (cron, Airflow-like)  
  - Data quality checks  
  - Cloud storage and orchestration  
  - Documentation, GitHub repos, CI/CD  
- [Contents](pillar4/README.md)
