## Overall Learning Objectives

By the end of this course, students will be able to:

* Write and execute Python scripts using score language features: variables, data types, control flow, loops, and functions.
* Work with Python's core data structures (lists, tuples, dictionaries, sets) and choose appropriate structures for different tasks.
* Navigate a professional environment using the command line, VS Code, and Git/GitHub.
* Read and write data from external sources including text files, CSV files, and public APIs.
* Write robust, modular programs using error handling, defensive programming, and reusable functions.
* Apply algorithmic thinking to sorting and searching problems.
* Demonstrate proficiency by building a CLI tool that integrates with a public API.

## Week-by-Week Learning Objectives

| Week | Lesson                         | Students will be able to...                                                                                                                                                                                                                                                                                                 |
|------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Python Basics                  | - Variables, data types, print/input<br>- Simple scripts that produce tangible output<br>- Debugging basics: reading error messages<br>- Conceptual intro to version control                                                                                                                                                |
| 2    | CLI & Professional Environment | - Install Python locally and configure VS Code<br>- Basic CLI navigation (cd, ls/dir, mkdir, pwd, etc.)<br>- Understand the role of the terminal in a professional development workflow<br>- Run Python scripts from the command line<br>- Install Git; understand repos and commits conceptually |
| 3    | Control Flow                   | - if/else logic and comparison operators<br>- Boolean operators (and, or, not)<br>- Decision-making scripts (e.g., text-based prompts)<br>- Create/clone a GitHub repository; make first commit and open a pull request                                                                                                     |
| 4    | Core Data Structures           | - Lists, tuples, dictionaries, and sets<br>- Why different structures exist and when to use each<br>- List comprehensions                                                                                                                                                                                                   |
| 5    | Iteration & Algorithms         | - For and while loops<br>- Loop patterns: counting, accumulating, searching<br>- Sorting and searching algorithms using loops<br>- Debugging loops<br>- Looping over structured data                                                                                                                                        |
| 6    | Functions & Scope              | - Defining functions with parameters and return values<br>- Understanding variable scope<br>- Refactoring earlier scripts into modular functions                                                                                                                                                                            |
| 7    | Text Data & Modules            | - Reading and writing .txt and .csv files<br>- Parsing lines into data structures (lists of dicts)<br>- Standard library modules: csv, os, datetime<br>- When to write your own code vs. import a module                                                                                                                    |
| 8    | Errors & Debugging             | - try/except and common runtime errors<br>- Defensive programming patterns<br>- Writing code that fails gracefully<br>- Conceptual intro to pip and virtual environments                                                                                                                                                    |
| 9    | External Libraries & APIs      | - requests library and JSON parsing<br>- Calling a public API and handling the response<br>- Connecting API data back to dicts and lists                                                                                                                                                                                    |
| 10   | Final Project I                | - Build a Python program that fetches data from a public web API, transforms it into structured Python data, and handles errors robustly<br>- Create a command-line interface that lets a user query or interact with the API data in real time.                                                                            |
| 11   | Final Project II               | - Extend the final project by building a data visualization that answers a specific question about API data or clean, process, and export API data into a structured CSV file for external use.                                                                                                                             |

### Note on Git/GitHub & CLI Progression

Version control and CLI skills are woven into the first three weeks alongside Python content, rather than occupying a dedicated week.

* Week 1: Students use an [online Python IDE](https://www.online-python.com/) since the focus is on Python syntax. A conceptual intro to version control (what/why) is included, but no tooling yet. Students upload .py file (downloaded from the IDE) for assignment submission.
* Week 2: Local environment setup; CLI navigation and terminal fluency; running Python scripts from the command line; Git installation and configuration. Students paste terminal output for assignment submission.
* Week 3: First content week (Control Flow). Students create/clone a GitHub repository and submit their assignment via first commit and PR, establishing the Git workflow for the rest of the course.
* Weeks 4-11: Normal Git workflow

## Final Project

The final project spans two weeks and uses a "structured choice" model: a mandatory core and CLI tool that all students complete (Week 10), followed by a choice of two extension tracks (Week 11).

### Week 10: Core Requirements + CLI Tool

Completed by all students.

**Phase 1: Core Requirements**
* External data integration: connect a public web API using the requests library.
* Data transformation: parse JSON response into a list of dictionaries.
* Defensive programming: implement try/except blocks to handle connection and runtime errors.
* Modular design: refactor all logic into reusable functions with clear parameters and return values.

**Phase 2: CLI Tool (required)**
* Build a command-line interface where users can query or interact with the fetched data in real time, including argument-based behavior.

### Week 11: Student Choice Extension

* Option A - Visual Analysis: Use fetched data to create visualizations using Matplotlib that answer specific data questions.
* Option B - Data Pipeline: Clean and process API data and export it into a structured CSV file for external use.

**Universal technical requirements:**
* Modular design: reusable functions with clear parameters and return values.
* Standard library usage
* Version control 
* Video design rationale and demo
