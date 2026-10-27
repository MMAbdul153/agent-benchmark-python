# Screenshot checklist — Progress Report 3 (11 placeholders)

For the 6 "test execution" screenshots, just re-run the listed command in a
terminal — the output will match what's already verified in the named
evidence file, since nothing in those folders has changed since verification.
For the 2 "chat" screenshots, scroll back in the existing conversation
(VS Code's Claude Code panel / your ChatGPT tab history) rather than
re-running anything, since those sessions already happened — re-running them
would produce a new, not-yet-logged result.

## T02 (5 screenshots)

1. **`images/t02-baseline.png`**
   ```
   cd task_templates\T02_average
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
   Should match `evidence/t02-baseline-output.txt` (12 tests, 1 failure).

2. **`images/t02-agentic-session.png`**
   Open VS Code on `experimental_runs\T02-agentic`. Screenshot either the
   Claude Code chat panel (if the session history is still there, showing the
   timestamps/turn report) or the edited `average()` function in
   `src/calculator.py` with the diff/change visible.

3. **`images/t02-agentic-final.png`**
   ```
   cd experimental_runs\T02-agentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
   Should match `evidence/t02-agentic-vscode-output.txt` (12/12 pass).

4. **`images/t02-nonagentic-chat.png`**
   Scroll back to the ChatGPT conversation where you submitted
   `t02-nonagentic-prompt.txt`. Screenshot the prompt and its code response.

5. **`images/t02-nonagentic-final.png`**
   ```
   cd experimental_runs\T02-nonagentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
   Should match `evidence/t02-nonagentic-output.txt` (12/12 pass).

## T03 (5 screenshots)

6. **`images/t03-baseline.png`**
   ```
   cd task_templates\T03_add_tests
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
   Should match `evidence/t03-baseline-output.txt` (8 tests, 0 failures, no
   TestAdd).

7. **`images/t03-agentic-session.png`**
   Open VS Code on `experimental_runs\T03-agentic`. Screenshot the Claude
   Code chat panel or the added `TestAdd` class in `tests/test_calculator.py`.

8. **`images/t03-agentic-final.png`**
   ```
   cd experimental_runs\T03-agentic
   python -m unittest discover -s tests -p "test_calculator.py" -v
   ```
   Should match `evidence/t03-agentic-vscode-output.txt` (12/12 pass).

9. **`images/t03-nonagentic-chat.png`**
   Scroll back to the ChatGPT conversation where you submitted
   `t03-nonagentic-prompt.txt`. Screenshot the prompt and its test-file
   response.

10. **`images/t03-nonagentic-final.png`**
    ```
    cd experimental_runs\T03-nonagentic
    python -m unittest discover -s tests -p "test_calculator.py" -v
    ```
    Should match `evidence/t03-nonagentic-output.txt` (12/12 pass).

## Results log (1 screenshot)

11. **`images/results-csv-update.png`**
    Open `results.csv` (VS Code or Excel) and screenshot it showing the T01
    rows plus the new T02/T03 preliminary-superseded, official, and (now
    filled-in) rows.

## If any re-run doesn't match the evidence file

Stop and tell me rather than using that screenshot — a mismatch would mean
something in the repo changed since verification, and we need to find out
why before it goes in the report.

## After you have the images

Send me the 11 files (or tell me they're saved in `images/` in the repo) and
I'll swap each `\ScreenshotPlaceholder{...}` for the matching
`\includegraphics` line and recompile the preview.
