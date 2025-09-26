"""
You are asked to design a function `greet_person` that builds a greeting string.

Rules:
- The function takes three parameters: `name`, `age`, and `city`.
- Each parameter should have NO default value (all required).
- The function should return a string formatted as:
  "Hello, my name is {name}, I am {age} years old, and I live in {city}."

BUT: the test code will ONLY call your function using **keyword arguments** (not positional ones).

Example:
greet_person(name="Anna", city="Madrid", age=29)
→ "Hello, my name is Anna, I am 29 years old, and I live in Madrid."

⚡ Solve this quickly — under 2 minutes — and remember: only keyword arguments will be passed!
"""

def greet_person(*, name, age, city) -> str:
    return f"Hello, my name is {name}, I am {age} years old, and I live in {city}."

print(greet_person(name="Anna", city="Madrid", age=29))
print(greet_person(name="Augustinus", city="Hippo", age=54))
