# T01: Correct Discount Validation

Correct the `apply_discount` function in `src/calculator.py`.

Requirements:

- A negative price must raise `ValueError`.
- A discount below 0 must raise `ValueError`.
- A discount above 100 must raise `ValueError`.
- Valid results must be rounded to two decimal places.
- Do not modify `average` or `add`.
- Do not change unrelated behavior.
- All existing tests must pass.

Expected baseline result:
- Exactly three tests fail.
- The failures must be:
  test_negative_price_raises
  test_negative_discount_raises
  test_discount_over_100_raises
- All average and add tests must pass.
