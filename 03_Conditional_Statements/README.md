# 🐍 Day 03 – Conditional Statements

Welcome to **Day 03** of my Python Programming Learning Journey 🚀

Today, I learned and practiced **Conditional Statements** in Python. Conditional statements are used to make decisions in a program based on whether a condition is `True` or `False`.

---

## 📚 Topics Covered

### 1. `if` Statement

The `if` statement executes a block of code when a condition is `True`.

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

**File:** `if.py`

---

### 2. `if-else` Statement

The `if-else` statement executes one block when the condition is `True` and another block when it is `False`.

```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**File:** `if_else.py`

---

### 3. `if-elif-else` Statement

The `if-elif-else` statement is used when there are multiple conditions.

```python
mark = 85

if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")
```

**File:** `elif.py`

---

### 4. Nested `if`

A nested `if` means using one `if` statement inside another `if` statement.

Example:

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")
    else:
        print("ID required")

else:
    print("Entry not allowed")
```

---

### 5. Conditional Expression

A conditional expression is a short way of writing an `if-else` statement.

Syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

## 📂 Files Created

```text
03_Conditional_Statements/
│
├── if.py
├── if_else.py
└── elif.py
```

---

## 💻 Practice Programs

I practiced programs using:

* `if` statements
* `if-else` statements
* `if-elif-else`
* Nested conditions
* Comparison operators
* Logical operators
* User input
* Conditional expressions

### Practice Examples

* Check Even or Odd
* Check Positive or Negative
* Check Voting Eligibility
* Find Largest of Two Numbers
* Find Largest of Three Numbers
* Grade Calculator
* Check Leap Year
* Check Positive, Negative or Zero

---

## 🧠 What I Learned

* Conditional statements are used for decision-making.
* `if` executes code when a condition is true.
* `else` handles the false condition.
* `elif` allows multiple conditions.
* Nested `if` can be used for complex decisions.
* Conditional expressions provide a shorter `if-else` syntax.
* Python uses indentation to define code blocks.

---

## 📈 Progress

**Day 03 – Conditional Statements:** ✅ Completed

```text
Day 01 – Python Basics          ✅
Day 02 – Operators              ✅
Day 03 – Conditional Statements ✅
Day 04 – Loops                  ⬜
Day 05 – Functions              ⬜
```

---

## 🔧 Git Commit

```bash
git add .
git commit -m "Complete Day 03 Python Conditional Statements"
git push origin main
```

---

## 🚀 Next Step

### Day 04 – Loops

Next, I will learn:

* `for` loop
* `while` loop
* Nested loops
* `break`
* `continue`
* `pass`

**Learn → Practice → Build → Commit → Improve 🚀**
