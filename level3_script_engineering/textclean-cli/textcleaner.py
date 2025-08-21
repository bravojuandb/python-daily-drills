"""
textcleaner.py — A small CLI to clean text files for data pipelines.

Usage examples:
  python textcleaner.py --input input.txt --output cleaned.txt --lower
  python textcleaner.py --input input.txt --output cleaned.txt --trim --collapse-spaces --lower --strip-empty
"""

from pathlib import Path
import argparse
import sys

def configure_logging(verbose: bool) -> None:
    """Stub: will set logging level/format in the next step."""
    pass

def run(args: argparse.Namespace) -> None:
    """Stub: will perform validation, cleaning, and I/O in later steps."""
    raise NotImplementedError("Implementation arrives in Steps 3–5.")

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

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    # If -h/--help is passed, argparse exits before this point.
    configure_logging(args.verbose)
    run(args)

if __name__ == "__main__":
    main()