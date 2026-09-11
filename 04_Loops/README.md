# 🔄 Day 04 – Python Loops

Welcome to **Day 04** of my **Python Programming Learning Journey** 🚀

Today I learned about **Loops in Python**. Loops are used to execute a block of code repeatedly based on a condition or over a sequence of values.

---

## 🎯 Topics Covered

* `for` loop
* `while` loop
* Nested loops
* `break` statement
* `continue` statement
* `pass` statement

---

## 📁 Files Created

```text
04_Loops/
│
├── for_loop.py
├── while_loop.py
└── nested_loop.py
```

---

## 🔹 1. For Loop

A `for` loop is used to repeat a block of code for each item in a sequence.

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## 🔹 2. While Loop

A `while` loop executes a block of code as long as the condition is `True`.

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

---

## 🔹 3. Nested Loop

A loop inside another loop is called a **nested loop**.

Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

## 🔹 4. Break Statement

The `break` statement is used to stop a loop immediately.

Example:

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

---

## 🔹 5. Continue Statement

The `continue` statement skips the current iteration and continues with the next iteration.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

---

## 🔹 6. Pass Statement

The `pass` statement is used when a statement is required syntactically but no action needs to be performed.

Example:

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## 🧪 Practice Programs

I practiced the following programs:

* Print numbers from 1 to 10
* Print even numbers
* Print odd numbers
* Print multiplication table
* Calculate the sum of numbers
* Reverse a number using a loop
* Find factorial of a number
* Use `break`
* Use `continue`
* Create patterns using nested loops

---

## 🧠 What I Learned

* How `for` loops work
* How `while` loops work
* Difference between `for` and `while`
* How to create nested loops
* How to stop a loop using `break`
* How to skip an iteration using `continue`
* How to use `pass`
* How loops are useful for solving programming problems

---

## 📊 Learning Progress

| Day    | Topic                  | Status        |
| ------ | ---------------------- | ------------- |
| Day 01 | Python Basics          | ✅ Completed   |
| Day 02 | Operators              | ✅ Completed   |
| Day 03 | Conditional Statements | ✅ Completed   |
| Day 04 | Loops                  | ✅ Completed   |
| Day 05 | Functions              | ⬜ Not Started |
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

**4 / 15 Days Completed → 26.67%**

```text
██████░░░░░░░░░░░░░░ 26.67%
```

---

## 🔧 Tools Used

* 🐍 Python
* 💻 VS Code
* 🌐 Git
* 📦 GitHub

---

## 📌 Git Commit

```bash
git add .
git commit -m "Complete Day 04 Python Loops"
git push origin main
```

---

## 🚀 Next Step

### Day 05 – Functions

Topics planned:

* Defining functions
* Function arguments
* Return values
* Default arguments
* Keyword arguments
* `*args`
* `**kwargs`
* Lambda functions
* Variable scope

---

## 🎯 Learning Approach

**Learn → Practice → Solve Problems → Commit → Improve 🚀**

---

⭐ This repository documents my daily Python learning progress and practical coding journey.
