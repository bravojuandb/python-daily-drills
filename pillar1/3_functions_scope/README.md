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
- explain why assigning to a name can create `UnboundLocalError`
- use `global` and `nonlocal` intentionally in small examples
- trace Local, Enclosing, Global, and Built-in name lookup

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

- `05_reading_vs_writing_globals.py`
  Contrast reading a global name with assigning a local name.

- `06_unbound_local_error.py`
  Fix a tiny `UnboundLocalError` case using `global` intentionally.

- `07_avoid_global_state.py`
  Replace hidden global state with explicit input and output.

- `08_enclosing_scope.py`
  Return an inner function that reads from an enclosing scope.

- `09_nonlocal_counter.py`
  Use `nonlocal` to build independent closure-based counters.

- `10_legb_name_lookup.py`
  Trace a small LEGB lookup example using local, enclosing, parameter, and built-in names.
