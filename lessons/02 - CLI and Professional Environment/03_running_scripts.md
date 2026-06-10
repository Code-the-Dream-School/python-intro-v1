# Running Python Scripts from the Command Line

**Objective**: By the end of this lesson, you will be able to:
  * Navigate to a project folder and run a Python script from the terminal
  * Read your program's output in the terminal
  * Recognize what an error looks like when running a script from the command line
  * Understand the workflow for running and testing scripts going forward

---

## From VS Code to the Terminal

In Week 1, you clicked a **Run** button in an online IDE. Now that you have Python installed locally and know how to navigate the terminal, you can run scripts the way developers do: from the command line.

The process is straightforward:

1. Open your terminal
2. Navigate to the folder where your `.py` file lives
3. Type `python` followed by the file name
4. Press Enter

Let's walk through it.

---

## Running Your First Local Script

Start by creating a simple script. Open VS Code, create a file called `hello.py` in your `working` folder, and add this code:

```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")
```

Now open your terminal and navigate to the folder where you saved the file:

```bash
cd ~/python_class/working
```

Make sure your virtual environment is active (you should see `(.venv)` at the start of your prompt). If it's not, activate it:

```bash
source .venv/bin/activate        # macOS / Linux
source .venv/Scripts/activate    # Windows (Git Bash)
```

Now run the script:

```bash
python hello.py
```

You should see:

```
What is your name? 
```

Type your name and press Enter:

```
What is your name? Jazmine
Hello, Jazmine! Welcome to Python.
```

That's it. The terminal is now doing what the online IDE used to do: running your code and displaying the output.

> **`python` vs `python3`:** Inside an active virtual environment, `python` always refers to Python 3. If you're outside a virtual environment, you may need to use `python3` instead. When in doubt, keep your virtual environment active.

---

## What You See in the Terminal

When you run a script, everything your code sends to `print()` appears in the terminal. This is called **standard output** (or **stdout**). The terminal is just showing you what your program prints, line by line, in order.

If your script doesn't have any `print()` calls, running it will produce no visible output:

```python
# silent.py
x = 10
y = 20
total = x + y
```

```bash
python silent.py
```

Output: (nothing appears)

The code ran successfully, it just didn't print anything. This is normal and not an error.

---

## When Something Goes Wrong

If your script has an error, Python will display the error message in the terminal instead of running the program. This is the same kind of traceback you learned about in Week 1's debugging lesson, just displayed in your terminal now instead of in the online IDE.

For example, save this buggy code as `broken.py`:

```python
print("Starting the program")
name = "Jazmine"
print(f"Hello, {namee}!")
```

Run it:

```bash
python broken.py
```

Output:

```
Starting the program
Traceback (most recent call last):
  File "/Users/jazmine/python_class/working/broken.py", line 3, in <module>
    print(f"Hello, {namee}!")
                    ^^^^^
NameError: name 'namee' is not defined. Did you mean: 'name'?
```

Notice a few things:

- `Starting the program` printed successfully because line 1 ran before the error
- The traceback tells you the file name, line number, and what went wrong
- Python even suggests a fix: "Did you mean: 'name'?"

Read the last line first, fix the issue in VS Code, save the file, and run it again. This is the development loop you'll use from now on: **edit in VS Code, run in the terminal, read the output, repeat**.

### AI Prompt: Scaffold Removal

Try creating your own buggy script on purpose. Introduce one of the errors you learned about in Week 1 (NameError, TypeError, SyntaxError). Run it from the terminal, then:

1. Read the error message and try to fix it yourself
2. If stuck, use your preferred AI chatbot:

> "I ran my Python script from the terminal and got this error: [paste the full traceback]. Can you ask me 3 questions that will help me figure out what's wrong?"

---

## The Development Workflow

Going forward, this is how you'll work on assignments and practice:

1. **Write code** in VS Code
2. **Save the file** (`Ctrl+S` on Windows/Linux, `Cmd+S` on Mac)
3. **Run it** from the terminal: `python filename.py`
4. **Read the output** or error message
5. **Fix and repeat**

> **Don't forget to save!** A common mistake is editing code in VS Code but forgetting to save before running it in the terminal. If your changes don't seem to be working, check that you saved the file first.

You can also open a terminal directly inside VS Code (Terminal > New Terminal from the menu bar, or `` Ctrl+` ``). This saves you from switching between windows. VS Code's built-in terminal works the same way as your regular terminal.

---

## Videos

**"Python Tutorial for Beginners 1: Install and Setup for Mac and Windows"** (Corey Schafer)

[Watch from 7:00 onward](https://www.youtube.com/watch?v=YYXdXT2l-Gg&t=420s) for a walkthrough of running Python from the terminal, including the interactive shell and executing script files. You can skip the installation section since you set that up in the previous lesson.

---

## Check for Understanding

**Question 1:** You type `python my_script.py` in the terminal and nothing happens (no output, no error). What is the most likely explanation?

* A) Python isn't installed
* B) The script ran successfully but has no `print()` statements
* C) The file doesn't exist
* D) There's a bug in the code

<details>
<summary>Answer</summary>

**B) The script ran successfully but has no `print()` statements.** If a script runs without errors but doesn't call `print()`, there's nothing to display. The code still executed.

</details>

**Question 2:** What should you do before running `python script.py` in the terminal?

* A) Make sure you're in the same folder as the script
* B) Close VS Code
* C) Restart your computer
* D) Delete any old `.py` files

<details>
<summary>Answer</summary>

**A) Make sure you're in the same folder as the script.** Use `cd` to navigate to the folder containing your file, or Python won't be able to find it.

</details>

**Question 3:** You edit your code in VS Code and run it in the terminal, but the old version still runs. What did you probably forget?

* A) To restart Python
* B) To save the file in VS Code
* C) To reinstall Python
* D) To close the terminal

<details>
<summary>Answer</summary>

**B) To save the file in VS Code.** The terminal runs whatever is saved on disk. If you edited the file but didn't save (`Ctrl+S` / `Cmd+S`), the terminal will run the old version.

</details>

---

## Further Reading

- [VS Code: Getting Started with Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Real Python: How to Run Your Python Scripts](https://realpython.com/run-python-scripts/)
