# Assignment 6 — Functions & Scope

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-5` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-6` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-6/`, create a new `assignment-6/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-6` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Default Parameters

Write a function `greet(name, greeting="Hello")` that prints a greeting. Call it three different ways:

1. With only a name argument
2. With both a name and a custom greeting
3. With the greeting passed as a keyword argument

Example output — your name and custom greeting might differ:

```
Hello, Alex!
Good morning, Alex!
Hello, Alex!
```

**Save as:** `warmup1.py`

---

### Warmup 2: Functions that Return Values

Write two functions:
- `celsius_to_fahrenheit(c)` — converts Celsius to Fahrenheit using `(c * 9/5) + 32`
- `fahrenheit_to_celsius(f)` — converts Fahrenheit to Celsius using `(f - 32) * 5/9`

Call each with a few test values and print the results. Use f-strings and round to one decimal place.

Example output — your test values and wording might differ:

```
0°C = 32.0°F
100°C = 212.0°F
72°F = 22.2°C
```

**Save as:** `warmup2.py`

---

### Warmup 3: Scope in Action

Demonstrate variable scope with two short examples in one file:

1. Define a variable inside a function. Try to access it outside the function and show the `NameError` — paste the error in a comment, then remove or comment out the line that causes it.
2. Show how `return` solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.

**Save as:** `warmup3.py`

---

### Warmup 4: Validation Function

Write a function `is_valid_score(score)` that returns `True` if `score` is an integer between 0 and 100 (inclusive), and `False` otherwise. Then use `input()` to ask the user for a score and convert it to an integer with `int()` before you check it. Call your function inside an `if` statement and print either `"Valid score."` or `"Invalid score — must be between 0 and 100."`.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Refactor the Number Cruncher

Open your `mini_project.py` from Assignment 5. You're going to refactor it so that each operation lives in its own function.

**Create a new file** (don't modify your Week 5 submission). Pull a copy of the `numbers` list from `week-5/data/numbers.py` into your new script.

Define the following functions, each taking `numbers` (a list) as a parameter:

- `find_min(numbers)` — returns the minimum value (your loop-based implementation, no `min()`)
- `find_max(numbers)` — returns the maximum value (your loop-based implementation, no `max()`)
- `search(numbers, target)` — returns the index of `target`, or `-1` if not found
- `bubble_sort(numbers)` — returns a **new sorted list** (do not modify the original)
- `show_menu()` — prints the menu options and returns the user's choice as a string
- `main()` — the while loop that calls `show_menu()` and dispatches to the right function

Call `main()` at the bottom of the file.

**Requirements:**
- No logic should live outside of a function (except the `numbers` list definition and the `main()` call)
- `bubble_sort` should return a new list, not sort in place
- Your `search` function should print "Found at index X" or "Not found" from inside `main()`, not inside `search()` itself — `search` just returns the index

**Save as:** `mini_project.py`

> **Why revisit Week 5?** This is exactly how real software gets built — you write something that works, then return to make it cleaner and easier to change. Your git history now shows both versions, which is version control doing its job.

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What does `return` do — how is it different from `print()`?
2. Walk through one function you wrote: what are its inputs, what does it do, and what does it return?
3. Show a place where breaking your code into functions made it cleaner or easier to understand. How does this connect to why Git history is useful?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

---

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-6`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-6
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
`assignment-6` branch, with files inside a `week-6/assignment-6/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (branch, PR base) are not graded from the code. This repo is
cumulative — folders from earlier weeks are expected to remain; do not tell the
student to remove prior-week work. This assignment refactors Assignment 5's
mini-project into a **new** file, so a second `mini_project.py` under `week-6/`
alongside the Week 5 one is correct and expected — do not treat either copy as
duplicated or stray code, and do not fault the student for leaving the Week 5
file unchanged (the assignment tells them not to modify it). The reviewer cannot
see Assignment 5's file or the provided `week-5/data/numbers.py` — grade the new
file on its own and do not fail anything that depends on seeing them. Expected
files: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.

- **Warmup 1 — Default Parameters** — a function `greet(name, greeting="Hello")`
  that prints a greeting, called three ways: with the name only, with a name and a
  custom greeting, and with the greeting passed as a keyword argument. `Use exactly
  as written`: the function name `greet`, its parameter names `name` and `greeting`,
  and the default value `"Hello"`. `Example — adapt to your own layout`: the name
  ("Alex"), the custom greeting ("Good morning"), and all printed wording are the
  student's own — grade the three call styles, not the strings.
- **Warmup 2 — Functions that Return Values** — two functions,
  `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`, each **returning**
  (not printing) its result, then called with a few values and printed with
  f-strings rounded to one decimal place. `Use exactly as written`: the function
  names, and the formulas `(c * 9/5) + 32` and `(f - 32) * 5/9`. `Example — adapt
  to your own layout`: the test values (0, 100, 72) and the output wording are the
  student's own — check the math instead (0°C → 32.0°F, 100°C → 212.0°F,
  72°F → 22.2°C). Required: both functions `return` a value, and results show one
  decimal place.
- **Warmup 3 — Scope in Action** — one file with two demonstrations: a variable
  defined inside a function that is inaccessible outside it, with the `NameError`
  pasted in a comment and the offending line removed or commented out; then the
  same value returned from the function, assigned in the outer scope, and printed.
  Required: the submitted file runs without error (the failing line is not left
  live), and the second demonstration uses `return`. `Example — adapt to your own
  layout`: the variable names, the pasted error text, and all wording are the
  student's own.
- **Warmup 4 — Validation Function** — a function `is_valid_score(score)` that
  returns `True` for an integer from 0 to 100 inclusive and `False` otherwise, then
  `input()` for a score, converted to an integer with `int()`, and the function
  called inside an `if` that prints one of the two messages. `Use exactly as
  written`: the function name `is_valid_score`, and the messages `Valid score.` and
  `Invalid score — must be between 0 and 100.`. Required, because the assignment
  states each one: the function **returns** a boolean rather than printing, the
  input is converted to an integer with `int()` before it is checked, and 0 and 100
  both count as valid. Do NOT additionally require `try`/`except` around the
  conversion — the assignment does not ask for it, so a crash on non-numeric input
  is not a failure.
- **Mini-Project — Refactor the Number Cruncher (`mini_project.py`)** — a new file
  with the `numbers` list copied in, defining six functions: `find_min(numbers)`,
  `find_max(numbers)`, `search(numbers, target)`, `bubble_sort(numbers)`,
  `show_menu()`, and `main()`, with `main()` called at the bottom. `Use exactly as
  written`: those six function names and their parameters, and `-1` as `search`'s
  not-found return value. Required, because the assignment states each one: no
  `min()` and no `max()` (the loop-based implementations carry over), `bubble_sort`
  returns a **new** list rather than sorting in place, `search` returns the index
  and does not print (the "Found at index X" / "Not found" message is printed from
  `main()`), and no logic lives outside a function apart from the `numbers` list
  and the `main()` call. `Example — adapt to your own layout`: the menu text and
  all message wording, and the list's contents (they come from the Week 5 data
  file) — do not fail on specific values, on menu formatting, or on the data
  file's path.
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video.

### Optional Deliverables/Tasks

**None.**

</details>
