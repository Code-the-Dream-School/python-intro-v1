# Assignment 8 — Errors & Debugging

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-7` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-8` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-8/`, create a new `assignment-8/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-8` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file. Data files for this week are in the `week-8/data/` folder — reference them from your `assignment-8/` working directory using the path `../data/filename`.

---

### Warmup 1: Validate Numeric Input

Write a loop that asks the user to enter a number. If they enter something that can't be converted to a number, catch the `ValueError` with `try`/`except`, print a message, and ask again. Once you have a valid number, print it and stop. The example session below shows the format — your inputs and message wording might differ:

```
Enter a number: hello
That's not a valid number. Try again.
Enter a number: abc
That's not a valid number. Try again.
Enter a number: 42
You entered: 42.0
```

**Save as:** `warmup1.py`

---

### Warmup 2: Safe Division

Ask the user for two numbers. Compute the result of dividing the first by the second. Use `try`/`except ZeroDivisionError` to catch division by zero and print a friendly message instead of crashing. The example sessions below show the format for two different inputs — your numbers and message wording might differ:

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

**Save as:** `warmup2.py`

---

### Warmup 3: Handle a Missing File

Write a script that attempts to open `../data/missing.txt` (this file does not exist). Use `try`/`except FileNotFoundError` to catch the error and print a helpful message rather than a traceback. The example below shows the format — your message wording might differ:

```
Error: "missing.txt" was not found. Please check the file path and try again.
```

**Save as:** `warmup3.py`

---

### Warmup 4: Virtual Environment Setup

Set up a virtual environment for your project, install the `requests` library, and generate a `requirements.txt` with `pip freeze`. Then write a short script that imports `requests` and prints its version. Paste the contents of your `requirements.txt` as a comment at the top of the file. The example below shows the format — your package list and version numbers will differ depending on when you install:

```python
# requirements.txt contents:
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.6
# requests==2.31.0
# urllib3==2.2.1
```

Example output — your version number will differ:

```
requests version: 2.31.0
```

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Defensive CSV Reader

The file `../data/messy_data.csv` contains a mix of valid and invalid rows. Each row should have three fields — `name`, `category`, and `amount` — but some rows have problems: missing values, non-numeric amounts, or extra columns.

Write a script that reads this file defensively and produces a clean summary. Your program must:

1. Wrap the file opening in `try`/`except FileNotFoundError`. If the file is missing, print an error message and stop.
2. Read the file with `csv.DictReader`.
3. Process each row inside a `try`/`except` block. Catch at minimum:
   - `ValueError` — when `amount` can't be converted to `float`
   - `KeyError` — in case a row is missing an expected column. Include this clause even if it never runs while you test: `csv.DictReader` usually fills a missing column with `None` instead of raising, so a `KeyError` may not come up with this data. Catching it is still good defensive practice.
4. Collect successfully parsed rows into a list of dictionaries.
5. Print a summary at the end:

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
  ...
```

> **Hint 1:** You can track skipped rows by storing a description of each failure, then printing them at the end. Use `enumerate(reader, start=1)` to get row numbers as you loop, so your first data row is row 1 like the example above.

> **Hint 2:** `csv.DictReader` handles extra fields by storing them under a `None` key rather than raising an exception, so you will need to check if `None in row` as a separate guard before the `try/except`. 

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is the difference between a syntax error and a runtime error? Give one example of each from your experience this week.
2. Walk through your row-by-row error handling in the mini-project. What exception are you catching, and why does catching it row-by-row (rather than once around the whole loop) matter?
3. Show your virtual environment setup and explain why `requirements.txt` matters when sharing or submitting code.

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

---

## Need a GitHub Review?

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-8`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-8
```

`origin` is your fork. `git pull origin main` syncs your local main with your fork on GitHub; it's normal to see "Already up to date."

**Save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-N  # send your branch to GitHub
```

Repeat `add → commit → push` as often as you like. Committing often gives you more points to return to if something goes wrong.

**Open your pull request:**

On GitHub, open a pull request from `assignment-N` into main. Confirm the base repository is your own fork (`your-username/python-intro-homework`), not `Code-the-Dream-School`.

**Submit your assignment:**

Use the button on the bottom of your lesson page to submit the link to your pull request.

**Close the loop:**

Assignment successful? You can merge your Pull Request.  

Assignment needs revisions?  Make your corrections on your local branch, and be sure to add, commit, and push them.  No need for a new pull request, when you push the changes your open pull request will reflect those new changes.  Resubmit your work the same way you first submitted - same pull request link too! - and you should see success.  

Problems?  Remember to connect with 1:1 mentors if you are experiencing any trouble with this GitHub Cycle.

Once you merge your pull request, be sure your local `main` branch also gets updated by running the following locally in your terminal:

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

**If something looks off:**

* Committed to main by accident? (You forgot to create your branch first.) Make the branch now: `git checkout -b assignment-N` carries your latest commits with it, then continue. Your work isn't lost.
* `git push` says your branch has "no upstream"? You haven't pushed this branch before. Run `git push origin assignment-N` to create it on your fork.
</details>

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

Work happens in the student's forked `python-intro-homework` repo, on an
`assignment-8` branch, with files inside a `week-8/assignment-8/` folder, reading
the provided data files in `week-8/data/` (reached as `../data/<filename>` from the
working folder). `Example — adapt to your own layout`: the folder path and
repo location are organizational conventions — do NOT fail correct code for
sitting in a different folder or path; the reviewer cannot see the student's
filesystem. **Any path form is acceptable** as long as the right file is opened.
Do not fail a path, and do not fail anything that depends on seeing the provided
data files, since the reviewer cannot read them. Submission mechanics (branch, PR
base) are not graded from the code. This repo is cumulative — folders from earlier
weeks are expected to remain; do not tell the student to remove prior-week work.
Expected files: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`,
`mini_project.py`.

- **Warmup 1 — Validate Numeric Input** — a loop that asks for a number, catches
  `ValueError` with `try`/`except` when the input cannot be converted, prints a
  message, and asks again, stopping once a valid number is entered. Required,
  because the assignment states each one: `try`/`except` catching `ValueError`
  specifically, a loop that repeats on bad input, and the value printed at the
  end. `Example — adapt to your own layout`: the sample inputs (hello, abc, 42),
  all prompt and message wording, and whether the result prints as `42.0` or `42`
  — grade the behavior, not the strings.
- **Warmup 2 — Safe Division** — asks for two numbers, divides the first by the
  second, and catches `ZeroDivisionError` with `try`/`except` so a zero
  denominator prints a message instead of crashing. `Use exactly as written`:
  `except ZeroDivisionError` (not a bare `except`). `Example — adapt to your own
  layout`: the sample numbers, the `÷` symbol, and all message wording are the
  student's own.
- **Warmup 3 — Handle a Missing File** — attempts to open a file that does not
  exist and catches `FileNotFoundError`, printing a message instead of a
  traceback. `Use exactly as written`: `except FileNotFoundError`. `Example —
  adapt to your own layout`: the message wording — the assignment asks for "a
  helpful message," so any clear message passes; do not require the sample text.
  Required: the script runs to completion without showing a traceback.
- **Warmup 4 — Virtual Environment Setup** — a script that imports `requests` and
  prints its version, with the contents of a `pip freeze`-generated
  `requirements.txt` pasted as a comment at the top. Required: `requests` is
  imported, its version is printed, and a requirements comment block is present.
  `Example — adapt to your own layout`: **every version number and the exact
  package list — these depend on when the student installed, so
  `requests==2.31.0` and the surrounding packages will not match. Do not fail a
  different version or a different set of transitive dependencies.** Whether
  `requirements.txt` is also committed as its own file is not specified by the
  assignment — do not fail either choice. The virtual environment itself cannot be
  seen by the reviewer; do not fail its absence.
- **Mini-Project — Defensive CSV Reader (`mini_project.py`)** — reads a messy CSV
  defensively and prints a summary. Required, because the assignment states each
  step: the file opening is wrapped in `try`/`except FileNotFoundError` (printing
  an error and stopping if missing), `csv.DictReader` reads the file, **each row is
  processed inside its own `try`/`except` inside the loop** (not one `try` wrapped
  around the whole loop), `ValueError` and `KeyError` are both caught, successfully
  parsed rows are collected into a list of dictionaries, and a summary is printed
  at the end. The summary must report rows attempted, rows parsed, rows skipped, a
  list of the skipped rows with a reason for each, and the clean data. `Example —
  adapt to your own layout`: the counts (14 / 9 / 5), the specific skipped-row
  reasons, the row contents, and all labels, spacing, and separators — these come
  from a data file the reviewer cannot read, so check that the summary reports
  each of those five things, not that the numbers or formatting match. Note on
  `KeyError`: `csv.DictReader` usually fills a missing column with `None` rather
  than raising, so a correct submission may have an `except KeyError` clause that
  never fires — require the clause to be present, but do not require evidence
  that it triggered, and do not fail a student for also guarding extra columns
  with a `None in row` check (Hint 2 tells them to).
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video.

### Optional Deliverables/Tasks

**None.**

</details>
