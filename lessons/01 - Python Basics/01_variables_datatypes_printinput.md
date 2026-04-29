# Variables, Data Types, Print/Input

**Objective**: By the end of this lesson, you will be able to:
  * Create variables and assign values to them
  * Identify and use Python's core data types: integers, floats, strings, and booleans
  * Display output with `print()` and collect user input with `input()`
  * Convert between data types using `int()`, `float()`, `str()`, and `bool()`
  * Use arithmetic, comparison, and logical operators
  * Format text using f-strings
  * Use common string methods like `split()`, `strip()`, `lower()`, and `replace()`

---

## Getting Started

For this first week, we'll be writing Python code in an **online IDE** — a website that lets you type and run Python code directly in your browser, with no installation needed. We'll set up Python on your own computer in Week 2.

**Go to [online-python.com](https://www.online-python.com/)** and try typing the following in the editor on the left, then click **Run**:

```python
print("Hello, world!")
```

You should see `Hello, world!` appear in the output panel. Congratulations — you just ran your first Python program!

---

## Variables

A **variable** is a name that stores a piece of data. Think of it like a labeled container — you choose the label, and Python remembers what's inside.

```python
name = "Jazmine"
age = 28
height = 5.8
```

In the code above:
- `name` stores the text `"Jazmine"`
- `age` stores the whole number `28`
- `height` stores the decimal number `5.8`

### Comments

You'll notice `#` symbols in many code examples throughout this course. The `#` marks a **comment** — Python ignores everything after `#` on that line. Comments are notes for humans reading the code, not instructions for the computer.

```python
# This is a comment — Python skips this line entirely
name = "Jazmine"   # This comment explains what the variable stores
```

The `=` sign in Python doesn't mean "equals" the way it does in math. It means **"assign the value on the right to the name on the left."**

You can change what a variable holds at any time:

```python
score = 10
print(score)  # Output: 10

score = 25
print(score)  # Output: 25
```

### Naming Rules

Python has a few rules for variable names:
- Use **lowercase letters** and separate words with **underscores**: `first_name`, `total_score`.
- Names can contain letters, numbers, and underscores, but **cannot start with a number**: `score1` is fine, `1score` is not.
- Choose **descriptive names** that make your code easy to read: `age` is better than `a`, and `student_count` is better than `x`.
- Avoid Python's reserved words like `if`, `for`, `True`, `False`, `while`, etc. Also avoid naming variables after built-in functions like `print`, `type`, or `input` — it won't cause an error, but it will stop those functions from working.

---

## Data Types

Every value in Python has a **type** — it tells Python what kind of data it's working with. The four most common types are:

| Type    | Syntax  | What it Stores          | Examples                               |
|---------|---------|-------------------------|----------------------------------------|
| Integer | `int`   | Whole numbers           | `42`, `-3`, `0`, `1000`                |
| Float   | `float` | Decimal numbers         | `3.14`, `-0.5`, `98.6`                 |
| String  | `str`   | Text (always in quotes) | `"hello"`, `"Code the Dream"`, `"123"` |
| Boolean | `bool`  | True or False           | `True`, `False`                        |

Examples:

```python
is_student = True        # Boolean
balance = 1000.75        # Float
first_name = "Charlie"   # String
number_of_days = 7       # Integer
```

You can check what type a value is using the `type()` function:

```python
print(type(42))          # Output: <class 'int'>
print(type(3.14))        # Output: <class 'float'>
print(type("hello"))     # Output: <class 'str'>
print(type(True))        # Output: <class 'bool'>
```

### A Note About Strings

Strings are text — any characters wrapped in quotation marks. You can use either single quotes `'hello'` or double quotes `"hello"`, but be consistent. If your text contains an apostrophe, use double quotes on the outside:

```python
message = "It's a great day!"
```

---

## Printing Output with `print()`

The `print()` function displays information on the screen. It's how your program communicates with the person running it.

```python
print("Welcome to Python!")
print(42)
print(3.14)
print(True)
```

You can print multiple items by separating them with commas. Python will add a space between each one:

```python
name = "Jazmine"
age = 28
print("Name:", name)          # Output: Name: Jazmine
print("Age:", age)            # Output: Age: 28
print(name, "is", age)        # Output: Jazmine is 28
```

---

## Collecting Input with `input()`

The `input()` function asks the user to type something and stores their response.

```python
name = input("What is your name? ")
print("Hello,", name)
```

When this code runs, it will:
1. Display `What is your name? ` and wait
2. The user types their name and presses Enter
3. Whatever they typed is stored in the variable `name`
4. The program prints a greeting using that name

**Important:** `input()` always returns a **string**, even if the user types a number. This matters when you want to do math with user input — we'll cover how to handle this in the next section.

```python
age = input("How old are you? ")
print(type(age))  # Output: <class 'str'> — it's text, not a number!
```

---

## Data Type Conversion

Sometimes you need to change a value from one type to another. This is called **type conversion** or **type casting**. Python gives you built-in functions for this:

| Function | What it does | Example |
|----------|-------------|---------|
| `int()` | Converts to a whole number | `int("42")` → `42` |
| `float()` | Converts to a decimal number | `float("3.14")` → `3.14` |
| `str()` | Converts to text | `str(42)` → `"42"` |
| `bool()` | Converts to True/False | `bool(1)` → `True` |

You might wonder why `bool(`) resolves to `True` — in Python, non-zero numbers are *truthy*.

### Why Does This Matter?

Remember how `input()` always returns a string? If you want to do math with user input, you need to convert it first:

```python
# This will NOT work the way you expect
age = input("Enter your age: ")
next_year = age + 1  # TypeError! You can't add a number to a string
```

```python
# This WILL work
age = input("Enter your age: ")
age = int(age)            # Convert the string to an integer
next_year = age + 1
print("Next year you will be", next_year)
```

You can also convert in one step:

```python
age = int(input("Enter your age: "))
```

**Watch out:** If the user types something that can't be converted, Python will crash with a `ValueError`. For example, `int("hello")` doesn't make sense and will cause an error. We'll learn how to handle this gracefully in Week 8 — for now, just be aware that conversion only works when the value makes sense for the target type.

### Implicit vs. Explicit Conversion

Python sometimes converts types **automatically** (called implicit conversion). For example, adding an integer and a float gives you a float:

```python
result = 3 + 2.5    # Python converts 3 to 3.0 automatically
print(result)        # Output: 5.5
print(type(result))  # Output: <class 'float'>
```

When you convert types yourself using `int()`, `float()`, `str()`, or `bool()`, that's called **explicit conversion**. Explicit is usually safer because you control exactly what happens:

```python
result = int(2.8) + 3   # You explicitly convert 2.8 to 2 (drops the decimal)
print(result)            # Output: 5
```

### AI Prompt: Retrieval Practice

Now that you've learned about variables, data types, and type conversion, let's test your understanding.

1. Open your preferred AI chatbot (ChatGPT, Microsoft Copilot, etc.)
2. Explain the difference between implicit and explicit data conversion in your own words.
3. Ask the AI to give you feedback on your explanation.

**Example Prompt:**
> "I just learned about implicit and explicit data conversion in Python. Here is my understanding of the difference: [your explanation]. Can you tell me what I got right and what I should refine in my understanding?"

---

## Operators

**Operators** are symbols that perform operations on values. Python has three main types.

### Arithmetic Operators

These do math:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `4 * 2` | `8` |
| `/` | Division | `9 / 3` | `3.0` |
| `//` | Integer division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation (power) | `2 ** 3` | `8` |

A few things to notice:
- `/` always gives you a float, even when the answer is a whole number: `9 / 3` gives `3.0`
- `//` drops the decimal part: `7 // 2` gives `3`, not `3.5`
- `%` gives you the remainder after division: `7 % 3` gives `1` because 7 divided by 3 is 2 with a remainder of 1

```python
total = 10 + 5
print(total)         # Output: 15

remainder = 10 % 3
print(remainder)     # Output: 1

squared = 4 ** 2
print(squared)       # Output: 16
```

### Comparison Operators

These compare two values and give you a boolean (`True` or `False`):

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 4` | `True` |
| `<` | Less than | `3 < 4` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `7 >= 3` | `True` |

Note the difference: `=` assigns a value, `==` checks if two values are equal.

```python
age = 20
print(age > 18)      # Output: True
print(age == 25)     # Output: False
```

### Logical Operators

These combine conditions:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and False` | `False` |
| `or` | At least one must be True | `True or False` | `True` |
| `not` | Reverses the value | `not True` | `False` |

```python
age = 20
has_id = True
print(age >= 18 and has_id)   # Output: True (both conditions are met)
print(age >= 21 or has_id)    # Output: True (at least one is met)
```

### AI Prompt: Predict-Then-Check

Study the following code **without running it**:

```python
x = 10
y = 3
print(x / y)
print(x // y)
print(x % y)
```

1. Predict what each line will print and why.
2. Open your preferred AI chatbot and use this prompt:

> "I'm learning Python operators. Looking at this code: [paste the code above]. I predict the output will be [your predictions] because [your reasoning]. Am I correct? If not, what am I misunderstanding?"

3. After the AI responds, run the code in [online-python.com](https://www.online-python.com/) to verify.

---

## Combining Strings

You can join strings together using the `+` operator. This is called **string concatenation**:

```python
first = "Code"
second = "the Dream"
combined = first + " " + second
print(combined)   # Output: Code the Dream
```

If you want to combine a string with a number, you must convert the number to a string first using `str()`:

```python
age = 28
message = "I am " + str(age) + " years old."
print(message)   # Output: I am 28 years old.
```

Without `str(age)`, Python will raise a `TypeError` because it doesn't know how to join text and numbers directly.

This works, but for longer messages it gets messy. The next section introduces a cleaner way.

---

## Formatted Strings (f-strings)

An **f-string** is a convenient way to put variables inside a string. You add the letter `f` before the opening quote, then put variable names inside curly braces `{}`:

```python
name = "Jazmine"
age = 28
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Jazmine and I am 28 years old.
```

This is much cleaner than the `+` concatenation approach from the previous section:

```python
# Using concatenation (harder to read)
print("My name is " + name + " and I am " + str(age) + " years old.")

# Using f-strings (much easier!)
print(f"My name is {name} and I am {age} years old.")
```

Notice that with f-strings, you don't need to convert `age` to a string with `str()` — Python handles it for you.

You can also do math inside the curly braces:

```python
price = 5
quantity = 3
print(f"Total: {price * quantity} items")    # Output: Total: 15 items
```

When working with decimal numbers, you may sometimes see unexpected results. Try running this:

```python
print(0.1 + 0.2)   # Output: 0.30000000000000004 (not 0.3!)
```

This is normal — computers store decimals approximately. To display a clean number with a specific number of decimal places, use `:.Nf` where N is the number of places you want:

```python
total = 0.1 + 0.2
print(f"Total: {total:.2f}")    # Output: Total: 0.30
```

---

## String Methods

Strings come with built-in tools called **methods** that let you transform and work with text. You use them by adding a dot `.` and the method name after the string or variable.

### Changing Case

```python
greeting = "Hello, World!"

print(greeting.lower())    # Output: hello, world!
print(greeting.upper())    # Output: HELLO, WORLD!
```

### Removing Extra Whitespace

`strip()` removes spaces (and other whitespace) from the beginning and end of a string. This is especially useful when working with user input:

```python
user_input = "   hello   "
print(user_input.strip())     # Output: hello
```

### Replacing Text

`replace()` swaps one piece of text for another:

```python
message = "I like cats"
new_message = message.replace("cats", "dogs")
print(new_message)   # Output: I like dogs
```

### Splitting Text into a List

`split()` breaks a string into a list of smaller strings at each space (or at a character you specify):

```python
sentence = "Code the Dream"
words = sentence.split()
print(words)   # Output: ['Code', 'the', 'Dream']

data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

Don't worry about lists yet — we'll cover them in depth in Week 4. For now, just know that `split()` breaks text apart.

### Joining Text Together

`join()` does the opposite of `split()` — it takes a list of strings and combines them:

```python
words = ["Code", "the", "Dream"]
combined = " ".join(words)
print(combined)   # Output: Code the Dream
```

---

## Videos

**Strings — Working with Textual Data** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=k9TUPpGqYTo) — covers string creation, concatenation, string methods, and f-string formatting.

**Integers and Floats — Working with Numeric Data** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=khKv-8q7YmY) — covers arithmetic operators, comparison operators, type conversion, and common numeric operations.

---

## AI Prompt: Scaffold Removal

Try the following exercise on your own before asking for help:

1. Write a short script that asks for a user's first name and last name using `input()`, then prints their full name in uppercase using an f-string and a string method.
2. If you get stuck, open your preferred AI chatbot and use one of these prompts:
   - *"I'm trying to combine input(), f-strings, and .upper() in Python. Can you give me 3 hints without giving me the answer?"*
   - *"I'm getting this error: [paste your error]. Ask me 3 questions that will help me solve this on my own."*

---

## Check for Understanding

**Question 1:** What type of data is stored in the variable `age` in the following code?

```python
age = 28
```

* A) String
* B) Integer
* C) Float
* D) Boolean

<details>
<summary>Answer</summary>

**B) Integer** — `28` is a whole number with no decimal point, so Python stores it as an `int`.

</details>

**Question 2:** What will the following code output?

```python
name = input("Enter your name: ")
print(type(name))
```

* A) `<class 'str'>`
* B) `<class 'int'>`
* C) It depends on what the user types
* D) An error

<details>
<summary>Answer</summary>

**A) `<class 'str'>`** — `input()` always returns a string, no matter what the user types.

</details>

**Question 3:** What will the following code output?

```python
num_str = "42"
num_int = int(num_str)
print(num_int + 8)
```

* A) `"428"`
* B) `50`
* C) `"50"`
* D) An error

<details>
<summary>Answer</summary>

**B) `50`** — The string `"42"` is converted to the integer `42`, then `42 + 8` gives `50`.

</details>

**Question 4:** What will the following code output?

```python
print(10 % 3)
```

* A) `3`
* B) `3.33`
* C) `1`
* D) `0`

<details>
<summary>Answer</summary>

**C) `1`** — The `%` operator gives the remainder. 10 divided by 3 is 3 with a remainder of **1**.

</details>

**Question 5:** What is the output of this code?

```python
name = "Jazmine"
print(f"Hello, {name}!")
```

* A) `Hello, name!`
* B) `Hello, {name}!`
* C) `Hello, Jazmine!`
* D) An error

<details>
<summary>Answer</summary>

**C) `Hello, Jazmine!`** — The `f` before the string makes it an f-string, so `{name}` is replaced with the value of the variable `name`.

</details>

---

## Further Reading

- [Python Official Documentation — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [W3Schools — Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [W3Schools — Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
