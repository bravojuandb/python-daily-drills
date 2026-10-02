# Linear Processing

Practice one traversal of a list while maintaining a small amount of state.
Start with Pillar 1's loops, conditions, functions, and integer lists. Each
drill adds or transfers one idea; no sorting or hashing is needed here.

## Drill order

| Drill | Main idea | Difference from the previous drill |
| --- | --- | --- |
| [01 - Count matches](drill_01_count_matches.py) | Conditional counting | Bridge from Python syntax to traversal and state |
| [02 - Running total](drill_02_running_total.py) | Accumulation | Each value contributes its amount, rather than one per match |
| [03 - Find maximum](drill_03_find_maximum.py) | Best-so-far candidate | Update only when a value improves the candidate |
| [04 - First minimum's position](drill_04_find_minimum.py) | Candidate position and ties | Return the first minimum's index instead of a value |
| [05 - Second largest](drill_05_second_largest.py) | Two distinct candidates | Maintain their relationship when one changes |
| [06 - Longest streak](drill_06_longest_streak.py) | State reset at a boundary | Track a current run and its best length; input order matters |

`running_total` returns one final integer, not prefix sums. Maximum returns a
value; minimum returns the zero-based index of its first occurrence. Both
return `None` for an empty list. Second largest means the second **distinct**
value and returns `None` when fewer than two distinct values exist. Longest
streak counts adjacent matches for a supplied target.

## Shared rules

These rules apply to all six drills:

- Inputs match the type hints: integer lists and, where present, an integer
  target. Negative values, zero, duplicates, and any input order are valid.
  Booleans and other types are excluded; no type validation is required.
- Return the result without changing the input or printing.
- Use one explicit `for` loop and scalar state to practice traversal and
  updates. `len()`, indexing, comparisons, and arithmetic are allowed.
  Drill 04 also permits `range()` and `enumerate()` to traverse with indices.
- Do not use sorting, slicing, extra collections, recursion, comprehensions,
  or helpers that perform the traversal for you. This includes `sum()`,
  `min()`, `max()`, `list.count()`, `Counter`, `reduce()`, `filter()`, and
  `groupby()`. Implement each drill directly rather than calling another drill.

## Working on a drill

Read its contract, propose an approach, and predict a small example before
running your implementation. Check empty and one-element inputs, duplicates,
negative values, and the drill's specific edge cases. Confirm the input is unchanged.
Explain what your state represents after each processed prefix and justify
the time and auxiliary-space costs, with `n` defined as the input length.
A property that remains true as the loop advances is called a loop invariant.

The files are unsolved templates. Their function bodies raise
`NotImplementedError` until you replace them with your attempt. Creating the
prompts does not establish correctness or understanding. Add focused tests
when working on the selected drill; there is no exercise completion deadline.

All six target O(n) time and O(1) auxiliary space under the usual constant-cost
model for integer operations. Exclude the existing input list from auxiliary
space. This simplification does not model the bit-level cost of arbitrarily
large Python integers.
