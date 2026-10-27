#!/usr/bin/env python3
"""Run the test suite for an experimental run folder, parse the results, and
append a verified row to results.csv.

Usage examples:
    # Non-agentic: script measures elapsed time itself around the test run.
    python scripts/bench_log.py --task T02 --condition nonagentic \
        --system "ChatGPT browser chat" --run 1 --turns 1 \
        --notes "Output applied verbatim"

    # Agentic: supply the agent's own real start/end timestamps instead.
    python scripts/bench_log.py --task T02 --condition agentic \
        --system "Claude Code in VS Code" --run 1 --turns 1 \
        --start-ts 2026-10-27T12:55:14.4427708-05:00 \
        --end-ts   2026-10-27T12:55:24.0246683-05:00 \
        --notes "Fixed average() per TASK.md"

This never fabricates anything:
- If --start-ts/--end-ts are not given, elapsed_seconds is the script's own
  wall-clock measurement around the test subprocess ONLY (labeled as such in
  the notes), not any setup/editing time before the script ran.
- regressions is computed by diffing the parsed failing-test names against
  the task's known baseline failures (scripts/tasks_config.json), never
  guessed.
- If the test output can't be parsed, nothing is logged and the script exits
  with an error instead of silently writing a blank/guessed row.
"""
import argparse
import csv
import json
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path


def parse_ts(s: str) -> datetime:
    """Parse an ISO-ish timestamp, tolerating PowerShell's 7-digit fractional
    seconds (from `Get-Date -Format o`) or any other sub/over-precise
    fractional-second count, which Python's datetime.fromisoformat rejects
    outright on some versions."""
    m = re.match(r"^(.*T\d{2}:\d{2}:\d{2})(\.\d+)?([+-]\d{2}:\d{2}|Z)?$", s)
    if not m:
        return datetime.fromisoformat(s)
    base, frac, tz = m.groups()
    frac = (frac or ".0")[1:]
    frac = (frac + "000000")[:6]
    tz = "" if tz in (None, "Z") else tz
    return datetime.fromisoformat(f"{base}.{frac}{tz}")


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "tasks_config.json"
RESULTS_CSV = REPO_ROOT / "results.csv"
EVIDENCE_DIR = REPO_ROOT / "evidence"

TEST_LINE_RE = re.compile(r"^(\S+) \([\w.]+\) \.\.\. (ok|FAIL|ERROR)\s*$")


def load_config():
    with CONFIG_PATH.open() as f:
        return json.load(f)


def run_dir_for(task, condition, run):
    name = f"{task}-{condition}" if run == 1 else f"{task}-{condition}-run{run}"
    return REPO_ROOT / "experimental_runs" / name


def run_tests(run_dir: Path):
    start = time.time()
    proc = subprocess.run(
        ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_calculator.py", "-v"],
        cwd=run_dir,
        capture_output=True,
        text=True,
    )
    elapsed = time.time() - start
    return proc.stdout + proc.stderr, elapsed


def parse_output(output: str):
    failed = []
    total = 0
    for line in output.splitlines():
        m = TEST_LINE_RE.match(line)
        if m:
            total += 1
            name, status = m.groups()
            if status != "ok":
                failed.append(name)
    return total, failed


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--task", required=True)
    parser.add_argument("--condition", required=True, choices=["agentic", "nonagentic"])
    parser.add_argument("--system", required=True)
    parser.add_argument("--run", type=int, default=1)
    parser.add_argument("--turns", type=int, required=True)
    parser.add_argument("--start-ts")
    parser.add_argument("--end-ts")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    config = load_config()
    if args.task not in config:
        raise SystemExit(f"Unknown task '{args.task}'. Known: {list(config)}")

    run_dir = run_dir_for(args.task, args.condition, args.run)
    if not run_dir.exists():
        raise SystemExit(f"Run folder not found: {run_dir}. Run bench_reset.py first.")

    output, script_elapsed = run_tests(run_dir)
    total, failed = parse_output(output)

    if total == 0:
        raise SystemExit(
            "Could not parse any test results from output -- aborting, "
            "nothing logged.\n\n" + output
        )

    baseline_failures = set(config[args.task].get("baseline_failures", []))
    regressions = len([f for f in failed if f not in baseline_failures])
    tests_passed = total - len(failed)
    completed = 1 if not failed else 0

    if args.start_ts and args.end_ts:
        try:
            start_dt = parse_ts(args.start_ts)
            end_dt = parse_ts(args.end_ts)
        except ValueError as e:
            raise SystemExit(f"Could not parse --start-ts/--end-ts: {e}")
        elapsed_seconds = round((end_dt - start_dt).total_seconds(), 2)
        elapsed_note = (
            f"elapsed_seconds = supplied start/end timestamps "
            f"({args.start_ts} to {args.end_ts})."
        )
    else:
        elapsed_seconds = round(script_elapsed, 3)
        elapsed_note = (
            f"elapsed_seconds = script-measured wall time around the test "
            f"subprocess only ({script_elapsed:.3f}s); excludes any "
            f"setup/editing time before this script ran."
        )

    full_notes = f"{args.notes.strip()} {elapsed_note}".strip()

    EVIDENCE_DIR.mkdir(exist_ok=True)
    run_label = f"{args.task.lower()}-{args.condition}-run{args.run}"
    out_path = EVIDENCE_DIR / f"{run_label}-output.txt"
    out_path.write_text(output)

    row = [
        args.task, args.condition, args.system, args.run, completed,
        tests_passed, total, regressions, elapsed_seconds, args.turns, full_notes,
    ]

    write_header = not RESULTS_CSV.exists()
    with RESULTS_CSV.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow([
                "task", "condition", "system", "run", "completed",
                "tests_passed", "tests_total", "regressions",
                "elapsed_seconds", "model_turns", "notes",
            ])
        writer.writerow(row)

    print(f"Logged: {row}")
    print(f"Full output saved to {out_path}")
    if failed:
        print(f"Failed tests: {failed}")


if __name__ == "__main__":
    main()
