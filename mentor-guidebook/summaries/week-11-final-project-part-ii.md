# Week 11 — Final Project Part II (Mentor Summary)

## Key concepts taught

- **Structured choice** — students pick ONE extension track that builds on their working Week 10 project (API fetch + `process_data()` + CLI). Both add a meaningful layer; neither is harder, just different work.
- **Option A — Visualization** — introduces `matplotlib` (new library). Build a function that turns processed data into a labeled bar chart answering a specific question, saved as a PNG. Core pattern is ~6 calls: `plt.bar(labels, values)`, `xlabel`/`ylabel`/`title`, `tight_layout()`, `savefig()`. Extract `labels`/`values` from the list-of-dicts via list comprehensions.
- **Option B — Data pipeline** — no new library; reuses `csv.DictWriter` (Week 7). The new work is judgment: a per-field cleaning framework (missing/`None` → `.get()` with sensible default; inconsistent type → `try/except` coercion; invalid/placeholder value → keep-with-default or skip), then export cleaned dicts to a well-structured CSV.
- **Written rationale** — both tracks require a 3–5 sentence `README.md` section explaining *why*, not just *what* (`## Visualization` for A, `## Data Cleaning Decisions` for B).

## The assignment — "Final Project Part II"

Extend the Week 10 project via one of two tracks, both graded on the same rubric.

- **Option A:** at least one `matplotlib` chart answering a stated question; axis labels + descriptive title + readable tick labels; saved `.png`; `## Visualization` write-up (what it shows, main takeaway, why that chart type).
- **Option B:** clean data with the per-field framework (handle missing, normalize types, filter invalid); export via `csv.DictWriter`; sample `.csv`; `## Data Cleaning Decisions` write-up (fields kept/dropped, missing/invalid handling, coercions).
- **Universal (both):** modular design (extension logic in dedicated functions with clear params/returns); at least one standard-library module beyond `csv` (e.g. `os`, `datetime`); version control via PR with incremental commits across *both* weeks (do NOT squash Week 10); a 2–4 min screen-recorded video demo running the project live, showing the deliverable, and explaining one technical decision + one "if I had more time."
- **Submission:** update the Week 10 PR (or new PR from same branch). PR must state chosen option, describe the extension, and include the video link (also in README). Final repo: `main.py`, extra `.py` files, `requirements.txt`, `README.md`, plus the `.png` (A) or `.csv` (B).

## Likely trouble spots

- **Broken Week 10 foundation** — the pre-flight checklist is real. If `fetch_data()`/`process_data()`/CLI aren't working, fix those first; extension code on a broken base is much harder to debug and submit.
- **(A) `savefig()` order** — call `plt.savefig()` *before* `plt.show()`; `show()` clears the figure, so saving after produces a blank PNG.
- **(A) matplotlib install** — `pip install matplotlib` then re-freeze `requirements.txt`. Steer students to run the standalone fake-data example before wiring in real data.
- **(A) unlabeled / cluttered charts** — missing axis labels or a title that doesn't state the question loses points. Long overlapping category labels need `plt.xticks(rotation=45, ha="right")`.
- **(A) mixing concerns** — filtering/transforming inside the viz code instead of relying on `process_data()`. Keep chart code to extract-and-plot.
- **(B) `.get()` defaults** — students crash on missing keys via direct indexing; nudge toward `.get(key, default)` with a field-appropriate default they can justify in the write-up.
- **(B) type coercion crashes** — `int()`/`float()` on `None`, `""`, or `"N/A"` raises; the conversion must be wrapped in `try/except (ValueError, TypeError)`.
- **(B) CSV formatting** — forgetting `newline=""` in `open()` (blank rows on Windows), missing `writeheader()`, or empty record list. Fieldnames come from `records[0].keys()`, so all cleaned dicts must share the same keys.
- **(B) description vs. decision** — the write-up must reflect genuine reasoning (why keep vs. skip, why this default), not narrate the code. This is the Meets/Exceeds line.
- **Both: standard-library requirement** — easy to forget the "one module beyond `csv`" rule; `datetime` for a timestamp or `os.path` for output paths is the natural fit.
- **Both: commit history** — single-commit dumps and squashed Week 10 history fail the version-control criterion; remind them to commit incrementally across the two weeks.
