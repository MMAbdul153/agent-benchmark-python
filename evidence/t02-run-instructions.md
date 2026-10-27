# T02 Run Instructions (to produce real evidence before submission)

I could not execute Python in this session (sandbox shell was unavailable), so the
steps below must be run on your machine, exactly as you did for T01. Nothing here
has been fabricated — run each command and paste the output back to me, or save it
to the listed evidence file, and I will help you write it up accurately.

## 1. Baseline (unmodified T02)

```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\task_templates\T02_average
python -m unittest discover -s tests -p "test_calculator.py" -v
```

Expected (per TASK.md and your Week 5-6 progress-report-2-summary.md, not yet
re-verified this session): 12 tests run, exactly 1 failure
(`test_empty_list_raises`), 0 errors.

Save the full terminal output to:
`evidence\t02-baseline-output.txt`

## 2. Agentic condition (already fixed in this session)

I edited `experimental_runs\T02-agentic\src\calculator.py` directly (repo/file
access, no manual logic correction beyond what the task required) so `average`
raises `ValueError` on an empty list. Run:

```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T02-agentic
python -m unittest discover -s tests -p "test_calculator.py" -v
```

Expected: 12/12 pass, 0 regressions. Save output to:
`evidence\t02-agentic-output.txt`

## 3. Non-agentic condition (you run this in ChatGPT yourself)

I did not run this condition — ChatGPT is a separate product I don't have access
to in this session, and the T01 methodology specifically used it as the
non-agentic system, so the comparison stays consistent if you use it again.

1. First run the baseline command in step 1 and copy its **real** output.
2. Open `evidence\t02-nonagentic-prompt.txt`, replace the bracketed placeholder
   baseline traceback with that real output.
3. Paste the full file into a new ChatGPT browser chat (same conditions as T01:
   no file access, no tool use).
4. Take its returned code verbatim (no manual edits) and save it to:
   `experimental_runs\T02-nonagentic\src\calculator.py`
5. Run:
   ```powershell
   cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T02-nonagentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
6. Save output to `evidence\t02-nonagentic-output.txt`

## 4. After you have real output

Paste me the three terminal outputs (or the saved .txt files) and I will:
- Append accurate rows to `results.csv` and `summary.csv` (task, condition,
  system, completed, tests passed/total, regressions, elapsed time, turns).
- Update the progress report with verified T02 results instead of placeholders.

Until you provide that output, the progress report will mark T02 results as
**pending verification**, not complete.
