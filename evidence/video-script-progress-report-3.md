# Video script — Progress Report 3 (target: 4 minutes, ~550 words)

Read this at a natural pace (~140 words/minute). Record your screen for each
section as marked, using the matching screenshot/file from the checklist.
Time markers are guides, not hard cutoffs — don't rush to hit them exactly.

---

## [0:00–0:20] Intro

"Hi, I'm Musa Abdulrafiu, and this is my progress update for Senior Seminar
One, covering Weeks 8 and 9 of my project benchmarking autonomous AI coding
agents against conventional LLM code generation. At the midterm, I had one
completed comparison: Task T01, discount validation, run under both an
agentic workflow — Claude Code in VS Code — and a non-agentic workflow —
ChatGPT browser chat. Both passed all 12 tests. Since then, I've completed
the same full comparison for two more tasks: T02 and T03."

*(Screen: title slide or repository homepage)*

## [0:20–1:10] T02 walkthrough

"Task T02 requires fixing the `average` function so an empty list raises a
ValueError instead of silently returning zero. The baseline run confirmed
the expected defect: 12 tests, exactly 1 failure.

*(Screen: t02-baseline.png)*

For the agentic condition, I scoped Claude Code in VS Code to only the T02
run folder, so it had no access to the rest of the repository. It fixed the
function, ran the tests itself, and reported real start and end timestamps —
9.58 seconds, in a single conversational turn. All 12 tests passed, 0
regressions.

*(Screen: t02-agentic-session.png, then t02-agentic-final.png)*

For the non-agentic condition, I submitted the same task to ChatGPT with no
file or tool access — just the task description, the code, and the baseline
output. It returned a correct fix on the first try. I applied it verbatim and
timed the whole exchange with an external stopwatch, the same method used for
T01: 9.03 seconds. Also 12 out of 12, zero regressions."

*(Screen: t02-nonagentic-chat.png, then t02-nonagentic-final.png)*

## [1:10–2:00] T03 walkthrough

"Task T03 is different — it's not a bug fix, it's test generation. The goal
is to add a test class for the `add` function covering positive integers,
floats, negative numbers, and large values, where no such tests exist yet.
The baseline is 8 passing tests and no `TestAdd` class.

*(Screen: t03-baseline.png)*

The agentic attempt added four new tests and left everything else untouched:
9.11 seconds, one turn, and the full suite — 8 existing plus 4 new — passed
at 12 out of 12.

*(Screen: t03-agentic-session.png, then t03-agentic-final.png)*

The non-agentic attempt also succeeded, in 5.28 seconds. One thing worth
mentioning: when I pasted ChatGPT's response, the double underscores in
`__main__` had been stripped by chat markdown formatting, turning valid
Python into a syntax error. I caught that, restored the literal text — not a
logic change — and documented it explicitly in the evidence rather than
treating it as a silent fix."

*(Screen: t03-nonagentic-chat.png, then t03-nonagentic-final.png)*

## [2:00–2:40] A methodology correction

"One thing I want to highlight rather than hide: my first pass at fixing T02
and T03 used a different AI system than the one used for T01. Since this
project's whole premise depends on holding every variable constant except
the one being studied, that would have confounded task identity with system
identity. I caught it, marked that attempt as a superseded preliminary check
in my results log rather than deleting it, and reran both tasks with the
correct, consistent system. I think that kind of correction — visible, not
buried — is part of what makes the result log trustworthy."

*(Screen: results-csv-update.png)*

## [2:40–3:20] What's next

"Going forward, I've built two small automation scripts — one to reset a
task folder to its pristine starting state, and one to run the test suite,
parse the results, and log them without any manual CSV editing. I tested
both against deliberately broken code before trusting them on real data. The
next step is repeated trials — right now every result here is a single run
per condition, which isn't enough to generalize from, so I'll be running
multiple trials per task per condition to get a real sense of variance."

*(Screen: scripts/README.md or terminal running bench_reset.py)*

## [3:20–3:40] Close

"That's where things stand at Weeks 8 and 9: T01 through T03 are all fully
verified in both conditions, the automation is in place for the next phase,
and the plan for the rest of the semester is repeated trials, timing
standardization, and a code-quality rubric. Thanks for watching."

---

**Word count: ~560 words → roughly 4 minutes at a natural pace.** Cut the
methodology-correction section short (to ~15 seconds) if you need to land
closer to 3 minutes; it's the one section that's more "nice to have" than
essential.
