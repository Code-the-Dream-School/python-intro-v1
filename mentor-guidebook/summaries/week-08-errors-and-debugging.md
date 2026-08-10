# Week 8 — Errors and Debugging (Mentor Summary)

## Key concepts taught
- **Syntax vs. runtime errors** — syntax errors stop the program from starting; runtime errors ("exceptions") happen mid-execution. Week is entirely about runtime errors.
- **Common exceptions** — table of the usual suspects (`ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`, `ZeroDivisionError`, `AttributeError`). Goal is recognition, not memorization.
- **try/except/else/finally** — catch a *specific named* exception; `as e` to inspect the object; `else` for the success path; `finally` for cleanup. Broad `except Exception` is discouraged except for genuinely unpredictable failures (e.g. network).
- **raise** — signal invalid input from inside a function; error propagates to caller.
- **logging module** — levels (DEBUG/INFO/WARNING/ERROR), `basicConfig(level=...)` as a threshold; framed as the mature alternative to `print` for developer-facing output.
- **Defensive programming** — anticipate vs. react. Input validation with `isinstance`/range/emptiness checks; **guard clauses** (early return, flat happy-path); explicit `None` checks before use.
- **Fail loud, not silent** — `except: pass` is banned; always log/print/return-default/re-raise.
- **assert** — for programmer-assumption checks during dev only; noted that `-O` disables it, so not for production/user validation.
- **Graceful degradation** — wrap risky I/O (file reads, network) in `try/except`, return safe defaults (`[]`, `""`), separate risky-work function from display function.
- **pip / venv / requirements.txt** — pip↔PyPI; why global installs cause version-conflict and reproducibility problems; `python3 -m venv .venv`, activate/deactivate, `pip freeze > requirements.txt` and `pip install -r`.

## The assignment — "Errors & Debugging"
Students build four warmups plus a defensive CSV reader, on an `assignment-8` branch in `week-8/assignment-8/`.

- **Warmup 1** (`warmup1.py`) — input loop catching `ValueError` until a valid number is entered.
- **Warmup 2** (`warmup2.py`) — safe division catching `ZeroDivisionError`.
- **Warmup 3** (`warmup3.py`) — open a missing file, catch `FileNotFoundError`.
- **Warmup 4** (`warmup4.py`) — create a venv, `pip install requests`, `pip freeze` into `requirements.txt`, print `requests.__version__`, paste requirements as a comment.
- **Mini-project** (`mini_project.py`) — read `../data/messy_data.csv` with `csv.DictReader`, guard file existence, process each row in try/except catching `ValueError` (bad `amount`) and `KeyError` (missing column), track attempted/parsed/skipped counts, and print a formatted report with per-row skip reasons.
- **Video reflection** (3–5 min) — syntax vs. runtime error example; explain row-by-row (vs. whole-loop) exception handling; demo venv setup and why `requirements.txt` matters. Submit PR link (URL1) + video link (URL2).

## Likely trouble spots
- **Local-env prerequisite (Warmup 4)** — this is the first time students must have a *working* venv on their own machine to install a real package. Activation differs by OS (`source .venv/bin/activate` vs `.venv/Scripts/activate`); Windows students especially get stuck. If their Week 2 setup was shaky, this surfaces now. Note pip/venv are introduced *conceptually* only — expect gaps in mechanics.
- **Broad except / silent swallowing** — students reflexively write `except:` or `except Exception: pass`. Lesson bans it, but old habits persist; watch for it in the mini-project.
- **Mini-project extra-column trap** — `csv.DictReader` puts extra fields under a `None` key rather than raising, so a `KeyError` never fires for extra columns. Hint 2 tells them to check `if None in row` as a *separate guard before* the try/except. Students who rely on catching an exception for this case will miss Row 7-style failures.
- **Row-by-row vs. whole-loop try/except** — the video explicitly probes this; a single try around the whole loop aborts on the first bad row instead of skipping and continuing. Common design mistake.
- **Return-default vs. return-None** — lesson pushes `[]`/`""` over `None` so callers don't branch on type; expect some to return `None` and then crash downstream.
- **assert misuse** — may reach for `assert` on user input; flag that `-O` disables it.
- **Git workflow** — same recurring pitfalls (committing to `main`, missing upstream on first push, PR base pointing at the CTD upstream instead of their fork).
