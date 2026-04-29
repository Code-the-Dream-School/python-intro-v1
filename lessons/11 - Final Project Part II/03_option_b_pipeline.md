# Option B — Data Cleaning and CSV Export

Option B has you clean, process, and export your data to a structured CSV file for external use.

---

## Why API Data Needs Cleaning

Public APIs return data in whatever format the API designer chose. In practice, this means:

- Some records are missing fields entirely
- Numbers are sometimes returned as strings (or strings as numbers)
- Some values are `None`, an empty string, or a placeholder like `"N/A"`
- Lists or nested dicts appear where you expected a simple value

Before exporting to CSV, you decide what to do with each of these situations. Those decisions, and the reasoning behind them, are what this track is about.

---

## A Per-Field Decision Framework

For every field you plan to include in your CSV, ask three questions:

**1. Can this field be missing or `None`?**

Use `.get()` with a sensible default so a missing key doesn't crash your program:

```python
name = record.get("name", "Unknown")
population = record.get("population", 0)
```

Choose defaults that make sense for the field. `0` is a reasonable default for a numeric field; `"Unknown"` or `""` may be appropriate for text. Document what you chose.

**2. Is the type consistent across records?**

Check whether a field comes back as `int`, `float`, or `str` depending on the record. If it's inconsistent, convert explicitly — but wrap the conversion in a `try/except` in case the value isn't convertible:

```python
try:
    area = float(record.get("area", 0))
except (ValueError, TypeError):
    area = 0.0
```

**3. Is the value valid for your use case?**

An empty string, `0`, `None`, or a placeholder like `"N/A"` might all mean "no data." Decide for each field whether to:
- **Keep the record** and fill a default value
- **Skip the record** entirely

If you skip it, filter it out before writing. If you fill a default, note what you chose and why.

---

## Filtering Invalid Records

To skip records that don't meet your criteria, write a helper function and use a list comprehension to apply it:

```python
def is_valid(record):
    """Return True if the record has the minimum required fields."""
    return bool(record.get("name")) and record.get("population") is not None

clean_records = [r for r in records if is_valid(r)]
```

Adjust the conditions to match what's actually required for your export to be useful.

---

## Building Your Cleaning Function

Organize all cleaning logic into a dedicated function. A good `clean_data()` function:

- Takes the raw list of dicts from your API
- Returns a new list of dicts with only the fields you want, in the types you want
- Does not modify the original records

```python
def clean_data(records):
    """
    Clean raw API records and return a list of dicts ready for CSV export.
    Skips records missing a name. Normalizes population to int.
    """
    cleaned = []
    for record in records:
        if not record.get("name"):
            continue

        cleaned.append({
            "name": record.get("name", "Unknown"),
            # add your other fields here, applying the framework above
        })
    return cleaned
```

The specific fields and cleaning rules depend on your chosen API and what you want the CSV to contain.

---

## Exporting with csv.DictWriter

You used `csv.DictWriter` in Week 7. A quick review:

```python
import csv

def export_to_csv(records, filename):
    """Export a list of dicts to a CSV file."""
    if not records:
        print("No records to export.")
        return

    fieldnames = list(records[0].keys())

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Exported {len(records)} records to {filename}.")
```

Call it after `clean_data()`:

```python
data = fetch_data()
cleaned = clean_data(data)
export_to_csv(cleaned, "output.csv")
```

---

## Writing Your Explanation

Your submission requires a brief explanation of the cleaning decisions you made. This is as important as the code — it demonstrates that you understood *why*, not just *how*. Add it to your `README.md` under a `## Data Cleaning Decisions` heading.

It should be 3–5 sentences that answer:

1. Which fields did you include in the CSV, and which did you leave out? Why?
2. What did you do with records that had missing or invalid values — skip them, or fill a default?
3. Was there any type coercion or normalization required?
