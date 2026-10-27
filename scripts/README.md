# Benchmark automation scripts

These replace the manual "copy folder, run tests, hand-type a CSV row" workflow
with two small, tested scripts. Both were verified against a throwaway copy of
this repo before being added here (including a deliberately broken fix, to
confirm regression detection actually works, and the exact timestamp format
Claude Code produces, to confirm elapsed-time parsing doesn't silently fail).

## 1. `bench_reset.py` — get a clean starting state

```powershell
python scripts\bench_reset.py --task T02 --condition agentic
python scripts\bench_reset.py --task T02 --condition agentic --run 2
python scripts\bench_reset.py --task T03 --condition nonagentic --run 3
```

Overwrites `experimental_runs/<task>-<condition>[-run<N>]/src` and `tests`
with a fresh copy of that task's pristine template (`task_templates/`), and
copies `TASK.md`. Run this before every trial. It never touches
`task_templates/` itself, so the pristine source of truth is always safe.

## 2. `bench_log.py` — run, parse, and log a trial

```powershell
# Agentic, with the agent's own real start/end timestamps:
python scripts\bench_log.py --task T02 --condition agentic --system "Claude Code in VS Code" --run 1 --turns 1 --start-ts 2026-10-27T12:55:14.4427708-05:00 --end-ts 2026-10-27T12:55:24.0246683-05:00 --notes "Fixed average() per TASK.md"

# Non-agentic, after pasting ChatGPT's output into the run folder:
python scripts\bench_log.py --task T02 --condition nonagentic --system "ChatGPT browser chat" --run 1 --turns 1 --notes "Output applied verbatim"
```

What it does:
- Runs `python -m unittest discover -s tests -p "test_calculator.py" -v`
  inside the run folder.
- Parses which tests passed/failed from the real output (never guesses).
- Computes `regressions` by comparing failing tests against the task's known
  baseline failures in `tasks_config.json` — a failure that's expected at
  baseline doesn't count as a regression; any other failure does.
- Computes `elapsed_seconds` from your supplied `--start-ts`/`--end-ts` if
  given (use the agent's own real timestamps), otherwise from the script's
  own wall-clock measurement around the test run only — and labels which one
  it used in the logged notes, so nobody reading `results.csv` later mistakes
  one kind of timing for another.
- Appends one row to `results.csv` and saves the full terminal output to
  `evidence/<task>-<condition>-run<N>-output.txt`.
- If it can't parse any test results, it aborts and logs nothing, rather than
  writing a blank or guessed row.

## Running repeated trials

To run, say, 5 agentic trials of T02:

```powershell
for ($i = 1; $i -le 5; $i++) {
    python scripts\bench_reset.py --task T02 --condition agentic --run $i
    # ... open VS Code on experimental_runs\T02-agentic-run$i, run Claude Code,
    #     get its start/end timestamps and turn count ...
    python scripts\bench_log.py --task T02 --condition agentic --system "Claude Code in VS Code" --run $i --turns <N> --start-ts <start> --end-ts <end> --notes "..."
}
```

Each trial gets its own isolated `experimental_runs/T02-agentic-run<N>/`
folder and its own row in `results.csv`, so nothing overwrites a previous
trial and you can compute completion rate / mean elapsed time / regression
rate across trials directly from the CSV.

## What this does NOT automate

- The actual agentic editing step (you still open VS Code and run Claude Code
  yourself) and the non-agentic ChatGPT step (still a manual paste) — those
  require a human in the loop by design, since they're the systems being
  measured.
- Nothing here invents a result it didn't observe. If a step can't be
  measured honestly, the script refuses rather than estimating.
