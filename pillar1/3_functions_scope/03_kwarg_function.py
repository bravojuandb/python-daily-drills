"""
Drill 03 - Keyword Argument Function

Write a function:
    greet_person(*, name: str, age: int, city: str) -> str

Requirements:
1. All three arguments must be keyword-only.
2. Return a sentence in this form:
   `"Hello, my name is {name}, I am {age} years old, and I live in {city}."`
3. If `city` is an empty string, use `"Unknown"` in the returned message instead.

Example:
>>> greet_person(name="Anna", age=29, city="Madrid")
'Hello, my name is Anna, I am 29 years old, and I live in Madrid.'
>>> greet_person(name="Anna", age=29, city="")
'Hello, my name is Anna, I am 29 years old, and I live in Unknown.'

Thinking goal:
This drill is about separating how a function is called from how it cleans and uses its inputs.
"""

def greet_person(*, name: str, age: int, city: str) -> str:
    city = city or "Unknown"

    return f"Hello, my name is {name}, I am {age} years old, and I live in {city}."

print(greet_person(name="Anna", age=29, city=""))


