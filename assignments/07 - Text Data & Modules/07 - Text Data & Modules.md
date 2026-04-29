# Assignment 7 — Text Data & Modules

## Submission Instructions

1.  **Create your branch:** From `main`, create a new `assignment-7` branch in your `python-intro-homework` repo.
2.  **Create your folder:** Inside the repo, create a new `assignment-7` folder and do all your work there.
3.  **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-7` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file. Data files for this week are in the `week-7/data/` folder — reference them from your `assignment-7/` working directory using the path `../data/filename`.

---

### Warmup 1: Read a Text File Line by Line

Open `../data/notes.txt` using a `with` block, read it line by line, and print each line with its number:

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

Use `csv.DictReader` to read `../data/students.csv` — it has three columns: `name`, `subject`, and `score`. Print each student's name and score on a single line:

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

Print today's date in the following format:

```
Today is April 24, 2026.
```

Use `datetime.now()` and `.strftime()`.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Expense Report Generator

The file `../data/expenses.csv` tracks personal spending across several categories:

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

**Extension (optional, ungraded):** Modify your program to work for any category, not just `"Food"`. Running it for `"Transport"` should produce a `transport_report.txt` with the same format.

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

Include the video link in your pull request description or `URL2` field in the submission form.

## Need a GitHub Review?

Open the dropdown box below:

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b week-[#]     
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin week-[#]        # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
</details>
