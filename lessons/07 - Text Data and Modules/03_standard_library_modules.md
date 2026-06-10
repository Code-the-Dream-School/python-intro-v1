# Standard Library Modules: `csv`, `os`, `datetime`, `argparse`

## Modules

### What Is a Module?

Python comes with a large collection of pre-built code you can use in your programs. This code is organized into **modules** — files that group related functions and tools together.

Instead of writing everything from scratch, you can import a module and use what's already in it.

### Importing Modules

There are a few different ways to bring a module's code into your program.

**Import the whole module**

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

When you use `import math`, you access its functions with the `math.` prefix. This makes it clear where each function comes from.

**Import a specific function**

```python
from math import sqrt
print(sqrt(16))  # Output: 4.0
```

`from math import sqrt` pulls just the `sqrt` function into your program directly, so you don't need the `math.` prefix.

**Use an alias**

```python
import math as m
print(m.sqrt(16))  # Output: 4.0
```

You can give a module a shorter nickname with `as`. This is common for modules with long names.

### The Python Standard Library

Python ships with a large set of modules built right in. This is called the **standard library**.

You've already worked with `csv` in the previous section. That's part of the standard library too. Here are a few more you'll use regularly:

| Module | What it does |
|--------|-------------|
| `csv` | Read and write CSV files |
| `os` | Work with files and folders on your computer |
| `datetime` | Work with dates and times |
| `math` | Mathematical functions |
| `random` | Generate random numbers |
| `argparse`| Parse command-line arguments |

You can browse the full standard library in the [official Python documentation](https://docs.python.org/3/library/index.html).

### Finding Your Way Around the Python Docs

The Python documentation is your reference guide for the standard library. Knowing how to read it is a useful skill.

When you look up a module, you'll find a description of what it does, a list of its functions with explanations, and example code. For example, try searching for "python datetime module" or go directly to the [datetime docs page](https://docs.python.org/3/library/datetime.html). You'll see `datetime.now()`, `.strftime()`, and other functions listed with their parameters and descriptions.

**Tip**: When the docs show something like `strftime(format)`, `format` is a placeholder for the argument you'll pass — the docs explain what values are accepted.

### Working with `os`

The `os` module lets your Python programs interact with the file system — finding where you are, checking if files exist, building paths, and listing folder contents.

**Get your current location**

```python
import os
print(os.getcwd())  # e.g., /Users/yourname/projects
```

`os.getcwd()` returns the directory your script is currently running from. This is useful when Python can't find a file and you're not sure where it's looking.

**Check if a file or folder exists**

```python
import os
if os.path.exists("data.csv"):
    print("Found it!")
else:
    print("File not found.")
```

It's good practice to check that a file exists before trying to open it.

**Build paths that work on any computer**

```python
import os
path = os.path.join("data", "sales", "report.csv")
print(path)
# Mac/Linux: data/sales/report.csv
# Windows:   data\sales\report.csv
```

File paths use different separators on different operating systems (`/` on Mac/Linux, `\` on Windows). `os.path.join()` builds the path correctly for whatever system is running your code — making your scripts portable.

**List files in a folder**

```python
import os
files = os.listdir("data")
print(files)  # ['report.csv', 'summary.txt', ...]
```

`os.listdir()` returns a list of everything in a folder — both files and subfolders.

### Working with `datetime`

The `datetime` module makes it straightforward to work with dates and times.

**Get the current date and time**

```python
from datetime import datetime
now = datetime.now()
print(now)  # e.g., 2024-03-15 14:32:05.123456
```

**Create a specific date**

```python
from datetime import datetime
birthday = datetime(1995, 6, 20)  # year, month, day
print(birthday)  # 1995-06-20 00:00:00
```

**Format a date as a readable string**

```python
from datetime import datetime
now = datetime.now()
print(now.strftime("%B %d, %Y"))  # e.g., March 15, 2024
```

`.strftime()` converts a datetime into a formatted string. The codes like `%B` and `%Y` represent parts of the date. Common ones:

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Four-digit year | 2024 |
| `%m` | Month as a number | 03 |
| `%B` | Full month name | March |
| `%d` | Day of the month | 15 |
| `%H` | Hour (24-hour) | 14 |
| `%M` | Minute | 32 |

You can find the full list of format codes in the [Python docs](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

### Working with `argparse`

The `argparse` module lets your scripts accept input from the command line, so users can customize behavior without editing the code itself.

Unlike the modules above, `argparse` involves a few setup steps rather than a single function call. The typical pattern is: create a parser, define what arguments to expect, then parse them. You have the option to use `argparse` in your final project, feel free to try the example yourself:

**Example:**

```python
import argparse

parser = argparse.ArgumentParser(description="Greet a user")
parser.add_argument("name", help="The name to greet")
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

Run it like this:

```
python greet.py Ada
# Output: Hello, Ada!
```

**Optional Arguments**

```python
parser.add_argument("--loud", action="store_true", help="Greet loudly")
```

Arguments starting with `--` are optional. `action="store_true"` means the flag is either present (`True`) or absent (`False`).

**Built-in Help**

`argparse` automatically generates a `--help` flag for your script:

```
python greet.py --help
```

This is especially useful once you combine `argparse` with `os` and `datetime` — for example, writing a script that takes a folder path as an argument and reports when each file was last modified.

### Check for Understanding

**Question**: You want to import only the `getcwd` function from the `os` module. Which of the following is correct?

* A) `import getcwd from os`
* B) `import os.getcwd`
* C) `from os import getcwd`
* D) `import os as getcwd`

<details>
<summary>Answer</summary>

**Answer**: C) `from os import getcwd`

</details>

