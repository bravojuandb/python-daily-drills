# 4. Pythonic Thinking

This chapter is where you start solving small problems with cleaner, more expressive tools.

Its job is to help you recognize when Python gives you a compact, readable construct that fits the problem better than a manual step-by-step approach.
If this section is solid, then data cleanup, concise helpers, and higher-level problem solving become much easier.

## What This Chapter Should Prove

After finishing `4_pythonic_thinking`, you should be able to:

- choose between comprehensions, generators, and built-ins with intention
- recognize when a one-pass transformation can be written clearly in one expression
- use `map()`, `filter()`, and `zip()` without losing readability
- combine light filtering with light transformation in the same construct
- use `any()`, `all()`, `sum()`, `min()`, and `max()` for direct questions
- work with small realistic data shapes like tags, filenames, and aligned records
- keep concise code understandable instead of merely short

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear expression or short function is the main solution
- the prompt states the expected output shape
- the solution uses the target Pythonic tool directly
- the drill includes one small condition, filter, or design decision
- the file stays short enough to solve in one sitting

## Drill Summary

- `01_list_compreh_transformation.py`
  Clean up messy user-entered tags with one list comprehension.

- `02_dict_compreh_builder.py`
  Build a stock lookup from aligned inputs with validation and normalization.

- `03_set_compreh_builder.py`
  Extract unique normalized file extensions in one set comprehension.

- `04_generator_expression.py`
  Stream large filenames lazily and reason about partial consumption.

- `05_any_all_checker.py`
  Ask two direct questions about quiz scores using generator expressions.

- `06_aggregator.py`
  Summarize daily sales with built-ins while handling empty input safely.

- `07_map_function_mapper.py`
  Use `map()` for two related username transformations that feel like real cleanup.

- `08_filter_odd_even.py`
  Split active and inactive usernames with `filter()` while preserving order.

- `09_zip_combiner.py`
  Combine usernames and scores into a report-ready mapping with mismatch protection.

- `10_comprehension_summary.py`
  Build a compact tag frequency summary by mixing selection and transformation.

- `11_generator_pipeline.py`
  Chain a small lazy pipeline over log messages and finish with one final built-in.
