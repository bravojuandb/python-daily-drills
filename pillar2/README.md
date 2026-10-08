# Pillar 2 — Data Structures & Problem Solving

Develop algorithmic reasoning through small exercises: understand a contract,
choose an approach, maintain state, verify behavior, and explain correctness
and cost. Pillar 1 supplies the Python syntax; Pillar 2 focuses on the decisions
made with those tools.

## Available now

The new curriculum starts with **Fundamentals & Complexity**, whose first
pattern is [Linear Processing](a_fundamentals_and_complexity/a_linear_processing/README.md).
It contains:

| Order | Drill | Main idea |
| --- | --- | --- |
| 01 | [Count matches](a_fundamentals_and_complexity/a_linear_processing/drill_01_count_matches.py) | Traverse and count matching values |
| 02 | [Running total](a_fundamentals_and_complexity/a_linear_processing/drill_02_running_total.py) | Accumulate one final total |
| 03 | [Find maximum](a_fundamentals_and_complexity/a_linear_processing/drill_03_find_maximum.py) | Maintain the greatest value seen |
| 04 | [First minimum's position](a_fundamentals_and_complexity/a_linear_processing/drill_04_find_minimum.py) | Track a candidate's index and preserve the first occurrence on ties |
| 05 | [Second largest](a_fundamentals_and_complexity/a_linear_processing/drill_05_second_largest.py) | Maintain two distinct candidates |
| 06 | [Longest streak](a_fundamentals_and_complexity/a_linear_processing/drill_06_longest_streak.py) | Track a current run and the longest seen |

Each file contains its prompt, typed function signature, examples, constraints,
edge cases, and reasoning questions. Function bodies raise `NotImplementedError`
until replaced with an attempt.

## Curriculum structure

Use three layers: **algorithmic family → pattern → progressive drills**.
For example:

```text
pillar2/
└── a_fundamentals_and_complexity/
    └── a_linear_processing/
        ├── README.md
        ├── drill_01_count_matches.py
        ├── drill_02_running_total.py
        ├── drill_03_find_maximum.py
        ├── drill_04_find_minimum.py
        ├── drill_05_second_largest.py
        └── drill_06_longest_streak.py
```

The agreed progression is below.

| Order | Family | Main focus |
| --- | --- | --- |
| A | Fundamentals & Complexity | Traversal, state, data-structure costs, and Big O |
| B | Searching & Sorting | Searching, ordering, and ranking |
| C | Hashing & Lookup | Sets, lookup tables, and frequencies |
| D | Sequence Patterns | Two pointers, sliding windows, and prefix sums |
| E | Stacks & Queues | LIFO and FIFO processing |
| F | Recursion | Smaller subproblems and termination |
| G | Divide & Conquer | Partitioning, merge sort, quicksort, and selection |
| H | Dynamic Programming | Repeated subproblems, memoization, and tabulation |
| I | Node-Based Structures | Linked lists, trees, and heaps |
| J | Graphs | Representation, traversal, and unweighted shortest paths |

## Working on a drill

1. Read its contract and constraints, then propose an approach.
2. Predict a small example before running your implementation.
3. Verify normal and boundary cases, including mutation when relevant.
4. Explain what the state represents as traversal progresses and why the
   result is correct. Define the input-size variables when analyzing time
   and auxiliary space.
