# T02 + T03 Run Instructions (produces real evidence)

Run these in PowerShell from anywhere (each block starts with its own `cd`).
Save each block's full terminal output to the listed file — copy/paste the
whole thing, including the `Ran N tests...` summary line.

## T02 — Average empty-list validation

### 1. Baseline (unmodified)
```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\task_templates\T02_average
python -m unittest discover -s tests -p "test_calculator.py" -v
```
Expected (not yet verified): 12 tests, 1 failure (`test_empty_list_raises`).
Save to: `evidence\t02-baseline-output.txt`

### 2. Agentic fix (already written)
```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T02-agentic
python -m unittest discover -s tests -p "test_calculator.py" -v
```
Expected: 12/12 pass, 0 regressions.
Save to: `evidence\t02-agentic-output.txt`

### 3. Non-agentic (you run this in ChatGPT)
1. Copy the real output from step 1.
2. Open `evidence\t02-nonagentic-prompt.txt`, replace the bracketed
   placeholder with that real output.
3. Paste the whole file into a fresh ChatGPT browser chat (no file access, no
   tools — same conditions as T01).
4. Save its returned code verbatim to
   `experimental_runs\T02-nonagentic\src\calculator.py`.
5. Run:
   ```powershell
   cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T02-nonagentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
6. Save to: `evidence\t02-nonagentic-output.txt`

---

## T03 — Add-function test generation

### 1. Baseline (unmodified — no TestAdd exists yet)
```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\task_templates\T03_add_tests
python -m unittest discover -s tests -p "test_calculator.py" -v
```
Expected (not yet verified): 8 tests, 0 failures (only TestDiscount +
TestAverage exist). This does NOT mean T03 is done — the add tests are the
task itself.
Save to: `evidence\t03-baseline-output.txt`

### 2. Agentic fix (already written)
`experimental_runs\T03-agentic\tests\test_calculator.py` already has a
TestAdd class added (positive ints, floats, negative, large numbers), with
`add`, `apply_discount`, and `average` left untouched.
```powershell
cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T03-agentic
python -m unittest discover -s tests -p "test_calculator.py" -v
```
Expected: 12/12 pass (8 existing + 4 new), 0 regressions.
Save to: `evidence\t03-agentic-output.txt`

### 3. Non-agentic (you run this in ChatGPT)
1. Copy the real output from step 1 above.
2. Open `evidence\t03-nonagentic-prompt.txt`, replace the bracketed
   placeholder with that real output.
3. Paste the whole file into a fresh ChatGPT browser chat.
4. Save its returned test file verbatim to
   `experimental_runs\T03-nonagentic\tests\test_calculator.py`.
5. Run:
   ```powershell
   cd C:\Users\Musaa\Desktop\agent-benchmark-python\experimental_runs\T03-nonagentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
6. Save to: `evidence\t03-nonagentic-output.txt`

---

## After you have all six outputs

Send me the six terminal outputs (paste them, or tell me you saved the .txt
files and I'll read them from the repo) and timestamps/turn counts if you
tracked them, and I will:
- Append real, verified rows to `results.csv` and `summary.csv` for T02 and
  T03 (both conditions each).
- Update `reports\progress_report_3.tex` with verified figures/tables instead
  of "pending" language.

Until then, T02 and T03 remain "code written, not yet verified" in the report.
