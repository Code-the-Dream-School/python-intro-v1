# Git Setup & Configuration

Last week you created a repository on GitHub. Right now it only exists remotely — in the cloud. This week, you'll install Git on your computer, connect it to your GitHub account, and **clone** your repository so that a local copy lives on your machine as well.

By the end of this week, your local machine and GitHub will be in sync and you'll be ready to start committing real code.

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

## Cloning Your Repository

**Cloning** copies your remote GitHub repository down to your local machine and sets up the connection between the two automatically.

### Watch this video on cloning a repository:
> [Cloning Your GitHub Repository](https://www.youtube.com/watch?v=L1Pg1DgQf1I)

To clone your repo:

- [ ] On your GitHub repository page, click the green **Code** button
- [ ] Select the **SSH** tab (not HTTPS)
- [ ] Click the copy icon to copy the address — it will look like `git@github.com:your-username/firstname-lastname-python.git`
- [ ] In your terminal, navigate to the folder where you want to store your work (for example, your Desktop or a `CodeTheDream` folder)
- [ ] Run: `git clone <paste your address here>`

After cloning, run `ls` (Mac/Linux) or `dir` (Windows) to confirm a new folder with your repository name has appeared.

## The Git / GitHub Workflow

The following image shows the full workflow. This week, we have completed the portion outlined with the red dashed line — your remote repository now has a connected local copy.

![Git Flow Diagram — Week 2](link-to-diagram)

## Assignment — Verify Your Setup

Let's confirm that Git, GitHub, and Python are all working together.

- [ ] Navigate into your cloned repository in the terminal: `cd firstname-lastname-python`
- [ ] Create a new file called `hello.py`
- [ ] Open it in VS Code and add one line: `print("Hello, my name is Your Name")`
- [ ] Run the script from your terminal to confirm it works: `python hello.py`
- [ ] Stage and commit the file:
  ```bash
  git add hello.py
  git commit -m "add hello.py"
  ```
- [ ] Push your changes to GitHub: `git push origin main`
- [ ] Go to your GitHub repository page and confirm that `hello.py` appears there
- [ ] Paste the link to your repository into the submission form when you submit this week
