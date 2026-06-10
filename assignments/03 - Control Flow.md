# Assignment 3 — Control Flow

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-3` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-3/`, create a new `assignment-3/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-3` into `main`

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

Ask the user for a number. Using two **separate** `if`/`elif`/`else` blocks — one for sign, one for parity — print two lines of output:

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

Example output:
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

Include the video link in your pull request description or the `URL1` field in the submission form.

---

## Review: The GitHub Cycle

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-3
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-3  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
