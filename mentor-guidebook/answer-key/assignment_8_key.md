# Assignment 8 Answer Key — Errors and Debugging

## File Setup

- Forked `python-intro-homework` repo → `assignment-8` branch off `main` → work in `week-8/assignment-8/`.
- Files expected: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py` (plus `requirements.txt`).
- **URL1** = PR link (`assignment-8` → `main`, into their own fork); URL2 = video (not assessed).

---

## Warmup 1: Validate Numeric Input (`warmup1.py`) — **Objective**

Loop asking for input; catch `ValueError` from `float()`/`int()`, reprint prompt; break on success.

Expected output:
```
Enter a number: hello
That's not a valid number. Try again.
Enter a number: abc
That's not a valid number. Try again.
Enter a number: 42
You entered: 42.0
```

**Correct if:** `try`/`except ValueError` wraps the conversion; invalid input reprompts instead of crashing; a valid number is printed and the loop stops. (`42.0` implies `float()` — `int()` printing `42` is also acceptable.)
**Common miss:** conversion left outside the `try`; bare `except:` or `except Exception:` instead of `ValueError`; no loop (only one retry); `input` itself inside the `except`.

---

## Warmup 2: Safe Division (`warmup2.py`) — **Objective**

Read two numbers, divide, catch `ZeroDivisionError`.

Expected output:
```
Enter the numerator: 10
Enter the denominator: 0
Can't divide by zero — please try a non-zero denominator.
```
```
Enter the numerator: 10
Enter the denominator: 4
10.0 ÷ 4.0 = 2.5
```

**Correct if:** division wrapped in `try`/`except ZeroDivisionError`; zero denominator prints a friendly message instead of a traceback; valid case prints the quotient.
**Common miss:** catching the wrong/overly broad exception; message wording differs (fine — judge behavior, not text); crashes on non-numeric input (not required to handle, but a `ValueError` guard is a plus, not a penalty).

---

## Warmup 3: Handle a Missing File (`warmup3.py`) — **Objective**

Attempt to open `../data/missing.txt`; catch `FileNotFoundError`.

Expected output:
```
Error: "missing.txt" was not found. Please check the file path and try again.
```

**Correct if:** `open()` wrapped in `try`/`except FileNotFoundError`; prints a helpful message, no traceback.
**Common miss:** catching `IOError`/`OSError`/`Exception` broadly (acceptable but less precise); reads the file inside `try` but prints error outside the `except`; forgetting the file is intentionally absent and "fixing" it by creating it.

---

## Warmup 4: Virtual Environment Setup (`warmup4.py`) — **hybrid (Objective output / Subjective setup)**

Create a venv, `pip install requests`, `pip freeze > requirements.txt`, import `requests`, print its version. `requirements.txt` contents pasted as a top comment.

Expected output (version will vary by install date):
```
requests version: 2.31.0
```

**Correct if:** script imports `requests` and prints `requests.__version__`; a `requirements.txt` comment block is present and includes `requests` plus its transitive deps (`certifi`, `charset-normalizer`, `idna`, `urllib3`). Exact version numbers will differ from the sample — do not penalize newer versions.
**Common miss:** hardcoding the version string instead of reading `requests.__version__`; `requirements.txt` missing or lacking the dependency pins; committing the `.venv/` folder into the PR (should be gitignored).

**Env gotchas:** the printed version must match the pin in their `requirements.txt`; a mismatch suggests they froze before installing or ran outside the activated venv. A `requirements.txt` with only `requests==...` (no transitive deps) means `pip freeze` wasn't actually used.

---

## Part 2: Mini-Project — Defensive CSV Reader (`mini_project.py`) — **hybrid (Subjective structure / Objective behavior)**

Reads `../data/messy_data.csv` with `csv.DictReader`, processes each row in its own `try`/`except`, collects clean rows, prints a summary. Counts below are exact for the shipped file (14 rows → 9 parsed, 5 skipped); the core skill being graded is the row-by-row handling, not exact wording.

Required behavior:
- File existence guarded with `try`/`except FileNotFoundError`; prints an error and stops if missing.
- `csv.DictReader` used to read rows.
- Each row processed in its own `try`/`except` catching at minimum `ValueError` (bad `float(amount)`) and `KeyError` (missing column).
- Extra-column rows guarded separately: `None in row` check (DictReader stores overflow fields under the `None` key rather than raising) — see Hint 2.
- Successful rows collected into a list of dicts.
- Summary printed: rows attempted / parsed / skipped, a list of skipped rows with reasons, and the clean data.

Expected summary for the shipped file:
```
=== CSV Report ===
Rows attempted:  14
Rows parsed:      9
Rows skipped:     5

Skipped rows:
  Row 3: ValueError — could not convert '' to float
  Row 5: ValueError — could not convert 'not_a_number' to float
  Row 7: extra column detected — skipped
  Row 11: ValueError — could not convert '' to float
  Row 13: ValueError — could not convert 'fifteen' to float

Clean data:
  Alice | Food | $12.50
  Bob | Transport | $8.75
  David | Utilities | $45.00
  Frank | Transport | $22.30
  Hana | Utilities | $88.00
  Ivan | Food | $6.40
  Jess | Transport | $14.20
  Lena | Food | $9.80
  Nina | Utilities | $33.60
```
The 5 skips are: Carol & Karl (empty amount), Eve (`not_a_number`), Marco (`fifteen`), and Grace (extra column — amount `15.00` is valid, but the trailing `extra_field` lands under the `None` key). Grace is the one caught by the `None in row` guard rather than the `try/except`. **Row numbers depend on how the student enumerates** — the assignment's `3/5/7/11/13` assumes `enumerate(reader, start=1)`; a `start=0` or header-counting choice shifts them. Grade the counts and reasons, not the exact indices.

**Grade on:**
- Row-by-row try/except (per-row, not one block around the whole loop) so one bad row doesn't abort the rest — this is the core skill being assessed.
- Specific exceptions caught (`ValueError`, `KeyError`), not a bare `except:`.
- The `None in row` guard for extra columns (or an equivalent field-count check). Missing this is the most common defect since DictReader won't raise on it.
- Counts are internally consistent (attempted = parsed + skipped) and skipped rows report a reason.

**Common miss:** single `try`/`except` wrapping the entire loop (one bad row ends processing); no `None`-key guard for extra columns; catching `Exception` broadly and hiding real bugs; `enumerate()` row numbers off by one (header row) — minor, note but don't fail; not stopping cleanly when the file is absent.
