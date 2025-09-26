"""
You are asked to build a function that squares numbers using a lambda.

Rules:
1. Define a lambda expression `square` that takes a single argument `x`
   and returns `x` squared.
2. Test it by mapping `square` over the list [1, 2, 3, 4, 5].
3. Convert the result into a list.

Expected output:
[1, 4, 9, 16, 25]

⚡ Solve this quickly — it’s a one-liner lambda, no need for `def`!
"""

square = lambda x: x * x 

print(list(map(square, [1, 2, 3, 4, 5])))



square = lambda x: x * x if x % 2 == 0 else x

print(list(map(square, [1, 2, 3, 4, 5])))