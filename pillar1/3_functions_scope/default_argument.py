"""
Default Argument Drill ⚡

Write a function `chant(phrase="CARPE DIEM", times=3)`  
that returns the phrase repeated `times` times, joined by spaces.

Examples:
chant()                     → "CARPE DIEM CARPE DIEM CARPE DIEM"
chant("AMOR VINCIT OMNIA")  → "AMOR VINCIT OMNIA AMOR VINCIT OMNIA AMOR VINCIT OMNIA"
chant("VENI VIDI VICI", 1)  → "VENI VIDI VICI"
"""

def chant(phrase="CARPE DIEM", times=3):
    return " ".join([phrase] * times)

def chant(phrase="CARPE DIEM", times=3):
    result = ""
    for i in range(times):
        result += phrase + " "
    return result.strip()


print(chant())