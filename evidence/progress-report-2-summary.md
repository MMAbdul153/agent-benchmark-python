# Progress Report 2 Pilot Summary

## Scope

This is a preliminary two-attempt pilot study using task **T01 only**. One agentic
attempt and one non-agentic attempt were conducted against the same task.

The T02 and T03 task templates were created and verified as part of this work, but
their experiments have **not** been run. They remain future work and no T02 or T03
result is reported here.

## Work Completed

- Three isolated task templates were prepared under `task_templates/`:
  `T01_discount`, `T02_average`, and `T03_add_tests`. Each contains only
  `src/calculator.py`, `tests/test_calculator.py`, and `TASK.md`.
- Each template was tested from inside its own folder, so that its own `src/`
  package was imported rather than the repository root's.
- **T01** had exactly three expected baseline failures:
  `test_negative_price_raises`, `test_negative_discount_raises`, and
  `test_discount_over_100_raises` (12 tests run, 3 failures, 0 errors).
- **T02** had exactly one expected baseline failure: `test_empty_list_raises`
  (12 tests run, 1 failure, 0 errors).
- **T03** passed all of its existing discount and average tests (8 tests, 0 failures,
  0 errors) and intentionally contains no `add` tests; generating them is the task.
- A T01 agentic attempt was completed.
- A T01 non-agentic attempt was completed.

## Methods

- Both T01 attempts started from identical files, copied from
  `task_templates/T01_discount` into `experimental_runs/T01-agentic` and
  `experimental_runs/T01-nonagentic`.
- SHA-256 hashes were used to verify the identical starting states. All three copies
  of `src/calculator.py` hashed to `2110ce52…976c1b39`, and all three copies of
  `tests/test_calculator.py` hashed to `156eca51…59f02a73`. These are recorded in
  `evidence/starting-state-hashes.txt`.
- Both conditions received the same `TASK.md` requirements.
- Both were evaluated using the same 12 public tests, via
  `python -m unittest discover -s tests -p "test_*.py" -v` run from inside each run
  folder.
- The agentic system could inspect files, edit `src/calculator.py`, and execute the
  test suite.
- The non-agentic model received only a static prompt packet
  (`evidence/nonagentic-prompt.txt`) containing the instruction, `TASK.md`, the
  current `calculator.py`, and the baseline failing-test output. It had no repository
  or terminal access, and its returned file was applied verbatim without correction.
- The test file hash was re-checked after each attempt and was unchanged in both
  conditions, confirming neither system modified the tests.
- No hidden tests and no repeated trials were used during this preliminary pilot.

## Results

Exact rows from `results.csv`:

```
task,condition,system,run,completed,tests_passed,tests_total,regressions,elapsed_seconds,model_turns,notes
T01,agentic,Claude Code in VS Code,1,1,12,12,0,45,1,"Wall-clock elapsed including file inspection, edit, and test execution"
T01,non-agentic,ChatGPT browser chat,1,1,12,12,0,4.32,1,"Model response time only; output applied verbatim, not directly comparable to agentic wall-clock"
```

Both conditions completed the task: each passed 12 of 12 tests with 0 regressions and
0 errors, in a single model turn. On this single task, the two conditions produced the
same functional outcome. The elapsed-time figures measure different things (see
Limitations) and no claim is made that either system is generally superior.

## Challenges

- **Isolating tasks without Git branches.** The constraint ruled out branch-per-task
  isolation, so separate directory copies under `experimental_runs/` were used, with
  the directory ignored by Git so run artifacts never enter the history.
- **Preventing changes from one attempt from affecting another.** Each condition works
  in its own copied tree, and hashes were recorded before and checked after to prove
  the runs stayed independent.
- **Avoiding incorrect imports.** Running the tests from the repository root silently
  imported the root `src/calculator.py` instead of the template's, because both expose
  a `src` package. Every test command is therefore run from inside its own task or run
  folder.
- **Comparing two workflows with different tool access.** The agentic condition can
  iterate against the test suite; the non-agentic one answers once from a static
  packet. Equalising the information they receive, without giving the non-agentic
  model execution ability it does not have, limits how directly the two can be
  compared.
- **Working within a limited reporting deadline**, which constrained the pilot to a
  single task and a single attempt per condition.

## Limitations

- Only one task (T01) was experimentally evaluated.
- Only one attempt was completed per condition.
- Only public tests were used; no withheld tests verify the solutions beyond what the
  visible suite checks.
- Runtime may not be directly comparable, because the two elapsed times were measured
  differently: the agentic figure is wall-clock time covering inspection, editing, and
  test execution, while the non-agentic figure is model response time alone.
- With one task, one trial per condition, and an identical outcome in both, the
  results cannot be generalized beyond this pilot.

## Next Steps

- Run T02 and T03 in both conditions.
- Add repeated trials per condition.
- Add withheld tests that are not shown to either system.
- Expand the range of task categories.
- Add coverage or complexity measurements where appropriate.
- Consider adding TypeScript tasks later.

## Evidence

- `evidence/starting-state-hashes.txt`
- `evidence/t01-baseline-output.txt`
- `evidence/t01-agentic-output.txt`
- `evidence/t01-nonagentic-output.txt`
- `results.csv`
- `summary.csv`
- GitHub repository: https://github.com/MMABDUL153/agent-benchmark-python
