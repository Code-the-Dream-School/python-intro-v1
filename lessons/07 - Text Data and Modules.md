# Lesson 7 — Text Data & Modules

**Lesson Overview**
So far, every value your programs have used was either typed into the code or entered by the user at runtime. This week you'll learn to read from and write to files, which means your programs can now work with data that exists in the real world: spreadsheets, logs, exported records. You'll also learn how Python's module system lets you tap into a library of pre-built tools, so you can spend more time solving problems and less time writing things from scratch.

**Learning Objectives**

This week, I can...

* Read from and write to .txt and .csv files using `open()` and the `with` statement.
* Parse a CSV file into a list of dictionaries and access fields by header name.
* Import and use modules from Python's standard library (`csv`, `os`, `datetime`).
* Decide when to import an existing module versus writing my own solution.

## Topics

1. **[Reading and Writing .txt and .csv Files](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/07%20-%20Text%20Data%20%26%20Modules/01_reading_writing_files.md)**

   `open()` with modes `r`, `w`, `a`; the `with` statement; reading line by line; `csv.reader` and `csv.writer`; `csv.DictReader` and
   `csv.DictWriter`

3. **[Parsing Lines Into Data Structures](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/07%20-%20Text%20Data%20%26%20Modules/02_parsing_to_data_structures.md)**
   
   Reading a CSV into a list of dictionaries; accessing fields by header name; connecting file I/O to the data structures from Week 5; a
   practical pattern used throughout data work

5. **[Standard Library Modules: csv, os, datetime](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/07%20-%20Text%20Data%20%26%20Modules/03_standard_library_modules.md)**
   
   Importing modules with `import` and `from ... import`; `csv` (already used above); `os` for file/directory operations; `datetime` for
   working with dates; using the Python docs to explore a module

7. **[When to Write Your Own Code vs. Import a Module](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/07%20-%20Text%20Data%20%26%20Modules/04_when_to_import.md)**

   Standard library vs. third-party packages vs. writing from scratch; how to find and evaluate a package; recognizing when a problem is
   already solved
