# CLI contract

A small command-line tool to clean text files for data pipelines.  
Uses **argparse** for CLI, **pathlib** for file handling, and **logging** for progress messages.  
Part of *python-daily-drills* (Pillar 3 – Script Engineering).


## Usage

- Minimal run: only lowercase the text
    ```bash
    python textcleaner.py --input input.txt --output cleaned.txt --lower
    ```
- Full pipeline: apply all steps
    ```bash
    python textcleaner.py --input input.txt --output cleaned.txt --trim --collapse-spaces --lower --strip-empty
    ```

## Required Flags
```bash
--input → Path to input .txt file
--output → Path to save cleaned .txt file
```

## Optional Flags

```bash
--lower → lowercase all text
--strip-empty → drop empty/whitespace-only lines
--collapse-spaces → replace multiple spaces with a single space (line-wise)
--trim → strip leading/trailing whitespace per line
--verbose → set logging level to INFO (default WARNING)
```

## Cleaning Pipeline

Cleaning steps are applied in this order, for the flags you enable:

1.	**Trim** → strip leading/trailing whitespace (so collapsing spaces works cleanly).
2.	**Collapse-spaces** → replace multiple spaces with one (line-wise).
3.	**Lower** → normalize case after spacing/trim fixes.
4.	**Strip-empty** → finally remove any lines that became empty.

## Logging

- **INFO:** start, file paths, enabled options, line counts before/after
- **WARNING:** non-fatal issues (e.g., empty input)
- **ERROR:** critical issues (missing/unreadable file)

## Constraints

- Pure Python standard library (argparse, pathlib, logging).
- Input: plain UTF-8 text.
- Output: overwrites if file exists; creates parent directories if needed.