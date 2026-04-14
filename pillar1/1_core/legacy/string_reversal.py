"""
String Reversal

You're given a string s. write a function that returns:
1. The reversed string.
2. True if the reversed string is exactrly the same as the original.
3. The middle character(s) of the reversed string (1 char if odd length, 2 chars if even length).

python
>>> analyze("radar")
("radar", True, "d")

>>> analyze("python")
("nohtyp", False, "ht")

"""

def string_reversal(s:str) -> tuple:
    reversed_s = s[::-1]
    
    mid = len(s) // 2
    if len(s) % 2 == 0:
        middle_chars = reversed_s[mid-1:mid+1]  # 2 chars if even
    else:
        middle_chars = reversed_s[mid]
    return reversed_s, s == s[::-1], middle_chars

print(string_reversal("radar"))