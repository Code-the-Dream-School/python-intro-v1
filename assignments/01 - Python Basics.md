# Assignment 1 — Python Basics

## Submission Instructions

This week's work is done in **Google Colab**, a free cloud notebook you run in your browser at [colab.research.google.com](https://colab.research.google.com/) — we'll work on local setup next week.

<!-- TODO: replace with a short video (or written walkthrough) showing how to use Google Colab. The previous link was an online-python.com walkthrough and no longer applies. -->

1. **Keep your whole script in one cell.** Colab lets you split code across multiple cells, but for this assignment put all of your code in a **single cell** so it runs top to bottom, just like the `.py` file you'll submit. See the Simple Scripts lesson for why this matters.
2. **Saving:** Colab saves automatically to your Google Drive as long as you're signed in with your Google account, so your notebook will be there next time. You can also save any time with **File → Save**.

When you're finished, you'll upload your code to the GitHub repository you created in Lesson 1.4 using GitHub's web editor and open a pull request. The steps below walk you through the whole process.

> **Don't feel concerned if the GitHub steps feel unfamiliar.** Terms like "branch" and "pull request" will be covered in detail in Weeks 2 and 3. For now, just follow the steps below. You don't need to understand what they mean yet.

Submit two links in CTD Learns:
- **URL1:** A link to your pull request on GitHub (see steps below)
- **URL2:** A link to your video reflection

---

### Step 1 — Copy your code from Google Colab

In Colab, click anywhere inside your code cell, select all of your code (**Ctrl+A** on Windows, **Cmd+A** on Mac), and copy it (**Ctrl+C** / **Cmd+C**). Because you kept everything in one cell, this grabs your entire script at once.

### Step 2 — Create a new file in your GitHub repository

1. Go to [github.com](https://github.com) and open the repository you created in Lesson 1, Section 4: Version Control (it should be named something like `maria-santiago-python`)
2. Click the **Add file** button near the top right, then choose **Create new file**
3. In the filename field at the top, type `assignment-1.py`
4. Click in the large text area below the filename and paste your code (**Ctrl+V** / **Cmd+V**)

### Step 3 — Commit to a new branch and open a pull request

Scroll down to the **Commit new file** section at the bottom of the page.

1. Leave the commit message as-is or write something brief like `Add assignment 1`
2. Select **Create a new branch for this commit and start a pull request**
3. GitHub will suggest a branch name — change it to `assignment-1`
4. Click **Propose new file**
5. On the next page (Open a pull request), click **Create pull request**

You now have an open pull request. Copy the URL from your browser's address bar — it will look like `https://github.com/your-username/your-repo-name/pull/1`. This is what you submit in CTD Learns as **URL1**.

### If you need to update your submission

If you need to make changes after submitting (for example, if your mentor asks you to fix something) you don't need to open a new pull request. Just edit the file on the same branch:

1. Go to your repository on GitHub
2. Click the branch dropdown (it says **main** by default) and select **assignment-1**
3. Click on `assignment-1.py` to open the file
4. Click the **pencil icon** (Edit this file) in the top right of the file view
5. Make your changes in the editor
6. Scroll down to **Commit changes**, leave the option set to **Commit directly to the `assignment-1` branch**, and click **Commit changes**

As before, grab the link and complete the assignment submission form.

---

## Assignment: Profile Card Builder

This week, you'll write one script that builds up to a formatted profile card. Each section adds a new concept.

Work through the sections in order. You don't need to delete earlier sections as you go; just keep adding to the same file.

---

### Section 1: Variables and Types

Declare one variable of each of the four basic types below, then print each variable along with its type using `type()`:

```python
name = "Alex"
age = 27
height = 5.9
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
```

Expected output:
```
Alex <class 'str'>
27 <class 'int'>
5.9 <class 'float'>
True <class 'bool'>
```

Use your own values — not the ones above!

---

### Section 2: User Input and Math

Add to your script: use `input()` to ask for the user's name and the year they were born. Compute their approximate age and print a sentence:

```
Hi, Jordan! You are approximately 24 years old.
```

> **Hint:** `input()` always returns a string. Convert the birth year to `int` before doing math.

---

### Section 3: Type Conversion and f-strings

Add to your script: ask the user to enter two numbers (as separate inputs). Convert both to `float`, multiply them, and print the result using an f-string:

```
12.5 × 4.0 = 50.0
```

---

### Section 4: Formatted Receipt

Add to your script: using only variables and `print()` — no `input()` — print a formatted receipt. Store the item name, price, and quantity in variables, and compute the total from those variables:

```
===========================
        RECEIPT
===========================
Item:      Python textbook
Price:     $29.99
Quantity:  2
---------------------------
Total:     $59.98
===========================
```

Use your own item, price, and quantity.

---

### Section 5: Mini-Project — Profile Card

Finally, tie it all together. Use `input()` to ask the user for:

1. Their name
2. Their hometown
3. Their favorite hobby
4. One fun fact about themselves
5. The year they were born

Then print a formatted profile card using f-strings. Compute their age from the birth year — don't ask for it directly.

```
╔══════════════════════════════╗
      PROFILE: Alex Rivera
╚══════════════════════════════╝
Hometown:   Chicago, IL
Hobby:      Rock climbing
Fun fact:   I've visited 12 countries.
Age:        27
```

Align the labels so the output looks clean.

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is a variable, and why does Python require you to pay attention to data types when writing code? Give an example from your assignment.
2. Walk through one section of your script and explain what it does line by line.
3. Describe a Python error message you encountered. What did it tell you, and how did you resolve it?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in the `URL2` field in the submission form.
