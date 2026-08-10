# Week 2 — CLI and Professional Environment (Mentor Summary)

**Environment this week:** Students leave online-python.com and build a real local setup: install Python 3.14+ (Windows natively + Git Bash, not WSL; macOS via python.org or Homebrew; Linux via package manager), verify `python`/`python3` and `pip`/`pip3`, create a `python_class/` parent with `working/` (lesson scratch) and `python-intro-homework/` (cloned fork), set up a `.venv`, and configure VS Code (Python extension + `Select Interpreter` → `.venv`). Development loop introduced: edit in VS Code, run `python file.py` in the terminal, read output, repeat.

**Git thread:** Install Git, `git config --global` name/email, generate an SSH key and register it with GitHub (deferred to The Odin Project guide), verify with `ssh -T git@github.com`. **This is the hand-off from the Week 1 personal repo** (`firstname-lastname-python`, now retired) to the shared homework repo: students **fork** `Code-the-Dream-School/python-intro-homework`, clone their fork over SSH, and run a `hello.py` smoke test (commit + push to their fork's `main`) to confirm everything's wired up. Actual assignment work then happens on an `assignment-2` branch → PR into their own fork's `main`. Submission is that PR (URL1) plus a video reflection link (URL2). Warmups require students to **paste terminal commands and output as comments** in the `.py` files — that pasted output is the proof-of-work, since mentors can't see their machine.

---

## Key concepts taught

- **Local Python install** — version check, `python` vs `python3` / `pip` vs `pip3` disambiguation (resolved once a venv is active).
- **Virtual environments** — `python -m venv .venv`, `source .../activate`, the `(.venv)` prompt indicator; must be reactivated per terminal session (VS Code / `.bashrc` snippet automates it).
- **CLI navigation** — `pwd`, `ls`/`ls -la`, `cd` (incl. `..`, `~`), `mkdir`/`mkdir -p`, `touch`; absolute vs relative paths; tab completion.
- **Running scripts** — `python file.py`, reading stdout, no-output-is-not-an-error, tracebacks in the terminal (same as Week 1, new venue).
- **Git setup** — `git --version`, global identity config, SSH auth to GitHub.
- **Fork + clone workflow** — why fork (own copy, no write access to shared repo), clone over SSH, PR base-repo gotcha.

## The assignment — Warmups + "Temperature Converter"

Work happens in a new `assignment-2` branch, in `week-2/assignment-2/`. Submit a PR link (URL1) and a video reflection (URL2) in CTD Learns.

- **Part 1 — Warmups (4 files):**
  1. `warmup1.py` — print "Python is working!"; paste command + output as comments.
  2. `warmup2.py` — CLI-navigate to the folder, then `input()` today's date and echo it; paste the nav commands used.
  3. `warmup3.py` — make a real commit, paste `git log --oneline`; then a second "what I learned" script, committed too.
  4. `warmup4.py` — deliberate bug, run it, paste the error, explain cause + fix.
- **Part 2 — `mini_project.py`:** F-to-C converter, `input()`, manual formula, f-string output rounded to one decimal.
- **Video reflection (3–5 min):** what/why of the terminal (walk through 2–3 commands), what `python script.py` actually does, and Git vs GitHub.
- **GitHub cycle reference** included: `checkout main` → `pull` → `checkout -b`, then `status`/`add`/`commit`/`push`, then close the loop after merge.

## Likely trouble spots

- **PR base defaults to the upstream repo** — the single most-flagged mistake. On a fork, GitHub pre-fills base as `Code-the-Dream-School/...`; students must switch it to `your-username/python-intro-homework`. A PR URL containing `Code-the-Dream-School` = wrong target, close and reopen.
- **Cloning the original instead of the fork** — SSH address must start with `git@github.com:your-username/`. Easy to copy from the wrong page.
- **venv not active** — `python`/`pip` ambiguity and "package not found" surprises trace back to a missing `(.venv)`. Reminder: it's per-session; each new terminal needs reactivation.
- **Editing without saving** — terminal runs what's on disk; unsaved VS Code edits look like "my fix didn't work."
- **SSH key setup** — the actual key generation is deferred to Odin's guide, not written out in-lesson. `ssh -T` permission errors should stop them (lesson says reach out to a mentor before proceeding).
- **Windows specifics** — native install (not WSL), Git Bash for all commands, "Add Python to PATH" at install, optional `winpty` alias if Python hangs.
- **Not taught yet, so acceptable:** no branching/merge-conflict depth, no `.gitignore`, no error handling in the converter (`try/except` is Week 8), and the *first real PR* was Week 1's web-editor flow — command-line PR mechanics are brand new here and expected to feel shaky.
