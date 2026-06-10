# Assignment 10 — Final Project Part I

## Project Requirements

Make sure you've read through the [Final Project Overview](../final-project-overview.md) to understand the full two-week arc, the API options, and the rubric your project will be evaluated against.

### Phase 1: Core Program

Complete Phase 1 before moving to Phase 2.

- Connect to your chosen public API using the `requests` library
- Parse the JSON response into a list of dictionaries with relevant fields extracted
- Handle connection errors and bad status codes with `try/except`
- Organize all fetching and parsing logic into functions with clear parameters and return values

### Phase 2: CLI Tool

Complete after Phase 1.

- Accept at least one form of user input (via `input()` prompts or `argparse` arguments)
- Implement at least one meaningful interaction: filter by a field, look up a specific record, or compare two results
- Display results in a readable, formatted way
- Handle unexpected input without crashing

### Submission

**Required files**

Your repository must include:

- `main.py` — the entry point for your CLI tool
- `requirements.txt` — list all third-party packages used (at minimum: `requests`)
- `README.md` — must include: project title, which API you used, how to install and run the program, and a description of the CLI interaction(s) you implemented

**Pull request**

Submit your work by opening a pull request from a feature branch (use `week-10-final-project` as the branch name). Your PR description should briefly explain what you built and which API you chose.

Your commit history should show incremental progress: at minimum, separate commits for getting the API working, parsing the data, and adding the CLI. Don't submit everything in a single commit.

**Video Reflection**

Record a short video (3–5 minutes) and include the link in your pull request description.

Your video should address:

1. Walk through your `fetch_data()` function. What does it do if the API call fails?
2. Demonstrate your CLI interaction live — show it running with at least one real input. What happens if a user enters something unexpected?
3. Walk through one decision you made about how to organize your code into functions and explain why you made it that way.

Requirements:
- 3–5 minutes
- Use screen sharing to show your running program and code
- Speak in your own words. No need to script it!

Upload to YouTube (unlisted) or Loom and paste the link in your PR description.

---

## Rubric

> Note that this only is the final project part I rubric. Next week contains the extension rubric.

| Category | Does Not Meet | Meets | Exceeds |
|---|---|---|---|
| **API Integration** | Program fails to connect to the API, or the call is broken and does not run. | Fetches data from the chosen API using `requests`. URL and parameters are clearly organized. | API call is in a dedicated function. Query parameters are passed as arguments rather than hard-coded. |
| **Data Transformation** | JSON response is not parsed, or program crashes when accessing data fields. | JSON is parsed into a list of dicts with relevant fields accessible by key. | Transformation is in a dedicated function. `.get()` is used to handle missing keys without crashing. |
| **CLI Tool** | No user interaction — program prints raw output with no input. | Accepts at least one form of user input and returns formatted results. At least one meaningful interaction is implemented. | Multiple interaction modes available. Output is clearly formatted. Unexpected input is handled without crashing. |
| **Error Handling** | No error handling — connection errors cause unhandled tracebacks. | `try/except` catches connection errors and bad status codes. User sees a clear error message instead of a traceback. | Errors are caught at the right level of the code. Program continues or exits gracefully with a helpful message. |
| **Code Organization** | All logic in one long script with no functions, or functions without parameters and return values. | Logic is split into functions with clear names, parameters, and return values. Each function has one responsibility. | Fetching, parsing, and display are cleanly separated. Code is readable without requiring comments to understand. |
| **Version Control** | Work submitted in a single commit or without a pull request. | Multiple commits show incremental progress. Work submitted via pull request. | Commit messages are descriptive and reflect meaningful stages of development. |

## Need a GitHub Review?

Open the dropdown box below:

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b week-[#]     
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin week-[#]        # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
</details>
