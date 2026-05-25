"""
Drill 02 - Default Argument

Write a function:
    chant(phrase: str = "carpe diem", times: int = 3) -> str

Requirements:
1. Return the phrase repeated `times` times, joined by `" | "`.
2. The returned phrase should be uppercased.
3. If `times` is `0`, return an empty string.
4. Use the default argument values unless new ones are provided.

Example:
>>> chant()
'CARPE DIEM | CARPE DIEM | CARPE DIEM'
>>> chant("veni vidi vici", 1)
'VENI VIDI VICI'

Thinking goal:
This drill is about choosing sensible defaults while still handling a small edge case intentionally.
"""

def chant(phrase: str = "carpe diem", times: int = 3) -> str:

    if times == 0:
        return ""
    
    result = []
    for _ in range(times):
        result.append(phrase.upper())

    return " | ".join(result)



if __name__ == "__main__":
    print(chant())