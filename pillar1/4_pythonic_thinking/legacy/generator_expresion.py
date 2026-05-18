"""
Create a generator expression that yields the cubes of all numbers from 1 to 10,
but only if the number is not divisible by 3.

- Assign it to a variable called `gen`.
- Use `next(gen)` twice to print the first two generated values.
- Then loop through the rest of the generator to print the remaining values.

Expected behavior:
gen produces → 1, 8, 64, 125, 343, 512, 1000
"""

gen = (x ** 3 for x in range(1,11) if x % 3 != 0)


print(next(gen))
print(next(gen))
print("This is the start of the loop:")

for val in gen:
    print(val)