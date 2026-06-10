# for and while Loops

**Objective**: By the end of this lesson, you will be able to:
  * Write `for` loops using `range()` and over sequences
  * Write `while` loops with proper termination conditions
  * Use `break` and `continue` to control loop behavior
  * Choose between `for` and `while` based on the situation

---

## Why Loops?

Many tasks in programming require repetition: printing each item in a list, asking for input until the user gets it right, or processing every row in a dataset. Writing the same code over and over isn't practical. Loops let you run a block of code multiple times with a single instruction.

Python has two types of loops: `for` (when you know how many times to repeat) and `while` (when you repeat until a condition changes).

---

## The `for` Loop

A `for` loop runs once for each item in a sequence. You've already used this pattern with lists in Week 4:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

The variable `fruit` takes on a new value each time through the loop: first `"apple"`, then `"banana"`, then `"cherry"`. When there are no more items, the loop ends.

### Looping with `range()`

The `range()` function generates a sequence of numbers. It's useful when you need to repeat something a specific number of times:

**`range(stop)`** generates numbers from 0 up to (but not including) `stop`:

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

Notice: `range(5)` gives you 5 numbers (0 through 4), not 1 through 5.

**`range(start, stop)`** lets you choose where to begin:

```python
for i in range(1, 6):
    print(i)
```

Output:
```
1
2
3
4
5
```

**`range(start, stop, step)`** lets you skip numbers:

```python
for i in range(0, 10, 2):
    print(i)
```

Output:
```
0
2
4
6
8
```

You can also count backwards:

```python
for i in range(5, 0, -1):
    print(i)
```

Output:
```
5
4
3
2
1
```

### Looping Over Strings

Strings are sequences too, so you can loop over each character:

```python
for char in "Python":
    print(char)
```

Output:
```
P
y
t
h
o
n
```

---

## The `while` Loop

A `while` loop keeps running as long as its condition is `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Output:
```
0
1
2
3
4
```

The line `count += 1` is critical. Without it, `count` would stay at 0 forever and the loop would never end. This is called an **infinite loop**, and it's one of the most common bugs you'll encounter. If your program seems stuck, press `Ctrl+C` in the terminal to stop it.

### When to Use `while` Instead of `for`

Use `while` when you don't know ahead of time how many times the loop will run. A classic example is validating user input:

```python
password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted!")
```

This keeps asking until the user types "secret". You can't use a `for` loop here because you don't know how many attempts the user will need.

### AI Prompt: Predict-Then-Check

Study this code without running it:

```python
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))
print(f"Total: {total}")
```

If the user enters `5`, `3`, `7`, `0`, what will the output be? Predict first, then check:

> "I'm learning while loops. I traced through this code with inputs 5, 3, 7, 0 and predicted the total would be [your answer]. Can you walk me through the loop iterations to check my reasoning?"

---

## Controlling Loops with `break` and `continue`

### `break`

The `break` statement exits the loop immediately, even if the condition hasn't been met:

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

Output:
```
0
1
2
3
4
```

The loop stops as soon as `num` reaches 5. The number 5 itself is never printed because `break` runs before `print()`.

### `continue`

The `continue` statement skips the rest of the current iteration and jumps to the next one:

```python
for num in range(6):
    if num == 3:
        continue
    print(num)
```

Output:
```
0
1
2
4
5
```

When `num` is 3, `continue` skips the `print()` and moves directly to `num = 4`.

### `break` with `while`

`break` is especially useful with `while True` loops, which would otherwise run forever:

```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You said: {answer}")
print("Goodbye!")
```

This is a common pattern for menu-driven programs where you want the user to keep interacting until they choose to stop.

---

## `for` vs. `while`: Quick Guide

| Use `for` when... | Use `while` when... |
|---|---|
| You know how many times to loop | You don't know how many times |
| You're iterating over a sequence | You're waiting for a condition to change |
| Example: processing each item in a list | Example: asking for input until it's valid |

When in doubt, start with `for`. You can always switch to `while` if you realize you need open-ended repetition.

---

## Videos

**"Python Tutorial for Beginners 7: Loops and Iterations"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ) for a detailed walkthrough of for loops, while loops, break, continue, and practical examples.

---

## Check for Understanding

**Question 1:** What does `range(3)` produce?

* A) `[1, 2, 3]`
* B) `[0, 1, 2]`
* C) `[0, 1, 2, 3]`
* D) `[3]`

<details>
<summary>Answer</summary>

**B) `[0, 1, 2]`.** `range(3)` generates numbers starting from 0 up to (but not including) 3.

</details>

**Question 2:** What happens if you forget `count += 1` inside a `while` loop?

* A) The loop runs once
* B) The loop never runs
* C) The loop runs forever (infinite loop)
* D) Python raises an error

<details>
<summary>Answer</summary>

**C) The loop runs forever (infinite loop).** Without updating the variable, the condition never becomes False, so the loop never stops. Press `Ctrl+C` to stop it.

</details>

**Question 3:** What is the output of this code?

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

* A) `1 2 3 4 5`
* B) `1 2 4 5`
* C) `1 2`
* D) `4 5`

<details>
<summary>Answer</summary>

**B) `1 2 4 5`.** `continue` skips the rest of the loop body when `i == 3`, so 3 is never printed. The loop continues with 4 and 5.

</details>

**Question 4:** Which loop type is best for "keep asking until the user types 'quit'"?

* A) `for`
* B) `while`
* C) Either works equally well
* D) Neither, you need recursion

<details>
<summary>Answer</summary>

**B) `while`.** You don't know how many times the user will type before quitting, so a `while` loop (which repeats until a condition changes) is the right choice.

</details>

---

## Further Reading

- [W3Schools: Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [W3Schools: Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python Official Documentation: The for Statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
