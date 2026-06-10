# Assignment 1 — Python Basics

## Submission Instructions

This week's work is done in an **online Python IDE** at [online-python.com](https://www.online-python.com/) — no local setup or GitHub yet.

Write all of your code in a single file. When you're done, use the **Share** button to generate a shareable link and submit it in CTD Learns.

> **Important:** online-python.com does not save your work automatically. Before closing your browser tab, either copy your code somewhere safe or generate your share link.

[**Here's a quick video explaining how to use online-python.com**](https://youtu.be/6GOKinRu0m0)

Submit two links in CTD Learns:
- **URL1:** A link to your video reflection
- **URL2:** Your shareable online-python.com link

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

Include the video link in the `URL1` field in the submission form.
