# Debugging Basics

**Objective**: By the end of this lesson, you will be able to:
  * Read a Python error message and identify the error type and line number
  * Recognize common error types: `SyntaxError`, `NameError`, `TypeError`, `ValueError`, and `IndentationError`
  * Use `print()` statements to inspect variable values and trace program flow
  * Apply a systematic approach to finding and fixing bugs

---

## What Is Debugging?

**Debugging** is the process of finding and fixing errors (called **bugs**) in your code. Every programmer, from beginners to professionals, spends time debugging. It's not a sign that you're doing something wrong; it's a normal part of writing code.

The good news is that Python tries to help you. When something goes wrong, Python gives you an **error message** that tells you what happened and where. Learning to read these messages is one of the most valuable skills you can develop.

---

## Reading Error Messages

When Python runs into a problem, it stops and displays an error message called a **traceback**. Let's look at one:

```python
print("Hello)
```

Output:
```
  File "main.py", line 1
    print("Hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

This looks scary at first, but it's actually giving you three useful pieces of information:

1. **Where**: `line 1` tells you which line the error is on
2. **What**: `SyntaxError` tells you the type of error
3. **Why**: `unterminated string literal` tells you what went wrong (in this case, a missing closing quote)

**Tip:** Always read error messages from the **bottom up**. The last line tells you the error type and description, and that's usually all you need to start fixing the problem.

**Note:** Error messages may look slightly different depending on your Python version or IDE. The important parts (the error type, line number, and description) are always there.

---

## Common Error Types

Here are the five errors you'll see most often as a beginner. Learning to recognize them will save you a lot of time.

### SyntaxError

Python found something it can't understand, usually due to a mistake in your code's structure. Your code won't run at all.

```python
print("Hello"
```

```
SyntaxError: '(' was never closed
```

Common causes: missing closing parenthesis `)`, missing closing quote `"`, missing colon `:`, using `=` instead of `==`.

### NameError

Python found a name it doesn't recognize. This usually happens when a variable hasn't been created yet or when a variable name is misspelled.

```python
print(mesage)
```

```
NameError: name 'mesage' is not defined
```

In this case, we misspelled `message` as `mesage`. Python doesn't guess what you meant; it only knows exact names.

This also happens when you try to use a variable that doesn't exist:

```python
print(total)
```

```
NameError: name 'total' is not defined
```

Here, the variable `total` was never created. You may have forgotten to define it, or it might be defined further down in your code (remember, Python runs top to bottom).

### TypeError

Python tried to do something with the wrong type of data. This happens when you mix types that Python can't combine, like adding a string and a number.

```python
age = "25"
print(age + 5)
```

```
TypeError: can only concatenate str (not "int") to str
```

Python sees `"25"` as text (a string) and `5` as a number (an integer). Since these are different types, Python doesn't know whether you want text concatenation or math addition. You'd fix this with `int(age) + 5` (if you want math) or `age + str(5)` (if you want text).

### IndentationError

Python uses spaces at the beginning of lines to understand the structure of your code. If the spacing is wrong, you get this error.

```python
name = "Jazmine"
  print(name)
```

```
IndentationError: unexpected indent
```

In this case, `print(name)` has extra spaces at the beginning that shouldn't be there. We haven't worked with indentation much yet (it becomes important in Week 3 with `if` statements), but if you see this error, check for accidental spaces at the start of a line.

### ValueError

Python received a value that has the right type but doesn't make sense for the operation, like trying to convert a word into a number.

```python
number = int("hello")
```

```
ValueError: invalid literal for int() with base 10: 'hello'
```

You'll see this often when using `int(input(...))` and the user types something that isn't a number. For now, just make sure to enter valid numbers when prompted. We'll learn how to handle this gracefully in Week 8.

---

## Debugging with Print Statements

When your code runs but produces the wrong result (no error message, just wrong output), `print()` statements are your best friend. This technique lets you peek inside your program to see what's actually happening.

### How It Works

Add temporary `print()` calls to check the values of your variables at different points in your program:

```python
bill = input("Bill amount? $")
tip_rate = input("Tip %? ")

print("DEBUG bill:", bill, type(bill))            # What is bill?
print("DEBUG tip_rate:", tip_rate, type(tip_rate)) # What is tip_rate?

bill = float(bill)
tip_rate = float(tip_rate)

print("DEBUG after conversion:", bill, tip_rate)   # Did conversion work?

tip_amount = bill * (tip_rate / 100)
print("DEBUG tip_amount:", tip_amount)             # Is the math correct?

total = bill + tip_amount
print(f"Total: ${total:.2f}")
```

By labeling each print with `"DEBUG"`, you can spot which lines are temporary and remove them once you've found the bug.

### Tips for Effective Print Debugging

- **Label your prints** so you know which one produced which output: use `"DEBUG variable_name:"` instead of just printing the value
- **Print the type too** by using `type()`, since many bugs come from a variable being a string when you expected a number
- **Add prints before and after** the line you suspect is causing the problem
- **Remove or comment out** your debug prints once you've fixed the issue (don't leave them in your final code)

### AI Prompt: Scaffold Removal

If you encounter a bug while practicing code from this lesson, don't ask the AI for the solution. Instead, try these prompts:

- *"I'm getting this error in my Python code: [paste the error message]. Can you give me 3 hints to help me figure out what's wrong, without giving me the answer?"*
- *"There's a bug in my code and I'm getting this error: [paste error]. Ask me 3 questions that will help me solve this on my own."*

---

## Putting It All Together

Here's a quick exercise. This code has **two bugs**. Try to spot them before reading the explanations:

```python
Name = "Jazmine"
print(f"Hello, {name}!")
age = input("How old are you? ")
next_year = age + 1
print(f"Next year you will be {next_year}")
```

**Important:** Python stops at the first error it encounters, so you'll only see one bug at a time. Fix it, run again, and the next one will appear. This is normal! Debugging is often a process of fixing one thing, running, finding the next issue, and repeating.

<details>
<summary>Bug 1</summary>

**NameError**: The variable is created as `Name` (capital N) on line 1, but used as `name` (lowercase n) on line 2. Python treats these as two completely different names. Fix: change `Name` to `name` on line 1.

</details>

<details>
<summary>Bug 2</summary>

**TypeError**: On line 4, `age` is a string (from `input()`) and `1` is an integer. Python can't add them together. Fix: convert `age` to an integer first with `int(age) + 1`.

</details>

Here's the corrected version:

```python
name = "Jazmine"
print(f"Hello, {name}!")
age = input("How old are you? ")
next_year = int(age) + 1
print(f"Next year you will be {next_year}")
```

---

## Videos

**"Introduction to Debugging in Python"** (LinkedIn Learning)

[Watch the video](https://www.youtube.com/watch?v=b7VbiZBg-dA), a short introduction to debugging concepts in Python, including reading error messages and common debugging techniques.

---

## AI Prompt: Retrieval Practice

Test your understanding of error types:

1. Open your preferred AI chatbot (ChatGPT, Microsoft Copilot, etc.)
2. Explain the difference between a `SyntaxError` and a `TypeError` in your own words.
3. Give an example of code that would cause each one.
4. Ask the AI to give you feedback on your explanation.

**Example Prompt:**
> "I just learned about Python error types. Here is my understanding of the difference between SyntaxError and TypeError: [your explanation], with these examples: [your code examples]. Can you tell me what I got right and what I should refine?"

---

## Check for Understanding

**Question 1:** You see this error message. What is the problem?

```
NameError: name 'score' is not defined
```

* A) Python doesn't have a variable called `score`
* B) The variable `score` has the wrong value
* C) There's a typo in the `print` function
* D) Python ran out of memory

<details>
<summary>Answer</summary>

**A) Python doesn't have a variable called `score`**. A `NameError` means you used a name that Python hasn't seen before. Either you forgot to create the variable, misspelled it, or it's defined on a later line.

</details>

**Question 2:** What is the primary purpose of using `print()` statements in debugging?

* A) To find and check variable values and program flow
* B) To slow down the program
* C) To remove errors automatically
* D) To show only the final output

<details>
<summary>Answer</summary>

**A) To find and check variable values and program flow**. Debug prints let you see what your variables actually contain at specific points, so you can figure out where things go wrong.

</details>

**Question 3:** What will this code produce?

```python
age = "20"
new_age = age + 1
print(new_age)
```

* A) `21`
* B) `"201"`
* C) A `TypeError`
* D) A `SyntaxError`

<details>
<summary>Answer</summary>

**C) A `TypeError`**. `age` is a string and `1` is an integer. Python can't add them together. You'd need `int(age) + 1` to get `21`.

</details>

**Question 4:** When reading a Python error message, which part should you read first?

* A) The first line
* B) The middle section
* C) The last line
* D) The file name

<details>
<summary>Answer</summary>

**C) The last line**. The last line of a traceback tells you the error type and a description of what went wrong. Read from the bottom up.

</details>

---

## Further Reading

- [W3Schools: Python Try Except](https://www.w3schools.com/python/python_try_except.asp), a preview of error handling (covered in depth in Week 8)
- [Python Official Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)
