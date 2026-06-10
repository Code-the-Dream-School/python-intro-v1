# Reading and Writing .txt and .csv Files

In Python, reading from and writing to text files is handled with the `open()` function. Text files contain plain text data, making them useful for storing logs, configuration settings, or simple data exports.

### Reading a Text File

To read a file, use `open()` with the `"r"` (read) mode.

```python
with open('example.txt', 'r') as file:
    content = file.read()  # Read the entire file as one string
    print(content)
```

The `with` statement ensures the file is closed automatically when the block exits — even if an error occurs. You always want to close files when you're done with them, and `with` handles that without extra code. You'll see this same pattern later in the course when working with database connections.

**Reading line by line**

If you want to process a file one line at a time, you can iterate over it directly or use `.readlines()`:

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character at the end
```

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()  # Returns a list — one string per line
    print(lines[0])           # First line
```

**Handling errors**

File operations can raise exceptions — for example, if the file doesn't exist or you don't have permission to open it. Wrapping them in a `try` block makes your code more robust:

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
```

You'll learn more about exception handling in a later lesson — for now, know that `try/except` is the standard way to handle file errors gracefully.

### Writing to a Text File

To write to a file, open it in `"w"` (write) or `"a"` (append) mode.

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
```

`"w"` mode creates the file if it doesn't exist, or **overwrites it completely** if it does. Use this carefully — existing content will be lost.

`"a"` (append) mode adds new content to the end of the file without touching what's already there:

```python
with open('example.txt', 'a') as file:
    file.write("\nA new line.")  # \n adds a newline before the new content
```

`write()` does not add a newline automatically — include `'\n'` in your string when you need one.

### Reading and Writing CSV Files

CSV (Comma-Separated Values) files store tabular data: each row is a line, and values are separated by commas. Python's built-in `csv` module handles the parsing and formatting for you.

#### Reading a CSV File

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings
```

#### Writing to a CSV File

```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])       # Header row
    writer.writerow(['Jazmine', 30, 'New York'])    # Data row
    writer.writerow(['Luis', 35, 'Chicago'])
```

The `newline=''` argument prevents extra blank lines from appearing on Windows.

#### Reading a CSV with DictReader

`csv.DictReader` works like `csv.reader`, but each row comes back as a dictionary with the column headers as keys. This makes your code more readable — you access values by name instead of index.

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])
```

No need to skip the header row or remember that index `0` is the name and index `1` is the age.

#### Writing a CSV with DictWriter

`csv.DictWriter` lets you write rows as dictionaries. You define the column names upfront, write a header row, then write your data:

```python
import csv

rows = [
    {'Name': 'Jazmine', 'Age': 30, 'City': 'New York'},
    {'Name': 'Luis', 'Age': 35, 'City': 'Chicago'},
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    writer.writerows(rows)
```

`DictReader` and `DictWriter` are especially useful when your CSV has many columns, or when you're reading data, transforming it, and writing it back out. The next section builds directly on this pattern.

### Video: Reading and Writing a CSV File

In this video, we'll demonstrate reading and writing to a real CSV file. After the video, practice using the W3 Resource tutorial [here](https://www.w3resource.com/python-exercises/csv/index.php).

**[View the video here](https://youtu.be/MWYRGLKMzAQ?feature=shared).**

### Check for Understanding

**Question**: What does the `"w"` mode do when opening a file in Python?

* A) Reads the file without making changes.
* B) Appends new data to the end of the file.
* C) Overwrites the file with new data, creating it if it doesn't exist.
* D) Opens the file for reading and writing without overwriting.

<details>
<summary>Answer</summary>

**Answer**: C) Overwrites the file with new data, creating it if it doesn't exist.

</details>

### AI Prompt: Retrieval Practice

Now that you have explored file handling and different file modes, let's check your knowledge:
1. Open your AI chatbot.
2. Explain the difference between opening a file in `"w"` (write) mode versus `"a"` (append) mode.
3. Ask the AI: "In what specific scenario would I accidentally lose data if I used the wrong mode?"

**Example prompt:** "I am learning about Python file modes. I think `'w'` mode is for [your explanation] and `'a'` mode is for [your explanation]. Is this correct? Also, can you explain the risk of using `'w'` on an existing file?"
