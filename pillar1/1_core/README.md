# 1. Core Data Types & Operations

This chapter is the foundation of Pillar 1.

Its job is not to be impressive on its own. Its job is to make later chapters feel natural.
If this section is solid, then control flow, functions, comprehensions, logic puzzles, and file work become much easier.

## What This Chapter Should Prove

After finishing `1_core`, you should be able to:

- read and write small expressions without hesitation
- extract values from strings, lists, tuples, sets, and dicts
- choose the right built-in data type for a tiny task
- transform simple inputs into predictable outputs
- understand which operations mutate data and which return new objects
- return results cleanly from functions before moving into control flow and abstraction

## Drill Standards For A Strong Second Pass

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the drill returns a value instead of relying on `print()`
- the prompt states the expected output shape
- the solution uses the target concept directly
- the drill includes one light constraint, edge case, or mini-real-world framing
- the file may include a demo block, but only under `if __name__ == "__main__":`

## Drills
- `01_interger_arithmetic.py`
  Practice the main arithmetic operators on two numbers and return the results in a clear order.

- `02_float_precision.py`
  Explore float behavior, rounding surprises, and the difference between `round()`, `floor()`, and `ceil()`.

- `03_modulo_madness.py`
  Build intuition for the modulo operator, especially with negative numbers.

- `04_string_slicing.py`
  Extract different parts of a string using start, stop, and step slicing.

- `05_string_reversal.py`
  Reverse a string, check whether it is symmetric, and inspect its middle character or characters.

- `06_f_string_formatting.py`
  Format a small text report with capitalization, zero-padding, and decimal precision.

- `07_word_split_join.py`
  Split a sentence into words, normalize the text, and join it back with a new separator.

- `08_replace_characters.py`
  Replace selected characters in a string while preserving the rest of the content.

- `09_list_indexing.py`
  Retrieve elements from specific positions using positive and negative indexes.

- `10_append_pop.py`
  Simulate list updates by appending items, removing items, and checking the final state.

- `11_list_sorting.py`
  Compare in-place sorting with creating a new sorted list in ascending and descending order.

- `12_list_slicing.py`
  Use slicing to select subsets of a list, reverse it, and skip elements with step values.

- `13_tuple_pack_unpack.py`
  Pack related values into a tuple and unpack them into readable variable names.

- `14_union_intersect_diff.py`
  Use set operations to compute combined, shared, and exclusive values between two groups.

- `15_dict_lookup_update.py`
  Read dictionary values safely, use default values, and update stored quantities.

- `16_dict_comprehension.py`
  Build a dictionary from paired inputs using a dictionary comprehension.
