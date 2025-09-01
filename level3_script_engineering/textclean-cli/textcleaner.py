"""
textcleaner.py — A small CLI to clean text files for data pipelines.

Usage examples:
  python textcleaner.py --input input.txt --output cleaned.txt --lower
  python textcleaner.py --input input.txt --output cleaned.txt --trim --collapse-spaces --lower --strip-empty
"""
import logging
from pathlib import Path
import argparse
import sys
import re

def configure_logging(verbose: bool) -> None:
    """Configure root logging: INFO when verbose, else WARNING."""
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s - %(message)s",
    )
    logging.info("Logging configured (level=%s)", logging.getLevelName(level))

def run(args: argparse.Namespace) -> None:
    """
    Validate paths and prepare for cleaning.
    (Next steps will add the actual line processing.)
    """
    in_path: Path = args.input
    out_path: Path = args.output

    # Log enabled options for traceability
    logging.info(
        "Start | input=%s output=%s options={trim=%s, collapse_spaces=%s, lower=%s, strip_empty=%s}",
        in_path, out_path, args.trim, args.collapse_spaces, args.lower, args.strip_empty
    )

    # 1) Input must exist and be a file
    if not in_path.exists():
        logging.error("Input file does not exist: %s", in_path)
        sys.exit(2)
    if not in_path.is_file():
        logging.error("Input path is not a file: %s", in_path)
        sys.exit(2)

    # 2) Guard against same input/output (after resolving symlinks)
    try:
        if in_path.resolve() == out_path.resolve():
            logging.error("Input and output paths refer to the same file: %s", in_path)
            sys.exit(2)
    except FileNotFoundError:
        # resolve() can raise if parent chains don’t exist yet; that’s okay.
        pass

    # 3) Ensure output parent dir exists
    out_parent = out_path.parent
    if out_parent and not out_parent.exists():
        logging.info("Creating output directory: %s", out_parent)
        out_parent.mkdir(parents=True, exist_ok=True)

    # Build the transform pipeline (Step 4)
    pipeline = build_pipeline(args)
    logging.info("Pipeline steps: %s", [fn.__name__ for fn in pipeline])

    # Hand off to the next steps (cleaning not implemented yet)
    raise NotImplementedError("Cleaning pipeline (Steps 4–5) not implemented yet.")

def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="textcleaner",
        description="Clean a UTF-8 text file via selectable steps (trim, collapse spaces, lower, strip-empty).",
        epilog="Constraints: stdlib only (argparse, pathlib, logging).",
    )
    parser.add_argument(
        "--input", required=True, type=Path,
        help="Path to input .txt file (UTF-8)."
    )
    parser.add_argument(
        "--output", required=True, type=Path,
        help="Path to save cleaned .txt file (overwrites if exists)."
    )
    parser.add_argument(
        "--lower", action="store_true",
        help="Lowercase all text."
    )
    parser.add_argument(
        "--strip-empty", dest="strip_empty", action="store_true",
        help="Drop empty/whitespace-only lines."
    )
    parser.add_argument(
        "--collapse-spaces", dest="collapse_spaces", action="store_true",
        help="Replace multiple spaces with a single space (line-wise)."
    )
    parser.add_argument(
        "--trim", action="store_true",
        help="Strip leading/trailing whitespace per line."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Set logging level to INFO (default WARNING)."
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s 0.1.0"
    )
    return parser

# --- Cleaning step functions ---

def step_trim(line: str) -> str:
    """Strip leading/trailing whitespace."""
    return line.strip()

# IMPORTANT: collapse only SPACE characters, not tabs.
SPACE_RUN = re.compile(r" {2,}")

def step_collapse_spaces(line: str) -> str:
    """Replace runs of 2+ spaces with a single space (line-wise)."""
    return SPACE_RUN.sub(" ", line)

def step_lower(line: str) -> str:
    """Lowercase the line."""
    return line.lower()

def should_keep_line(line: str, strip_empty: bool) -> bool:
    """
    Return True if the line should be kept.
    If strip_empty is True, drop empty/whitespace-only lines.
    """
    if not strip_empty:
        return True
    return line.strip() != ""

def build_pipeline(args: argparse.Namespace):
    """
    Build the ordered list of transform functions based on flags.
    Order per README: trim -> collapse-spaces -> lower
    (strip-empty is a filter, applied after transforms)
    """
    pipeline = []
    if args.trim:
        pipeline.append(step_trim)
    if args.collapse_spaces:
        pipeline.append(step_collapse_spaces)
    if args.lower:
        pipeline.append(step_lower)
    return pipeline

def apply_pipeline(line: str, pipeline) -> str:
    """Apply each transform in order to a single line."""
    for fn in pipeline:
        line = fn(line)
    return line

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    # If -h/--help is passed, argparse exits before this point.
    configure_logging(args.verbose)
    run(args)

if __name__ == "__main__":
    main()
    