# Video script — Progress Report 3 (SHORT, target: 3 minutes, ~400 words)

Read at a natural pace (~135 words/minute). Screen cues are in brackets.

---

## [0:00–0:20] Intro

"Hi, I'm Musa Abdulrafiu, with a progress update for Senior Seminar One,
covering Weeks 8 and 9 of my benchmark comparing autonomous AI coding agents
against conventional LLM code generation. At the midterm, I had one
completed comparison, Task T01. Since then, I've finished the same full
comparison for two more tasks: T02 and T03, both fully verified in both
conditions."

*(Screen: repository homepage)*

## [0:20–1:10] T02

"T02 fixes the `average` function so an empty list raises a ValueError
instead of returning zero. The baseline confirmed the defect: 12 tests, 1
failure.

*(Screen: t02-baseline.png)*

For the agentic condition, I scoped Claude Code in VS Code to only the T02
folder. It fixed the function, ran the tests itself, and reported real
timestamps: 9.58 seconds, one turn, 12 out of 12 passing.

*(Screen: t02-agentic-session.png, then t02-agentic-final.png)*

For the non-agentic condition, ChatGPT received the same task with no file
or tool access. It returned a correct fix on the first try. I applied it
verbatim and timed it with a stopwatch: 9.03 seconds, also 12 out of 12."

*(Screen: t02-nonagentic-chat.png, then t02-nonagentic-final.png)*

## [1:10–2:00] T03

"T03 is test generation, not a bug fix: add a test class for the `add`
function covering integers, floats, negatives, and large values, where none
exist yet. Baseline: 8 passing tests, no TestAdd class.

*(Screen: t03-baseline.png)*

The agentic attempt added four tests correctly in 9.11 seconds, one turn —
all 12 passed.

*(Screen: t03-agentic-session.png, then t03-agentic-final.png)*

The non-agentic attempt also succeeded, in 5.28 seconds. One thing worth
noting: ChatGPT's response had its double underscores stripped by chat
formatting, turning valid Python into a syntax error. I caught that, restored
the literal text — not a logic change — and documented it rather than fixing
it silently."

*(Screen: t03-nonagentic-chat.png, then t03-nonagentic-final.png)*

## [2:00–2:40] Results and what's next

"Every task so far has been fully verified by actually running the tests,
not just trusting a model's claim. I also built two small scripts — one to
reset a task to its pristine state, one to run tests and log results
automatically — both tested against deliberately broken code before I
trusted them. The next step is repeated trials, since every result right now
is a single run per condition."

*(Screen: results.csv or terminal running bench_reset.py)*

## [2:40–3:00] Close

"T01 through T03 are complete in both conditions. Next up: repeated trials,
timing standardization, and a code-quality rubric. Thanks for watching."

---

**Word count: ~400 words → about 3 minutes at a natural pace.**
