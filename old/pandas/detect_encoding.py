"""
pip install chardet

"""

import chardet

with open("sample.csv", "rb") as f:
    result = chardet.detect(f.read())

print(result)

