# Pillar 1 — Fluency & Logic Drills

## 1. Core Data Types & Operations
- Integer Arithmetic → `+ - * / // % **`
- Float Precision & Rounding → `round()`, `math.floor`, `math.ceil`
- Modulo Madness → `%`
- String Slicing → `s[start:stop:step]`
- String Reversal → slicing `[::-1]`
- f-String Formatting → `f"{var}"`
- Word Split & Join → `.split()`, `.join()`
- Replace Characters → `.replace()`
- List Indexing → `list[i]`
- List Append & Pop → `.append()`, `.pop()`
- List Sorting (asc/desc) → `.sort()`, `sorted()`
- List Slicing with Steps → `list[start:stop:step]`
- Tuple Packing & Unpacking → `(a, b)`, `a, b = tuple`
- Set Union/Intersection/Difference → `| & -`
- Dictionary Lookup & Update → `dict[key]`, `.get()`, `.update()`
- Dictionary Comprehension → `{k: v for ...}`

---

## 2. Control Flow
- If/Else Classifier → `if / elif / else`
- Nested If Puzzle → nested `if`
- Loop Counting with Range → `for i in range()`
- Loop with Enumerate → `enumerate()`
- Loop with Zip → `zip()`
- Break & Continue Maze → `break`, `continue`
- Ternary Operator → nested ternary logic
- Truthy/Falsy and Missing Values → truthiness plus `None` handling
- Tag and Filter Scores → filtering plus per-item classification
- First Matching Task → `continue`, `break`, fallback return
- Loop Summary Report → one-pass counting with multiple conditions

---

## 3. Functions & Scope
- Pure Function → deterministic transformation
- Default Argument Function → `def f(x=...)`
- Keyword Argument Function → keyword-only parameters
- Global vs Local Scope → `global`, variable shadowing
- Lambda One-Liner → `lambda x: ...`
- Recursive Factorial → recursion plus validation
- Recursive Fibonacci → recursion plus boundary checks
- Helper and Wrapper → pure helper plus public function
- Mutating vs Non-Mutating → state changes versus copied result
- Recursive Entrypoint → validation wrapper plus recursive worker

---

## 4. Pythonic Thinking
- List Comprehension Transformation → `[x for ...]`
- Dict Comprehension Builder → `{k: v for ...}`
- Set Comprehension Builder → `{x for ...}`
- Generator Expression → `(x for ... in ...)`
- Any/All Checker → `any()`, `all()`
- Aggregator → `sum()`, `min()`, `max()`
- Map Function Mapper → `map()`
- Filter Odd/Even → `filter()`
- Zip Combiner → `zip()`
- Comprehension Summary → filtering plus normalization in one expression
- Generator Pipeline → lazy filtering plus `sum()`

---

## 5. Iteration & Sequence Tricks
- Forward & Backward Iteration → `for`, `reversed()`
- Step-Sized Slicing → `seq[start:stop:step]`
- Nested Loop Grid → nested `for`
- Flatten Nested List → comprehension `[x for sub in L for x in sub]`
- Enumerate with Index → `enumerate()`
- Chunked Sequence → slicing in fixed jumps
- Pairwise Differences → neighboring comparisons
- Windowed Groups → overlapping sequence windows

---

## 6. Logic Puzzles
- FizzBuzz Variations → `%`, overlapping rules
- Palindrome Detector → normalization plus slicing `[::-1]`
- Duplicate Finder → `set()`, `collections.Counter`
- Balanced Parentheses Checker → stack (`list`), loop
- Prime Number Tester → loops, `%`
- Nearest Repeat Distance → last-seen index tracking
- Word Pattern Matcher → two-way mapping consistency
- Interval Merger → sorting plus overlap handling

---

## 7. Error Handling
- Basic Try/Except → `try / except`
- Raise Custom Exception → `raise`
- Custom Error Message Formatter → precise `ValueError` messages
- Parse Int or None → conversion fallback
- Safe Lookup → `KeyError` handling
- Validation Entrypoint → validate first, then run normal logic

---

## 8. Input/Output Basics
- User Input Echo → `input()`
- Number Guessing with Input → `input()`, `int()`
- Print Formatting Challenge → `print()`, `f-strings`
- Simple File Reader → `open(..., "r")`, `.readlines()`
- Simple File Writer → `open(..., "w")`, `.write()`
- Append Log Entry → `open(..., "a")`
- Count File Lines → read plus filtering
- Copy Nonempty Lines → read, filter, write
