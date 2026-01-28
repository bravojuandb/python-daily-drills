# Bronze Ingestion – Bash & Orchestration Drills

Each drill is designed to take **15 minutes**.  
Complete them in order. Together, they cover **every concept** used in your working scripts.

---

## Drill 01 — Bash execution & arguments

**Goal**  
Understand how a Bash script receives input.

**Tasks**
- Create a script `drill01_args.sh`
- Print the script name and the values of `$1` and `$2`
- Run it with two arguments: `2002-01 2002-03`

**Outcome**
- You can explain how `FROM` and `TO` are populated
- You know how arguments reach a script

---

## Drill 02 — Variables & quoting

**Goal**  
Understand variable assignment and safe expansion.

**Tasks**
- Define three variables: `A=hello`, `B="hello world"`, `C=""`
- Print them with and without quotes
- Observe the differences

**Outcome**
- You know when and why to quote variables
- You avoid word-splitting bugs

---

## Drill 03 — while loops & termination

**Goal**  
Control repetition with conditions.

**Tasks**
- Write a `while` loop that prints months from `2002-01` to `2002-03`
- Stop exactly at the end month
- Print the current month on each iteration

**Outcome**
- You can reason about loop start/stop conditions

---

## Drill 04 — Bash string manipulation

**Goal**  
Transform strings without external tools.

**Tasks**
- Given `current="2002-01"`
- Convert it to `200201` using Bash only
- Print both values

**Outcome**
- You understand parameter expansion
- You don’t need `sed` for simple cases

---

## Drill 05 — Deterministic path building

**Goal**  
Build predictable filesystem paths.

**Tasks**
- Given `BASE_DIR=data/raw/comext_products`
- Given `month=2002-01`
- Print the full output path for `full_200201.7z`

**Outcome**
- You understand deterministic data layouts

---

## Drill 06 — Idempotency with files

**Goal**  
Make scripts safe to re-run.

**Tasks**
- Write a script that:
  - Creates a file
  - Skips creation if the file already exists
- Run it twice

**Outcome**
- You understand idempotent behavior
- You can explain “safe re-runs”

---

## Drill 07 — External commands & failure

**Goal**  
Learn how scripts fail correctly.

**Tasks**
- Use `curl` to download a small file
- Add `set -e`
- Force a failing URL and observe behavior

**Outcome**
- You know why pipelines must fail fast
- You understand exit codes

---

## Drill 08 — Temporary directories

**Goal**  
Avoid partial or corrupted outputs

**Tasks**
- Create a temporary directory
- Write a file into it
- Move the file to a final location
- Delete the temporary directory

**Outcome**
- You understand atomic operations
- You know why temp folders exist

---

## Drill 09 — Orchestration with Python

**Goal**  
Use Python as a controller, not a worker.

**Tasks**
- Write a Python script that runs:
  - one Bash script
  - then another
- Stop execution if the first fails

**Outcome**
- You understand `subprocess.run`
- You understand orchestration vs logic

---
