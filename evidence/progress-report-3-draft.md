# Progress Report — Post-Midterm Update (Draft)

Status markers used below: **[VERIFIED]** = confirmed by inspecting the actual
repository files this session; **[NEW]** = work completed in this session;
**[PENDING]** = not yet done, needs your action before it can be reported as
complete.

## 1. Where the project stood at the midterm

- T01 (discount validation) was the only experimentally evaluated task.
- One agentic attempt (Claude Code in VS Code) and one non-agentic attempt
  (ChatGPT browser chat) were run on T01, both completing 12/12 tests with 0
  regressions. **[VERIFIED]** — matches `results.csv`, `summary.csv`, and
  `evidence/progress-report-2-summary.md`.
- T02 and T03 task templates existed and were verified (T02's baseline was
  confirmed to produce exactly one failure, `test_empty_list_raises`), but
  **no experiment had been run on either task.** **[VERIFIED]**

## 2. Work completed this session

- Set up isolated run folders for T02, mirroring the T01 methodology:
  `experimental_runs/T02-agentic/` and `experimental_runs/T02-nonagentic/`,
  each seeded from the unmodified `task_templates/T02_average` starting state.
  **[NEW]**
- Applied an agentic-style fix to `average()` in
  `experimental_runs/T02-agentic/src/calculator.py`: it now raises
  `ValueError` when given an empty list, with `apply_discount` and `add`
  left untouched. **[NEW — code only, not yet test-verified]**
- Prepared `evidence/t02-nonagentic-prompt.txt`, a static prompt packet in
  the same format used for T01, for pasting into a fresh ChatGPT session to
  collect the non-agentic T02 attempt. **[NEW]**
- Wrote `evidence/t02-run-instructions.md` with the exact commands needed to
  generate real baseline, agentic, and non-agentic test output for T02.
  **[NEW]**

## 3. What is explicitly NOT done yet

- The T02 test suite has **not been executed** this session (no shell access
  was available). The code fix has not been verified to actually pass 12/12
  tests. **[PENDING — run `evidence/t02-run-instructions.md` steps 1–2]**
- The non-agentic T02 attempt has not been run — this requires a live ChatGPT
  session, which only you can do. **[PENDING — step 3]**
- `results.csv` / `summary.csv` have not been updated with any T02 row,
  because no real numbers exist yet to log. **[PENDING]**
- T03 remains untouched.

## 4. Suggested framing for today's report

Rather than claiming T02 is complete, this update should honestly state: the
T02 experimental harness is built and a candidate agentic fix has been
written, but verification is in progress and will be finalized within
[however many days you choose] with real test output appended to the
results log. This keeps the report consistent with your experimental-rigor
standard (no invented results) while still showing concrete, visible
progress since the midterm.

## 5. Next steps (in order)

1. Run the three commands in `evidence/t02-run-instructions.md` and save the
   outputs.
2. Send me the outputs (or the saved files) — I will append real rows to
   `results.csv`/`summary.csv` and fold the verified numbers into the report.
3. Decide whether today's report includes T02 as "in progress, code fix
   written, verification pending" or waits to report T02 only once fully
   verified.
4. After T02 is closed out, move to T03 using the same pattern.
