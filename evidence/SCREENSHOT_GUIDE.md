# Screenshot Guide — Progress Report 2

Four screenshots are required. Save each with the exact filename shown, in this
`evidence/` folder.

## 1. `repository-pr2.png`

The GitHub repository page at https://github.com/MMABDUL153/agent-benchmark-python
showing:

- the `task_templates` folder
- the `evidence` folder
- `results.csv`
- `summary.csv`
- the latest Progress Report 2 commit (message and hash visible in the commit bar)

## 2. `task-folders.png`

The VS Code Explorer panel showing all three templates under `task_templates`:

- `T01_discount`
- `T02_average`
- `T03_add_tests`

Expand one template so that its `src`, `tests`, and `TASK.md` entries are visible.

## 3. `evaluation-output.png`

The terminal, or `evidence/t01-agentic-output.txt` opened in the editor, showing the
final T01 agentic test run. All 12 test names must be legible, along with the final
summary lines:

```
Ran 12 tests in 0.001s

OK
```

## 4. `results-summary.png`

`results.csv` and `summary.csv` open and readable, clearly enough that both pilot
conditions and their actual values can be read — the `agentic` and `non-agentic`
rows with their `completed`, `tests_passed`, `tests_total`, `regressions`,
`elapsed_seconds`, and `model_turns` values.
