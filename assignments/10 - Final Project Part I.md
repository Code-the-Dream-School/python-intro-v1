# Assignment 10 — Final Project Part I

## Project Requirements

Make sure you've read through the [Final Project Overview](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/resources/final-project-overview.md) to understand the full two-week arc and the API options. The rubric this part is graded against is in the Rubric section below.

### Phase 1: Core Program

Complete Phase 1 before moving to Phase 2.

- Connect to your chosen public API using the `requests` library
- If your chosen API requires an API key (REST Countries does), keep the key in an environment variable and read it with `os.environ.get()`, the same way you did in Assignment 9. Never commit your key — your repository is public.
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

1. Walk through your data-fetching function (for example, `fetch_data()`). What does it do if the API call fails?
2. Demonstrate your CLI interaction live — show it running with at least one real input. What happens if a user enters something unexpected?
3. Walk through one decision you made about how to organize your code into functions and explain why you made it that way.

Requirements:
- 3–5 minutes
- Use screen sharing to show your running program and code
- Speak in your own words. No need to script it!

Upload to YouTube (unlisted) or Loom and paste the link in your PR description.

---

## Guidelines

> Note that these guidelines are only for the final project Part I. Next week contains the extension guidelines.

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

## Review: The GitHub Cycle

This is your repeatable workflow. For the final project your branch is `week-10-final-project`, so use that branch name in every command below.

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b week-10-final-project
```

`origin` is your fork. `git pull origin main` syncs your local main with your fork on GitHub; it's normal to see "Already up to date."

**Save your progress:**

```bash
git status                            # see what's changed (run this often)
git add .                             # stage all changes
git commit -m "describe what you did and why"
git push origin week-10-final-project # send your branch to GitHub
```

Repeat `add → commit → push` as often as you like. Committing often gives you more points to return to if something goes wrong.

**Open your pull request:**

On GitHub, open a pull request from `week-10-final-project` into main. Confirm the base repository is your own fork (`your-username/python-intro-homework`), not `Code-the-Dream-School`.

**Close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

**If something looks off:**

* Committed to main by accident? (You forgot to create your branch first.) Make the branch now: `git checkout -b week-10-final-project` carries your latest commits with it, then continue. Your work isn't lost.
* `git push` says your branch has "no upstream"? You haven't pushed this branch before. Run `git push origin week-10-final-project` to create it on your fork.
</details>

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

This is **Part I of a two-week final project**, submitted from a feature branch named
`week-10-final-project` with a pull request. `Example — adapt to your own layout`: the
repo layout is not specified by this assignment — the three required files may sit at
the repo root, in a `week-10/` folder, or in a project folder of the student's choosing.
Do NOT fail correct work over where the files live; the reviewer cannot see the
student's filesystem. The branch for this assignment is `week-10-final-project`, not an
`assignment-10` branch — do not require the earlier weeks' naming. Submission mechanics
(fork, branch, PR base) and commit history
are not gradable from the code itself. This repo is cumulative — folders from earlier
weeks are expected to remain; do not tell the student to remove prior-week work. The
project assumes the virtual environment and `requirements.txt` habit from Assignment 8;
the reviewer cannot see a virtual environment, so do not fail its absence.

**The student chooses their own public API**, so the reviewer cannot know what the
response looks like, which fields exist, or what the output should say. Grade the
structure and behavior of the code, never the specific data, field names, or printed
values. Some public APIs require a free API key; if the student's does, **the reviewer
cannot see that key**, because it belongs in an environment variable rather than in the
code. An absent key value must never be failed. What can be checked is that the request
sends the key (usually in an `Authorization` header) and reads it from the environment
instead of a literal in the file — a key hardcoded into a committed file is worth
flagging. If the chosen API is simply unreachable, do not fail a student whose code is
structurally correct.

- **Phase 1 — Core Program** — connects to the chosen API with `requests`, parses the
  JSON into a list of dictionaries with the relevant fields extracted, handles
  connection errors and bad status codes with `try`/`except`, and keeps the fetching and
  parsing logic in functions with clear parameters and return values. Required, because
  the assignment states each one: the `requests` library is used, the parsed result is a
  list of dictionaries, both connection errors and bad status codes are handled, and the
  logic lives in functions rather than at the top level. `Example — adapt to your own
  layout`: **function names are the student's own.** The video question mentions
  `fetch_data()` as an example — do not require that name, or any particular name.
- **Phase 2 — CLI Tool** — accepts user input (`input()` prompts or `argparse`),
  implements a meaningful interaction, displays results readably, and handles unexpected
  input without crashing. Required: **at least one** form of input and **at least one**
  meaningful interaction — filtering by a field, looking up a record, or comparing two
  results all qualify equally. One interaction is sufficient; do not expect several, and
  do not prefer one kind over another. `Example — adapt to your own layout`: all prompt
  wording, output formatting, and the choice of interaction.
- **`main.py`** — the CLI entry point. `Use exactly as written`: the filename `main.py`.
- **`requirements.txt`** — lists the third-party packages used, including `requests`.
  `Use exactly as written`: the filename. `Example — adapt to your own layout`: the
  package list and all version numbers, which depend on when the student installed.
- **`README.md`** — includes the project title, which API was used, how to install and
  run the program, and a description of the CLI interaction(s) implemented. Required:
  all four of those pieces are present. `Example — adapt to your own layout`: the
  wording, structure, and length are the student's own.
- **Video reflection** — a 3–5 minute video answering the three listed questions, with
  the link in the pull request description (this assignment routes the link through the
  PR, not a separate submission field). It is not part of the code and is not assessed
  here. Do not fail the code submission for anything about the video.
- **No extension work is expected yet.** The visualization and data-cleaning tracks
  belong to Part II (Assignment 11). Do not fail Part I for lacking them.

### Optional Deliverables/Tasks

Everything in the rubric table's **Exceeds** column is above the passing bar. A
submission that fully "Meets" every row is complete and correct. **Do not fail, or mark
down, a student for omitting any of the following:**

- **Query parameters passed as arguments** rather than hard-coded into the URL.
- **`.get()` used for missing keys** — handling missing data without crashing is an
  Exceeds behavior for Data Transformation, not a Phase 1 requirement.
- **Multiple interaction modes.** Phase 2 requires only one.
- **Errors caught at a specific level of the code**, or the program continuing rather
  than exiting after an error. Phase 1 requires only that errors are caught and a clear
  message is shown.
- **Fetching, parsing, and display separated into distinct functions**, and code that
  reads clearly without comments. Phase 1 requires functions with clear parameters and
  return values, not a particular decomposition.
- **Descriptive commit messages reflecting meaningful development stages.** Multiple
  commits are required; their wording is not.

</details>
