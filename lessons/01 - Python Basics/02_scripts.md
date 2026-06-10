# Simple Scripts

**Objective**: By the end of this lesson, you will be able to:
  * Understand how Python runs code from top to bottom
  * Write a complete script that combines variables, `input()`, `print()`, and operators
  * Build a program step by step, testing as you go
  * Save and share your work from the online IDE

---

## What Is a Script?

In the previous lesson, you learned individual concepts — variables, data types, operators — and ran small code examples to see how they work. A **script** is a file that combines multiple concepts into a complete program that does something useful, from start to finish.

Think of the difference like this:
- **Individual lines** are like typing single sentences — each one stands on its own
- **A script** is like writing a full paragraph — the lines build on each other and work together to produce a result

Every `.py` file you create is a script. When you click **Run**, Python starts at line 1 and executes each line in order until it reaches the end.

```python
# Line 1 runs first
name = "Jazmine"

# Line 2 runs second
print(f"Hello, {name}!")

# Line 3 runs third
print("Welcome to Python!")
```

Output:
```
Hello, Jazmine!
Welcome to Python!
```

**Order matters.** If you try to use a variable before you create it, Python will raise an error:

```python
print(f"Hello, {name}!")   # NameError! Python doesn't know what 'name' is yet
name = "Jazmine"
```

---

## Building a Script Step by Step

The best way to write a script is to build it **one piece at a time**, running your code after each change to make sure it works. Don't try to write the whole program at once — even experienced developers build and test in small steps.

Let's walk through building a simple tip calculator, one step at a time.

### Step 1: Get the Input

Start by asking the user for the information you need:

```python
bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")
```

Run it. Does it ask you both questions? Great. Move to the next step.

### Step 2: Convert and Calculate

Remember that `input()` always returns a string. Convert the values to numbers and do the math:

```python
bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate / 100)   # Convert percentage to decimal: 20 becomes 0.20
total = bill + tip_amount
```

We divide `tip_rate` by 100 to turn the percentage into a decimal — for example, entering `20` becomes `0.20`, so `50 * 0.20` gives us a $10 tip.

**Note:** If you accidentally type a word instead of a number (like `"twenty"` instead of `20`), Python will crash with a `ValueError`. For now, just make sure to enter actual numbers. We'll learn how to handle these errors gracefully in Week 8.

Run it. The program will ask your two questions and then finish — you won't see any output yet, and that's expected. If it runs without an error, the math is working behind the scenes. We'll display the results in the next step.

### Step 3: Display the Output

Now add `print()` statements with f-strings to show the results:

```python
bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate / 100)
total = bill + tip_amount

print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
```

Run it and enter `50` for the bill and `20` for the tip. You should see:

```
Tip: $10.00
Total: $60.00
```

### Step 4: Make It Look Better

Polish the output to make it more readable:

```python
bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate / 100)
total = bill + tip_amount

print("========================")
print("     TIP CALCULATOR     ")
print("========================")
print(f"Bill:    ${bill:.2f}")
print(f"Tip:     ${tip_amount:.2f}")
print(f"Total:   ${total:.2f}")
print("========================")
```

Output (with bill = 50, tip = 20):
```
========================
     TIP CALCULATOR     
========================
Bill:    $50.00
Tip:     $10.00
Total:   $60.00
========================
```

That's a complete, working script — built in four small steps.

### AI Prompt: Predict-Then-Check

Before reading on, try modifying the tip calculator on your own:

1. Can you add a line that splits the total evenly between 2 people?
2. Predict what your output will look like, then run it to check.
3. If you get stuck, use your preferred AI chatbot:

> "I have a working tip calculator in Python and I want to add a bill-splitting feature. Can you give me a hint about what math I need, without writing the code for me?"

---

## The Build-Test-Build Pattern

Notice the pattern we used above:

1. **Write a few lines** (just one piece of the program)
2. **Run it** to check for errors
3. **Fix anything broken** before moving on
4. **Add the next piece** and repeat

This is how developers actually work. If you write 30 lines and then run for the first time, you might get an error on line 5 — and now you have to figure out which of those 30 lines caused it. If you run after every 3-4 lines, you always know exactly where the problem is.

**Tip:** If you're unsure whether your math or variables are correct, add a temporary `print()` to check. Notice below that we combine `input()` and `float()` into a single line — this is a shorthand for the two-step pattern you already know:

```python
bill = float(input("Bill amount? $"))       # Same as: bill = input(...) then bill = float(bill)
tip_rate = float(input("Tip %? "))

tip_amount = bill * (tip_rate / 100)
print("DEBUG:", tip_amount)   # Temporary — just to check the value

total = bill + tip_amount
```

Once you've confirmed it's working, delete the `DEBUG` line.

---

## Using the Online IDE

For this week, we're using [online-python.com](https://www.online-python.com/) to write and run our code. Here's what you need to know:

### Writing and Running Code

- Type your code in the **editor panel** on the left
- Click the **Run** button (or press the play icon) to execute your script
- Output appears in the **console panel** on the right
- If your script uses `input()`, type your response in the console and press Enter

### Saving and Sharing Your Work

**online-python.com does not save your work automatically.** If you close the tab, your code is gone. To save your work:

1. Click the **Share** button at the top of the editor
2. This generates a unique link to your code
3. Copy and save this link — you'll submit it for your assignment

**Backup tip:** Before closing your browser, also copy your code and paste it into a note or text file on your computer. This way you have a backup if anything goes wrong with the share link.

---

## Putting It All Together

Here's another complete script that combines everything from this lesson and the previous one — variables, `input()`, type conversion, operators, f-strings, and string methods:

```python
# A simple greeting card generator

print("=== Greeting Card Generator ===")
print()                               # print() with nothing inside prints a blank line

name = input("Who is this card for? ")
occasion = input("What's the occasion? (birthday, graduation, etc.) ")
sender = input("Who is it from? ")

name = name.strip().upper()       # Chaining: strip() runs first, then upper() runs on the result
occasion = occasion.strip().lower()
sender = sender.strip().upper()

print()
print("╔══════════════════════════════╗")
print(f"   Happy {occasion}, {name}!")
print()
print("   Wishing you all the best.")
print(f"   — {sender}")
print("╚══════════════════════════════╝")
```

Output (with inputs "jazmine", "birthday", "carlos"):
```
=== Greeting Card Generator ===

╔══════════════════════════════╗
   Happy birthday, JAZMINE!

   Wishing you all the best.
   — CARLOS
╚══════════════════════════════╝
```

Notice how we **chain** two methods together: `.strip().upper()` means "first remove extra spaces, then convert to uppercase." Python runs them left to right, so `strip()` cleans up the input and `upper()` transforms the cleaned result. Calling `print()` with no arguments prints a blank line, which helps space out the output.

---

## Videos

**Your First Python Program** (Programming with Mosh)

[Watch from 8:49 to 22:51](https://www.youtube.com/watch?v=kqtD5dpn9C8&t=529s) — covers writing your first program, how Python executes code, and running scripts. You can skip the installation section at the start since we're using an online IDE this week.

---

## AI Prompt: Retrieval Practice

Test what you've learned about writing scripts by explaining it to an AI:

1. Open your preferred AI chatbot (ChatGPT, Microsoft Copilot, etc.)
2. Explain the following in your own words:
   - Why is it better to build a script in small steps rather than writing the whole thing at once?
   - What's the difference between running individual lines of code and running a complete script?
3. Ask the AI to give you feedback on your explanation.

**Example Prompt:**
> "I just learned about writing Python scripts and the build-test-build pattern. Here is my understanding: [your explanation]. Can you tell me what I got right and what I should refine?"

---

## Check for Understanding

**Question 1:** What happens when Python encounters this code?

```python
print(greeting)
greeting = "Hello!"
```

* A) It prints `Hello!`
* B) It prints `greeting`
* C) It raises a `NameError`
* D) It prints nothing

<details>
<summary>Answer</summary>

**C) It raises a `NameError`** — Python runs code from top to bottom. On line 1, the variable `greeting` hasn't been created yet, so Python doesn't know what it refers to.

</details>

**Question 2:** You write 20 lines of code and click Run. You get an error. What's the best approach for next time?

* A) Write all the code first, then fix all errors at the end
* B) Write a few lines at a time and run after each addition
* C) Don't run the code until you're completely sure it's correct
* D) Delete everything and start over

<details>
<summary>Answer</summary>

**B) Write a few lines at a time and run after each addition** — This is the build-test-build pattern. It's much easier to find and fix errors when you know exactly which lines you just added.

</details>

**Question 3:** How do you save your work in online-python.com?

* A) It saves automatically
* B) Press Ctrl+S
* C) Click the Share button to generate a link
* D) Download the file to your computer

<details>
<summary>Answer</summary>

**C) Click the Share button to generate a link** — online-python.com does not save automatically. The Share button creates a unique URL to your code that you can submit for your assignment.

</details>

---

## Further Reading

- [online-python.com](https://www.online-python.com/) — The online IDE we're using this week
- [W3Schools — Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)
- [Real Python — Code Your First Python Program](https://realpython.com/courses/python-basics-first-program/)
