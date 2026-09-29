# T02: Correct Empty-List Average Behavior

Correct the `average` function in `src/calculator.py`.

Requirements:

- A nonempty list must return its arithmetic average.
- A single-element list must return that element.
- An empty list must raise `ValueError`.
- Do not modify `apply_discount` or `add`.
- Do not change unrelated behavior.
- All existing tests must pass.

Expected baseline result:
- Exactly one test fails:
  test_empty_list_raises
- All discount and add tests must pass.
