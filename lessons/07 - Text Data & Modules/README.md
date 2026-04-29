# Lesson 7 — Text Data & Modules

**Lesson Overview**
Students connect Python to the outside world by reading and writing files, then learn how the module system lets them extend Python's capabilities without reinventing the wheel.

## Topics

1. **[Reading and Writing .txt and .csv Files](01_reading_writing_files.md)**
   *Ported from Python Essentials — PE 2.2 (File Handling)*
   `open()` with modes `r`, `w`, `a`; the `with` statement; reading line by line; `csv.reader` and `csv.writer`; `csv.DictReader` and `csv.DictWriter`

2. **[Parsing Lines Into Data Structures (Lists of Dicts)](02_parsing_to_data_structures.md)**
   *Ported and expanded from Python Essentials — PE 2.2*
   Reading a CSV into a list of dictionaries; accessing fields by header name; connecting file I/O to the data structures from Week 5; a practical pattern used throughout data work

3. **[Standard Library Modules: csv, os, datetime](03_standard_library_modules.md)**
   *Ported from Python Essentials — PE 2.3 (Introduction to Modules), PE 2.5 (Working with the OS)*
   Importing modules with `import` and `from ... import`; `csv` (already used above); `os` for file/directory operations; `datetime` for working with dates; using the Python docs to explore a module

4. **[When to Write Your Own Code vs. Import a Module](04_when_to_import.md)**
   *New content*
   Standard library vs. third-party packages vs. writing from scratch; how to find and evaluate a package; recognizing when a problem is already solved
