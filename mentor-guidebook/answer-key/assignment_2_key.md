# Assignment 2 Answer Key — CLI and Professional Environment

## File Setup

- Work happens in the student's **forked** `python-intro-homework` repo (URL should read `github.com/their-username/...`, not `Code-the-Dream-School`), on an `assignment-2` branch, inside a `week-2/assignment-2/` folder.
- Five files, run locally from the terminal: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.
- Submitted as a **pull request** from `assignment-2` into `main` **on their own fork**. **URL1** = the PR link; URL2 = video (not assessed). If the PR URL contains `Code-the-Dream-School`, it's pointed at the wrong base.
- The warmups require students to **paste the terminal command(s) and output as comments** in the `.py` files. That pasted text is the proof-of-work — for warmups, verify it's plausible and matches what the script actually does.

---

## Warmup 1: Prove Python Is Working — **Objective**

Prints one line; command + output pasted as a comment at the top:

```python
# Command: python warmup1.py
# Output:  Python is working!
```
```python
print("Python is working!")
```

**Correct if:** script prints `Python is working!` and the comment block shows the `python warmup1.py` command with matching output.
**Common miss:** comment block missing, or pasted output doesn't match the actual `print()`.

## Warmup 2: Navigate with the CLI — **Objective** (with subjective proof-of-work)

Asks for today's date with `input()` and echoes it in a sentence; navigation commands pasted as a comment.

```
What is today's date? April 24, 2026
You said today is April 24, 2026.
```
```python
# Navigation commands I used:
# cd Desktop/python-intro-homework
# cd week-2/assignment-2
```

**Correct if:** uses `input("What is today's date? ")` and prints the entered date back in a sentence; comment shows plausible `cd`/`ls`/`pwd` commands landing in `week-2/assignment-2/`.
**Common miss:** hard-coding the date instead of using `input()`; navigation comment missing or clearly bogus (e.g. paths that don't reach the assignment folder).

## Warmup 3: First Git Commit — **Objective** (with subjective proof-of-work)

Pastes `git log --oneline` output as a comment, then prints a short "what I learned" message.

```python
# git log --oneline output:
# a3f91bc Add warmup1 and warmup2 for week 2
```
```python
print("This week I learned how to run Python from the terminal and commit with Git.")
```

**Correct if:** comment shows real-looking `git log --oneline` output (short hash + message) with at least one meaningful commit, and the script prints a learning message.
**Common miss:** no pasted log, or a placeholder/copy-paste of the example verbatim rather than their own commit.

## Warmup 4: Read an Error Message — **Objective** (with subjective explanation)

A deliberate bug, run and read, then **fixed** so the file runs cleanly, plus a comment describing (1) the error text, (2) the cause, (3) the fix.

```python
# 1. Error: NameError: name 'nam' is not defined
# 2. Cause: typo — referenced 'nam' instead of 'name'
# 3. Fix: corrected the variable name to 'name'
name = "Sam"
print(f"Hello, {name}!")
```

**Correct if:** the submitted file runs without error (bug is fixed) and the comment names a real error type (`NameError`, `TypeError`, `SyntaxError`, etc.), what caused it, and how it was resolved.
**Common miss:** leaving the file broken (only introducing the bug, never fixing it); vague explanation that doesn't name the actual error or cause.

## Mini-Project: Temperature Converter — **Objective**

Prompts for Fahrenheit, converts with `celsius = (fahrenheit - 32) * 5 / 9`, prints the result rounded to one decimal via an f-string.

```
Enter a temperature in Fahrenheit: 72
72.0°F is 22.2°C.
```
```python
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius:.1f}°C.")
```

**Correct if:** input cast to a number, the given formula used (no library converter), and output rounded to exactly one decimal (`:.1f` or `round(celsius, 1)`) in an f-string. Check the math: 72 → 22.2, 32 → 0.0, 212 → 100.0.
**Common miss:** integer division or forgetting `float()` (breaks on decimal input); rounding to more/zero decimals; hard-coding a value instead of using `input()`.
