# 🐍 Day 11 – Python Modules & Packages

Welcome to **Day 11** of my Python Programming Learning Journey 🚀

Today I learned about **Modules and Packages in Python** and practiced how to create and use a custom module.

The main focus was on **importing modules, creating custom modules, and reusing functions from another Python file**.

---

## 📚 Topics Covered

### 1. Python Modules

A **module** is a Python file that contains reusable Python code such as functions, variables, and classes.

Example:

```python
import math_operations
```

---

### 2. `import`

The `import` statement is used to import another Python module.

Example:

```python
import math_operations

result = math_operations.add(10, 20)

print(result)
```

---

### 3. Custom Modules

Python allows us to create our own modules.

For example, `math_operations.py` can contain mathematical functions:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

These functions can then be used in `main.py`.

---

### 4. Module Reusability

A major advantage of modules is **code reusability**.

Instead of writing the same function again, we can create it once inside a module and import it whenever required.

```text
math_operations.py
        ↓
     import
        ↓
     main.py
```

---

### 5. `__name__ == "__main__"`

I also learned about the purpose of:

```python
if __name__ == "__main__":
    print("Program started")
```

This condition allows code to run when the Python file is executed directly.

---

## 📂 Repository Structure

```text
11_Modules_Packages/
│
├── main.py
└── math_operations.py
```

---

## 📄 Files Description

### `main.py`

This file is used as the main Python program and imports functions from the custom module.

### `math_operations.py`

This file contains mathematical operations that can be reused in `main.py`.

---

## 💻 Practice Programs

### 1. `main.py`

* Imported a custom Python module
* Used functions from the module
* Practiced module-based code organization

### 2. `math_operations.py`

* Created a custom module
* Defined mathematical operations
* Practiced code reusability

---

## 🧠 What I Learned

Through Day 11, I learned:

* What a Python module is
* How to create a custom module
* How to import a module using `import`
* How to use functions from another Python file
* How modules improve code reusability
* How to organize Python code using separate files
* Basic usage of `__name__ == "__main__"`

---

## 📊 Learning Progress

**Day 11 Progress:** `100%`

**Overall Progress:** `73.33%`

**11 / 15 Days Completed**

```text
███████████████░░░░░ 73.33%
```

---

## 🏆 Current Status

* ✅ Completed: **11 / 15 Days**
* 📈 Current Progress: **73.33%**
* 📚 Current Level: **Python Fundamentals + OOP + Modules**
* 🚀 Next Step: **Day 12 – Advanced Python**

---

## 🎯 Goal

My goal is to learn how to **organize and reuse Python code** using modules and gradually move toward larger and more practical Python programs.

---

## 🚀 Next Step

### Day 12 – Advanced Python

Next, I will learn:

* List Comprehension
* Dictionary Comprehension
* Set Comprehension
* Iterators
* Generators
* Decorators
* `map()`
* `filter()`
* `reduce()`

---

## 🔥 Learning Journey

> **Learn → Practice → Build → Improve → Repeat**

⭐ Continuing my Python Programming Learning Journey step by step.
