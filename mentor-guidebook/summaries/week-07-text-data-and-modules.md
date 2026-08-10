# Week 7 — Text Data and Modules (Mentor Summary)

## Key concepts taught

- **File I/O with `open()`** — `"r"`/`"w"`/`"a"` modes; **`with` block** framed as auto-closing (and previewed as the same pattern for later DB connections). `"w"` overwrites, `"a"` appends; `write()` adds no newline.
- **Reading text** — `.read()` (whole file), iterate line-by-line, or `.readlines()`; `.strip()` to drop trailing `\n`.
- **`csv` module** — `csv.reader` (rows as lists, manual `next()` to skip header) vs. `csv.DictReader` (rows as dicts keyed by header). Also `csv.writer`/`DictWriter` with `newline=''`.
- **Parsing to list-of-dicts** — the `file → structured data → useful output` pipeline: `list(csv.DictReader(f))`, then convert, filter (list comps), aggregate. Connects back to Week 5 lists/dicts.
- **All CSV values are strings** — must `float()`/`int()` explicitly before math. Hammered in both lesson and CFU.
- **Standard library tour** — import styles (`import`, `from ... import`, `as`); `os` (`getcwd`, `path.exists`, `path.join`, `listdir`), `datetime` (`.now()`, `.strftime()` codes, `strptime`), plus a mention of `math`/`random`. Emphasis on reading the official docs.
- **`argparse`** — introduced but explicitly optional (final-project only); parser → `add_argument` → `parse_args` pattern.
- **When to import vs. write your own** — three-tier mental model: stdlib first → vetted PyPI package → roll your own; how to evaluate a PyPI package (activity, downloads, docs, license).

## The assignment — "Expense Report Generator"

Four warmups plus a mini-project; data files live in `week-7/data/`, referenced from `assignment-7/` via `../data/filename`.

- **Warmup 1** (`warmup1.py`) — read `notes.txt` line-by-line in a `with` block, print `Line N:` with `.strip()`.
- **Warmup 2** (`warmup2.py`) — `csv.DictReader` on `students.csv`; print `name: score`.
- **Warmup 3** (`warmup3.py`) — `os`: `getcwd()`, `path.exists()` check, `path.join()` to rebuild the data path (previews mini-project).
- **Warmup 4** (`warmup4.py`) — `datetime.now()` + `.strftime()` to print `Today is Month DD, YYYY.`
- **Mini-project** (`mini_project.py` + committed `food_report.txt`) — verify `expenses.csv` exists → read to list-of-dicts → cast `amount` to `float` → filter to `Food` → total → **write** a formatted report (header w/ today's date, one line per expense, `Total:` to 2 decimals). Optional ungraded extension: parameterize by any category.
- **Video reflection** (3–5 min): what `with open(...)` does, walkthrough of CSV→list-of-dicts, and one import-vs-write-your-own decision from the project. Submit PR link (URL1) + video link (URL2) in CTD Learns.

## Likely trouble spots

- **Strings from `DictReader`** — the central trap; forgetting `float(row['amount'])` before summing throws `TypeError` (or concatenates). The mini-project depends on getting this right.
- **Relative paths** — `../data/...` is relative to where the script *runs*, not where it lives. Running from the repo root instead of `assignment-7/` breaks `path.exists()` and quietly makes the mini-project exit early with the "not found" branch. Point them at `os.getcwd()` to diagnose.
- **`"w"` clobbers** — re-running the report or a warmup with `"w"` silently destroys prior content; the AI-prompt exercise leans on this but some won't connect it.
- **`write()` needs explicit `\n`** — reports come out as one mashed line without it.
- **`strftime` codes** — `%B %d, %Y` vs. muscle-memory formats; expect date-format fiddling in Warmup 4 and the report header.
- **Deferred: exception handling** — `try/except` is shown for file errors but explicitly "learn more later" (Week 8). The assignment uses `os.path.exists()` as the guard instead of catching exceptions; some students will reach for `try/except` prematurely.
- **`argparse`** — optional and only lightly explained; ambitious students may attempt it in the mini-project and stall on the setup boilerplate. Steer them to the simpler category-loop for the extension.
- **PR link vs. repo link** — recurring submission error: students submit the repo homepage instead of the actual PR URL.
