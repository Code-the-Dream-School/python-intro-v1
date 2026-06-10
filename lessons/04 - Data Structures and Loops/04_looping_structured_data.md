# Looping Over Structured Data

**Objective**: By the end of this lesson, you will be able to:
  * Loop over lists, dictionaries, and sets using `for` loops
  * Use `.items()` to loop over dictionary keys and values together
  * Work with lists of dictionaries as a pattern for tabular data
  * Apply loop patterns to filter, transform, and summarize structured data

---

## Loops Meet Data Structures

In the previous lessons, you learned about lists, tuples, dictionaries, and sets. Now you'll combine them with `for` loops to process real data. This is one of the most practical skills in Python: nearly every program that works with data involves looping over a collection.

---

## Looping Over Lists

You've already seen this pattern:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

You can also use the index with `enumerate()` if you need to know the position:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

Output:
```
0: apple
1: banana
2: cherry
```

### Common Loop Patterns with Lists

**Filtering** (keeping items that match a condition):

```python
scores = [85, 42, 91, 67, 73, 55, 88]
passing = []
for score in scores:
    if score >= 70:
        passing.append(score)
print(passing)   # Output: [85, 91, 73, 88]
```

**Accumulating** (building up a total):

```python
prices = [12.99, 5.50, 8.75, 3.25]
total = 0
for price in prices:
    total += price
print(f"Total: ${total:.2f}")   # Output: Total: $30.49
```

**Transforming** (creating a new list from an old one):

```python
names = ["jazmine", "carlos", "amir"]
capitalized = []
for name in names:
    capitalized.append(name.title())
print(capitalized)   # Output: ['Jazmine', 'Carlos', 'Amir']
```

---

## Looping Over Dictionaries

Dictionaries give you three ways to loop:

**Loop over keys (default):**

```python
student = {"name": "Carlos", "grade": "A", "score": 95}
for key in student:
    print(key)
```

Output:
```
name
grade
score
```

**Loop over values:**

```python
for value in student.values():
    print(value)
```

Output:
```
Carlos
A
95
```

**Loop over keys and values together with `.items()`:**

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:
```
name: Carlos
grade: A
score: 95
```

The `.items()` pattern is the most useful because you get both the key and value in each iteration.

### AI Prompt: Predict-Then-Check

Study this code without running it:

```python
inventory = {"apples": 5, "bananas": 12, "cherries": 3}
for item, count in inventory.items():
    if count < 10:
        print(f"Low stock: {item} ({count})")
```

Predict the output, then check:

> "I'm learning to loop over Python dictionaries. I predict this code will print [your prediction]. Can you walk me through how `.items()` provides both the key and value?"

---

## Looping Over Sets

You can loop over a set just like a list, but remember: **sets are unordered**. The items may appear in a different order each time.

```python
tags = {"python", "beginner", "tutorial"}
for tag in tags:
    print(tag)
```

The output will include all three tags, but the order is not guaranteed.

---

## Lists of Dictionaries

One of the most important patterns in Python is the **list of dictionaries**. This is how you represent tabular data (like a spreadsheet) in Python: each dictionary is a row, and each key is a column name.

```python
students = [
    {"name": "Jazmine", "grade": "A", "score": 95},
    {"name": "Carlos", "grade": "B", "score": 82},
    {"name": "Amir", "grade": "A", "score": 91},
    {"name": "Priya", "grade": "C", "score": 74}
]
```

This pattern shows up everywhere:
- **Week 7**: when you read data from CSV files, you'll get lists of dictionaries
- **Week 9**: when you fetch data from an [API](https://aws.amazon.com/what-is/api/), the response is usually a list of dictionaries
- **Final Project**: your command-line-interfacde (CLI) tool will process lists of dictionaries from an API

### Looping Over a List of Dictionaries

```python
for student in students:
    print(f"{student['name']}: {student['score']}")
```

Output:
```
Jazmine: 95
Carlos: 82
Amir: 91
Priya: 74
```

### Filtering

```python
honor_roll = []
for student in students:
    if student["score"] >= 90:
        honor_roll.append(student["name"])
print(honor_roll)   # Output: ['Jazmine', 'Amir']
```

### Finding a Value

```python
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")   # Output: Class average: 85.5
```

### Building New Data from Old

```python
summary = []
for student in students:
    summary.append({
        "name": student["name"],
        "passed": student["score"] >= 70
    })
print(summary)
# Output: [{'name': 'Jazmine', 'passed': True}, {'name': 'Carlos', 'passed': True}, 
#          {'name': 'Amir', 'passed': True}, {'name': 'Priya', 'passed': True}]
```

---

## Videos

**"Python Tutorial for Beginners 4: Lists, Tuples, and Sets"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=W8KRzm-HUcc) for iteration examples over lists and sets. Also review the dictionary video from the previous lesson for dictionary looping.

---

## Check for Understanding

**Question 1:** What does `.items()` return when you loop over a dictionary?

* A) A list of keys
* B) A list of values
* C) Pairs of keys and values as tuples
* D) A single string

<details>
<summary>Answer</summary>

**C) Pairs of keys and values as tuples.** Each iteration gives you a `(key, value)` tuple, which you can unpack into two variables: `for key, value in dict.items()`.

</details>

**Question 2:** What will this code output?

```python
scores = [85, 42, 91, 67]
high = []
for s in scores:
    if s >= 80:
        high.append(s)
print(high)
```

* A) `[85, 91]`
* B) `[42, 67]`
* C) `[85, 42, 91, 67]`
* D) `[]`

<details>
<summary>Answer</summary>

**A) `[85, 91]`.** The loop checks each score and only appends those that are 80 or above.

</details>

**Question 3:** You have a list of dictionaries representing books. How would you access the title of the first book?

```python
books = [
    {"title": "Dune", "author": "Herbert"},
    {"title": "1984", "author": "Orwell"}
]
```

* A) `books["title"]`
* B) `books[0]["title"]`
* C) `books.title[0]`
* D) `books[0][0]`

<details>
<summary>Answer</summary>

**B) `books[0]["title"]`.** First, `books[0]` gets the first dictionary in the list. Then `["title"]` accesses the value for the key `"title"` in that dictionary.

</details>

---

## Further Reading

- [W3Schools: Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Real Python: How to Iterate Through a Dictionary](https://realpython.com/iterate-through-dictionary-python/)
- [Python Official Documentation: Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
