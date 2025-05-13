"""
Short drill on reading a CSV file using Pandas. 

This is Version 2 of a basic script that demonstrates:
- How to read a CSV file using Pandas
- How to use `pathlib` to manage file paths
- How to make the script runnable from any directory using `__file__`
- Wrap the script into a try except block, and add sys basic error handling and graceful exit.

This script is part of my supplier data pipeline project

COMMON ERRORS ENCOUNTERED:

    UnicodeDecodeError  fails to read the file. Satandard decoding utf-8
    pandas.errors.ParserError  fails because of the delimiter. standard: ","

"""
from pathlib import Path
import pandas as pd
import sys

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "sample.csv"
OUTPUT_DIR = BASE_DIR / "output.csv"

print(">>> Script started")

try:
    df = pd.read_csv(DATA_DIR, encoding= "latin1", delimiter=";")
    print(">>> DataFrame loaded")
    print(f"\n This is a sample of the data frame:\n {df}")
    print(f"\nThese are the column names of the data frame:\n {df.columns}")
    print("\nColumn types and non-null counts:")
    print(df.info())

except FileNotFoundError:
    sys.stderr.write(f"Error: The file '{DATA_DIR} was not found.\n")
    sys.exit(1)
except pd.errors.ParserError as error:
    sys.stderr.write(f"Error: Pandas could not parse the file: {error}\n")
    sys.exit(1)
except Exception as error:
    sys.stderr.write(f"An unexpected error occurred: {error}\n")
    sys.exit(1)