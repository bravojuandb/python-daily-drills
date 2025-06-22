"""
Short drill on reading a CSV file using Pandas. 

This is Version 3 of a basic script that demonstrates:
- How to read a CSV file using Pandas
- How to use `pathlib` to manage file paths
- How to make the script runnable from any directory using `__file__`
- Wrap the script into a try except block, and add sys basic error handling and graceful exit.
- Convert it into a function called: load_csv

This script is part of my supplier data pipeline project


"""
from pathlib import Path
import pandas as pd
import sys


print(">>> Script started")

def load_csv (file_path) -> pd.DataFrame:

    try:
        df = pd.read_csv(file_path, encoding= "latin1", delimiter=";")
        print(">>> DataFrame loaded")
        print(f"\n This is a sample of the data frame:\n {df}")
        print(f"\nThese are the column names of the data frame:\n {df.columns}")
        print("\nColumn types and non-null counts:")
        print(df.info())

    except FileNotFoundError:
        sys.stderr.write(f"Error: The file '{file_path} was not found.\n")
        sys.exit(1)
    except pd.errors.ParserError as error:
        sys.stderr.write(f"Error: Pandas could not parse the file: {error}\n")
        sys.exit(1)
    except Exception as error:
        sys.stderr.write(f"An unexpected error occurred: {error}\n")
        sys.exit(1)

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "sample.csv"
    OUTPUT_DIR = BASE_DIR / "output.csv"
    load_csv(DATA_DIR)