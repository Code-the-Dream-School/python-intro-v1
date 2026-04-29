# Assignment 4 — Core Data Structures

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-4` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-4/`, create a new `assignment-4/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-4` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: List Operations

Create a hardcoded list of 8 numbers. Without using any loops, print:

1. The first item
2. The last item (use a negative index)
3. A slice containing only the middle four items
4. The full list in reverse order

Example output (your numbers will differ):
```
First:   42
Last:    40
Middle:  [83, 5, 61, 29]
Reversed: [40, 86, 22, 59, 3, 78, 47, 14]
```

**Save as:** `warmup1.py`

---

### Warmup 2: Dictionary Operations

Create a hardcoded dictionary representing a student with these keys: `name`, `grade`, and `subjects` (a list of subject strings). Then:

1. Print each key-value pair using `.items()` in a `for` loop
2. Add a new key `"graduated"` with the value `False`
3. Print the updated dictionary

**Save as:** `warmup2.py`

---

### Warmup 3: Set Operations

Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:

1. The union (all languages from both lists, no duplicates)
2. The intersection (languages in both lists)
3. The difference (languages only in the first list)

**Save as:** `warmup3.py`

---

### Warmup 4: List Comprehensions

Start with a hardcoded list of integers. Use list comprehensions to produce two new lists:

1. Only the even numbers from the original list
2. Every number from the original list squared

Print both results.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Student Roster Analyzer

A data file is provided in `week-4/data/roster.py`. Copy the `students` list from that file into your script — it contains dictionaries with `name`, `score`, and `subject` fields.

Using loops and data structure operations, your script must:

1. **Find the top scorer** — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in `max()` on the list directly.
2. **Calculate the class average** — accumulate the total score in a loop, then divide.
3. **List all unique subjects** — use a set to collect subjects as you loop, then print them.
4. **List high scorers** — use a list comprehension to get the names of all students who scored above 75.

Example output:
```
Top scorer:       Sara (91)
Class average:    81.3
Subjects offered: {'Python', 'Data', 'Web'}
High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']
```

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is the difference between a list and a dictionary — when would you reach for each one?
2. Walk through your list comprehension: what problem did it solve, and how is it different from a `for` loop that does the same thing?
3. What was surprising or confusing about working with nested data (dictionaries inside a list)?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in your pull request description or the `URL1` field in the submission form.

---

## Review: The GitHub Cycle

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-4
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-4  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
