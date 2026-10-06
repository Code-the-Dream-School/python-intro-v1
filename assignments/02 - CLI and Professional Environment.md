# Assignment 2 — CLI & Professional Environment

## Before You Start: You Should Already Have Forked and Cloned

This assignment assumes you've completed the setup steps from this week's lesson, specifically that you have:

1. **Forked** the shared `Code-the-Dream-School/python-intro-homework` repository to your own GitHub account, and
2. **Cloned your fork** to your local machine.

All of your work this week happens inside your **local clone of your fork**: the `python-intro-homework` folder on your computer. When you check the address of your repo, it should read `github.com/your-username/python-intro-homework`, with *your* username, not `Code-the-Dream-School`.

If you haven't forked and cloned yet, stop and complete the ["Forking and Cloning the Homework Repository" section](https://github.com/Code-the-Dream-School/python-intro-v1/blob/92a0e1a83e71dc7ca5bf1bc14d67c3bb1948ed46/lessons/02%20-%20CLI%20and%20Professional%20Environment/05_git_configuration.md) of the setup lesson first.

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-2` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-2/`, create a new `assignment-2/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-2` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

> **Point your PR at your own fork, not the original.** Because your repo is a fork, GitHub will default your pull request's *base* to `Code-the-Dream-School/python-intro-homework`. That's the wrong target. When you open the PR, check the base repository dropdown and make sure it reads `your-username/python-intro-homework` — if your PR URL contains `Code-the-Dream-School`, close it and open a new one against your own fork. (This is covered in more detail in the setup lesson.)

> **This is your first GitHub PR submission using the command line.** In Week 1 you used GitHub's web editor as a shortcut to submit your work. This week you'll do the same thing (create a branch, add your files, open a pull request) using Git in your terminal, the way developers work in practice. The concepts are the same; the tools are just more powerful. If anything about the workflow is unclear, reach out to your mentor before the due date. 
>
> It's normal to have questions about GitHub — don't wait until the last minute to ask for help!
---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file. Run each script from your terminal using `python warmup1.py`, etc.

---

### Warmup 1: Prove Python Is Working

Write a script that prints the following message:

```
Python is working!
```

Run it from your terminal. Then paste the terminal command you used and the output as a comment at the top of the file:

```python
# Command: python warmup1.py
# Output:  Python is working!
```

**Save as:** `warmup1.py`

---

### Warmup 2: Navigate with the CLI

Using only your terminal (no file explorer), navigate to your `week-2/assignment-2/` folder. Then write a script that asks the user `"What is today's date? "` using `input()` and prints it back in a sentence. The example below shows the format — the date will be whatever the user types:

```
You said today is April 24, 2026.
```

At the top of the file, paste the two or three terminal commands you used to navigate there (e.g., `cd`, `ls`, `pwd`). Your own paths will differ from the example below:

```python
# Navigation commands I used:
# cd Desktop/python-intro-homework
# ls
# cd week-2/assignment-2
```

**Save as:** `warmup2.py`

---

### Warmup 3: First Git Commit

Make at least one meaningful commit with your warmup files so far, and run `git log --oneline`. Paste the output as a comment. Your hash and message will differ from the example below:

```python
# git log --oneline output:
# a3f91bc Add warmup1 and warmup2 for week 2
```

Then write a short script that prints a message of your choice — something that describes what you learned this week. Commit this file too.

**Save as:** `warmup3.py`

---

### Warmup 4: Read an Error Message

Write a script that contains a deliberate bug — for example, use a variable name that hasn't been defined, or forget to convert a string to an integer before doing math. Run it, read the error message, then fix the bug. Add a comment block describing:

1. What the error message said (paste it)
2. What caused it
3. How you fixed it

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Temperature Converter

Write a script that:

1. Asks the user to enter a temperature in Fahrenheit
2. Converts it to Celsius using the formula: `celsius = (fahrenheit - 32) * 5 / 9`
3. Prints the result rounded to one decimal place. The example below shows the format — your input and result will differ:

```
Enter a temperature in Fahrenheit: 72
72.0°F is 22.2°C.
```

**Requirements:**
- Handle the conversion yourself (no built-in converter functions)
- Use an f-string for the output
- Round to exactly one decimal place

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is the terminal and why does a developer need to be comfortable using it? Walk through two or three CLI commands you used this week.
2. Explain what happens when you run `python script.py` in the terminal. What is Python actually doing?
3. What is Git, and what problem does it solve? Explain the difference between Git and GitHub.

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.

---

## Review: The GitHub Cycle

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-2
```

Here `origin` is your fork. `git pull origin main` brings your local `main` in sync with your fork on GitHub — which matters once you've merged a PR and want those changes locally. Early on it may report "Already up to date," and that's fine.

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-2  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like. Committing often gives you more points to return to if something goes wrong.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

Work happens in the student's **forked** `python-intro-homework` repo, on an
`assignment-2` branch, with files inside a `week-2/assignment-2/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (fork, branch, PR base) are not graded from the code. Expected files:
`warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.

- **Warmup 1 — Prove Python Is Working** — script prints the message, and a
  comment block at the top shows the `python warmup1.py` command and its output.
  `Use exactly as written`: the printed message is `Python is working!`.
- **Warmup 2 — Navigate with the CLI** — script uses `input("What is today's
  date? ")` and prints the entered date back in a sentence; a comment block shows
  the navigation commands used. `Example — adapt to your own layout`: the date
  ("April 24, 2026") and the navigation paths (`cd Desktop/python-intro-homework`,
  etc.) are samples — the date comes from input and the student's paths will
  differ; do not require the literal example text.
- **Warmup 3 — First Git Commit** — a comment block shows real `git log --oneline`
  output (short hash + message, at least one meaningful commit), and the script
  prints a "what I learned" message. `Example — adapt to your own layout`: the hash
  (`a3f91bc`) and commit message are samples — do not require the literal example;
  any real-looking log output and any learning message pass.
- **Warmup 4 — Read an Error Message** — the file contains a deliberate bug that
  the student then FIXED, so the submitted file runs cleanly, plus a comment naming
  the error, its cause, and the fix. `Example — adapt to your own layout`: the
  specific bug and error type are the student's choice — do not require a
  particular one. Required: the submitted file runs without error (bug fixed, not
  left broken).
- **Mini-Project — Temperature Converter (`mini_project.py`)** — prompts for a
  Fahrenheit temperature with `input()`, converts it, and prints the result rounded
  to one decimal place using an f-string. `Use exactly as written`: the conversion
  formula `celsius = (fahrenheit - 32) * 5 / 9` (no library converter). `Example —
  adapt to your own layout`: the sample input/output (72 → 22.2) comes from input —
  check the math instead (72 → 22.2, 32 → 0.0, 212 → 100.0). Required: input cast
  to `float`, and exactly one decimal place (`:.1f` or `round(celsius, 1)`).
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything about
  the video.

### Optional Deliverables/Tasks

**None.**

</details>
