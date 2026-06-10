# pip and Virtual Environments

**Objective**: By the end of this lesson, you will be able to:
  * Explain what `pip` is and how it connects to PyPI
  * Describe what a virtual environment is and why it matters
  * Create and activate a virtual environment using `venv`
  * Install a package into an active virtual environment
  * Generate a `requirements.txt` file and use it to reproduce an environment

---

## Good News: You've Already Been Using These

In Week 2, you set up a virtual environment for this course. You may not have understood exactly why at the time, you just ran the commands and got on with learning Python. This lesson is about understanding the tools you've been using and adding one new skill: `requirements.txt`.

---

## What Is `pip`?

`pip` is Python's **package installer**. It's a tool that lets you download and install third-party libraries — code written by other developers that you can use in your own programs.

When you run `pip install requests`, pip:
1. Connects to **PyPI** (the Python Package Index — `pypi.org`), a public repository of Python packages
2. Downloads the `requests` package and any packages it depends on
3. Installs everything into your Python environment so you can `import` it

PyPI hosts hundreds of thousands of packages: libraries for making HTTP requests, reading spreadsheets, analyzing data, building web apps, and much more. `pip` is your access point to all of them.

To verify that pip is available in your environment:

```bash
pip --version
```

---

## The Problem pip Alone Doesn't Solve

Without a virtual environment, `pip install` installs packages globally — into your system's Python installation. This causes two problems:

**Problem 1: Version conflicts.** Project A needs `requests` version 2.28. Project B needs version 2.31. You can only have one version installed globally, so one project always breaks.

**Problem 2: Reproducibility.** If you share your code with a teammate, they won't know which packages to install, or which versions. Their environment will likely differ from yours, and the code may not work.

Virtual environments solve both problems.

---

## What Is a Virtual Environment?

A **virtual environment** is an isolated copy of Python for a specific project. It has its own folder for installed packages, completely separate from every other project on your computer.

Think of it like this: instead of one shared kitchen where everyone cooks and ingredients get mixed up, each project gets its own private kitchen stocked with exactly what it needs.

When you activate a virtual environment:
- `python` and `pip` point to the versions inside that environment
- Any packages you install go into that environment only
- Other projects on your machine are unaffected

---

## Creating and Activating a Virtual Environment

Python 3.3 and newer include the `venv` module for creating virtual environments. The convention for the environment folder name is `.venv`:

```bash
python3 -m venv .venv
```

This creates a `.venv` folder in your project directory. You won't need to look inside it — just activate it.

**To activate (Mac/Linux):**

```bash
source .venv/bin/activate
```

**To activate (Windows Git Bash):**

```bash
source .venv/Scripts/activate
```

Once activated, your terminal prompt changes to show the environment name:

```
(.venv) $
```

That prefix is your signal that the environment is active. Any `pip install` you run now installs only into this environment.

To deactivate when you're done:

```bash
deactivate
```

---

## Installing Packages Into Your Environment

With the virtual environment active, install packages the same way you always have:

```bash
pip install requests
```

The package installs into `.venv/` — not into your system Python. You can verify what's installed:

```bash
pip list
```

---

## `requirements.txt`

A `requirements.txt` file records exactly which packages your project depends on, so anyone else (or your future self on a new computer) can recreate the same environment in one command.

**Generate it** after installing your packages:

```bash
pip freeze > requirements.txt
```

`pip freeze` lists every installed package with its exact version number. The `>` sends that output into a file called `requirements.txt`. Open it and you'll see something like:

```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

**Install from it** on a new machine or in a new environment:

```bash
pip install -r requirements.txt
```

This installs every package at exactly the right version. Your teammate's environment will match yours.

**When to update it:** Any time you install a new package for the project, re-run `pip freeze > requirements.txt` to keep the file current.

---

### AI Prompt: Retrieval Practice

Before moving on, answer these questions from memory:

1. What is PyPI, and how does pip connect to it?
2. What is the difference between installing a package globally and into a virtual environment?
3. What does `pip freeze > requirements.txt` do, and why does it matter?

Then share your answers with an AI chatbot:

> "I just learned about pip and virtual environments in Python. Here's my understanding of the key concepts: [your answers]. What did I get right? What should I add or correct?"

---

## Videos

**"Python Tutorial: pip - An in-depth look at the package management system"** (Corey Schafer)

[Watch the video](https://youtu.be/U2ZN104hIcc?si=tUOOcEqah4OFdbDZ) — covers pip, PyPI, and installing packages.

**"Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module"** (Corey Schafer)

[Watch the video](https://youtu.be/Kg1Yvry_Ydk?si=k03Y2GoFRggUkSNP) — walks through creating, activating, and using virtual environments. **If you're on Windows, search for his Windows-specific venv tutorial.**

---

## Check for Understanding

**Question 1:** What does `pip` stand for, and what does it do?

* A) Python Internal Package; it manages Python's built-in modules
* B) Package Installer for Python; it downloads and installs third-party libraries from PyPI
* C) Python Import Protocol; it handles the `import` statement
* D) Python Interactive Prompt; it opens the Python REPL

<details>
<summary>Answer</summary>

**B) Package Installer for Python; it downloads and installs third-party libraries from PyPI** — `pip` connects to the Python Package Index (PyPI), downloads the package you request along with any packages it depends on, and installs them into your current Python environment.

</details>

**Question 2:** Why is installing packages globally (without a virtual environment) a problem?

* A) Global installation is slower than virtual environment installation
* B) pip doesn't work without a virtual environment
* C) Different projects may need different versions of the same package, which is impossible globally
* D) Global packages can't be imported with `import`

<details>
<summary>Answer</summary>

**C) Different projects may need different versions of the same package, which is impossible globally** — With a global installation, you can only have one version of any package at a time. Virtual environments let each project have its own set of packages at the exact versions it needs, without affecting any other project.

</details>

**Question 3:** After activating a virtual environment, how do you know it's active?

* A) Python runs faster
* B) The terminal prompt shows the environment name in parentheses, e.g., `(.venv) $`
* C) `import` statements stop working
* D) pip is no longer available

<details>
<summary>Answer</summary>

**B) The terminal prompt shows the environment name in parentheses, e.g., `(.venv) $`** — The `(.venv)` prefix is the visual signal that the environment is active. Any `pip install` you run while it's showing will install into that environment, not globally.

</details>

**Question 4:** What does `pip freeze > requirements.txt` do?

* A) Installs all packages listed in `requirements.txt`
* B) Deletes all installed packages
* C) Lists installed packages and saves them with exact version numbers to `requirements.txt`
* D) Upgrades all installed packages to their latest versions

<details>
<summary>Answer</summary>

**C) Lists installed packages and saves them with exact version numbers to `requirements.txt`** — `pip freeze` outputs every installed package with its exact version. The `>` redirects that output into the file. This lets anyone else run `pip install -r requirements.txt` to recreate your exact environment.

</details>

**Question 5:** A teammate clones your project and runs `pip install -r requirements.txt`. What happens?

* A) pip uninstalls all their existing packages
* B) pip installs every package listed in `requirements.txt` at the exact versions specified
* C) pip installs only the packages missing from their system
* D) pip creates a new virtual environment automatically

<details>
<summary>Answer</summary>

**B) pip installs every package listed in `requirements.txt` at the exact versions specified** — `pip install -r requirements.txt` reads the file and installs each package at the exact version listed. This ensures your teammate's environment matches yours, which is why keeping `requirements.txt` up to date matters. It does not create the virtual environment — your teammate needs to do that first.

</details>

---

## Further Reading

- [pip Documentation — User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Python Documentation — venv: Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [PyPI — The Python Package Index](https://pypi.org/)
- [Real Python — Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
