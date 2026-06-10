# Debugging Loops

**Objective**: By the end of this lesson, you will be able to:
  * Identify and fix off-by-one errors in loops
  * Recognize and stop infinite loops
  * Avoid common accumulator initialization mistakes
  * Use print statements to trace loop execution step by step

---

## A New Class of Bugs

In Week 1, you learned to debug simple scripts by reading error messages and using print statements. Loops introduce a new category of bugs: your code might run without any error message but produce wrong results, or it might run forever and never finish.

These bugs are harder to spot because the problem isn't in a single line, it's in how the loop behaves over multiple iterations. The key to debugging loops is **tracing**: following your code step by step, either on paper or with print statements, to see exactly what happens at each iteration.

---

## Off-by-One Errors

An **off-by-one error** means your loop runs one too many or one too few times. This is the most common loop bug.

### `range(n)` vs. `range(1, n + 1)`

```python
# Goal: print numbers 1 through 5

# Bug: starts at 0, ends at 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Fix: start at 1, stop at 6
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5
```

Remember: `range(stop)` always starts at 0, and the stop value is **never included**.

### `<` vs. `<=`

```python
# Goal: process items at indices 0 through 4 (5 items)

data = [10, 20, 30, 40, 50]

# Bug: <= goes one too far
for i in range(0, len(data) + 1):  # range(0, 6) includes index 5
    print(data[i])
# IndexError: list index out of range

# Fix: use < or just range(len(data))
for i in range(len(data)):
    print(data[i])
# Works correctly
```

**Tip:** When you see an `IndexError` inside a loop, check your `range()` boundaries first.

---

## Infinite Loops

An **infinite loop** is a `while` loop that never stops because the condition never becomes `False`.

### Forgetting to Update the Loop Variable

```python
# Bug: count never changes
count = 0
while count < 5:
    print(count)
    # Missing: count += 1
# This prints 0 forever!
```

The fix is simple, but easy to forget:

```python
count = 0
while count < 5:
    print(count)
    count += 1    # This line makes the loop eventually stop
```

### Updating in the Wrong Direction

```python
# Bug: count goes up when it should go down
count = 10
while count > 0:
    print(count)
    count += 1    # Goes to 11, 12, 13... never reaches 0
```

Fix: `count -= 1` to count down.

### How to Stop an Infinite Loop

If your terminal seems frozen or keeps printing the same thing, press `Ctrl+C` (or `Cmd+C` on Mac). This sends an interrupt signal that stops the program. It's not a bug in your computer; you'll use `Ctrl+C` regularly during development.

---

## Wrong Accumulator Initialization

Starting your accumulator at the wrong value gives wrong results without any error message.

### Sum Starting at 1 Instead of 0

```python
# Bug: total starts at 1 instead of 0
numbers = [10, 20, 30]
total = 1
for num in numbers:
    total += num
print(total)   # Output: 61 (should be 60)
```

Fix: `total = 0`.

### List Not Initialized

```python
# Bug: forgot to create the empty list
for name in ["Jazmine", "Carlos", "Amir"]:
    results.append(name.upper())
# NameError: name 'results' is not defined
```

Fix: add `results = []` before the loop.

### Accumulator Inside the Loop

```python
# Bug: total resets to 0 every iteration
numbers = [10, 20, 30]
for num in numbers:
    total = 0        # This resets total each time!
    total += num
print(total)   # Output: 30 (only the last number)
```

Fix: move `total = 0` to before the loop.

---

## Mutating a List While Iterating

Changing a list while you're looping over it causes unpredictable behavior. Python might skip items or raise errors.

```python
# Bug: removing items while iterating
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)   # Output: [1, 3, 5]? Maybe... but not always reliable
```

The safe approach is to build a new list instead:

```python
numbers = [1, 2, 3, 4, 5]
odds = []
for num in numbers:
    if num % 2 != 0:
        odds.append(num)
print(odds)   # Output: [1, 3, 5] (always reliable)
```

Or use a list comprehension:

```python
numbers = [1, 2, 3, 4, 5]
odds = [num for num in numbers if num % 2 != 0]
print(odds)   # Output: [1, 3, 5]
```

---

## Tracing Loops with Print Statements

When a loop gives wrong output, add a print inside the loop to see what's happening at each step:

```python
# Something is wrong with this average calculation
scores = [85, 92, 78, 95, 88]
total = 0
count = 0
for score in scores:
    total += score
    count += 1
    print(f"  DEBUG: score={score}, total={total}, count={count}")
average = total / count
print(f"Average: {average}")
```

Output:
```
  DEBUG: score=85, total=85, count=1
  DEBUG: score=92, total=177, count=2
  DEBUG: score=78, total=255, count=3
  DEBUG: score=95, total=350, count=4
  DEBUG: score=88, total=438, count=5
Average: 87.6
```

By watching the values change at each step, you can pinpoint exactly where things go wrong. Label your debug prints clearly and remove them once the bug is fixed.

### Tracing on Paper

Before adding print statements, try tracing the loop on paper. Draw a table with columns for each variable and one row per iteration. This forces you to think through the logic step by step and often reveals the bug faster than staring at the code.

### AI Prompt: Scaffold Removal

If you encounter a loop bug, try debugging it yourself first. If you're stuck after 10 minutes:

> "My Python loop is supposed to [describe goal], but instead it [describe wrong behavior]. Here's my code: [paste code]. Can you ask me 3 questions to help me find the bug, without telling me the answer?"

---

## Videos

**"Python Tutorial for Beginners 7: Loops and Iterations"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ) and pay attention to the debugging sections where he demonstrates common loop mistakes.

---

## Check for Understanding

**Question 1:** What is the output of this code?

```python
for i in range(5):
    print(i + 1)
```

* A) `0 1 2 3 4`
* B) `1 2 3 4 5`
* C) `1 2 3 4`
* D) `0 1 2 3 4 5`

<details>
<summary>Answer</summary>

**B) `1 2 3 4 5`.** `range(5)` produces 0 through 4, but `i + 1` shifts each value up by 1.

</details>

**Question 2:** What causes an infinite loop?

* A) Using `for` instead of `while`
* B) The loop condition never becomes False
* C) Using `break` inside the loop
* D) Printing inside the loop

<details>
<summary>Answer</summary>

**B) The loop condition never becomes False.** This usually happens when you forget to update the variable that the condition depends on.

</details>

**Question 3:** What is wrong with this code?

```python
numbers = [10, 20, 30]
for num in numbers:
    total = 0
    total += num
print(total)
```

* A) `total` is never defined
* B) `total` is reset to 0 every iteration
* C) The loop doesn't run
* D) There is no bug

<details>
<summary>Answer</summary>

**B) `total` is reset to 0 every iteration.** The line `total = 0` is inside the loop, so it resets the total each time. Move it before the loop to fix it.

</details>

**Question 4:** What should you do when a loop produces wrong output but no error?

* A) Delete the loop and start over
* B) Add print statements inside the loop to trace variable values
* C) Add more items to the list
* D) Change `for` to `while`

<details>
<summary>Answer</summary>

**B) Add print statements inside the loop to trace variable values.** This lets you see what's happening at each iteration, making it easier to spot where the logic goes wrong.

</details>

---

## Further Reading

- [Real Python: Common Python Mistakes](https://realpython.com/python-common-mistakes/)
- [Python Official Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
