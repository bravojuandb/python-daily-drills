# 2. Control Flow

This chapter is where the core data-type work starts turning into decisions and repetition.

Its job is to make you comfortable with branching, looping, and choosing the right flow for a tiny task.
If this section is solid, then functions, comprehensions, logic puzzles, and file work become much easier to reason about.

## What This Chapter Should Prove

After finishing `2_control_flow`, you should be able to:

- choose between `if`, `elif`, and `else` without hesitation
- trace nested conditions carefully
- use `for` loops to build or inspect results step by step
- pair iteration tools like `range()`, `enumerate()`, and `zip()` with the right problem
- control loop behavior with `break` and `continue`
- write short conditional expressions when they genuinely improve clarity
- recognize and use Python truthiness directly

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the drill returns a value instead of relying on `print()`
- the prompt states the expected output shape
- the solution uses the target control-flow concept directly
- the drill includes one light constraint, edge case, or mini-real-world framing
- the file may include a demo block, but only under `if __name__ == "__main__":`

## Drill Summary

- `01_if_else_classifier.py`
  Classify a temperature into categories with one special edge case.

- `02_nested_if_puzzle.py`
  Use nested `if` statements to classify numbers by sign, parity, and magnitude.

- `03_loop_counting_with_range.py`
  Use `range()` to accumulate only the values that match a condition.

- `04_loop_enumerate.py`
  Label items with 1-based positions while filtering by a rule.

- `05_loop_with_zip.py`
  Combine aligned lists and derive a status string for each pair.

- `06_break_continue_maze.py`
  Ignore broken values, stop at the first usable match, and handle a fallback case.

- `07_ternary_operator.py`
  Use nested ternary logic for a compact three-way label.

- `08_truthy_falsy.py`
  Distinguish missing values from present-but-empty values with truthiness.

- `09_tag_and_filter_scores.py`
  Filter invalid values, classify the rest, and preserve order without a comprehension.

- `10_first_matching_task.py`
  Ignore blocked items, stop at the first real match, and return a fallback when needed.

- `11_loop_summary_report.py`
  Walk through a sequence once and build a category summary from multiple conditions.
