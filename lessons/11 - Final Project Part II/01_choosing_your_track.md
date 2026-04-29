# Choosing Your Extension Track

You've built the core program and CLI tool. Now, it's time to extend it into something really cool.

Week 11 has two options. Both take what you built in Week 10 and add a meaningful layer on top. Read this page before you start building, then go to your chosen track's lesson and read it before writing any code.

---

## What Each Track Produces

**Option A — Data Visualization**

You'll write a function that takes your processed data and generates a bar chart answering a specific question you pose. You'll save the chart as a PNG file and write a short explanation of what it shows. This helps you prepare for some of the data visualization work you'll do in Python for Data Engineering & Analysis.

What you turn in: a PNG image, a written explanation in your `README.md`, and the code that produced it.

**Option B — Data Pipeline**

You'll write a function that cleans your API data — handling missing values, normalizing types, filtering out invalid records — and exports it to a well-structured CSV file. You'll document the cleaning decisions you made and why. This helps you prepare for the full ETL pipeline you'll build in Python for Cloud & AI.

What you turn in: a sample CSV file, a written explanation in your `README.md`, and the code that produced it.

---

## What's New in Each Track

| | Option A | Option B |
|---|---|---|
| **New library** | `matplotlib` — you haven't used this before! | None |
| **Familiar tool** | — | `csv.DictWriter` — you used this in Week 7 |
| **New concept** | Constructing a chart from your data | Applying a cleaning decision framework |
| **Written deliverable** | What the chart shows and why you chose it | Why you made each cleaning decision |

If you choose Option A, expect to spend a little time learning the library mechanics before connecting it to your project data. The lesson walks you through a standalone example first, so you can see a chart before you touch your project at all. You'll learn how to use `matplotlib` in Python for Data Engineering and Analysis, so this gives you a leg up in your next class.

If you choose Option B, the export mechanics are familiar. The new work is the judgment involved in cleaning — deciding what to do with missing fields, inconsistent types, and invalid records, then explaining those choices. You'll work closely with data cleaning in both Python for Data Engineering & Analysis and Python for Cloud & AI, so this is great prep for future coursework.

---

## Which Should You Choose?

Ask yourself: **Which interests you more: presenting your data visually, or cleaning and structuring it for another use?**

* Option A is a good fit if you want to tell a story with your data, or if you're curious about how Python produces charts.
* Option B is a good fit if you're more interested in data work — processing, structuring, and exporting data so it could be used in a spreadsheet, a database, or another program.

Neither track is harder than the other, they just involve different kinds of work. Pick the one that sounds more interesting!

---

## Before You Start Week 11

Check these off before you open a new file:

- [ ] Your Week 10 project runs without errors from start to finish
- [ ] `fetch_data()` successfully returns data from your API
- [ ] `process_data()` returns a list of dictionaries with the fields you need
- [ ] Your CLI tool accepts user input and displays results
- [ ] All Week 10 work is committed and submitted via pull request

If any of these aren't true yet, fix those issues before starting Week 11. Extension code built on a broken foundation will be harder to debug and harder to submit.

---

## Ready? Go to Your Track's Lesson

Once you've chosen:

- **Option A:** Read [Option A — Data Visualization with matplotlib](02_option_a_visualization.md) before writing any code.
- **Option B:** Read [Option B — Data Cleaning and CSV Export](03_option_b_pipeline.md) before writing any code.
