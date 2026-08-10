# Assignment 2 — CLI & Professional Environment

## Before You Start: You Should Already Have Forked and Cloned

This assignment assumes you've completed the setup steps from this week's lesson, specifically that you have:

1. **Forked** the shared `Code-the-Dream-School/python-intro-homework` repository to your own GitHub account, and
2. **Cloned your fork** to your local machine.

All of your work this week happens inside your **local clone of your fork**: the `python-intro-homework` folder on your computer. When you check the address of your repo, it should read `github.com/your-username/python-intro-homework`, with *your* username, not `Code-the-Dream-School`.

If you haven't forked and cloned yet, stop and complete the ["Forking and Cloning the Homework Repository" section](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/02%20-%20CLI%20and%20Professional%20Environment/04_git_setup.md) of the setup lesson first.

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

Using only your terminal (no file explorer), navigate to your `week-2/assignment-2/` folder. Then write a script that asks the user `"What is today's date? "` using `input()` and prints it back in a sentence:

```
You said today is April 24, 2026.
```

At the top of the file, paste the two or three terminal commands you used to navigate there (e.g., `cd`, `ls`, `pwd`):

```python
# Navigation commands I used:
# cd Desktop/python-intro-homework
# ls
# cd week-2/assignment-2
```

**Save as:** `warmup2.py`

---

### Warmup 3: First Git Commit

Make at least one meaningful commit with your warmup files so far, and run `git log --oneline`. Paste the output as a comment:

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
3. Prints the result rounded to one decimal place:

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
