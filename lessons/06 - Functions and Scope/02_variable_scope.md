# Variable Scope

When you define a variable inside a function, it only exists inside that function. This is called **scope**. Understanding it is essential for writing functions that behave predictably.

### Local Variables

A variable created inside a function is **local** to that function. It doesn't exist outside of it:

```python
def set_name():
    name = "Priya"

set_name()
print(name)  # NameError: name 'name' is not defined
```

Even though `set_name()` ran and assigned `"Priya"` to `name`, that variable only existed during the function call. Once the function returned, it was gone.

### Local Variables Don't Affect Globals

What if there's already a global variable with the same name? Python creates a **separate local variable** which doesn't touch the global:

```python
name = "Hima"

def set_name():
    name = "Priya"

set_name()
print(name)  # Output: Hima
```

The `name = "Priya"` inside the function is a brand-new local variable. Python treats any assignment inside a function as creating a local, not modifying the global with the same name.

### Reading Globals from Inside a Function

Functions *can* read global variables, they just can't reassign them by default:

```python
greeting = "Hello"

def say_hello(name):
    print(greeting + ", " + name + "!")  # reads the global 'greeting'

say_hello("Marcus")  # Output: Hello, Marcus!
```

Python looks outward to the global scope when a name isn't found locally. However, relying on this too heavily makes code hard to follow. If a function needs a value, it's almost always clearer to pass it as a parameter.

You *can* modify a global from inside a function using the `global` keyword:

```python
count = 0

def increment():
    global count
    count += 1
```

This works, but it's generally a sign to reconsider your design. Functions that modify global state are harder to test and reason about. In most cases, it's better to pass the value in and `return` a new one.

### Why Local Scope Is a Feature

Local scope might feel like a restriction at first, but it's a protection. Without it, every function you called could accidentally overwrite your variables. With it:

- Functions are **isolated**: they can't interfere with each other's internal variables
- Code is **predictable**: a variable's value doesn't change unless you explicitly change it
- Functions are **reusable**: you can call the same function from anywhere without side effects

### A Common Scope Bug

One of the most frequent beginner mistakes is forgetting to `return` a value and then trying to use the result:

```python
def add(a, b):
    total = a + b  # computed but never returned

result = add(3, 5)
print(result)  # Output: None
```

The function computed `8`, but it never sent that value back. `result` is `None` because that's what Python returns when a function has no explicit `return`. The fix:

```python
def add(a, b):
    return a + b
```

If you ever see `None` where you expected a number or string, check whether your function is missing a `return` statement.

### 🎬 Video: Variable Scope

**[Watch: Python Tutorial: Variable Scope (Corey Schafer)](https://www.youtube.com/watch?v=QVdf0LgmICw)**

### AI Learning Prompt: Predict-Then-Check

Study the following code without running it:

```python
label = "original"

def relabel():
    label = "updated"
    print("Inside:", label)

relabel()
print("Outside:", label)
```

1. Predict what the two `print` calls will output. Will the outside `label` be affected by the reassignment inside `relabel()`?

2. Then paste the code and your prediction into an AI chatbot:

   > "I'm learning Python variable scope. Here's a code snippet: [paste code]
   > I predicted the output would be [your prediction] because [your reasoning].
   > Was I correct? If not, can you explain what's happening and why?"

3. Run the code in VS Code to confirm.

### Check for Understanding

**Question**: What happens when a function assigns to a variable that has the same name as a global variable?

* A) The global variable is overwritten
* B) Python raises a `NameError`
* C) A new local variable is created; the global is unchanged
* D) Python uses the global variable's value instead

<details>
<summary>View answer</summary>

**Answer**: C) A new local variable is created. Python treats any assignment inside a function as defining a local variable. The global is not affected.

</details>

**Question**: What will the following code print?

```python
x = 10

def show():
    print(x)

show()
```

* A) An error — `x` is not defined inside the function
* B) `10`
* C) `None`
* D) `0`

<details>
<summary>View answer</summary>

**Answer**: B) `10` — `show()` reads but does not assign `x`, so Python looks outward to the global scope and finds it there.

</details>

**Question**: A function runs without errors, but the variable you expected to hold its result is `None`. What is the most likely cause?

* A) The function is not defined
* B) The function is missing a `return` statement
* C) The variable was declared inside the function
* D) Python discards return values automatically

<details>
<summary>View answer</summary>

**Answer**: B) When a function doesn't explicitly return a value, Python returns `None` by default. Check that your function has a `return` statement and that it's returning the right thing.

</details>

**Question**: Which of the following is the cleanest way to make a function update a value?

```python
# Option A
total = 0
def add(n):
    global total
    total += n

# Option B
def add(total, n):
    return total + n
```

* A) Option A — using `global` is the standard approach
* B) Option B — pass the value in, return the new value
* C) Both are equally good
* D) Neither — functions can't modify numbers

<details>
<summary>View answer</summary>

**Answer**: B) Option B is cleaner. Passing the value as a parameter and returning the result makes the function self-contained and easy to test — you can call `add(5, 3)` and verify the output directly. Option A works but creates hidden dependencies on global state.

</details>
