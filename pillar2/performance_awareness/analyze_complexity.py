"""
Drill — Analyze Algorithmic Complexity (O(n) vs O(log n))

Be quick and precise: For EACH snippet, answer ONLY "O(n)" or "O(log n)" and add a 1-sentence justification.

1) 
def f(arr):
    i = 1
    while i < len(arr):
        i *= 2
    return True

2)
def g(n):
    for i in range(n):
        pass
    return True

3)
def h(n):
    i = n
    steps = 0
    while i > 0:
        i //= 2
        steps += 1
    return steps

4)
def k(arr):
    s = 0
    for x in arr:
        s += x
    return s

5)
def m(sorted_arr, target):
    lo, hi = 0, len(sorted_arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] == target:
            return True
        elif sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

6)
def p(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] > 0: j -= 1
        elif arr[i] + arr[j] < 0: i += 1
        else: return True
    return False

7)
def q(n):
    i = 1
    while i <= n:
        # inner loop runs a constant number of ops
        i *= 2
    return True

8)
def r(n):
    # visiting every 3rd item once across the array
    for i in range(0, n, 3):
        pass
    return True

9)
def s(arr):
    # prefix sums built in one pass
    pref = [0] * (len(arr) + 1)
    for i, x in enumerate(arr, 1):
        pref[i] = pref[i-1] + x
    return pref

10)
def t(n):
    # halve, then do a tiny constant loop each time
    while n > 1:
        for _ in range(5):
            pass
        n //= 2
    return True

Your turn — reply with:
1) O(?) – short reason
2) O(?) – short reason
...
10) O(?) – short reason
"""