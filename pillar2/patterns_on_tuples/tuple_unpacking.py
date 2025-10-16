"""
Challenge: Swap Variables via Tuple Unpacking

You are given two variables, `a` and `b`, whose values are unknown but different.  
You must **swap their values** without using any temporary variable or external storage.

For example:
    a = 42
    b = 99

After your operation:
    a == 99
    b == 42

⚡️ Be quick and precise: show the minimal, Pythonic one-liner solution possible.  
Then, explain *why* Python allows this syntax (what happens internally).
"""

def swap_varibles(a: any, b: any) -> tuple:
    a, b = b, a
    return a, b

print(swap_varibles(42, 99))