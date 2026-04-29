# GitHub Workflow: Branches, Commits, and Pull Requests

Last week you installed Git, connected it to GitHub, and pushed your first file. This week you'll learn the full workflow you'll use for every assignment going forward: creating a **branch**, committing your changes, and opening a **pull request**.

## Why Branches?

So far you've been committing directly to `main`. In a real project, `main` represents the stable, working version of your code. Branches let you do new work in an isolated space without touching `main` until you're ready.

Think of `main` as a clean copy of your project. Each week, you'll create a new branch off of it, do your work there, and then merge it back in once it's been reviewed. This keeps your history organized and makes it easy for a reviewer to see exactly what changed.

## Creating a Branch

Make sure you're in your repository folder, on the `main` branch, and up to date before starting:

```bash
git checkout main
git pull origin main
```

Then create a new branch for this week's work:

```bash
git checkout -b week-3
```

The `-b` flag creates the branch and switches to it in one step. You can verify you're on the right branch with:

```bash
git branch --show-current
```

You should see `week-3`.

## Making Changes

Open your repository in VS Code and make some changes — add a new Python file or update `hello.py` with something from what you've been practicing. Save your work when you're done.

## Staging and Committing

Once you've made changes, use `git status` to see what Git has noticed:

```bash
git status
```

> **Reading `git status` output:** Git uses three states to describe your files:
>
> - **Untracked** — Git sees the file but has never been asked to track it. Newly created files appear here.
> - **Modified (not staged)** — Git is tracking the file and has detected changes, but those changes are not yet included in your next commit.
> - **Staged** — Changes are queued and ready to be saved in your next commit.
>
> Think of staging like packing a box before shipping it. `git add` puts things in the box. `git commit` seals and labels it.

Stage your changes and commit them:

```bash
git add .
git commit -m "describe what you added or changed"
```

> **Writing good commit messages:** Describe *what changed and why*, not just "week 3 work." A good message lets anyone read the history and understand what each commit contains without opening it.

Then push your branch to GitHub:

```bash
git push origin week-3
```

## Opening a Pull Request

### Watch this video on creating a Pull Request:
[Creating a Pull Request Video](https://www.youtube.com/watch?v=89hjRfX0dS4)

- [ ] Go to your GitHub repository page — you should see a notice that `week-3` had a recent push, with a green **Compare & pull request** button. Click it.
- [ ] Add any notes or questions for your reviewer in the description field
- [ ] Click **Create pull request**
- [ ] Copy the URL of your pull request (it will look like `https://github.com/your-username/firstname-lastname-python/pull/1`) and paste it into your assignment submission form

## Merging and Syncing Back

Once your PR has been reviewed and approved, it can be merged into `main` on GitHub. This week, go ahead and merge it yourself so you can see how the process works.

After merging on GitHub, bring your local `main` branch up to date:

```bash
git checkout main
git pull origin main
```

This step is important — it keeps your local `main` in sync with GitHub so that next week's starting point is clean.

## The Git / GitHub Workflow

The following image shows the complete workflow. This week, we completed the full cycle.

![Git Flow Diagram — Week 3](link-to-diagram)

---

## The Full Cycle — Your Weekly Reference

From here on, you will repeat this sequence for every assignment:

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b week-4        # replace with the current week number
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin week-4        # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

> **Why does the order matter?** Each step moves your code between three places: your working files, your local Git history, and GitHub. `add` moves changes into the staging area. `commit` saves a snapshot to your local history. `push` sends that history to GitHub. Skipping a step means your changes don't make it all the way through.

> **Common errors:**
> - *"nothing to commit, working tree clean"* — You haven't made any changes since your last commit, or you forgot to save the file.
> - *"fatal: The current branch has no upstream branch"* — Run the full push command: `git push --set-upstream origin week-4`
> - *"Your branch is behind 'origin/main'"* — Run `git pull origin main` to sync before continuing.

## Assignment — Your First PR

- [ ] Starting from `main`, create a new branch called `week-3`
- [ ] Add a new Python file to your project. It can be anything you've been working on in the course so far — a script with a function, a loop, or a simple program
- [ ] Stage and commit your changes with a descriptive commit message
- [ ] Push your branch to GitHub and open a pull request
- [ ] Merge your pull request on GitHub, then pull the changes back to your local `main`
- [ ] Paste your pull request link into the submission form
