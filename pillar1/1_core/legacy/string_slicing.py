def string_slicing_drill():
    s = "DataEngineer"

    slice1 = s[0:4]
    slice2 = s[4:]
    slice3 = s[:4]
    slice4 = s[-3:]
    slice5 = s[:-3]
    slice6 = s[::2] # every 2nd char
    slice7 = s[::-1] # reversed string
    slice8 = s[1:8:2]

    return slice1, slice2, slice3, slice4, slice5, slice6, slice7, slice8


print(string_slicing_drill())