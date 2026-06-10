# CLI Navigation

**Objective**: By the end of this lesson, you will be able to:
  * Explain what the terminal is and why developers use it
  * Open a terminal on your operating system
  * Use essential commands: `pwd`, `ls`, `cd`, `mkdir`, and `touch`
  * Understand the difference between absolute and relative paths
  * Use tab completion to type commands faster

---

## What Is the Terminal?

The **terminal** (also called the **command line** or **shell**) is a text-based interface for interacting with your computer. Instead of clicking folders and icons, you type commands and press Enter.

This might feel unfamiliar at first. You've probably spent years using a graphical interface with windows, menus, and a mouse. The terminal strips all of that away and gives you a blank line with a blinking cursor. That's intentional: the terminal is faster and more precise for the kinds of tasks developers do every day, like navigating to a project folder, running a script, or managing files.

You don't need to memorize everything in this lesson right away. These commands will become second nature with practice, just like keyboard shortcuts.

---

## Opening Your Terminal

How you open the terminal depends on your operating system. In the previous lesson, we recommended **Git Bash** for Windows users, so that's what we'll use here.

- **Windows**: Open **Git Bash** (installed with Git). You can find it in your Start menu or by right-clicking on your desktop and selecting "Git Bash Here."
- **macOS**: Open **Terminal** (found in Applications > Utilities) or use Spotlight (`Cmd + Space`, then type "Terminal").
- **Linux**: Open your distribution's terminal application (usually called Terminal or Konsole).

Once open, you'll see a **prompt** that looks something like this:

```
username@computer:~$
```

The `$` (or `%` on some Macs) is where you type your commands. The text before it shows your username, computer name, and current location.

---

## Checking Your Location with `pwd`

The first command to learn is `pwd`, which stands for **print working directory**. It tells you exactly where you are in your computer's file system.

```bash
pwd
```

Output (example):
```
/Users/jazmine
```

This is your **home directory**, the starting point when you open a new terminal. On Windows with Git Bash, it might look like `/c/Users/jazmine`.

Think of your file system like a tree of folders. `pwd` is like asking "which folder am I standing in right now?"

---

## Listing Files with `ls`

The `ls` command **lists** the files and folders in your current directory.

```bash
ls
```

Output (example):
```
Desktop    Documents    Downloads    Music    Pictures
```

These are the same folders you'd see if you opened your home directory in a file browser, just displayed as text instead of icons.

To see more detail, including hidden files, use:

```bash
ls -la
```

Hidden files (whose names start with a dot, like `.bashrc` or `.venv`) won't show up with plain `ls`, but `ls -la` reveals them. You'll encounter hidden files when working with Git and virtual environments.

---

## Navigating with `cd`

The `cd` command **changes directory**, moving you from one folder to another.

```bash
cd Documents
```

Now run `pwd` to confirm you moved:

```bash
pwd
```

Output:
```
/Users/jazmine/Documents
```

To go **back up** one level (to the parent folder), use two dots:

```bash
cd ..
```

To jump straight back to your home directory from anywhere:

```bash
cd ~
```

And to go to a folder that's several levels deep in one command:

```bash
cd Documents/python_class/working
```

### AI Prompt: Predict-Then-Check

Before running each command below, predict what `pwd` will show afterward. Then run it and check.

```bash
cd ~
cd Documents
cd ..
cd Downloads
pwd
```

If your prediction was wrong, use your preferred AI chatbot:

> "I'm learning terminal navigation. I expected `pwd` to show [your prediction] after running these commands, but it showed [actual result]. Can you explain why?"

---

## Creating Folders with `mkdir`

The `mkdir` command **makes a new directory** (folder).

```bash
mkdir my_project
```

This creates a folder called `my_project` inside your current directory. You can verify it exists with `ls`:

```bash
ls
```

Then navigate into it:

```bash
cd my_project
```

You can also create nested folders in one step using the `-p` flag:

```bash
mkdir -p python_class/working
```

This creates `python_class` and `working` inside it, even if `python_class` doesn't exist yet.

---

## Creating Files with `touch`

The `touch` command creates a new, empty file.

```bash
touch hello.py
```

This creates an empty file called `hello.py` in your current directory. You can confirm it exists:

```bash
ls
```

Output:
```
hello.py
```

> **Windows Git Bash note:** `touch` works in Git Bash. If you ever use the Windows Command Prompt (cmd) instead, you would use `echo. > hello.py`, but we recommend sticking with Git Bash for this course.

---

## Absolute vs. Relative Paths

When you tell the terminal where to go, you can use two kinds of paths:

**Absolute paths** start from the root of your file system and give the full location. On macOS and Linux, they start with `/`. In Git Bash on Windows, they also start with `/`, like `/c/Users/jazmine`.

```bash
cd /Users/jazmine/Documents/python_class
```

This works no matter where you currently are, because it describes the complete path from the top.

**Relative paths** start from your current location:

```bash
cd python_class/working
```

This only works if `python_class` is inside the folder you're currently in.

Here are the shorthand symbols you'll use in relative paths:

| Symbol | Meaning | Example |
|--------|---------|---------|
| `.` | Current directory | `cd ./working` (same as `cd working`) |
| `..` | Parent directory (one level up) | `cd ..` |
| `~` | Home directory | `cd ~` |

Most of the time, relative paths are shorter and easier to type. Absolute paths are useful when you need to jump to a specific location regardless of where you are.

---

## Tab Completion

Here's a trick that will save you a lot of typing: **tab completion**. Start typing the name of a file or folder, then press the `Tab` key, and the terminal will finish the name for you.

For example, if you have a folder called `python_class` and you type:

```bash
cd pyt
```

Then press `Tab`, the terminal will complete it to:

```bash
cd python_class
```

If there are multiple matches (like `python_class` and `python_homework`), pressing `Tab` twice will show you all the options.

Tab completion prevents typos and saves time. Get in the habit of using it for every command.

---

## Quick Reference

Here's a summary of the commands you learned in this lesson:

| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Print current directory | `pwd` |
| `ls` | List files and folders | `ls` |
| `ls -la` | List all files including hidden ones | `ls -la` |
| `cd` | Change directory | `cd Documents` |
| `cd ..` | Go up one level | `cd ..` |
| `cd ~` | Go to home directory | `cd ~` |
| `mkdir` | Create a new folder | `mkdir my_project` |
| `mkdir -p` | Create nested folders | `mkdir -p parent/child` |
| `touch` | Create an empty file | `touch hello.py` |

---

## Videos

**"Beginner's Guide to the Bash Terminal"** (Joe Collins)

[Watch the first 20 minutes](https://www.youtube.com/watch?v=oxuRxtrO2Ag) for a friendly walkthrough of the terminal, navigation commands, and file management basics.

---

## Check for Understanding

**Question 1:** What does the `pwd` command do?

* A) Creates a new directory
* B) Lists the files in your current directory
* C) Prints the full path of your current directory
* D) Moves you to a different directory

<details>
<summary>Answer</summary>

**C) Prints the full path of your current directory.** `pwd` stands for "print working directory" and shows you exactly where you are in the file system.

</details>

**Question 2:** You are in `/Users/jazmine/Documents`. What does `cd ..` do?

* A) Takes you to `/Users/jazmine/Documents/..`
* B) Takes you to `/Users/jazmine`
* C) Takes you to your home directory
* D) Gives you an error

<details>
<summary>Answer</summary>

**B) Takes you to `/Users/jazmine`.** The `..` symbol means "parent directory," which is one level up from where you are.

</details>

**Question 3:** What is the difference between an absolute path and a relative path?

* A) Absolute paths are shorter than relative paths
* B) Absolute paths start from the root (`/`) and work from anywhere; relative paths start from your current location
* C) Relative paths are faster for the computer to process
* D) There is no difference; they are interchangeable terms

<details>
<summary>Answer</summary>

**B) Absolute paths start from the root (`/`) and work from anywhere; relative paths start from your current location.** For example, `/Users/jazmine/Documents` is absolute, while `Documents` is relative (and only works if you're in `/Users/jazmine`).

</details>

**Question 4:** You're in your home directory. You want to create a folder called `projects` and immediately navigate into it. Which commands would you run?

* A) `mkdir projects` then `cd projects`
* B) `cd projects` then `mkdir projects`
* C) `touch projects` then `cd projects`
* D) `ls projects`

<details>
<summary>Answer</summary>

**A) `mkdir projects` then `cd projects`.** You need to create the folder first with `mkdir`, then move into it with `cd`. You can't `cd` into a folder that doesn't exist yet.

</details>

---

## Further Reading

- [The Odin Project: Introduction to the Command Line](https://www.theodinproject.com/lessons/foundations-command-line-basics)
- [MDN Web Docs: Command Line Crash Course](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Command_line)
- [Ubuntu: The Linux Command Line for Beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
