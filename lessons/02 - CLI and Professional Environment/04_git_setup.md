# Git Setup & Configuration

Last week you created a personal repository (`firstname-lastname-python`) and submitted Assignment 1 into it through GitHub's website. That repository was just for Week 1. **From this week on, all of your homework lives in a single shared repository maintained by Code the Dream** — you'll make your own copy of it (a **fork**) and work in that copy for the rest of the course. You can leave the Week 1 repo alone; you won't need it again.

This week you'll install Git on your computer, connect it to your GitHub account, and **fork and clone** the homework repository so that a local copy lives on your machine. By the end of the week, your local machine and GitHub will be in sync and you'll be ready to start committing real code.

## Installing and Configuring Git

Follow the steps below to install Git and tell it who you are.

### Install Git

- [The Odin Project – Setting Up Git](https://www.theodinproject.com/paths/foundations/courses/foundations/lessons/setting-up-git)

If you are on Windows, the Odin page does not include a direct link to the installer. You can find it here:
- [Git for Windows](https://git-scm.com/downloads/win)

After installing, open your terminal (or VS Code's built-in terminal) and confirm it worked:

```bash
git --version
```

You should see something like `git version 2.x.x`. If you see a version number, Git is installed.

### Configure Your Identity

Git needs to know your name and email so that your commits are labeled correctly. Run these two commands, replacing the values with your own:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

You only need to do this once. Git will use these values for every project on your machine.

## Setting Up SSH Authentication

To communicate securely with GitHub, you'll set up an **SSH key** — a pair of files that act like a digital ID card. When you push or pull code, GitHub checks your key instead of asking for a password every time.

The Odin Project setup guide you followed above walks through generating an SSH key and registering it with GitHub. If you haven't completed that step yet, go back and do it now before continuing.

Once your key is registered, you can verify the connection with:

```bash
ssh -T git@github.com
```

You should see a message like:

```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see that message, you're connected. If you see a permission error instead, reach out to a mentor before moving on — the next steps depend on this working.

## Forking and Cloning the Homework Repository

Starting this week, all of your homework lives in a shared repository maintained by Code the Dream. You won't work in that shared repo directly. Instead, you'll make your own copy of it, a **fork**, that lives under your own GitHub account. You'll do all your work in your fork, and submit pull requests against your fork.

**Why fork instead of clone directly?** The shared repo includes data files you'll use in assignments, and it's owned by Code the Dream. Forking gives you your own full copy that you can push branches to and open pull requests against, without needing write access to the shared repo. Everyone in the class works from their own fork.

### Step 1: Fork the repository

- [ ] Go to the shared repository: [github.com/Code-the-Dream-School/python-intro-homework](https://github.com/Code-the-Dream-School/python-intro-homework)
- [ ] In the top-right corner, click the **Fork** button
- [ ] On the "Create a new fork" screen, leave the defaults as they are and click **Create fork**
- [ ] Wait a moment — GitHub will take you to your new fork. Its address will be `github.com/your-username/python-intro-homework`. Confirm your username (not `Code-the-Dream-School`) appears at the top.

You now have your own copy of the homework repo. This is the repo you'll clone and work in for the rest of the course.

### Step 2: Clone your fork

**Cloning** copies your fork down to your local machine and sets up the connection between the two automatically.

#### Watch this video on cloning a repository:
> [Cloning Your GitHub Repository](https://www.youtube.com/watch?v=L1Pg1DgQf1I)

To clone your fork:

- [ ] On **your fork's** page (`github.com/your-username/python-intro-homework`), click the green **Code** button
- [ ] Select the **SSH** tab (not HTTPS)
- [ ] Click the copy icon to copy the address — it will look like `git@github.com:your-username/python-intro-homework.git`
- [ ] In your terminal, navigate to the folder where you want to store your work (for example, your Desktop or a `CodeTheDream` folder)
- [ ] Run: `git clone <paste your address here>`

> **Make sure you're cloning your fork, not the original.** The address should start with `git@github.com:your-username/` — with *your* username. If it starts with `git@github.com:Code-the-Dream-School/`, you've copied the address of the shared repo by mistake. Go back to your own fork's page and copy from there.

After cloning, run `ls` (Mac/Linux) or `dir` (Windows) to confirm a new `python-intro-homework` folder has appeared.

### A note on pull requests: submit to your own fork

> When you open a pull request later this week, GitHub will try to be "helpful" and **default the target to the original Code the Dream repository**. This is the single most common mistake with a forked workflow, so read this carefully now.

Every pull request has a *base* (where your changes are headed) and a *compare* (where your changes are coming from). Because your repo is a fork, GitHub assumes you want to send your changes back to the original and pre-fills the base as `Code-the-Dream-School/python-intro-homework`. **That is not what you want.** You want the base to be your *own* fork.

When you open a PR, check the base branch dropdown at the top of the page:

- ✅ **Correct:** base repository is `your-username/python-intro-homework`, base branch `main`
- ❌ **Incorrect:** base repository is `Code-the-Dream-School/python-intro-homework`

If the base shows `Code-the-Dream-School`, click the base repository dropdown and change it to `your-username/python-intro-homework` before creating the PR. Your PR URL should read `github.com/your-username/python-intro-homework/pull/[number]` — if you see `Code-the-Dream-School` in that URL, the PR is pointed at the wrong place. Close it and open a new one against your own fork.

Sending a PR to the original repo by accident won't break anything — the maintainers simply won't merge it — but it means your work isn't submitted correctly and your mentor can't review it. When in doubt, double-check the base repository name.

## Verify Your Setup

Before starting the assignment, do a quick smoke test to confirm that Git, GitHub, and Python are all working together. You'll do this inside the fork you just cloned.

- [ ] Navigate into your cloned fork in the terminal: `cd python-intro-homework`
- [ ] Create a new file called `hello.py`
- [ ] Open it in VS Code and add one line: `print("Hello, my name is Your Name")`
- [ ] Run the script from your terminal to confirm it works: `python hello.py`
- [ ] Stage and commit the file:
  ```bash
  git add hello.py
  git commit -m "add hello.py"
  ```
- [ ] Push your changes to GitHub: `git push origin main`
- [ ] Go to your fork's page on GitHub (`github.com/your-username/python-intro-homework`) and confirm that `hello.py` appears there

If `hello.py` shows up on your fork, everything is connected and you're ready to start the assignment. The graded work goes on its own `assignment-2` branch — see the assignment instructions for the branch, folder, and pull request steps.
