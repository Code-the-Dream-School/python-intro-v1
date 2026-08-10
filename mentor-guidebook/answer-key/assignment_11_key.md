# Assignment 11 Answer Key — Final Project Part II

## File Setup

- Forked `python-intro-homework` repo. Week 11 continues on the **same feature branch as Week 10** — the assignment names `week-10-final-project` (there is no new `week-11` branch). Students update the Week 10 PR or open a fresh PR from that same branch. **URL1** = PR link; URL2 = video (not assessed).
- Combined commit history across both weeks should show incremental progress; Week 10 commits must **not** be squashed.
- Student does **ONE** track, not both. The PR description states which (A or B).
- Repo must contain `main.py`, any other `.py` files, `requirements.txt`, `README.md`, and the track deliverable: a `.png` (Option A) **or** a sample `.csv` (Option B).
- Extension is built on the Week 10 project — output varies by student's chosen API. Grade on structure and correctness, not exact values.

---

## Universal Requirements — apply to BOTH tracks

**Modular design — Subjective**

**Passing:** extension logic lives in dedicated function(s) with clear parameters and return values, separate from Week 10 code (e.g. a `make_chart()` / `clean_data()` / `export_to_csv()` function called from `main.py`).
**Failing:** extension logic dumped inline into an existing function or written as one top-level script block with no reusable function.

**Standard library beyond `csv` — Objective**

**Correct if:** at least one standard-library module *other than* `csv` is imported and actually used for something real (`os`/`os.path` for file paths, `datetime` for timestamps, etc.). `matplotlib` is third-party and does **not** satisfy this.
**Common miss:** importing a module but never using it; assuming `csv` (Option B) or `matplotlib` (Option A) counts — neither does. Option A students in particular often forget this rule since their track adds no stdlib naturally.

**Version control — Subjective**

**Passing:** multiple commits across the two weeks, submitted via PR.
**Failing:** all extension work in a single commit, or Week 10 history squashed away.

---

## Option A — Visual Analysis (Matplotlib)

*Grade this section only if the student chose Option A.*

**Chart renders and answers a stated question — Objective**

**Correct if:** running the project produces a saved **PNG** file, and the chart visualizes a specific question the student poses about their data (e.g. "Top 10 countries by population"). The chart must be built from the project's already-processed data, not hardcoded lists.
**Common miss:** no PNG saved (only `plt.show()`); `plt.savefig()` called *after* `plt.show()`, producing a blank image; chart still using the lesson's fake `["Category A", ...]` data.

**Chart type fits the data question — Subjective**

**Passing:** chart type suits categorical-vs-count data (a bar chart is the taught/expected default and is fine).
**Failing:** a chart type that misrepresents the data for the stated question (e.g. a line chart implying continuity across unordered categories).

**Labeling and readability — Subjective**

**Passing:** descriptive title (states the question), x- and y-axis labels (units where relevant), readable tick labels; long/overlapping labels rotated (`plt.xticks(rotation=...)`) or `tight_layout()` used.
**Failing:** unlabeled axes, no/generic title, or tick labels cut off or overlapping into unreadability.

**README `## Visualization` section — Subjective**

**Passing:** 3–5 sentences covering what question the chart answers, the main takeaway, and why that chart type. (Written deliverable — assess it lives here, but the video rationale itself is not graded.)
**Failing:** section missing, or a bare description of the code with no takeaway or type justification.

---

## Option B — Data Pipeline (CSV export)

*Grade this section only if the student chose Option B.*

**Produces a well-structured CSV via `csv` module — Objective**

**Correct if:** running the project writes a **CSV** file using `csv.DictWriter` (or `csv.writer`) with a header row (`writeheader()`) and consistent columns per record. Cleaning happens in a dedicated function; export is separate.
**Common miss:** hand-building CSV with string joins/`print` instead of the `csv` module; no header row; `open(..., newline="")` omitted (blank lines between rows on some platforms).

**Data cleaning handles edge cases — Subjective**

**Passing:** applies the per-field framework — missing keys via `.get()` with sensible defaults, type coercion wrapped in `try/except (ValueError, TypeError)`, and invalid records either filled with a documented default or filtered out before writing. Original records not mutated.
**Failing:** direct `record["key"]` access that will `KeyError` on missing fields; no type handling where the API returns inconsistent types; bad/empty/`"N/A"` records written through unchanged.

**CSV structure and headers — Objective**

**Correct if:** every row has the same fields in the same order, headers match the dict keys, and only the intended fields are exported (nested dicts/lists flattened or dropped, not written raw).
**Common miss:** raw nested dict/list dumped into a cell; header row missing or not matching keys.

**README `## Data Cleaning Decisions` section — Subjective**

**Passing:** 3–5 sentences covering which fields were included/excluded, what was done with missing/invalid values (skip vs. default), and any type coercion. Reflects genuine decisions, not a code walkthrough.
**Failing:** section missing, or restates the code without explaining the choices.
