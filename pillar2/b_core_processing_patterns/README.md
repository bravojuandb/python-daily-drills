# 2. Core Processing Patterns

This chapter builds the small transformations that appear inside nearly every
data-processing problem.

## What This Chapter Should Prove

- distinguish filtering, mapping, and reduction
- count and group in one pass
- build lookup indexes
- deduplicate with an explicit conflict policy
- join records without nested loops
- compose patterns without mixing unrelated responsibilities

## Drill Order

1. Filter active records
2. Normalize records
3. Reduce transaction totals
4. Count frequencies
5. Group records
6. Build an index
7. Deduplicate with last-write-wins
8. Join records by key
