# Assignment 3 — Control Flow

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-2` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-3` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-3/`, create a new `assignment-3/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-3` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Letter Grades

Start with a hardcoded `score` variable (pick any number 0–100). Use `if`/`elif`/`else` to print the corresponding letter grade:

| Score | Grade |
|-------|-------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

Example output:
```
Score: 84
Grade: B
```

**Save as:** `warmup1.py`

---

### Warmup 2: Age Categories

Use `input()` to ask the user for their age. Convert it to an integer, then use `if`/`elif`/`else` with `and` to check ranges and print which category they fall into:

| Age range | Category |
|-----------|----------|
| 0–12 | Child |
| 13–17 | Teen |
| 18–64 | Adult |
| 65 and up | Senior |

Example output:
```
Enter your age: 16
You are a Teen.
```

**Save as:** `warmup2.py`

---

### Warmup 3: Boolean Expression Practice

Write a script that evaluates the five expressions below and prints each one with its result. Add a comment on each line explaining *why* the result is what it is:

```python
print(not True and False)
print(True or False and False)
print(not (5 > 3))
print(10 == 10 and 4 != 4)
print(not False or not True)
```

Example format:
```
False   # not True is False; False and False is False
```

**Save as:** `warmup3.py`

---

### Warmup 4: Sign and Parity

Ask the user for a number. Using two **separate** `if`/`elif`/`else` blocks — one for sign, one for parity — print two lines of output. The examples below show the format for two different inputs — your number will differ:

```
Enter a number: -7
-7 is negative.
-7 is odd.
```

```
Enter a number: 0
0 is zero.
0 is even.
```

Handle `0` as its own sign case (neither positive nor negative).

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Day Planner

Write a program that asks the user for a **day of the week** and a **time of day** (morning, afternoon, or evening), then suggests an activity.

**Requirements:**
- Cover at least **3 days × 3 times = 9 combinations** with distinct suggestions
- Handle any unrecognized day or time with a friendly fallback message
- Normalize input so capitalization doesn't matter (e.g., `"Monday"` and `"monday"` both work)

Example output (the suggestion and fallback wording are your own — any sensible messages are fine):
```
What day is it? Tuesday
What time of day? morning
Suggestion: Morning Python class — great time to focus!
```

```
What day is it? Saturday
What time of day? evening
Suggestion: Perfect night for a movie or trying a new recipe.
```

```
What day is it? blah
What time of day? morning
Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...
```

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. Explain how Python decides which branch of an `if`/`elif`/`else` block to run. Walk through an example from your code.
2. What does a Boolean operator like `and` or `or` do? Give a real example of when you'd use one.
3. Walk through the Git workflow you used to submit this assignment — branch, add, commit, push, pull request. What does each step do?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

---

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-3`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-3
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
`assignment-3` branch, with files inside a `week-3/assignment-3/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (branch, PR base) are not graded from the code. Expected files:
`warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.

- **Warmup 1 — Letter Grades** — a hardcoded `score`, then an `if`/`elif`/`else`
  chain that prints the letter grade using the table (90–100 A, 80–89 B, 70–79 C,
  60–69 D, below 60 F). `Example — adapt to your own layout`: the score (84) is the
  student's own pick — do not require a specific value. Required: boundaries land
  right (90→A, 80→B, 70→C, 60→D, below 60→F) and `elif` is used so only one branch
  fires.
- **Warmup 2 — Age Categories** — `input()` → `int()`, then `if`/`elif`/`else`
  using `and` to bound the ranges (0–12 Child, 13–17 Teen, 18–64 Adult, 65+
  Senior). `Example — adapt to your own layout`: the age (16) comes from input.
  Required: `int()` conversion, and ranges bounded so they don't overlap.
- **Warmup 3 — Boolean Expression Practice** — prints the five given expressions,
  each with a `#` comment explaining why. `Use exactly as written`: evaluate
  exactly the five expressions shown; the results are `False`, `True`, `False`,
  `False`, `True`. `Example — adapt to your own layout`: the comment wording is the
  student's own — accept any sound reasoning; do not require the literal sample
  comment text.
- **Warmup 4 — Sign and Parity** — `input()` → number, then two **separate**
  `if`/`elif`/`else` blocks (one for sign, one for parity), printing two lines; `0`
  handled as its own sign case. `Example — adapt to your own layout`: the number
  (−7, 0) comes from input and the exact sentence wording is flexible. Required:
  `0` reported as zero (not positive/negative), parity via `% 2` (works for
  negatives), and two independent blocks rather than one merged chain.
- **Mini-Project — Day Planner (`mini_project.py`)** — asks for a day and a time of
  day, normalizes input so capitalization doesn't matter, suggests an activity, and
  gives a fallback for any unrecognized day or time. `Example — adapt to your own
  layout`: the suggestion and fallback wording are the student's own — any sensible,
  distinct messages pass. Required: at least 9 day×time combinations (≥3 days × 3
  times) with distinct suggestions, case-normalized input (e.g. `.lower()`), and a
  fallback message.
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything about
  the video.

### Optional Deliverables/Tasks

**None.**

</details>
