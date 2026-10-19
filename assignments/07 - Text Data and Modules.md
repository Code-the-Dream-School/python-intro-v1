# Assignment 7 — Text Data & Modules

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-6` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-7` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-7/`, create a new `assignment-7/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-7` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file. Data files for this week are in the `week-7/data/` folder — reference them from your `assignment-7/` working directory using the path `../data/filename`.

---

### Warmup 1: Read a Text File Line by Line

Open `../data/notes.txt` using a `with` block, read it line by line, and print each line with its number.

Example output — the line numbering is the point; your file's text comes from the provided data file:

```
Line 1: Python is great for working with files.
Line 2: You can read, write, and append text.
Line 3: The 'with' statement keeps things clean.
Line 4: Always close your files when you're done.
```

Use `.strip()` to remove the trailing newline from each line before printing.

**Save as:** `warmup1.py`

---

### Warmup 2: Read a CSV with DictReader

Use `csv.DictReader` to read `../data/students.csv` — it has three columns: `name`, `subject`, and `score`. Print each student's name and score on a single line.

Example output — the names and scores come from the provided CSV:

```
Jazmine: 88
Luis: 74
Sara: 91
Marcus: 83
Priya: 95
```

**Save as:** `warmup2.py`

---

### Warmup 3: Use the os Module

Write a single script that does all three of the following:

1. Print your current working directory using `os.getcwd()`.
2. Check whether `../data/expenses.csv` exists using `os.path.exists()`. Print `"expenses.csv found."` or `"expenses.csv not found."` accordingly.
3. Use `os.path.join()` to build the path `"../data/expenses.csv"` from its parts (`".."`, `"data"`, `"expenses.csv"`) and print the result. You'll use this same pattern in the mini-project.

**Submit as:** `warmup3.py`

---

### Warmup 4: Use the datetime Module

Print today's date in the following format. The example below shows the format — your date will be the day you run the script:

```
Today is April 24, 2026.
```

Use `datetime.now()` and `.strftime()`.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Expense Report Generator

The file `../data/expenses.csv` tracks personal spending across several categories. The example below shows the file's structure (it is truncated — the real file has more rows):

```
date,category,description,amount
2024-03-01,Food,Grocery store,54.30
2024-03-02,Transport,Bus pass,35.00
...
```

Write a program that analyzes this data and writes a formatted report to a new file. Follow these steps:

1. Use `os.path.exists()` to verify that `../data/expenses.csv` exists before opening it. If it doesn't, print an error message and stop.
2. Read `../data/expenses.csv` into a list of dictionaries using `csv.DictReader`.
3. Convert the `amount` field to `float` for each row.
4. Filter the list to only rows where `category` is `"Food"`.
5. Calculate the total amount spent on Food.
6. Write a report to `food_report.txt` with this structure:
   - First line: `Food Expense Report — generated [today's date as "Month DD, YYYY"]`
   - One line per food expense: `[date]: $[amount]`
   - Last line: `Total: $[total to 2 decimal places]`

> **Hint:** All values from `csv.DictReader` come back as strings. Remember to convert `amount` with `float()` before doing any math.

**Optional:** If you want extra practice, modify your program to work for any category, not just `"Food"`. Running it for `"Transport"` should produce a `transport_report.txt` with the same format.

**Save as:** `mini_project.py` (and include `food_report.txt` to show your output)

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. Explain what `with open(...) as f:` does and why Python uses this pattern for file handling.
2. Walk through your code that reads a CSV and parses it into a list of dictionaries. What does each step do?
3. Look back at the When to Import vs. Write Your Own lesson. Describe one decision you made in your mini-project about whether to use a module or write something yourself — what was the task, and why did you make that call?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

## Need a GitHub Review?

Open the dropdown box below:

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-7`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-7
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
`assignment-7` branch, with files inside a `week-7/assignment-7/` folder, reading
the provided data files in `week-7/data/`. `Example — adapt to your own layout`:
the folder path and repo location are organizational conventions — do NOT fail
correct code for sitting in a different folder or path; the reviewer cannot see
the student's filesystem. The assignment suggests reaching the data as
`../data/<filename>`, but **any path form is acceptable** — relative, absolute,
`os.path.join()`, or `week-7/data/...` — as long as the right file is opened. Do
not fail a path, and do not fail anything that depends on seeing the provided data
files, since the reviewer cannot read them. Submission mechanics (branch, PR base)
are not graded from the code. This repo is cumulative — folders from earlier weeks
are expected to remain; do not tell the student to remove prior-week work.
Expected files: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`,
`mini_project.py`, and the generated `food_report.txt`.

- **Warmup 1 — Read a Text File Line by Line** — opens `notes.txt` in a `with`
  block, reads it line by line, and prints each line prefixed with its number,
  using `.strip()` to drop the trailing newline. Required, because the assignment
  states each one: a `with` block, line-by-line reading (not one bulk read), a
  number on each line, and `.strip()`. `Example — adapt to your own layout`: the
  file's text and the exact prefix punctuation — the reviewer cannot see
  `notes.txt`, so do not fail differing content or wording.
- **Warmup 2 — Read a CSV with DictReader** — uses `csv.DictReader` to read
  `students.csv` (columns `name`, `subject`, `score`) and prints each student's
  name and score on one line. `Use exactly as written`: `csv.DictReader` (not
  `csv.reader` or manual splitting), and the column names `name`, `subject`, and
  `score`. `Example — adapt to your own layout`: the names and scores come from
  the provided CSV, and the separator between name and score is the student's own.
- **Warmup 3 — Use the os Module** — one script that prints the working directory
  with `os.getcwd()`, checks the expenses file with `os.path.exists()` and prints
  one of the two messages, then builds the path from its parts with
  `os.path.join()` and prints it. `Use exactly as written`: the three functions
  `os.getcwd()`, `os.path.exists()`, and `os.path.join()`, and the messages
  `expenses.csv found.` and `expenses.csv not found.`. `Example — adapt to your
  own layout`: the printed working directory (it is whatever machine ran the
  script) and the path pieces passed to `os.path.join()`. Note the file is named
  `warmup3.py` — the assignment says "Submit as" here rather than "Save as", but
  it means the same thing.
- **Warmup 4 — Use the datetime Module** — prints today's date formatted as
  "Month DD, YYYY" using `datetime.now()` and `.strftime()`. `Use exactly as
  written`: `datetime.now()` and `.strftime()`, and the "Month DD, YYYY" format
  (e.g. `April 24, 2026`). `Example — adapt to your own layout`: **the date itself
  — it is whatever day the student ran the script, so it will never match the
  example. Do not fail a different date.** The surrounding sentence wording is
  also the student's own.
- **Mini-Project — Expense Report Generator (`mini_project.py`)** — reads the
  expenses CSV and writes a formatted report. Required, because the assignment
  states each step: `os.path.exists()` guards the file before opening it (printing
  an error and stopping if missing), `csv.DictReader` reads the rows into a list of
  dictionaries, each `amount` is converted with `float()`, the rows are filtered to
  `category == "Food"`, the Food total is calculated, and a report is written to
  `food_report.txt`. `Use exactly as written`: the report's three-part structure —
  a first line `Food Expense Report — generated <today's date as "Month DD,
  YYYY">`, one line per food expense as `<date>: $<amount>`, and a last line
  `Total: $<total to 2 decimal places>`. The total must show 2 decimal places.
  `Example — adapt to your own layout`: the report's date (whatever day it was
  generated), the specific expense rows and totals (they come from the provided
  CSV, which the reviewer cannot read), and where `food_report.txt` is written.
- **`food_report.txt`** — the generated report is committed alongside the script,
  as the assignment asks. Its contents come from the provided data, so check the
  structure, not the numbers.
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video. Question 3 points back to a course lesson the reviewer cannot
  see; that is fine, because no part of the code is graded against it.

### Optional Deliverables/Tasks

- **Optional extension — any category** — if attempted, the program works for any
  category rather than only `"Food"`, so running it for `"Transport"` writes a
  `transport_report.txt` in the same format. The assignment marks this
  **Optional**: do NOT fail a student for omitting it, and do not expect
  `transport_report.txt` to exist. A student who did generalize the program still
  passes the required work as long as a Food report is produced.

</details>
