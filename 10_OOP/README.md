# 🐍 Day 10 – Python Object-Oriented Programming

Welcome to **Day 10** of my Python Programming Learning Journey 🚀

Today I learned about **Object-Oriented Programming (OOP) in Python**, including classes, objects, inheritance, polymorphism, and encapsulation.

OOP helps organize Python programs using **classes and objects**, making programs easier to understand, maintain, and reuse.

---

# 📚 Topics Covered

## 1. Classes and Objects

A **class** is a blueprint for creating objects.

An **object** is an instance of a class.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Mohamed", 20)

print(student.name)
print(student.age)
```

**File:** `class_object.py`

---

## 2. Inheritance

Inheritance allows one class to use the properties and methods of another class.

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.sound()
dog.bark()
```

The `Dog` class inherits from the `Animal` class.

**File:** `inheritance.py`

---

## 3. Polymorphism

Polymorphism allows the same method name to have different behavior for different classes.

```python
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

The same `sound()` method produces different results.

**File:** `polymorphism.py`

---

## 4. Encapsulation

Encapsulation is used to restrict direct access to data inside a class.

Python uses naming conventions such as `__` for private members.

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def display(self):
        print(self.__marks)


student = Student()

student.display()
```

The `__marks` variable is treated as a private member.

**File:** `encapsulation.py`

---

# 📂 OOP Concepts

```text
Object-Oriented Programming
│
├── Classes & Objects
├── Inheritance
├── Polymorphism
└── Encapsulation
```

---

# 💻 OOP Practice

I practiced the following Object-Oriented Programming concepts:

* Creating classes
* Creating objects
* Using constructors inside classes
* Using instance variables
* Implementing inheritance
* Understanding polymorphism
* Implementing encapsulation

---

# 📂 Repository Structure

```text
10_OOP/
│
├── class_object.py
├── inheritance.py
├── polymorphism.py
└── encapsulation.py
```

---

# 📄 Files Description

### `class_object.py`

Contains basic examples of creating classes and objects.

Topics:

* Classes
* Objects
* Attributes
* Instance variables

---

### `inheritance.py`

Contains examples of inheritance.

Topics:

* Parent class
* Child class
* Inheriting methods
* Code reuse

---

### `polymorphism.py`

Contains examples of polymorphism.

Topics:

* Same method name
* Different behavior
* Method overriding

---

### `encapsulation.py`

Contains examples of encapsulation.

Topics:

* Data hiding
* Private members
* `__`
* Accessing data through methods

---

# 🧠 What I Learned

Through Day 10, I learned:

* What Object-Oriented Programming is
* How to create classes
* How to create objects
* How instance variables work
* How inheritance works
* How polymorphism works
* How encapsulation works
* How OOP helps organize and reuse code

---

# 📝 Practice Programs

I practiced the following four OOP programs:

```text
1. class_object.py
   → Classes and Objects

2. inheritance.py
   → Inheritance

3. polymorphism.py
   → Polymorphism

4. encapsulation.py
   → Encapsulation
```

---

# 📈 Learning Progress

**Overall Progress:** `66.67%` 🎯

**10 / 15 Days Completed**

```text
Python Basics          ✅
Operators              ✅
Conditions             ✅
Loops                  ✅
Functions              ✅
Data Structures        ✅
Strings                ✅
File Handling          ✅
Exception Handling     ✅
OOP                    ✅
Modules & Packages     ⬜
Advanced Python        ⬜
SQLite                 ⬜
Practice Programs      ⬜
Mini Projects          ⬜
```

### Progress Bar

```text
█████████████░░░░░░░ 66.67%
```

---

# 🎯 Day 10 Goal

The goal of Day 10 was to understand the basic concepts of **Object-Oriented Programming in Python**.

I learned how to create classes and objects and practiced **inheritance, polymorphism, and encapsulation**.

**Status:** ✅ Completed

---

# 🚀 Next Step

### Day 11 – Modules & Packages

Topics to learn:

* Modules
* `import`
* `from ... import`
* Built-in Modules
* Creating Custom Modules
* Packages
* `__name__ == "__main__"`

---

## 👨‍💻 Learning Journey

**Learn → Practice → Build → Improve 🚀**

**Day 10 Completed Successfully! 🎉**

**10 / 15 Days Completed → 66.67% Progress 🐍**
