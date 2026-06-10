# Loop Patterns: Counting, Accumulating, Searching

**Objective**: By the end of this lesson, you will be able to:
  * Recognize and apply three common loop patterns: counter, accumulator, and search
  * Write nested loops for working with multi-dimensional data
  * Choose between `for` and `while` for different patterns
  * Build a mental toolkit of reusable loop structures

---

## Why Learn Patterns?

Most loops you write will follow one of a few common structures. Once you recognize these patterns, you won't have to figure out each loop from scratch. Instead, you'll think "this is a counter problem" or "this is a search problem" and reach for the right pattern.

---

## Pattern 1: Counter

The **counter pattern** tracks how many times something happens. You start a counter variable at 0, then add 1 each time a condition is met.

```python
words = ["hello", "world", "hi", "python", "go", "code"]
short_count = 0
for word in words:
    if len(word) <= 3:
        short_count += 1
print(f"Words with 3 or fewer letters: {short_count}")
```

Output:
```
Words with 3 or fewer letters: 2
```

The structure is always the same:
1. Create a counter variable (set to 0)
2. Loop through the data
3. Inside the loop, check a condition and increment the counter
4. After the loop, use the counter

### Another Example: Counting Vowels

```python
text = "Hello World"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print(f"Vowels: {vowel_count}")
```

Output:
```
Vowels: 3
```

---

## Pattern 2: Accumulator

The **accumulator pattern** builds up a result as the loop runs. This could be a running total, a growing list, or a concatenated string.

### Numeric Accumulator (Running Total)

```python
expenses = [45.99, 12.50, 8.75, 23.00, 67.30]
total = 0
for expense in expenses:
    total += expense
print(f"Total spent: ${total:.2f}")
```

Output:
```
Total spent: $157.54
```

### List Accumulator (Building a New List)

```python
names = ["jazmine", "carlos", "amir", "priya"]
capitalized = []
for name in names:
    capitalized.append(name.title())
print(capitalized)
```

Output:
```
['Jazmine', 'Carlos', 'Amir', 'Priya']
```

### String Accumulator

```python
words = ["Code", "the", "Dream"]
result = ""
for word in words:
    result += word + " "
print(result.strip())
```

Output:
```
Code the Dream
```

The structure is always:
1. Create an accumulator variable (0 for numbers, `[]` for lists, `""` for strings)
2. Loop through the data
3. Add to the accumulator each iteration
4. After the loop, use the accumulated result

### AI Prompt: Retrieval Practice

Open your preferred AI chatbot and explain the difference between the counter pattern and the accumulator pattern in your own words. Give one example of each.

> "I just learned about loop patterns in Python. Here is my understanding of counters vs accumulators: [your explanation]. Can you tell me if I'm on the right track?"

---

## Pattern 3: Search

The **search pattern** looks through data for a specific item or condition. It typically uses a `for` loop with `break`, or a `while` loop.

### Search with `for` and `break`

```python
students = ["Jazmine", "Carlos", "Amir", "Priya"]
target = "Amir"
found = False
for student in students:
    if student == target:
        found = True
        break

if found:
    print(f"Found {target}!")
else:
    print(f"{target} not in the list.")
```

Output:
```
Found Amir!
```

The `break` is important here. Once you find what you're looking for, there's no reason to keep looping through the rest of the list.

### Search with `while` (User Input)

```python
secret = 42
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"You got it in {attempts} attempts!")
```

This combines the search pattern with the counter pattern, counting how many attempts the user makes.

### Finding an Index

```python
scores = [85, 92, 78, 95, 88]
target = 95
index = -1
for i in range(len(scores)):
    if scores[i] == target:
        index = i
        break

if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")
```

Output:
```
Found 95 at index 3
```

Note: Python has a built-in `list.index()` method and the `in` keyword for simple searches. The manual search pattern is worth learning because it teaches you how searching works in the background, and you'll need it when your search logic is more complex than a simple equality check.

---

## Nested Loops

A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}", end="\t")
    print()
```

Output:
```
1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	
2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	
3 x 1 = 3	3 x 2 = 6	3 x 3 = 9	
```

The `end="\t"` puts a tab instead of a newline after each print, and `print()` by itself starts a new line after each row.

### Nested Loops with Lists of Dictionaries

```python
classrooms = [
    {"teacher": "Ms. Park", "students": ["Amir", "Jazmine"]},
    {"teacher": "Mr. Liu", "students": ["Carlos", "Priya", "Sam"]}
]

for classroom in classrooms:
    print(f"\n{classroom['teacher']}:")
    for student in classroom["students"]:
        print(f"  - {student}")
```

Output:
```

Ms. Park:
  - Amir
  - Jazmine

Mr. Liu:
  - Carlos
  - Priya
  - Sam
```

Nested loops are powerful, but keep nesting to 2 levels when possible. Three or more levels of nesting becomes difficult to read and debug.

---

## Videos

**"Python Tutorial for Beginners 7: Loops and Iterations"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ) for more loop examples, including nested loops and practical use cases.

---

## Check for Understanding

**Question 1:** You need to count how many numbers in a list are greater than 100. Which pattern is this?

* A) Search
* B) Counter
* C) Accumulator
* D) Nested loop

<details>
<summary>Answer</summary>

**B) Counter.** You start a count at 0 and add 1 each time you find a number greater than 100.

</details>

**Question 2:** What is the initial value of the accumulator variable when building a running total?

* A) `1`
* B) `[]`
* C) `0`
* D) `""`

<details>
<summary>Answer</summary>

**C) `0`.** For a numeric total, you start at 0. For a list accumulator you'd use `[]`, and for a string accumulator you'd use `""`.

</details>

**Question 3:** Why is `break` useful in the search pattern?

* A) It prevents infinite loops
* B) It stops the loop once you've found what you're looking for
* C) It resets the loop variable
* D) It skips to the next iteration

<details>
<summary>Answer</summary>

**B) It stops the loop once you've found what you're looking for.** There's no point checking the remaining items after you've already found a match.

</details>

---

## Further Reading

- [Real Python: Python "for" Loops](https://realpython.com/python-for-loop/)
- [Automate the Boring Stuff: Flow Control](https://automatetheboringstuff.com/2e/chapter2/)
- [Python Official Documentation: More on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
