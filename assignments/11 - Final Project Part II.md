# Assignment 11 — Final Project Part II

## Universal Requirements

These apply no matter which extension track you choose.

- **Modular design:** All extension logic in reusable functions with clear parameters and return values
- **Standard library usage:** Use at least one standard library module beyond `csv` (e.g., `os`, `datetime`)
- **Version control:** All work committed and submitted via pull request; commit history shows incremental progress across both weeks
- **Video demo:** A screen-recorded video (2–4 min) walking through your running project and explaining one technical decision you made

---

## Option A Requirements — Visualization (choose Option A or Option B, not both)

- Use `matplotlib` to create at least one chart that answers a specific question you pose about your data
- Label your chart: axis labels, a descriptive title, and readable tick labels
- Save the chart as a PNG file
- Include a written explanation in `README.md` (under `## Visualization`) describing what the chart shows, what the main takeaway is, and why you chose that chart type

## Option B Requirements — Data Cleaning (choose Option A or Option B, not both)

- Clean the data: handle missing values, normalize field types, and filter invalid records, deciding field by field how to handle each problem and recording those decisions in your README
- Export the cleaned data to a well-structured CSV file using `csv.DictWriter`
- Include a written explanation in `README.md` (under `## Data Cleaning Decisions`) describing which fields you included, what you did with missing or invalid values, and any type coercion applied

---

## Submission

**Required files**

Your final repository must include:

- `main.py` — the entry point for your CLI tool
- Any additional `.py` files you created
- `requirements.txt` — all third-party packages used
- `README.md` — complete with project description, API used, how to run, CLI interactions, extension track, written explanation (Visualization or Data Cleaning Decisions section, depending on your track), and your video demo link
- **Option A only:** the chart saved as a `.png` file
- **Option B only:** a sample exported `.csv` file

**Pull request**

Update your pull request from Week 10 (or open a new one from your same feature branch, depending on your class workflow). Your PR description should:

- Confirm which option you chose (A or B)
- Briefly describe what the extension adds to the project
- Include your video demo link

Your combined commit history across both weeks should show incremental progress. Do not squash your Week 10 commits.

**Video Demo**

Record a 2–4 minute video showing your completed project. Include the link in your PR description and in your `README.md`.

Your video should address:

1. Run the complete project from `main.py` entry to output — show it working live.
2. Show the extension deliverable (your chart or your CSV file) and explain one decision you made while building it.
3. If you had more time, what would you add or improve?

Requirements:
- 2–4 minutes
- Show your running program on screen — don't just describe it
- Speak in your own words

Upload to YouTube (unlisted) or Loom.

---

## Guidelines

> Note that these guidelines are for Part II. The full final project guidelines are in the [Final Project Overview](https://github.com/Code-the-Dream-School/intro-to-python-v1/blob/main/resources/final-project-overview.md).

| Category | Does Not Meet | Meets | Exceeds |
|---|---|---|---|
| **Extension Track** | Extension not attempted, or broken and does not run. | Extension requirements met: chart answers a stated question with appropriate labels (A), or CSV exported with cleaned data and written explanation (B). | Chart is polished and well-labeled (A), or data cleaning handles multiple edge cases with clear reasoning (B). Written explanation reflects genuine decision-making, not just a description of the code. |
| **Modular Design** | Extension logic mixed into existing functions or written as one monolithic block. | Extension logic is in dedicated functions with clear parameters and return values. | Functions are well-named and single-purpose. The extension integrates cleanly with the Week 10 codebase. |
| **Standard Library** | No standard library module used beyond `csv`. | At least one standard library module used appropriately. | Standard library usage is well-chosen and adds real value (e.g., `datetime` for timestamps, `os.path` for file handling). |
| **Version Control** | All extension work in a single commit. | Multiple commits show incremental progress. Work submitted via pull request. | Commit messages are descriptive and reflect meaningful stages of development across both weeks. |
| **Video Demo** | No video submitted, or video does not show the running program. | 2–4 minute video walks through the running project and explains one technical decision. | Technical explanation goes beyond what the code says to *why* the decision was made. |

## Need a GitHub Review?

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

## Review: The GitHub Cycle

This is your repeatable workflow. This week you continue on the same feature branch you created in Week 10 (`week-10-final-project`), so you do not create a new one. Use that branch name in every command below, unless your class workflow uses a different one.

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout week-10-final-project   # your existing branch from Week 10
```

`origin` is your fork. `git pull origin main` syncs your local main with your fork on GitHub; it's normal to see "Already up to date."

**Save your progress:**

```bash
git status                            # see what's changed (run this often)
git add .                             # stage all changes
git commit -m "describe what you did and why"
git push origin week-10-final-project # send your branch to GitHub
```

Repeat `add → commit → push` as often as you like. Committing often gives you more points to return to if something goes wrong.

**Open your pull request:**

On GitHub, open a pull request from `week-10-final-project` into main. Confirm the base repository is your own fork (`your-username/python-intro-homework`), not `Code-the-Dream-School`.

**Close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

**If something looks off:**

* Committed to main by accident? (You forgot to switch to your project branch first.) If you have not made the branch yet, `git checkout -b week-10-final-project` carries your latest commits with it. If the branch already exists from Week 10, switch to it with `git checkout week-10-final-project` and ask your CIL for help moving those commits. Your work isn't lost either way.
* `git push` says your branch has "no upstream"? You haven't pushed this branch before. Run `git push origin week-10-final-project` to create it on your fork.
</details>

## 🎉 Congrats on submitting your Python Intro final project!

The foundational work you've put in during this class is going to make you a strong developer!

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

This is **Part II of a two-week final project** — the extension week. **The student
chooses ONE extension track: Option A (visualization) or Option B (data cleaning).**
The two are alternatives, not a combined checklist. A student who completed Option A
must NOT be failed for anything in Option B, and vice versa. Check the PR description
or `README.md` to see which track they chose, then grade only that track's
requirements. Doing both is not expected and earns no penalty either way.

`Example — adapt to your own layout`: the repo layout is not specified — the required
files may sit at the repo root, in a `week-11/` folder, or in a project folder of the
student's choosing, and the chart or CSV may be saved anywhere. Do NOT fail correct work
over file locations; the reviewer cannot see the student's filesystem. The Git workflow
reference at the bottom of the page uses `week-10-final-project`, the Week 10 feature
branch, but this assignment says to reuse it "depending on your class workflow" — so do
not require any particular branch name, and never expect an `assignment-11` branch.
Submission mechanics and
commit history are not gradable from the code itself.

**This week's diff contains both weeks' work.** The assignment tells students to update
their Week 10 pull request from the same branch and explicitly not to squash their Week
10 commits, so Week 10's `main.py`, its API fetching and parsing, and its CLI are all
expected to be present. That earlier code is **not re-graded here** — do not fault its
quality, do not treat it as stray or duplicated, and never tell the student to remove or
squash it. Grade the extension that Part II adds. The student also chose their own
public API in Week 10, so the reviewer cannot know the response structure, field names,
or output values — grade structure and behavior, never the data.

- **Universal — Modular design** — the extension logic lives in reusable functions with
  clear parameters and return values, not inlined into existing code or written as one
  block. `Example — adapt to your own layout`: function names and how the work is split
  are the student's own.
- **Universal — Standard library usage** — **at least one** standard library module
  beyond `csv` is used (the assignment names `os` and `datetime` as examples). One is
  sufficient; do not expect several, and do not require a specific module — any
  appropriate standard library module counts.
- **Universal — Version control** — the work is committed and submitted via pull
  request, with more than a single commit. Not gradable from the code itself.
- **Universal — Video demo** — a 2–4 minute screen recording of the running project
  that explains one technical decision, linked in both the PR description and the
  `README.md`. The video is not assessed here; do not fail the code submission for
  anything about it.
- **Option A (only if the student chose A) — Visualization** — `matplotlib` is used to
  build **at least one** chart that answers a question the student poses about their
  data; the chart has axis labels, a descriptive title, and readable tick labels; it is
  saved as a `.png` file that is committed; and `README.md` contains a `## Visualization`
  section explaining what the chart shows, the main takeaway, and why that chart type was
  chosen. Required: one chart, the three labeling elements, the saved PNG, and all three
  parts of the written explanation. `Example — adapt to your own layout`: the question
  asked, the chart type, the styling, the filename, and where the PNG is saved. `Use
  exactly as written`: `matplotlib`, and the `## Visualization` heading in the README —
  though do not fail a different heading level if the section is clearly present.
- **Option B (only if the student chose B) — Data Cleaning** — missing values are
  handled, field types are normalized, and invalid records are filtered, with a
  field-by-field decision for each problem; the cleaned data is exported to a
  well-structured CSV using `csv.DictWriter`; a sample exported `.csv` is committed; and
  `README.md` contains a `## Data Cleaning Decisions` section describing which fields
  were included, what was done with missing or invalid values, and any type coercion
  applied. `Use exactly as written`: `csv.DictWriter` (not `csv.writer` or manual string
  joining), and the `## Data Cleaning Decisions` heading — again, do not fail a different
  heading level if the section is clearly present. `Example — adapt to your own layout`:
  which fields were kept, every cleaning decision made, the CSV's column set, and the
  filename.
- **`main.py`** — still the entry point, carried forward from Week 10. `Use exactly as
  written`: the filename.
- **Additional `.py` files** — any extra modules the student created are expected and
  welcome. Do not fault extra files, and do not require them either.
- **`requirements.txt`** — lists the third-party packages used. Option A students should
  have `matplotlib` listed. `Example — adapt to your own layout`: the package list and
  all version numbers.
- **`README.md`** — includes the project description, the API used, how to run it, the
  CLI interactions, which extension track was chosen, the track's written explanation
  section, and the video demo link. Required: all seven pieces. `Example — adapt to your
  own layout`: wording, structure, and length.

### Optional Deliverables/Tasks

Everything in the rubric table's **Exceeds** column is above the passing bar. A
submission that fully "Meets" every row is complete and correct. **Do not fail, or mark
down, a student for omitting any of the following:**

- **A polished chart** beyond the required labels (A), or **cleaning that handles
  multiple edge cases** with extended reasoning (B).
- **A written explanation that reflects genuine decision-making** rather than describing
  the code. The explanation is required; its depth is not.
- **Well-named, single-purpose functions** and an extension that **integrates cleanly**
  with the Week 10 codebase. Dedicated functions with clear parameters and return values
  are the requirement.
- **Standard library usage that "adds real value"** (the table's example: `datetime` for
  timestamps, `os.path` for file handling). Any appropriate module meets the bar.
- **Descriptive commit messages** spanning both weeks. Multiple commits are required;
  their wording is not.
- **A technical explanation in the video that goes beyond the code to the "why."**

</details>
