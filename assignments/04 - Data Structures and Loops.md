# Assignment 4 — Core Data Structures

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-3` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-4` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-4/`, create a new `assignment-4/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-4` into `main`
   - **URL2:** A link to your video reflection

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

## Part 2: Mini-Project — Student Roster Analyzer

A data file is provided in `week-4/data/roster.py`. Copy the `students` list from that file into your script — it contains dictionaries with `name`, `score`, and `subject` fields.

Using loops and data structure operations, your script must:

1. **Find the top scorer** — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in `max()` on the list directly.
2. **Calculate the class average** — accumulate the total score in a loop, then divide.
3. **List all unique subjects** — use a set to collect subjects as you loop, then print them.
4. **List high scorers** — use a loop and `.append()` to get the names of all students who scored above 75.

Example output:
```
Top scorer:       Priya (95)
Class average:    81.25
Subjects offered: {'Python', 'Data', 'Web'}
High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']
```

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is the difference between a list and a dictionary — when would you reach for each one?
2. Walk through how you found the top scorer without using max() — what does your loop track and why?
3. What was surprising or confusing about working with nested data (dictionaries inside a list)?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

---

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-4`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-4
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

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

Work happens in the student's forked `python-intro-homework` repo, on an
`assignment-4` branch, with files inside a `week-4/assignment-4/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (branch, PR base) are not graded from the code. This repo is
cumulative — folders from earlier weeks are expected to remain; do not tell the
student to remove prior-week work. Expected files: `warmup1.py`, `warmup2.py`,
`warmup3.py`, `mini_project.py`.

- **Warmup 1 — List Operations** — a hardcoded list of 8 numbers, then four
  printed results: the first item, the last item using a negative index, a slice
  of the middle four items, and the full list reversed. `Example — adapt to your
  own layout`: the numbers and the label wording (`First:`, `Last:`, etc.) are the
  student's own — the assignment says the numbers will differ. Required: no loops
  in this file, a negative index for the last item, and a four-item middle slice.
- **Warmup 2 — Dictionary Operations** — a hardcoded dictionary printed pair by
  pair with `.items()` in a `for` loop, then a new key added and the updated
  dictionary printed. `Use exactly as written`: the keys `name`, `grade`, and
  `subjects`, and the added key `"graduated"` with the value `False`. `Example —
  adapt to your own layout`: the student's own name, grade, and subject values.
  Required: `subjects` holds a list of strings, and `.items()` is used.
- **Warmup 3 — Set Operations** — two hardcoded lists of programming languages
  with some overlap, each converted to a set, then the union, the intersection,
  and the difference (first list only) printed. `Example — adapt to your own
  layout`: the languages are the student's own pick. Required: sets used rather
  than manual de-duplication, and all three operations printed.
- **Mini-Project — Student Roster Analyzer (`mini_project.py`)** — the `students`
  list copied in from the provided `week-4/data/roster.py`, then four results
  printed: the top scorer's name and score, the class average, the unique
  subjects, and the names scoring above 75. Required: the top scorer is found with
  a loop that tracks the highest score and its name (calling `max()` on the list
  directly is not allowed), the class average accumulates a total in a loop and
  then divides (`sum()` is not allowed), a set collects the subjects, and the high
  scorers are gathered with a loop and `.append()`. The assignment states each of
  these constraints, so hold the line on them. `Example — adapt to your own
  layout`: the sample values (`Priya (95)`, `81.25`, etc.) come from the provided
  data file, and the output labels and spacing are the student's own — do not fail
  differing formatting, and do not fail on the data file's path (the reviewer
  cannot see the provided file or the student's filesystem).
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video.

### Optional Deliverables/Tasks

**None.**

</details>
