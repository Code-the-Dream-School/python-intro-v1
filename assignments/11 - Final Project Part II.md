# Assignment 11 — Final Project Part II

## Universal Requirements

Apply to both options.

- **Modular design:** All extension logic in reusable functions with clear parameters and return values
- **Standard library usage:** Use at least one standard library module beyond `csv` (e.g., `os`, `datetime`)
- **Version control:** All work committed and submitted via pull request; commit history shows incremental progress across both weeks
- **Video demo:** A screen-recorded video (2–4 min) walking through your running project and explaining one technical decision you made

---

## Option A Requirements

- Use `matplotlib` to create at least one chart that answers a specific question you pose about your data
- Label your chart: axis labels, a descriptive title, and readable tick labels
- Save the chart as a PNG file
- Include a written explanation in `README.md` (under `## Visualization`) describing what the chart shows, what the main takeaway is, and why you chose that chart type

## Option B Requirements

- Clean the data: handle missing values, normalize field types, and filter invalid records using the per-field decision framework
- Export the cleaned data to a well-structured CSV file using `csv.DictWriter`
- Include a written explanation in `README.md` (under `## Data Cleaning Decisions`) describing which fields you included, what you did with missing or invalid values, and any type coercion applied

---

## Submission

**Required files**

Your final repository must include:

- `main.py` — the entry point for your CLI tool
- Any additional `.py` files you created
- `requirements.txt` — all third-party packages used
- `README.md` — complete with project description, API used, how to run, CLI interactions, extension track, and written explanation (Visualization or Data Cleaning Decisions section, depending on your track)
- **Option A only:** the chart saved as a `.png` file
- **Option B only:** a sample exported `.csv` file

**Pull request**

Update your pull request from Week 10 (or open a new one from your same feature branch, depending on your class workflow). Your PR description should:

- Confirm which option you chose (A or B)
- Briefly describe what the extension adds to the project
- Include your video demo link

Your combined commit history across both weeks should show incremental progress. Do not squash your Week 10 commits.

**Video Demo**

Record a 2–4 minute video showing your completed project. Include the link in your PR description and in your `README.md`.

Your video should address:

1. Run the complete project from `main.py` entry to output — show it working live.
2. Show the extension deliverable (your chart or your CSV file) and explain one decision you made while building it.
3. If you had more time, what would you add or improve?

Requirements:
- 2–4 minutes
- Show your running program on screen — don't just describe it
- Speak in your own words

Upload to YouTube (unlisted) or Loom.
---

## Rubric

> Note that this is the Part II rubric. Can also point to the full [final project rubric](https://github.com/Code-the-Dream-School/intro-to-python-v1/blob/main/resources/final-project-overview.md).

| Category | Does Not Meet | Meets | Exceeds |
|---|---|---|---|
| **Extension Track** | Extension not attempted, or broken and does not run. | Extension requirements met: chart answers a stated question with appropriate labels (A), or CSV exported with cleaned data and written explanation (B). | Chart is polished and well-labeled (A), or data cleaning handles multiple edge cases with clear reasoning (B). Written explanation reflects genuine decision-making, not just a description of the code. |
| **Modular Design** | Extension logic mixed into existing functions or written as one monolithic block. | Extension logic is in dedicated functions with clear parameters and return values. | Functions are well-named and single-purpose. The extension integrates cleanly with the Week 10 codebase. |
| **Standard Library** | No standard library module used beyond `csv`. | At least one standard library module used appropriately. | Standard library usage is well-chosen and adds real value (e.g., `datetime` for timestamps, `os.path` for file handling). |
| **Version Control** | All extension work in a single commit. | Multiple commits show incremental progress. Work submitted via pull request. | Commit messages are descriptive and reflect meaningful stages of development across both weeks. |
| **Video Demo** | No video submitted, or video does not show the running program. | 2–4 minute video walks through the running project and explains one technical decision. | Technical explanation goes beyond what the code says to *why* the decision was made. |

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

## 🎉 Congrats on submitting your Python Intro final project!

The foundational work you've put in during this class is going to make you a strong developer!
