# Parsing Lines Into Data Structures (Lists of Dicts)

In the previous section, you used `csv.reader` to loop through a CSV file row by row. Each row came back as a plain list — you had to remember that index `0` was the name, index `1` was the price, and so on.

This section introduces a better pattern: reading a CSV into a **list of dictionaries**, where each row becomes a dictionary and field names come from the header row. This is one of the most common patterns in data work, and it connects directly to the lists and dicts you learned in Week 5.

### From csv.reader to csv.DictReader

Recall how `csv.reader` works:

```python
import csv

with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        print(row[0], row[2])  # product name and price — by index
```

`csv.DictReader` does the same thing, but returns each row as a dictionary with the header names as keys:

```python
import csv

with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['product'], row['price'])  # access by name
```

No need to skip the header or track which index is which. This makes your code easier to read and much easier to update when the CSV structure changes.

### Collecting All Rows Into a List

Reading one row at a time is fine for simple tasks, but often you want to load the whole file into memory so you can work with it freely — filter it, sort it, or process it multiple times.

The pattern: create an empty list, then append each row as you loop:

```python
import csv

records = []
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        records.append(row)
```

Or more concisely, wrap the reader in `list()`:

```python
import csv

with open('products.csv', 'r') as file:
    records = list(csv.DictReader(file))
```

Either way, `records` is now a list of dicts — one dict per row.

### What the Data Structure Looks Like

Given this CSV:

```
product,category,price,quantity
Notebook,Stationery,4.99,150
Pen,Stationery,1.49,500
Stapler,Office,12.99,75
```

You'd get:

```python
[
    {'product': 'Notebook', 'category': 'Stationery', 'price': '4.99', 'quantity': '150'},
    {'product': 'Pen', 'category': 'Stationery', 'price': '1.49', 'quantity': '500'},
    {'product': 'Stapler', 'category': 'Office', 'price': '12.99', 'quantity': '75'},
]
```

Notice that all values are **strings** — `csv.DictReader` doesn't convert numbers for you. You'll need to cast them explicitly if you want to do math:

```python
price = float(row['price'])
quantity = int(row['quantity'])
```

### Working with the Data

Once you have a list of dicts, you can apply everything you know about lists and dicts.

**Loop through and print fields**

```python
for item in records:
    print(f"{item['product']}: ${item['price']}")
```

**Filter to rows matching a condition**

```python
stationery = [item for item in records if item['category'] == 'Stationery']
```

**Convert numeric fields across all rows**

```python
for item in records:
    item['price'] = float(item['price'])
    item['quantity'] = int(item['quantity'])
```

### A Complete Mini Pipeline

Here's a full example that reads a CSV, converts numeric fields, filters rows, and computes a result:

```python
import csv

# Load all rows into memory
with open('products.csv', 'r') as file:
    records = list(csv.DictReader(file))

# Convert numeric fields
for item in records:
    item['price'] = float(item['price'])
    item['quantity'] = int(item['quantity'])

# Filter to one category
office_items = [item for item in records if item['category'] == 'Office']

# Compute total inventory value
total_value = sum(item['price'] * item['quantity'] for item in office_items)
print(f"Office inventory value: ${total_value:.2f}")
```

This is the **file → structured data → useful output** pattern you'll use throughout the rest of the course.

### Check for Understanding

**Question**: After reading a CSV file with `csv.DictReader`, what type is the value `row['price']` if the CSV contains `4.99`?

* A) `float`
* B) `int`
* C) `str`
* D) It depends on the data in the file

<details>
<summary>Answer</summary>

**Answer**: C) `str` — `csv.DictReader` always returns string values. You need to convert them explicitly with `float()` or `int()` if you want to do math.

</details>
