# Tests

This folder contains behavior tests for the drills being worked on. They cover
expected results, edge cases, and errors defined by each prompt. Ordering and
changes to the input are covered when the prompt specifies those rules.

The tests use `assert` for returned values and `pytest.raises` for exceptions.
Pillar 2 tests are grouped by chapter. Unsolved drills and archived exercises
are outside the current test suite.

Algorithm choice and time and space complexity are checked through code review
and reasoning. A correct result alone does not prove that a solution follows
the required technique, and timing measurements do not prove Big-O complexity.

Passing tests provide evidence for the cases they cover, not every possible
input or every drill in the repository.
