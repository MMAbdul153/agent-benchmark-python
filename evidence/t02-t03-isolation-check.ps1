# Run this BEFORE opening VS Code / Claude Code, and again AFTER each agentic
# run, to prove the agent did not touch anything outside its own run folder.
# Save both outputs (e.g. isolation-before.txt / isolation-after.txt) — if the
# "before" and "after" hashes for every file EXCEPT the one being edited are
# identical, the run was properly isolated.

$root = "C:\Users\Musaa\Desktop\agent-benchmark-python"

$paths = @(
    "$root\task_templates\T02_average\src\calculator.py",
    "$root\task_templates\T02_average\tests\test_calculator.py",
    "$root\task_templates\T03_add_tests\src\calculator.py",
    "$root\task_templates\T03_add_tests\tests\test_calculator.py",
    "$root\experimental_runs\T02-nonagentic\src\calculator.py",
    "$root\experimental_runs\T02-nonagentic\tests\test_calculator.py",
    "$root\experimental_runs\T03-nonagentic\src\calculator.py",
    "$root\experimental_runs\T03-nonagentic\tests\test_calculator.py",
    "$root\src\calculator.py",
    "$root\tests\test_calculator.py"
)

foreach ($p in $paths) {
    if (Test-Path $p) {
        Get-FileHash -Algorithm SHA256 $p
    } else {
        Write-Output "MISSING: $p"
    }
}
