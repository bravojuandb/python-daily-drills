# 7. Error Handling

This chapter is where you start treating failure as part of the program, not an interruption from outside it.

Its job is to help you notice what can go wrong, decide what should be caught versus raised, and keep error behavior explicit instead of accidental.
If this section is solid, then validation, file work, and user-facing code become much safer to build.

## What This Chapter Should Prove

After finishing `7_error_handling`, you should be able to:

- use `try` / `except` for a focused failure case
- decide when to return a fallback versus when to raise
- define and use a custom exception
- attach a clear message to invalid input
- validate input before deeper work begins
- keep exception handling narrow instead of swallowing unrelated problems

## Drill Standards

Each drill in this chapter should ideally meet this bar:

- one clear function is the main solution
- the prompt states the expected output shape
- the solution uses the target error-handling concept directly
- the drill includes at least one concrete invalid-input case
- the file stays short enough to solve in one sitting

## Drill Summary

- `01_basic_try_except.py`
  Catch one specific runtime failure and return a clear fallback.

- `02_raise_custom_exception.py`
  Define a custom exception and raise it when a business rule is broken.

- `03_custom_error_message_formatter.py`
  Validate input and raise different messages for different invalid cases.

- `04_parse_int_or_none.py`
  Convert text to an integer safely and separate bad input from good input.

- `05_safe_lookup.py`
  Handle a missing key intentionally instead of crashing.

- `06_validation_entrypoint.py`
  Combine validation and raising so the happy path stays clean.
