"""
Short drill on reading a CSV file using Pandas.

Related to my supplier data pipelina project



COMMON ERRORS:

UnicodeDecodeError  fails to read the file. Satandard decoding utf-8
pandas.errors.ParserError  fails because of the delimiter. standard: ","


"""




print(">>> Script started")

import pandas as pd

df = pd.read_csv("sample.csv", encoding= "latin1", delimiter=";")

print(">>> DataFrame loaded")

