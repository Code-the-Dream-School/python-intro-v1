# Week 6 — Functions and Scope (Mentor Summary)

## Key concepts taught

- **Defining & calling** — `def name():` + colon + indented body; defining ≠ running, nothing happens until called. Framed as "write once, use many times" (copy-paste is the anti-pattern).
- **Parameters vs. arguments** — parameter = the variable in `def`, argument = the value passed in. Multiple params supported.
- **Return values** — `return` hands a value back to the caller for use in expressions; contrasted with functions that just `print`. **No `return` → implicit `None`** hammered as the signature bug.
- **Default parameters** — `def greet(name="stranger")`; defaults must come *after* required params. Keyword-argument calls introduced in the assignment (Warmup 1), not the lesson.
- **Scope** — variables assigned inside a function are **local**; gone after the call (`NameError` outside). Same-name assignment creates a *new local*, never touches the global.
- **Reading vs. reassigning globals** — functions can read outer/global names, but any assignment makes a local. `global` keyword shown but explicitly discouraged; "pass in, return out" is the endorsed pattern.
- **Refactoring** — restructure without changing behavior. Method: identify one-sentence chunks → extract one function at a time → add docstrings → wire up under a guard.
- **Docstrings** — triple-quoted first line; surface in `help()` and tooltips.
- **`if __name__ == "__main__":`** — run-directly-vs-imported guard; framed as the entry-point "table of contents." Multi-file/import mechanics deferred.

## The assignment — "Functions & Scope"

Four standalone warmup files plus a refactor of the Week 5 mini-project.

- **Warmup 1 — Default params:** `greet(name, greeting="Hello")` called three ways (positional, custom, keyword arg). `warmup1.py`
- **Warmup 2 — Return values:** `celsius_to_fahrenheit` / `fahrenheit_to_celsius`, f-strings rounded to 1 decimal. `warmup2.py`
- **Warmup 3 — Scope:** trigger a `NameError` (paste it in a comment, then comment out the line), then show `return` fixing it. `warmup3.py`
- **Warmup 4 — Validation:** `is_valid_score(score)` returns bool for int 0–100; drive with `input()` inside an `if`. `warmup4.py`
- **Part 2 — Refactor the Number Cruncher:** new file; copy the `numbers` list from Week 5. Required functions: `find_min`, `find_max` (loop-based, no builtins), `search` (returns index or `-1`), `bubble_sort` (returns a **new** list, no in-place), `show_menu`, `main` (while loop dispatcher). No logic outside functions except the list def and `main()` call. Print "Found/Not found" from `main()`, not from `search`.
- **Video reflection (3–5 min):** `return` vs `print`, walk one function's inputs/output, show where functions cleaned up code + tie to Git history. Submit PR link (URL1) + video (URL2) into `assignment-6`.

## Likely trouble spots

- **`return` vs `print`** — the central confusion. Students print inside a function and expect a usable value; `result = f(...)` then holds `None`. The Predict-Then-Check exercise targets exactly this.
- **Reassignment doesn't mutate the global** — passing a variable in, reassigning the param, and expecting the outer variable to change (the `score`/`update_score` snippet). Local-shadowing is unintuitive here.
- **Forgetting to `return`** — silent `None` with no error; tell them to check for a missing `return` whenever a result is `None`.
- **`bubble_sort` mutating in place** — requirement is a *new* sorted list; students who sort the original (or return `None` from an in-place sort) miss the spec. A copy (`sorted_list = numbers[:]`) is the fix.
- **`search` doing its own printing** — spec says `search` only returns the index; the "Found at index X" / "Not found" print belongs in `main()`. Easy to conflate.
- **Logic leaking outside functions** — Part 2 forbids top-level logic except the list and `main()` call; leftover stray code from the Week 5 version is common.
- **Keyword arguments** — used in Warmup 1 but not actually taught in the lessons; some students won't know `greet(name, greeting="...")` call syntax.
- **`global` temptation** — a few will reach for `global` (Warmup 3 / mini-project) instead of return; the lessons discourage it, so nudge toward parameters + return.
