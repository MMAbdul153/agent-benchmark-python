# Benchmark Tasks (Python)

## Task 1: Fix discount rounding and validation

- File: `src/calculator.py`, function `apply_discount`.
- Problem:
  - Currently allows discounts > 100% and negative prices.
  - Specification:
    - If `price < 0` -> raise `ValueError`.
    - If `discount_percent < 0` or `discount_percent > 100` -> raise `ValueError`.
    - Otherwise, apply discount and round to 2 decimal places.
- Tests: `tests/test_calculator.py::TestDiscount`.

## Task 2: Correct average behavior for empty lists

- File: `src/calculator.py`, function `average`.
- Problem:
  - Currently returns `0.0` for empty list.
  - Specification:
    - For empty list, raise `ValueError("numbers list cannot be empty")`.
- Tests: `tests/test_calculator.py::TestAverage`.

## Task 3: Add unit tests for `add`

- File: `src/calculator.py`, function `add`.
- Problem:
  - No tests; agent/LLM must create a robust test suite.
  - Specification:
    - Test integers, floats, negative numbers, and large values.
- Tests: `tests/test_calculator.py::TestAdd`.