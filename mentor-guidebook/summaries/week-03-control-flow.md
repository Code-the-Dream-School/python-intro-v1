# Week 3 — Control Flow (Mentor Summary)

**Environment this week:** Students now work locally in VS Code (installed Week 2) and run scripts from the terminal. No new install. `input()`-driven scripts run in the terminal, not the online IDE.

**Git thread:** This week *unpacks* the full Git workflow — branch → add → commit → push → PR → merge → pull back to `main` — rather than introducing it cold. Students already forked, branched, and opened a PR in Week 2; the lesson slows down to explain what each step does (staging states, commit hygiene, why branches). Work happens in their forked `python-intro-homework` repo on an `assignment-3` branch (inside a `week-3/assignment-3/` folder), submitted as a **PR link** (not the repo homepage) plus a video reflection. Expect friction with the mechanics, not the Python.

---

## Key concepts taught

- **Indentation & blocks** — colons `:` start blocks; 4-space standard; no mixing tabs/spaces; reading `IndentationError`.
- **Comparison operators** — `==`, `!=`, `<`, `>`, `<=`, `>=` return booleans; `=` (assign) vs `==` (compare) called out explicitly.
- **`if` / `elif` / `else`** — branch selection; first true branch wins; flattening nested conditionals into `elif` chains.
- **`int(input())`** — `input()` always returns a string; wrap in `int()` for numeric comparison.
- **Logical operators** — `and`, `or`, `not`; truth tables; precedence (`not` → `and` → `or`) and parentheses for clarity.
- **Truthy/falsy** — `0`, `""`, `None`, `[]` are falsy; used for input-presence checks (`if name:`).
- **`.lower()` normalization** — canonicalize yes/no and text input before comparing.
- **Git workflow** — branches, staging (untracked/modified/staged), commit messages, push, PR, merge, sync back to `main`.

## The assignment — "Warmups + Day Planner"

Four warmup scripts plus one mini-project, each a separate `.py` file, submitted via first PR + a 3–5 min video reflection.

- **Warmup 1 (`warmup1.py`)** — hardcoded `score` → letter grade via `if`/`elif`/`else`.
- **Warmup 2 (`warmup2.py`)** — `int(input())` age → Child/Teen/Adult/Senior using ranges with `and`.
- **Warmup 3 (`warmup3.py`)** — evaluate 5 boolean expressions, comment *why* each result holds (precedence practice).
- **Warmup 4 (`warmup4.py`)** — one number, **two separate** `if` blocks (sign, then parity); `0` is its own sign case.
- **Mini-project (`mini_project.py`)** — Day Planner: day + time-of-day → activity, ≥9 combinations, case-normalized input, friendly fallback for unrecognized input.
- **Video reflection** — explain branch selection, what `and`/`or` do, and walk through the Git workflow they used.
- **Submission** — PR link (`.../pull/N`) + video link in CTD Learns.

## Likely trouble spots

- **`=` vs `==`** — the classic first-conditional bug; assignment in a condition or comparison with a single `=`.
- **Branch ordering** — Warmup 2, the Day Planner, and the lesson's Senior-card extension all break if the narrower/higher check isn't placed before the general one. First true branch wins; unreachable branches are the predictable failure.
- **Forgetting `int()`** — comparing string input numerically "works" for `==` but silently misbehaves for `<`/`>`; or `ValueError` on non-numeric input (try/except **not taught yet** — crashing on bad input is acceptable).
- **Precedence in Warmup 3** — `or` binds loosest; expect confusion on `True or False and False`. Encourage tracing `not` → `and` → `or`.
- **Input normalization** — skipping `.lower()` makes `"Monday"` fail against `"monday"`. Assignment explicitly requires case-insensitivity.
- **Git mechanics over Python** — committing to `main` instead of branching, "no upstream branch" on first push, submitting the repo URL instead of the PR URL, forgetting the `week-3/assignment-3/` folder. The lesson pre-empts these; the errors still land. Only the second week doing this by hand, so treat fumbling as expected.
- **Deferred topics** — no loops, functions, `match`, or exception handling yet. Scripts are linear and hardcode/prompt their inputs; don't push students toward `while` retry loops or `try/except`.
