# Planning Your Project

## Before You Write Code

The most common sticking point in a project like this isn't writing Python, it's figuring out *what* to write. Students who skip straight to code often end up rewriting functions multiple times because they didn't know what shape their data was in.

Phase 0 takes about 15 minutes. It's not graded. But it will make Phases 1 and 2 significantly smoother.

---

## Step 1 — Explore Your API in the Browser

Before opening VS Code, open your API's base URL directly in a browser tab. You'll see the raw JSON response.

Spend a few minutes reading it:

- Is the top-level response a list, or a dict with a key that contains a list?
- What fields does each record have?
- Are any fields nested (dicts inside dicts, or lists inside dicts)?
- Are any fields obviously missing or `null` for some records?

> **Tip:** Install a browser extension like JSON Formatter to make raw JSON easier to read. VS Code also has a built-in prettifier — paste the response into a new `.json` file and use the format document shortcut (`Shift+Alt+F` on Windows, `Shift+Option+F` on Mac).

---

## Step 2 — Answer These Questions Before You Code

Write your answers down — in a comment at the top of `main.py`, in a notebook, or on paper. The format doesn't matter; having the answers written does.

**1. What is the URL you'll call?**
Write the exact endpoint, including any query parameters you plan to use.

**2. What is the shape of the response?**
Is the top-level response a list? A dict with a list inside it? If it's a dict, what key holds the records you care about?

**3. Which 3–5 fields will your program use?**
List the field names exactly as they appear in the JSON. Note if any are nested inside another dict.

**4. What can a user do with your CLI?**
Describe the one core interaction in one sentence. For example: *"A user can type a region name and see all countries in that region."*

**5. Where could things go wrong?**
Name two things that could fail at runtime — a bad network connection, a missing field, unexpected user input — and where in your code you'd handle each one.

---

## Step 3 — Set Up the Starter Repository

Clone the starter repository and verify your environment before writing any project code.

**Starter repository structure:**

```
final-project/
├── main.py           ← Start here. Function stubs are defined; you write the bodies.
├── requirements.txt  ← Add third-party packages here (start with: requests)
└── README.md         ← Fill this in as you build. Required for submission.
```

**`main.py` comes with these stubs:**

```python
def fetch_data():
    """Fetch data from the API. Returns a list of dictionaries."""
    pass


def process_data(records):
    """Extract or transform the fields you need. Returns a list of dictionaries."""
    pass


def display_results(results):
    """Print results to the terminal in a readable format."""
    pass


def main():
    """Entry point for the CLI tool."""
    pass


if __name__ == "__main__":
    main()
```

You're not required to keep exactly this structure: rename functions, add parameters, split into multiple files if you want to.

**Verify your environment:**

```bash
# In your project directory:
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

pip install requests
pip freeze > requirements.txt
python main.py                  # Should run without errors (does nothing yet)
```

If `python main.py` runs without errors, you're ready for Phase 1.
