# 🐍 Day 05 – Python Functions

Welcome to **Day 05** of my **Python Programming Learning Journey** 🚀

Today I completed learning **Functions in Python**. Functions are reusable blocks of code that help organize programs, reduce code repetition, and make code easier to understand and maintain.

---

## 🎯 Topics Covered

* Defining Functions
* Calling Functions
* Function Arguments
* Return Values
* Default Arguments
* Keyword Arguments
* `*args`
* `**kwargs`
* Lambda Functions
* Variable Scope

---

## 📁 Files Created

```text
05_Functions/
│
├── functions.py
├── arguments.py
└── lambda.py
```

---

## 🔹 1. Defining Functions

A function is created using the `def` keyword.

```python
def greet():
    print("Hello, Python!")

greet()
```

Output:

```text
Hello, Python!
```

---

## 🔹 2. Function Arguments

Arguments allow us to pass values to a function.

```python
def add(a, b):
    print("Sum:", a + b)

add(10, 20)
```

Output:

```text
Sum: 30
```

---

## 🔹 3. Return Values

The `return` statement sends a result back from a function.

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)
```

Output:

```text
20
```

---

## 🔹 4. Default Arguments

A default value can be assigned to a function parameter.

```python
def greet(name="Bavas"):
    print("Hello", name)

greet()
greet("Rahul")
```

Output:

```text
Hello Bavas
Hello Rahul
```

---

## 🔹 5. Keyword Arguments

Keyword arguments allow us to pass values using parameter names.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Bavas")
```

Output:

```text
Name: Bavas
Age: 20
```

---

## 🔹 6. `*args`

`*args` allows a function to accept multiple positional arguments.

```python
def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20, 30))
```

Output:

```text
60
```

---

## 🔹 7. `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name="Bavas", age=20, course="Python")
```

Output:

```text
name : Bavas
age : 20
course : Python
```

---

## 🔹 8. Lambda Functions

A lambda function is a small anonymous function.

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

Another example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

---

## 🔹 9. Variable Scope

Python has different variable scopes.

### Local Variable

A variable created inside a function is called a local variable.

```python
def example():
    x = 10
    print(x)

example()
```

### Global Variable

A variable created outside a function is called a global variable.

```python
x = 20

def example():
    print(x)

example()
```

---

## 🧪 Practice Programs

I practiced the following programs:

* Create a simple function
* Add two numbers using a function
* Find the largest number using a function
* Calculate factorial using a function
* Check even or odd using a function
* Calculate square using lambda
* Use default arguments
* Use keyword arguments
* Practice `*args`
* Practice `**kwargs`
* Practice local and global variables

---

## 🧠 What I Learned

* How to define and call functions
* How to pass arguments to functions
* How to return values
* How default arguments work
* How keyword arguments work
* How `*args` works
* How `**kwargs` works
* How lambda functions work
* Difference between local and global variables
* How functions improve code reusability

---

## 📊 Learning Progress

| Day    | Topic                  | Status        |
| ------ | ---------------------- | ------------- |
| Day 01 | Python Basics          | ✅ Completed   |
| Day 02 | Operators              | ✅ Completed   |
| Day 03 | Conditional Statements | ✅ Completed   |
| Day 04 | Loops                  | ✅ Completed   |
| Day 05 | Functions              | ✅ Completed   |
| Day 06 | Data Structures        | ⬜ Not Started |
| Day 07 | Strings                | ⬜ Not Started |
| Day 08 | File Handling          | ⬜ Not Started |
| Day 09 | Exception Handling     | ⬜ Not Started |
| Day 10 | OOP                    | ⬜ Not Started |
| Day 11 | Modules & Packages     | ⬜ Not Started |
| Day 12 | Advanced Python        | ⬜ Not Started |
| Day 13 | SQLite                 | ⬜ Not Started |
| Day 14 | Practice Programs      | ⬜ Not Started |
| Day 15 | Mini Projects          | ⬜ Not Started |

### 📈 Overall Progress

**5 / 15 Days Completed → 33.33%**

```text
███████░░░░░░░░░░░░░ 33.33%
```

---

## 🔧 Tools Used

* 🐍 Python
* 💻 VS Code
* 🔧 Git
* 🌐 GitHub

---

## 📌 Git Commit

```bash
git add .
git commit -m "Complete Day 05 Python Functions"
git push origin main
```

### Example Commit Messages

```text
Complete Day 05 Python Functions
Add function examples
Add function arguments examples
Add return value examples
Add lambda function examples
```

---

## 🚀 Next Step

### Day 06 – Data Structures

Topics planned:

* Lists
* Tuples
* Sets
* Dictionaries
* List Comprehension
* Dictionary Comprehension

---

## 🎯 Learning Approach

**Learn → Practice → Build → Commit → Improve 🚀**

---

⭐ This repository documents my daily Python learning progress and practical coding journey.
