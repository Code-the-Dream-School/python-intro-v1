# Defining Functions: Parameters and Return Values

Up to this point, every script you've written runs top to bottom as one sequence of instructions. That works fine for short programs, but it gets hard to manage as they grow. What if you need to do the same thing in three different places? Copy-pasting code creates bugs and makes changes painful.

**Functions** solve this by giving a block of code a name. You define it once, then call it whenever you need it.

### Why Functions?

Here's a script without functions:

```python
print("Hello, Aisha!")
print("Welcome back. You have 3 new messages.")

print("Hello, Marcus!")
print("Welcome back. You have 3 new messages.")

print("Hello, Priya!")
print("Welcome back. You have 3 new messages.")
```

If you need to change the welcome message, you'd update it in three places. With a function, you update it once:

```python
def greet(name):
    print("Hello, " + name + "!")
    print("Welcome back. You have 3 new messages.")

greet("Aisha")
greet("Marcus")
greet("Priya")
```

Now the logic lives in one place. This is the core value of functions: **write once, use many times**.

### Defining and Calling a Function

A function is defined using the `def` keyword, followed by a name, parentheses, and a colon. The body is indented:

```python
def greet():
    print("Hello, world!")
```

To run the function, **call** it by name:

```python
greet()  # Output: Hello, world!
```

*Defining* a function doesn't run code. Nothing happens until you *call* the function.

### Parameters and Arguments

Parameters make functions flexible. They're variables you define inside the parentheses of `def`, and they receive values when the function is called:

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Jazmine")  # Output: Hello, Jazmine!
greet("Luis")     # Output: Hello, Luis!
```

The value you pass in (`"Jazmine"`) is an **argument**. The variable that receives it (`name`) is a **parameter**. You can define as many parameters as you need:

```python
def add(a, b):
    print(a + b)

add(3, 5)  # Output: 8
```

### Return Values

So far, functions have printed things directly. But often you want a function to **compute** something and hand the result back so you can use it elsewhere. That's what `return` does:

```python
def square(number):
    return number * number

result = square(4)
print(result)  # Output: 16
```

The `return` statement sends a value back to whoever called the function. You can use that value directly in expressions:

```python
print(square(5) + square(3))  # Output: 34
```

**Note:** If a function doesn't have a `return` statement, it implicitly returns `None`. It's easy to get caught off guard by this — if you see `None` where you expected a value, check whether you forgot to `return` something.

### Default Parameters

You can give a parameter a **default value**, making it optional when calling the function:

```python
def greet(name="stranger"):
    print("Hello, " + name + "!")

greet()          # Output: Hello, stranger!
greet("Luis")    # Output: Hello, Luis!
```

When a caller doesn't provide a value, the default is used. Parameters with defaults must come *after* any required parameters in the function definition.

### 🎬 Video: Functions

**"Python Tutorial for Beginners 8: Functions"** (Corey Schafer)

**[Watch the video here](https://www.youtube.com/watch?v=9Os0o3wzS_I).** Our supplemental video for this section overviews functions, arguments, and parameters, along with worked examples.

### AI Learning Prompt: Predict-Then-Check

Study the following code without running it in your editor:

```python
score = 50

def update_score(current_score):
    current_score = current_score + 10
    return current_score

update_score(score)

print(score)
```

1. Open your preferred AI chatbot and use the following prompt:

> "I am studying Python functions and scope. Looking at this code: [paste code]
> I predict it will print [insert your predicted number] because [insert your reasoning about why the variable `score` did or did not change].
> Am I correct? If not, what am I misunderstanding about how parameters and return values work in relation to global variables?"

2. After the AI responds, run the code in your VSCode environment to see if your prediction was correct.
3. If the output surprised you, ask the AI: "Can you explain why the global variable `score` remained the same even though I passed it into the function?"

### Check for Understanding

**Question**: What is the purpose of the `return` statement in a function?

* A) To stop the function
* B) To send a value back to the caller
* C) To print a message
* D) To define a variable

<details>
<summary>View answer</summary>

**Answer**: B) To send a value back to the caller. The `return` statement makes the function's output available for use elsewhere in the program.

</details>

**Question**: What will be the output of the following code?

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Luis")
```

* A) `Hello, stranger!`
* B) `Hello, Luis!`
* C) `Hello, name!`
* D) `Luis`

<details>
<summary>View answer</summary>

**Answer**: B) `Hello, Luis!` — the string `"Luis"` is passed as the argument for the `name` parameter.

</details>
