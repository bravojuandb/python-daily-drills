# 6. Logic Puzzles

This chapter is where small Python tools start getting used inside actual reasoning problems.

Its job is to make you trace rules carefully, test edge cases, and choose a sensible approach instead of only recalling syntax.
If this section is solid, then debugging, interview-style questions, and medium-sized exercises become much less intimidating.

## What This Chapter Should Prove

After finishing `6_logic_puzzles`, you should be able to:

- turn a verbal rule set into precise branching logic
- test edge cases before trusting a result
- choose between direct checks, stacks, sets, counters, and loops
- trace state across several steps without losing the invariant
- recognize when a simpler formulation exists inside a puzzle

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the prompt states the expected output shape
- the drill includes at least one edge case or hidden trap
- the solution should require some reasoning, not just syntax recall
- the file stays short enough to solve in one sitting

## Drill Summary

- `01_fizzbuzz_variations.py`
  Apply several overlapping divisibility rules without missing the combined cases.

- `02_palindrome_detector.py`
  Normalize text and check symmetry while ignoring noise.

- `03_duplicate_finder.py`
  Identify repeated values without returning them more than once.

- `04_balanced_parentheses_checker.py`
  Track opening and closing symbols with a stack and protect the invariant.

- `05_prime_number_tester.py`
  Test divisibility carefully and stop once a proof is found.

- `06_nearest_repeat_distance.py`
  Track positions to find the smallest gap between repeated values.

- `07_word_pattern_matcher.py`
  Keep two-way consistency between a pattern and a word sequence.

- `08_interval_merger.py`
  Merge overlapping ranges while preserving sorted order.
