# Assignment 8 — Errors & Debugging

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-8` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-8/`, create a new `assignment-8/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-8` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Validate Numeric Input

Write a loop that asks the user to enter a number. If they enter something that can't be converted to a number, catch the `ValueError` with `try`/`except`, print a message, and ask again. Once you have a valid number, print it and stop:

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

Ask the user for two numbers. Compute the result of dividing the first by the second. Use `try`/`except ZeroDivisionError` to catch division by zero and print a friendly message instead of crashing:

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

Write a script that attempts to open `../data/missing.txt` (this file does not exist). Use `try`/`except FileNotFoundError` to catch the error and print a helpful message rather than a traceback:

```
Error: "missing.txt" was not found. Please check the file path and try again.
```

**Save as:** `warmup3.py`

---

### Warmup 4: Virtual Environment Setup

Set up a virtual environment for your project, install the `requests` library, and generate a `requirements.txt` with `pip freeze`. Then write a short script that imports `requests` and prints its version. Paste the contents of your `requirements.txt` as a comment at the top of the file.

```python
# requirements.txt contents:
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.6
# requests==2.31.0
# urllib3==2.2.1
```

Expected output:
```
requests version: 2.31.0
```

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Defensive CSV Reader

The file `../data/messy_data.csv` contains a mix of valid and invalid rows. Each row should have three fields — `name`, `category`, and `amount` — but some rows have problems: missing values, non-numeric amounts, or extra columns.

Write a script that reads this file defensively and produces a clean summary. Your program must:

1. Use `try`/`except FileNotFoundError` to check that the file exists before opening it. If not, print an error and stop.
2. Read the file with `csv.DictReader`.
3. Process each row inside a `try`/`except` block. Catch at minimum:
   - `ValueError` — when `amount` can't be converted to `float`
   - `KeyError` — when an expected column is missing from a row
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

> **Hint:** You can track skipped rows by storing a description of each failure, then printing them at the end. Use `enumerate()` to get row numbers as you loop.

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

Include the video link in your pull request description or the `URL1` field in the submission form.

---

## Need a GitHub Review?

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-8
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-8  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
</details>
