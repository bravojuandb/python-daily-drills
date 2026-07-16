# Pillar 2 — Data Structures & Problem Solving

Pillar 2 moves from knowing Python syntax to choosing representations, recognizing
reusable patterns, and explaining why a solution is correct and efficient.

## How to Work Through This Pillar

Complete the chapters and drills in numeric order. Each drill contains a prompt,
function signature, requirements, examples, and a thinking goal. Replace `pass`
with your solution, then add a few examples under a main guard if useful.

For every solution, ask:

- What information must be stored?
- Does order, uniqueness, or mutability matter?
- Which operation happens most often?
- What invariant remains true while the algorithm runs?
- What are the time and auxiliary-space costs?

## Complexity Checks

Every drill ends with a short complexity check. Its purpose is practical:

- **Interview training:** practise explaining why your solution works and scales.
- **Data-manipulation skill:** recognize when lists, sets, dictionaries, sorting,
  or extra indexes will become expensive as the data grows.

After each solution, state its worst-case time and extra-space Big-O. Then give
one sentence naming the main cost and why your chosen structure or pattern fits.

Example: “`O(n)` time because every record is visited once; `O(k)` extra space
because the dictionary stores one entry per distinct customer.”

## How to Test Each Drill

Write the tests after reading the prompt but before considering the drill
complete. Use `pytest` and follow this short cycle:

1. Test the main example or normal case.
2. Add an empty-input or boundary case when the prompt allows one.
3. Test ordering, duplicates, ties, exceptions, and mutation rules when relevant.
4. Run the individual test while solving, then run the chapter tests when done.
5. Add a regression test whenever you discover a bug or overlooked edge case.

Start with plain `assert` statements. Introduce parametrized tests, fixtures, and
shared helpers only when repetition makes them useful. Test observable behavior,
not implementation details. Keep Big-O analysis in the drill's complexity check;
runtime-based complexity tests are usually unreliable.

Aim for at least one correctness test per drill, several edge-case tests for
algorithmic drills, and broader malformed-data tests for applied challenges.

## Chapters

1. **Data Structure Selection** — choose lists, tuples, sets, dictionaries,
   stacks, and queues deliberately.
2. **Core Processing Patterns** — filter, map, reduce, count, group, index,
   deduplicate, and join records.
3. **Searching, Ordering & Ranking** — search efficiently, sort with explicit
   tie rules, and select top results.
4. **Sequence & Traversal Patterns** — use two pointers, windows, prefix sums,
   stacks, queues, DFS, BFS, and visited sets.
5. **Complexity & Tradeoffs** — analyze runtime and memory, compare alternative
   designs, and benchmark responsibly.
6. **Applied Challenges** — combine several patterns in realistic pipelines.

## Drill Standard

Every drill should eventually have:

- one focused public function or small class
- type hints and a clear return contract
- deterministic behavior, including ties and edge cases
- no work performed merely by importing the module
- examples protected by `if __name__ == "__main__":`
- a stated time and space complexity when algorithms are central

## Legacy Material

The original Pillar 2 material is preserved unchanged in `legacy/`, grouped by
its former chapter names. It is reference material and is not part of the new
recommended drill order.
