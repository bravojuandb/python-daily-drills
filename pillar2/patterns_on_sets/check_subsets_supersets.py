"""
Challenge: Check Subsets and Supersets

You are given two sets of city codes representing train networks.  
Your task is to determine their **subset** and **superset** relationships.

Example:
    network_A = {"MAD", "BCN", "ROM", "PAR"}
    network_B = {"MAD", "BCN"}

Expected:
    network_B is a subset of network_A  
    network_A is a superset of network_B

Rules:
- Use `.issubset()` and `.issuperset()` methods (or `<=` and `>=` operators).
- Print results in readable form, e.g.:
      "B is subset of A: True"
      "A is superset of B: True"
- Add a test case where the relationship is False.

⚡️ Be quick and precise:
1. Create two sets with overlap.
2. Check subset/superset relationships in both directions.
3. Explain in one sentence what makes a set a *strict* subset vs a *subset*.
"""

def check_subset_superset(a: set, b: set) -> None:
    if a.issuperset(b):
        print(f"{a} is a superset of {b}")
    else:
        print(f"{a} is NOT a superset of {b}")

    if a.issubset(b):
        print(f"{a} is a subset of {b}")
    else:
        print(f"{a} is NOT a subset of {b}")


network_A = {"MAD", "BCN", "ROM", "PAR"}
network_B = {"MAD", "BCN"}

print(check_subset_superset(network_A, network_B))

# 3. 
# A set is a strict subset of another 
# if all its elements are contained in the other set 
# and the sets are not equal.