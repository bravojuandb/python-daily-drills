# 3. Functions & Scope

This chapter is where small scripts start becoming reusable building blocks.

Its job is to make you comfortable defining functions, choosing parameters carefully, and understanding which names belong where.
If this section is solid, then recursion, abstraction, and larger program structure become much easier to reason about.

## What This Chapter Should Prove

After finishing `3_functions_scope`, you should be able to:

- write small functions with clear inputs and return values
- recognize what makes a function pure versus stateful
- choose when default arguments improve clarity
- read and call functions with keyword arguments confidently
- understand the difference between local scope and global scope
- use lambda expressions when the job is genuinely tiny
- trace recursive functions through base cases and repeated calls

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the drill returns a value instead of relying on `print()`
- the prompt states the expected output shape
- the solution uses the target function or scope concept directly
- the drill includes one light constraint, edge case, or design choice
- the file stays short enough to solve in one sitting

## Drill Summary

- `01_pure_function.py`
  Normalize text in a deterministic way without mutating external state.

- `02_default_argument.py`
  Use defaults thoughtfully while handling a small formatting edge case.

- `03_kwarg_function.py`
  Build a readable string using required keyword-only arguments.

- `04_global_local_scope.py`
  Contrast intentional global mutation with a local variable that only looks similar.

- `05_lambda_one_liner.py`
  Use a tiny lambda with `map()` for a transformation that includes a condition.

- `06_recursive_factorial.py`
  Practice recursion with a clear base case and one invalid-input rule.

- `07_recursive_fibonacci.py`
  Trace recursive structure with two base cases and a boundary check.

- `08_helper_and_wrapper.py`
  Separate one pure helper from one public function that prepares the input.

- `09_mutating_vs_non_mutating.py`
  Write two similar functions where one mutates state and the other returns a fresh result.

- `10_recursive_entrypoint.py`
  Pair input validation in one function with recursion in another.
