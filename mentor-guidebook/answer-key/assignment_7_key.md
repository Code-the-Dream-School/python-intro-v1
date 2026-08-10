# Assignment 7 Answer Key — Text Data and Modules

## File Setup

- Forked `python-intro-homework` repo, `assignment-7` branch, work in a `week-7/assignment-7/` folder. PR from `assignment-7` into `main`. **URL1** = PR link; URL2 = video (not assessed).
- Six files expected: `warmup1.py`–`warmup4.py`, `mini_project.py`, and the generated `food_report.txt`.
- Data files (provided in `week-7/data/`, referenced as `../data/...`): `notes.txt`, `students.csv`, `expenses.csv`. These are not in the student's folder — paths use `../data/`.
- `argparse` and `try/except` are **deferred**. File-existence guarding is done with `os.path.exists()`, not exception handling. Flag a student who wraps `open()` in `try/except` — not wrong, but ahead of the curriculum; the intended tool is `os.path.exists()`.

---

## Warmup 1: Read a Text File Line by Line — **Objective**

`with open('../data/notes.txt')`, iterate, `.strip()`, print numbered lines:

```
Line 1: Python is great for working with files.
Line 2: You can read, write, and append text.
Line 3: The 'with' statement keeps things clean.
Line 4: Always close your files when you're done.
```

**Correct if:** uses a `with` block, strips the trailing newline, and prepends a line number.
**Common miss:** no `.strip()` → blank lines between rows (double-spaced output); manual line counter off by one, or `enumerate` starting at 0.

## Warmup 2: Read a CSV with DictReader — **Objective**

`csv.DictReader` on `../data/students.csv`; print `name` and `score`:

```
Jazmine: 88
Luis: 74
Sara: 91
Marcus: 83
Priya: 95
```

**Correct if:** uses `csv.DictReader` and accesses fields by key (`row['name']`, `row['score']`).
**Common miss:** using `csv.reader` and indexing by position (or forgetting to skip the header, so a `name: score` header row prints). Scores are strings — fine here since no math is done.

## Warmup 3: Use the os Module — **Objective**

Three prints in one script:

```
/absolute/path/to/assignment-7        # from os.getcwd(), student-specific
expenses.csv found.
../data/expenses.csv
```

**Correct if:** all three run — `os.getcwd()`, an `os.path.exists('../data/expenses.csv')` check printing the found/not-found message, and `os.path.join('..', 'data', 'expenses.csv')`.
**Common miss:** hard-coding the "found" message instead of branching on `os.path.exists()`; building the join path by string concatenation instead of `os.path.join()`. The exact `getcwd()` output is machine-specific — don't grade its value.

## Warmup 4: Use the datetime Module — **Objective**

`datetime.now()` + `.strftime("%B %d, %Y")`:

```
Today is April 24, 2026.
```

(Date will match the day they ran it.)

**Correct if:** uses `.strftime` with full month name (`%B`), numeric day, four-digit year, wrapped in the sentence with trailing period.
**Common miss:** manual date string; wrong format codes (`%m`/`%M` mix-up, `%y` two-digit year). A zero-padded day (`April 04`) is acceptable.

## Part 2: Mini-Project — Expense Report Generator — **Objective** (with minor subjective formatting)

Guard with `os.path.exists()`, read `../data/expenses.csv` with `csv.DictReader` into a list of dicts, cast `amount` to `float`, filter to `category == "Food"`, sum, and write `food_report.txt`:

```
Food Expense Report — generated August 10, 2026
2024-03-01: $54.3
2024-03-03: $8.75
2024-03-05: $42.0
2024-03-07: $67.2
2024-03-09: $13.4
Total: $185.65
```

(From the shipped `expenses.csv`: five Food rows, total **$185.65**. The generated-date line reflects the run day. Per-line amounts show as raw floats — `$54.3` not `$54.30` — unless the student applies `:.2f`; see the per-line trap below.)

**Correct if:** existence check happens **before** opening; rows read via `DictReader`; `amount` converted with `float()`; only `Food` rows written; total computed (not hard-coded) and formatted to 2 decimals (`:.2f`).

**Common miss:**
- **Per-line amount trap:** printing the raw float gives `$54.3`, not `$54.30`. The header/total spec forces 2 decimals on the total; a careful student also formats each line with `:.2f`. Accept either, but note if line amounts drop trailing zeros.
- Filtering on the string before casting is fine; forgetting `float()` → `TypeError` or string-concatenated "sum".
- **`None`-key / extra-column trap:** `expenses.csv` has a `description` column the report ignores. If a student uses `csv.reader` with positional indexes and miscounts columns, `amount` (index 3) gets misread. With `DictReader`, a trailing blank line in the CSV yields an empty/`None`-valued row — casting `float(None)`/`float('')` will crash; a robust solution skips empties. Watch for this if the file ends with a newline.
- No existence guard, or opening the file first and only then checking.

**Formatting (subjective):** exact spacing, em-dash vs hyphen in the header, and whether the report ends with a newline are free — accept any clean, readable layout matching the three-part structure.

**Extension (ungraded):** generalizing to any category (e.g. `transport_report.txt`) is optional — do not weight it.
