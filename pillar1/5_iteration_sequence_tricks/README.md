# 5. Iteration & Sequence Tricks

This chapter is where ordinary loops start turning into sharper sequence-handling habits.

Its job is to make you comfortable moving through data in different directions, stepping through it at different speeds, and reshaping it without losing track of order.
If this section is solid, then nested data, windowing patterns, and loop-based problem solving become much easier to handle.

## What This Chapter Should Prove

After finishing `5_iteration_sequence_tricks`, you should be able to:

- iterate forward and backward with intention
- use slicing to sample or skip values cleanly
- flatten nested data without confusion
- use nested loops when the shape of the problem genuinely requires them
- combine indexes and values without manual bookkeeping
- preserve order while transforming or regrouping a sequence

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the prompt states the expected output shape
- the solution uses the target iteration or sequence trick directly
- the drill includes one small twist around order, shape, or boundaries
- the file stays short enough to solve in one sitting

## Drill Summary

- `01_forward_backward_iter.py`
  Iterate through the same sequence in two directions and combine the results.

- `02_step_sized_slicing.py`
  Use slicing with different step sizes and stop points.

- `03_nested_loop_grid.py`
  Build a patterned grid character by character with nested loops.

- `04_flatten_nested_list.py`
  Flatten nested lists while preserving the original left-to-right order.

- `05_enumerate_with_index.py`
  Combine positions and values into labeled outputs.

- `06_chunked_sequence.py`
  Split a flat sequence into fixed-size chunks without losing leftover values.

- `07_pairwise_differences.py`
  Compare neighboring values in order and return the gaps between them.

- `08_windowed_groups.py`
  Build overlapping windows from a sequence and handle short inputs safely.
