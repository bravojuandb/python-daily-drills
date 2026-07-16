# 5. Complexity & Tradeoffs

This chapter makes performance reasoning part of solution design rather than an
afterthought.

## What This Chapter Should Prove

- derive time and auxiliary-space complexity from code
- identify when a set or dictionary changes the complexity class
- compare nested scans with prebuilt indexes
- reason about copying, mutation, and memory
- select sorting or a heap based on input shape
- design repeatable benchmarks without timing setup work

## Drill Order

1. Classify growth rates
2. Count operations
3. List versus set membership
4. Nested-loop join versus indexed join
5. Copy versus mutation
6. Shallow versus recursive memory
7. Full sort versus heap selection
8. Reliable microbenchmark
