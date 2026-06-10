# Local Python Setup & VS Code

In Week 1, you wrote Python in an online IDE. That was intentional — getting a feel for the language right away is more valuable (and more fun!) than spending your first session installing software.

Now it's time to move to a local development environment on your own machine. Online IDEs are great for learning the basics, but they have real limitations: you can't install arbitrary packages, save files the way you want, or connect your work to GitHub. As your programs grow more complex, you'll need a proper local setup. This page walks through each step: installing Python, verifying the installation, setting up a package manager, organizing your working folders, and configuring VS Code. Work through the steps in order, each one builds on the last.

---

## 1. Install Python

Download Python from the official website: [python.org](https://www.python.org/downloads/) Make sure you download the latest version — it should be at least Version 3.14.

Installation instructions vary by operating system:

- **Windows**
  - Install Python natively in Windows (not through the Windows Subsystem for Linux). Later lessons use `matplotlib` for graphs, and getting graphical output to display correctly in a WSL environment requires complex configuration that is outside the scope of this class.
  - During installation, make sure to check **Add Python to PATH**. This allows you to run Python from any terminal window.
  - After installation, use **Git Bash** for all terminal commands in this class.
  - If Python hangs when you run it in Git Bash, add this line to your `~/.bash_profile`: `alias python='winpty python.exe'`

- **macOS**
  - macOS may come with an older version of Python pre-installed. To ensure you have Python 3, download the latest version from [python.org](https://www.python.org/downloads/) or install it via Homebrew:
    ```bash
    brew install python
    ```

- **Linux**
  - Most Linux distributions include Python, but confirm you have Python 3. Install or upgrade using your system's package manager:
  - **Debian/Ubuntu:**
    ```bash
    sudo apt update
    sudo apt install python3
    ```
  - **Fedora:**
    ```bash
    sudo dnf install python3
    ```
  - **Arch Linux:**
    ```bash
    sudo pacman -S python
    ```

---

## 2. Verify Your Python Installation

After installing, confirm Python 3 is available by opening a terminal and running:

```bash
python --version
```

If that returns a version starting with `3.x.x`, you're set. On some systems — particularly macOS and Linux — Python 3 is installed as `python3` to distinguish it from an older Python 2 installation:

```bash
python3 --version
```

Use whichever command returns a `3.x.x` version. You should see something like:

```
Python 3.12.3
```

> **Try the interactive shell:** Run `python` (or `python3`) without any arguments to open Python's interactive shell. You can type code directly and see it execute immediately — a great way to experiment with ideas from the lessons. Press `Ctrl-D` to exit.

---

## 3. Verify pip

**pip** is Python's package installer. It lets you add libraries like `pandas`, `numpy`, and `matplotlib` to your Python environment. pip is included automatically with Python 3.4 and above, so you likely already have it.

Check that it's available:

```bash
pip --version
```

On systems where Python is installed as `python3`, pip may be installed as `pip3`:

```bash
pip3 --version
```

If pip isn't found, reinstall Python and make sure **Add Python to PATH** is checked during installation.

To upgrade pip to the latest version:

```bash
python -m pip install --upgrade pip
```

> **Note on `python` vs `python3`:** Once you set up a virtual environment in the next step, you won't need to worry about this distinction anymore. Inside an active virtual environment, `python` and `pip` always refer to Python 3.

---

## 4. Create Your Working Folder and Virtual Environment

### Folder structure

Your work in this class will live in two places:

- A **`python_homework`** folder — your assignment repository, which you'll clone from GitHub in the first lesson
- A **`working`** folder — a scratch space for trying out code samples from the lessons (this should be kept separate from your assignment repository)

A good way to organize this is to create a parent folder called `python_class` that contains both:

```
python_class/
├── working/          ← for lesson code samples
└── python_homework/  ← cloned from GitHub (set up in Lesson 1)
```

### Virtual environments

Python projects use **virtual environments** to manage their dependencies — a self-contained collection of packages installed specifically for one project. This keeps packages from different projects from interfering with each other. It also means that once you're inside an active virtual environment, you can always use `python` and `pip` regardless of how your system installed Python.

Create your `working` folder, navigate into it, and set up a virtual environment:

- **Windows (Git Bash):**
  ```bash
  python -m venv .venv
  source .venv/Scripts/activate
  code .
  ```

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  code .
  ```

Once activated, you'll see `(.venv)` at the start of your terminal prompt. **This indicator tells you the virtual environment is active.** You need it active whenever you're installing packages or running your code.

> **Important:** The virtual environment only stays active for the duration of your terminal session. Each time you open a new terminal window, you'll need to run the `source` command again to reactivate it. The VS Code setup in the next step automates this for you.

---

## 5. Set Up VS Code for Python

VS Code works well for Python development and is what this class uses. A few things to configure:

- **Install the Python extension** from the VS Code Extensions panel (search for "Python" by Microsoft)

- **Select your interpreter:** Open the Command Palette (`Ctrl-Shift-P` on Windows/Linux, `Cmd-Shift-P` on macOS), type `Python: Select Interpreter`, and choose the option that includes `.venv` in the path. This tells VS Code to use your virtual environment's Python.

- **Windows users — automate venv activation:** Add the following lines to your `~/.bashrc` file (create it if it doesn't exist). This automatically activates your virtual environment whenever you open a Git Bash terminal in a folder that has one:
  ```bash
  if [ -f ./.venv/Scripts/activate ]; then
      source ./.venv/Scripts/activate
  fi
  ```

When everything is configured correctly, any terminal you open inside VS Code should show `(.venv)` at the start of the prompt. That's how you know the virtual environment is active and ready to use.
