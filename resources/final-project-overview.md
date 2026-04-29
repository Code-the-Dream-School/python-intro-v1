# Final Project Overview

> This page is a reference you can return to throughout the course. We recommend reading it during Week 9 before you begin building.

Your final project is a Python CLI tool that connects to a real public API, transforms the data it returns, and lets a user interact with that data in real time. You'll build the core program in Week 10 and add an extension in Week 11 based on your interests.

By the end of the project, you'll have a complete, working Python program that demonstrates everything you've learned: fetching data from the web, organizing it into useful structures, writing clean modular code, handling errors gracefully, and presenting results to a user.

---

## Timeline

### Week 10 — Core Program + CLI Tool

Everyone builds the same foundation this week.

**Phase 1: Core Program**

- Fetch data from a public API using `requests`
- Parse the JSON response into a list of dictionaries
- Handle errors with `try/except` blocks
- Organize all logic into clean, reusable functions

**Phase 2: CLI Tool**

Add a command-line interface that lets users interact with the data in real time:

- Accept user input (via `input()` prompts or command-line arguments)
- Display results in a readable, formatted way
- Include at least one meaningful interaction — for example, filter by a field, look up a specific record, or compare two results

---

### Week 11 — Your Choice of Extension

After completing Week 10, choose the extension track that interests you more.

**Option A — Visual Analysis**

Build a data visualization that answers a specific question about your data.

- Use `matplotlib` to create at least one meaningful chart or graph
- The visualization must answer a question you pose (e.g., "Which region has the highest average population?")
- Include a brief written explanation of what the visualization shows and why you chose it

**Option B — Data Pipeline**

Clean, process, and export your data to a structured CSV file for external use.

- Handle missing values, normalize field types, and filter out invalid records
- Export the cleaned data to a well-structured CSV using `csv.DictWriter`
- Include a brief written explanation of your cleaning decisions and why you made them

---

## Choosing Your API

You'll work with the same API across both weeks, so pick one that genuinely interests you. Three recommended options are listed below. All are free, require no API key, and return data that works well for this project.

### Option 1 — REST Countries

A database of every country in the world, with data on population, area, region, languages, capital city, and more.

- **Base endpoint:** `https://restcountries.com/v3.1/all`
- **CLI ideas:** filter countries by region, find the largest or most populous country, compare two countries side by side
- **Option A:** bar chart of the top 10 countries by population or area
- **Option B:** export a clean CSV of country names, regions, populations, and areas
- **Docs:** https://restcountries.com

### Option 2 — Open Library Search

A search API for books and authors. Query by author, title, or subject and get a list of matching books with publication year, subject tags, and page count.

- **Base endpoint:** `https://openlibrary.org/search.json?author=tolkien`
- **CLI ideas:** search for books by author or subject, filter by decade, look up a specific title
- **Option A:** bar chart of books published per decade for a given author
- **Option B:** export search results to CSV with title, author, year, and subject
- **Docs:** https://openlibrary.org/developers/api

### Option 3 — PokeAPI

A complete Pokémon database with stats (HP, attack, defense, speed, special attack, special defense), types, and abilities for every Pokémon.

- **Base endpoint:** `https://pokeapi.co/api/v2/pokemon/{name}` (look up one Pokémon at a time by name)
- **Note:** Unlike the other two options, PokeAPI requires a separate HTTP request for each Pokémon you want data on. This is a common real-world API pattern, but it's worth knowing before you start.
- **CLI ideas:** look up a Pokémon by name, compare the stats of two Pokémon, filter a list by type
- **Option A:** bar chart comparing all six stats for a Pokémon, or a head-to-head stat comparison
- **Option B:** build a list from user input and export each Pokémon's stats to CSV
- **Docs:** https://pokeapi.co/docs/v2

> **Using a different API:** If you'd like to use an API not listed here, check with your class's Cohort Instructional Leader (CIL) first. It must be free, require no API key for basic access, and return a list of records that can be structured as a list of dictionaries.

---

## Deliverables

By the end of Week 11, your project repository should contain:

- [ ] `main.py` — the entry point for your CLI tool
- [ ] Any additional `.py` files for your module code
- [ ] `requirements.txt` listing any third-party packages used
- [ ] `README.md` describing your project, the API you used, how to run it, and which extension track you chose
- [ ] **Option A only:** the generated chart as a `.png` file, plus your written explanation
- [ ] **Option B only:** a sample exported CSV file, plus your written explanation of cleaning decisions
- [ ] A screen-recorded video (2–4 minutes) walking through your running project and explaining one technical decision you made

---

## Rubric

Your project will be evaluated on the following criteria.

| Category | Does Not Meet Expectations | Meets Expectations | Exceeds Expectations |
|---|---|---|---|
| **API Integration** | Program fails to connect to the API, or the call is broken and does not run. | Program successfully fetches data from the chosen API using `requests`. URL and parameters are clearly organized. | API call is wrapped in a dedicated function. Query parameters are passed as arguments rather than hard-coded. |
| **Data Transformation** | JSON response is not parsed, or the program crashes when accessing data fields. | JSON response is parsed into a list of dictionaries with relevant fields extracted and accessible by key. | Transformation is in a dedicated function. `.get()` is used to handle missing keys without crashing. |
| **CLI Tool** | No user interaction — program just prints raw output with no input. | Accepts at least one form of user input and returns formatted results. At least one meaningful interaction (filter, lookup, or comparison) is implemented. | Multiple interaction modes available. Output is clearly formatted and easy to read. Unexpected input is handled without crashing. |
| **Error Handling** | No error handling — connection errors or bad data cause unhandled tracebacks. | `try/except` blocks catch connection errors and bad status codes. User sees a clear error message instead of a traceback. | Errors are caught at the right level of the code. Program continues or exits gracefully with a helpful message. |
| **Code Organization** | All logic is in one long script with no functions, or functions that do not use parameters and return values. | Logic is split into functions with clear names, parameters, and return values. Each function has a single responsibility. | Fetching, parsing, and display are cleanly separated. Code is readable without requiring comments to understand. |
| **Extension Track** | Extension is not attempted, or is broken and does not run. | Extension requirements are met: visualization answers a stated question (A), or CSV is exported with cleaned data (B). Written explanation is included. | Visualization is polished and well-labeled (A), or data cleaning handles multiple edge cases with clear reasoning (B). Written explanation reflects genuine decision-making. |
| **Version Control** | Work is submitted in a single commit, or without a pull request. | Multiple commits show incremental progress. Work is submitted via pull request. | Commit messages are descriptive and reflect meaningful stages of development. |
