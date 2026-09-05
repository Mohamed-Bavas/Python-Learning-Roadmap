# 🐍 Day 01 – Python Basics

Welcome to **Day 01** of my Python Programming Learning Journey 🚀

Today I started learning the fundamental concepts of Python programming. The focus was on understanding Python syntax, variables, data types, input/output, type casting, constants, and comments.

---

## 🎯 Learning Objectives

By completing Day 01, I learned:

* Introduction to Python
* Python syntax
* Variables
* Constants
* Data types
* Input and output
* Type casting
* Comments
* Basic Python program structure

---

# 📚 Topics Covered

## 1. Introduction to Python

Python is a high-level, interpreted, general-purpose programming language.

### Key Features

* Easy to learn
* Simple and readable syntax
* Interpreted language
* Dynamically typed
* Object-oriented
* Large standard library
* Supports automation and scripting
* Widely used in software development, data science, AI, and embedded-related applications

Example:

```python
print("Hello, World!")
```

---

## 2. Python Syntax

Python uses indentation to define blocks of code.

Example:

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Python does not require `{}` braces to define blocks.

---

## 3. Variables

A variable is used to store data.

Example:

```python
name = "Bavas"
age = 20
height = 165.5
```

Multiple variables:

```python
name, age, city = "Bavas", 20, "Chennai"
```

---

## 4. Constants

Python does not have a strict constant keyword.

By convention, constants are written using uppercase letters.

Example:

```python
PI = 3.14159
MAX_SPEED = 120
```

---

## 5. Data Types

Python provides several built-in data types.

### Common Data Types

| Data Type | Example             |
| --------- | ------------------- |
| `int`     | `10`                |
| `float`   | `10.5`              |
| `complex` | `2 + 3j`            |
| `str`     | `"Python"`          |
| `bool`    | `True`              |
| `list`    | `[1, 2, 3]`         |
| `tuple`   | `(1, 2, 3)`         |
| `set`     | `{1, 2, 3}`         |
| `dict`    | `{"name": "Bavas"}` |

Example:

```python
age = 20
price = 99.50
name = "Python"
is_active = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_active))
```

---

## 6. Input and Output

### Output

The `print()` function is used to display information.

```python
print("Hello Python")
print("Welcome to my learning journey")
```

### Input

The `input()` function is used to get data from the user.

```python
name = input("Enter your name: ")

print("Hello", name)
```

---

## 7. Type Casting

Type casting means converting one data type into another.

### Common Functions

```python
int()
float()
str()
bool()
```

Example:

```python
age = input("Enter your age: ")

age = int(age)

print("Your age is:", age)
```

Another example:

```python
number = 10

value = float(number)

print(value)
```

---

## 8. Comments

Comments are used to explain code.

Python uses `#` for single-line comments.

```python
# This is a comment

name = "Python"  # Store Python as a string
```

Comments are ignored by the Python interpreter.

---

# 💻 Practice Programs

During Day 01, I practiced basic programs such as:

### 1. Hello World

```python
print("Hello, World!")
```

### 2. Display Name

```python
name = input("Enter your name: ")
print("Hello", name)
```

### 3. Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)
```

### 4. Display Data Types

```python
name = "Bavas"
age = 20
height = 165.5
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

### 5. Type Casting

```python
number = "100"

value = int(number)

print(value)
print(type(value))
```

---

# 📂 Folder Structure

```text
01_Python_Basics/
│
├── README.md
├── hello_world.py
├── variables.py
├── constants.py
├── data_types.py
├── input_output.py
├── type_casting.py
└── comments.py
```

---

# 🛠️ Tools Used

* 🐍 Python
* 💻 VS Code
* 🔧 Git
* 🌐 GitHub

---

# 📈 Day 01 Progress

| Topic                  | Status |
| ---------------------- | ------ |
| Introduction to Python | ✅      |
| Python Syntax          | ✅      |
| Variables              | ✅      |
| Constants              | ✅      |
| Data Types             | ✅      |
| Input & Output         | ✅      |
| Type Casting           | ✅      |
| Comments               | ✅      |

### 🎯 Day 01 Status: ✅ COMPLETED

---

# 🔧 Git Commit

```bash
git add .
git commit -m "Complete Day 01 Python Basics"
git push origin main
```

---

# 🧠 Key Takeaways

Today I learned how to:

* Write basic Python programs
* Create and use variables
* Understand different data types
* Get input from users
* Display output using `print()`
* Convert data between different types
* Use comments to make code understandable
* Follow Python indentation and syntax rules

---

## 🚀 Next Step

### Day 02 – Operators

Next, I will learn:

* Arithmetic Operators
* Relational Operators
* Logical Operators
* Assignment Operators
* Bitwise Operators
* Membership Operators
* Identity Operators

**Learning Journey:**
**Learn → Practice → Build → Commit → Improve 🚀**
