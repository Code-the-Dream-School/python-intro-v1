# `if` / `else` and Comparison Operators

**Objective:** By the end of this lesson, you'll be able to:

* Explain the role of indentation in Python syntax for defining code blocks and scope, contrasting it with languages that use braces `{}`.
* Implement proper indentation syntax, including the use of colons `:` and adhering to the 4-space community standard without mixing tabs and spaces.
* Identify and troubleshoot `IndentationError` bugs in Python scripts.
* Utilize comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) to evaluate conditions and return boolean values.
* Differentiate between the assignment operator (`=`) and the equality operator (`==`).
* Construct conditional structures using `if`, `elif`, and `else` to control program execution flow based on specific conditions.
* Convert user input strings into integers using `int()` to enable numerical comparisons.
* Analyze and trace the execution flow of nested conditional statements and rewrite them into flatter, more readable structures.

## Block Structure and Indentation

In Python, indentation plays a crucial role in the syntax of the language. Unlike many other programming languages, which use braces `{}` or other markers to denote code blocks, Python uses indentation to group statements and define the scope of loops, functions, classes, and conditional statements.

**Why Indentation Matters in Python**

* **Defining Code Blocks:** Indentation tells Python where a block of code begins and ends.
* **Enforcing Readability:** The clean and readable structure makes Python code easier to follow.

**Key Concepts:**

* **Indentation in Control Structures:**
    * All code under control structures (such as `if`, `else`, `for`, `while`, and function definitions) must be indented. You always put a colon `:` before starting an indented block on the next line.

* **Consistent Indentation:**
    * Consistency is key. Python does not allow mixing tabs and spaces. Use either spaces or tabs but never both.
    * The Python community's standard is to use 4 spaces per indentation level.

**Block Structure Example:**

```python
def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
```

In the above example, the function `check_number` defines the first level of indentation. The `if`, `elif`, and `else` blocks define additional indentation levels for the code that falls under each condition.

**Indentation Error Example:**

```python
def check_number(num):
if num > 0:          # Error: this line should be indented inside the function
    print("Positive number")
```

In the above case, Python will raise an error: `IndentationError: expected an indented block`.

Read [this article from Geeks for Geeks](https://www.geeksforgeeks.org/indentation-in-python/) to learn more about the importance of indentation, format, and structure when writing code blocks in Python.


## Conditional Statements

Conditional statements enable code to execute only when specific conditions are met. Python uses `if`, `elif`, and `else` statements to handle different conditions.

### Comparison Operators

Before writing conditionals, you need a way to compare values. **Comparison operators** evaluate two values and return either `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 4` | `True` |
| `<` | less than | `3 < 4` | `True` |
| `>` | greater than | `10 > 5` | `True` |
| `<=` | less than or equal to | `5 <= 5` | `True` |
| `>=` | greater than or equal to | `7 >= 3` | `True` |

> **Watch out:** `==` checks whether two values are *equal*. A single `=` assigns a value to a variable — these are different and easy to mix up!

### if, elif, and else

* `if`: Checks the initial condition. If `True`, it runs the code block.
* `elif`: Stands for "else if"; checks an additional condition if the previous one was `False`.
* `else`: Runs if none of the previous conditions were `True`.

```python
age = 20

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

**Try it yourself:** Replace the first line with the version below and run the script. You can type in any age and see which message prints.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

> **Why `int()`?** The `input()` function always returns a string. Wrapping it in `int()` converts the string `"20"` into the number `20` so you can compare it with `>=`.

### Nested Conditionals

You can nest conditionals inside each other for more complex decision-making.

```python
score = 85

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        print("C")
```

> **Tip:** You can usually rewrite nested `if`/`else` blocks as a flat `if`/`elif`/`else` chain, which is easier to read. The example above could become `if score >= 90 ... elif score >= 80 ... else ...`.


### Check for Understanding

**Question:** What will the following code output if `age = 16`?

```python
if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

* A) "You're an adult!"
* B) "You're a teenager."
* C) "You're a child."
* D) No output

<details>

<summary>View answer</summary>

**Answer**: B) "You're a teenager."

`16 >= 18` is `False`, so the `if` branch is skipped. `16 >= 13` is `True`, so the `elif` branch runs.

</details>


## AI Learning Prompt: Retrieval Practice

Now that you've read about conditionals, let's reinforce that knowledge:

1. Open your preferred AI chatbot (CTD's AI Reviewer, ChatGPT, etc.).
2. Explain in your own words how `if`, `elif`, and `else` work together — and what happens when more than one condition could be `True`.
3. Ask the AI to give you feedback on your explanation.

**Example Prompt:**

> "I just learned about `if`, `elif`, and `else` in Python. Here's my understanding of how they work: [your explanation]. Can you tell me what I got right and what I should refine?"
