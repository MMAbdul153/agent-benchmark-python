#!/usr/bin/env python3
"""Reset (or create) an isolated experimental run folder from its pristine
task template.

Usage:
    python scripts/bench_reset.py --task T02 --condition agentic
    python scripts/bench_reset.py --task T02 --condition agentic --run 2
    python scripts/bench_reset.py --task T03 --condition nonagentic --run 3

This OVERWRITES the target run folder's src/ and tests/ with a fresh copy of
the task's pristine template, and copies TASK.md. Run this before every new
trial so each attempt starts from a known, byte-identical baseline state.
It never touches task_templates/ itself.
"""
import argparse
import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "tasks_config.json"


def load_config():
    with CONFIG_PATH.open() as f:
        return json.load(f)


def run_dir_for(task, condition, run):
    name = f"{task}-{condition}" if run == 1 else f"{task}-{condition}-run{run}"
    return REPO_ROOT / "experimental_runs" / name


def reset_run(task, condition, run, config):
    if task not in config:
        raise SystemExit(f"Unknown task '{task}'. Known tasks: {list(config)}")

    template_dir = REPO_ROOT / config[task]["template"]
    if not template_dir.exists():
        raise SystemExit(f"Template folder not found: {template_dir}")

    run_dir = run_dir_for(task, condition, run)

    for sub in ("src", "tests"):
        src = template_dir / sub
        dst = run_dir / sub
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    task_md_src = template_dir / "TASK.md"
    if task_md_src.exists():
        shutil.copy2(task_md_src, run_dir / "TASK.md")

    print(f"Reset {run_dir} from pristine {template_dir}")
    return run_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--task", required=True, help="Task id, e.g. T02")
    parser.add_argument("--condition", required=True, choices=["agentic", "nonagentic"])
    parser.add_argument("--run", type=int, default=1, help="Trial number (default 1)")
    args = parser.parse_args()

    config = load_config()
    reset_run(args.task, args.condition, args.run, config)


if __name__ == "__main__":
    main()
