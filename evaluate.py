# evaluate.py
import subprocess
import time
import csv
from pathlib import Path

RESULTS_FILE = Path("results.csv")

def run_tests():
    start = time.time()
    proc = subprocess.run(
        ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        capture_output=True,
        text=True,
    )
    duration = time.time() - start
    success = proc.returncode == 0
    return success, duration, proc.stdout, proc.stderr

def log_result(system_name: str, mode: str, task_id: str,
               success: bool, duration: float, iterations: int,
               notes: str = ""):
    header = ["system", "mode", "task_id", "success", "duration_sec",
              "iterations", "notes"]
    write_header = not RESULTS_FILE.exists()
    with RESULTS_FILE.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow([system_name, mode, task_id,
                         int(success), round(duration, 3),
                         iterations, notes])

if __name__ == "__main__":
    # Example: baseline run (no AI fix)
    success, duration, out, err = run_tests()
    print(out)
    print("Success:", success, "Duration:", duration)