# Refactoring Earlier Scripts Into Functions

You can write working Python scripts without ever defining a function. But as scripts grow, code written top-to-bottom becomes hard to read, hard to change, and impossible to reuse.

**Refactoring** means restructuring code without changing what it does. In this section, you'll take a working script and break it into well-named functions, step by step.

### The Starting Script

Here's a grade calculator that collects test scores, computes an average, assigns a letter grade, and prints a summary — the kind of script you'd write using tools from earlier weeks.

```python
name = input("Enter your name: ")

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

average = (score1 + score2 + score3) / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nStudent: {name}")
print(f"Average score: {average:.1f}")
print(f"Letter grade: {grade}")
```

This works, but everything is tangled together at the top level: input, calculation, and output are mixed in one flat sequence. There's no way to reuse the grading logic in another script, and changing one part risks breaking another.

### Step 1 — Identify Logical Chunks

Before writing any functions, read through the script and ask: "What distinct tasks is this doing?"

Annotating the script:

```python
# --- Task 1: Collect student name and scores ---
name = input("Enter your name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

# --- Task 2: Compute the average ---
average = (score1 + score2 + score3) / 3

# --- Task 3: Assign a letter grade ---
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# --- Task 4: Display the results ---
print(f"\nStudent: {name}")
print(f"Average score: {average:.1f}")
print(f"Letter grade: {grade}")
```

Four clear tasks. Each one is a good candidate for a function. A useful rule: **if you can describe a block in one sentence, it's probably a function**.

### Step 2 — Extract Functions One at a Time

Start with the simplest chunk and work outward.

**Extract Task 2: compute the average**

```python
def calculate_average(scores):
    return sum(scores) / len(scores)
```

Now that logic is reusable — you could call it with any list of numbers.

**Extract Task 3: assign the letter grade**

```python
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
```

**Extract Task 1: collect scores**

```python
def get_student_info():
    name = input("Enter your name: ")
    scores = []
    for i in range(1, 4):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)
    return name, scores
```

Notice this version uses a loop instead of three separate variables. This is a cleaner approach now that we're thinking in functions.

**Extract Task 4: display results**

```python
def print_summary(name, average, grade):
    print(f"\nStudent: {name}")
    print(f"Average score: {average:.1f}")
    print(f"Letter grade: {grade}")
```

### Step 3 — Add Docstrings

A **docstring** is a one-line string at the top of a function body that describes what it does, enclosed in triple quotes:

```python
def calculate_average(scores):
    """Return the average of a list of numeric scores."""
    return sum(scores) / len(scores)

def assign_grade(average):
    """Return a letter grade (A–F) for a given numeric average."""
    if average >= 90:
        return "A"
    ...
```

Write a docstring when a function's purpose isn't immediately obvious from its name. One clear sentence is enough. Docstrings show up in editor tooltips and in Python's built-in `help()` system, they're the lightest form of documentation that actually travels with the code.

### Step 4 — The `if __name__ == "__main__":` Guard

Now that your functions are defined, where does the code that *calls* them go?

The professional pattern is to put it inside a guard:

```python
if __name__ == "__main__":
    name, scores = get_student_info()
    average = calculate_average(scores)
    grade = assign_grade(average)
    print_summary(name, average, grade)
```

**What does this do?** `__name__` is a special variable Python sets automatically. When you run a file directly (`python grades.py`), Python sets `__name__` to `"__main__"`. When another file *imports* your file, `__name__` is set to the module name instead.

Without this guard, all your top-level code runs automatically the moment anyone imports your file. With it, only the function definitions are loaded on import — the program only runs when you execute the file directly. This becomes important when you start building multi-file programs.

### The Final Refactored Script

```python
def get_student_info():
    """Prompt for a student's name and three test scores."""
    name = input("Enter your name: ")
    scores = []
    for i in range(1, 4):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)
    return name, scores


def calculate_average(scores):
    """Return the average of a list of numeric scores."""
    return sum(scores) / len(scores)


def assign_grade(average):
    """Return a letter grade (A–F) for a given numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def print_summary(name, average, grade):
    """Print a formatted grade report."""
    print(f"\nStudent: {name}")
    print(f"Average score: {average:.1f}")
    print(f"Letter grade: {grade}")


if __name__ == "__main__":
    name, scores = get_student_info()
    average = calculate_average(scores)
    grade = assign_grade(average)
    print_summary(name, average, grade)
```

Compare this to the original. The behavior is identical. But now:
- Each function can be understood in isolation
- `calculate_average` and `assign_grade` can be reused in other scripts
- The `if __name__ == "__main__":` block reads like a table of contents for how the program flows

### AI Learning Prompt: Scaffold Removal

Here is a short script with no functions:

```python
print("=== Temperature Converter ===")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

if fahrenheit > 100:
    description = "hot"
elif fahrenheit > 60:
    description = "warm"
else:
    description = "cold"

print(f"{celsius}°C is {fahrenheit:.1f}°F — that's {description}.")
```

Your task: refactor this script into named functions. Then use the following AI prompt to get feedback:

> "I'm learning to refactor Python scripts into functions. Here's my original script: [paste original]
> Here's my refactored version: [paste your version]
> Can you evaluate my refactoring? Did I break it into reasonable functions? Are my function names clear? Did I handle parameters and return values correctly? What would you do differently?"

### Check for Understanding

**Question**: Which of the following is the best reason to extract a block of code into a function?

* A) The block is more than 5 lines long
* B) The block performs one clear task that might be reused or tested on its own
* C) The block contains an `if` statement
* D) The block uses a variable defined elsewhere in the script

<details>
<summary>View answer</summary>

**Answer**: B) A function should do one clear thing. Length and the presence of conditionals aren't reliable indicators — what matters is whether the logic is cohesive and whether isolating it makes the code easier to understand and reuse.

</details>

**Question**: What does the `if __name__ == "__main__":` guard do?

* A) It prevents functions from being called more than once
* B) It ensures the script only runs when executed directly, not when imported as a module
* C) It defines the entry point that every Python program requires
* D) It checks whether the script has syntax errors before running

<details>
<summary>View answer</summary>

**Answer**: B) When a file is run directly, Python sets `__name__` to `"__main__"`. When it's imported by another file, `__name__` is the module's name instead. The guard lets other files import your functions without triggering the top-level program logic.

</details>

**Question**: What is a docstring and where does it go?

* A) A comment placed above a function that describes its parameters
* B) A string literal on the first line inside a function body, enclosed in triple quotes
* C) A special variable that stores a function's return value
* D) A description written into the `def` line

<details>
<summary>View answer</summary>

**Answer**: B) A docstring is a string literal placed as the first statement inside a function body, using triple quotes (`"""`). It describes what the function does and is accessible via Python's `help()` system and editor tooltips.

</details>
