# Pillar 2 — Data Structures & Problem Solving (Bridging Logic and Data)

## 1. Foundational Algorithms
- ✅ Sorting Numbers → `sorted()`, custom `key`
- ✅ Sorting Dicts by Value → `sorted(dict.items(), key=...)`
- ✅ Binary Search Implementation → `while low <= high`
- ✅ Counting Frequencies → `collections.Counter`
- ✅ Aggregating Totals → `sum()`, grouping by key
- ✅ BONUS: Group Transactions by customer
- ✅ Manual Min/Max Finder → loops
- ✅ Detecting Duplicates → sets
- ✅ Intersection of Lists → `set(list1) & set(list2)`
- ✅ Flatten Nested List → `[x for sub in L for x in sub]`
- ✅ Big-O Estimation (mental drills)

---

## 2. Data Structure Patterns
### Lists
- ✅ Append/Extend & In-Place Sort  
- ✅ Merge Two Lists Alternately  
- ✅ Rotate List Elements (left/right)
- ✅ Slice Copy vs Reference Test

### Tuples
- ✅ Swap Variables via Tuple Unpacking  
- ✅ Store Immutable Records  
- ✅ Tuple as Dict Keys (coordinates, pairs)

### Sets
- ✅ Remove Duplicates  
- ✅ Check Subsets/Supersets  
- ✅ Compare Unique Items Across Lists  
- ✅ Set-Based Membership Speed Test  

### Dicts
- ✅ Count Word Occurrences  
- ✅ Group Items by Category  
- ✅ Merge Two Dicts with Conflict Rules  
- ✅ Invert a Dict (value→key)
- ✅ Nested Dict Access (safe `.get()`)

### Stack/Queue Simulations
- ✅ Build Stack with `list` → `.append()` / `.pop()`
- ✅ Build Queue with `collections.deque`
- ✅ Evaluate Expression (LIFO logic)
- ✅ Check Balanced Brackets (stack)

---

## 3. Applied Challenges
*Drills marked with * are to be treated as project_style drills*
- ✅ CSV Row Aggregator (manual parsing) *
- ✅ Word Frequency Counter (text file)
- ✅ Unique Visitors Counter (from log entries)
- ✅ Detect Top-N Items (sorting by counts)
- ✅ Group Transactions by Customer (dict of lists)
- ✅ Simple ETL Transform (clean → aggregate → output) *
- ✅ Recursive Directory Walk (simulate folder scan) *
- ✅ Recursively Flatten Nested Dict *
- ✅ Merge and Deduplicate JSON-like lists *
- ✅ Build Mini Leaderboard (sort + dict)

---

## 4. Performance Awareness
- ✅ Benchmark List vs Set Lookup → `%timeit`
- ✅ Compare Loop vs Comprehension Runtime
- ✅ Memory Use via `sys.getsizeof()`
- ✅ Optimize Nested Loops into Dict Lookup
- ✅ Analyze Algorithmic Complexity (O(n), O(log n))

## 5. Common Patterns

Each pattern concludes with a **15-minute drill** — a concise, practical exercise to reinforce the concept.

- **Iteration & Filtering** → selective traversal  
  *Drill:* read a CSV and filter only rows where "status" == "active".

- **Mapping & Transformation** → same size, new meaning  
  *Drill:* convert a list of strings into dicts with derived fields (e.g. split "name,age" → {"name": ..., "age": ...}).

- **Aggregation** → reduction  
  *Drill:* sum or average numerical values from a JSON list.

- **Grouping** → partition + aggregate  
  *Drill:* group transactions by customer and compute total amount.

- **Searching** → efficient lookup  
  *Drill:* implement linear and binary search on a sorted list of IDs.

- **Recursion** → self-similar decomposition  
  *Drill:* recursively count files in nested folders.

- **Sorting & Ranking** → comparison + order  
  *Drill:* sort products by price and output the top 5.

- **State Tracking** → remember what matters  
  *Drill:* validate a string of parentheses using a stack.

- **Error-Aware Processing** → fail safely  
  *Drill:* safely parse rows from a CSV with missing fields and log errors.