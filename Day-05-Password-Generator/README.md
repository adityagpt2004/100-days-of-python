# 🔐 Day 05 - Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-CLI%20Tool-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

The **Password Generator** is a Python program that creates secure passwords based on the user's preferences.

---

# 🎯 Project Description

This program generates a password containing:

* Letters (uppercase and lowercase)
* Numbers
* Symbols

The user can also choose between **Easy** and **Hard** password modes.

---

# ⚙️ Features

### Easy Password

* Letters, symbols, and numbers are added **in order**
* Example:

```text
abcd!@123
```

---

### Hard Password

* Characters are **randomly shuffled**
* Produces a more secure password

Example:

```text
3a@1Bd!2c
```

---

# 🧭 User Inputs

The program asks the user for:

1. Password type:

```
Easy or Hard
```

2. Number of letters

3. Number of symbols

4. Number of numbers

---

# 🖥️ Example Run

```text
Welcome to the PyPassword Generator!

What type of Password do you need. Type 'Easy' or 'Hard':
hard

How many letters would you like in your Password?
5

How many symbols would you like?
2

How many numbers would you like?
3

Generated Password:
a7B#2m!9D
```

---

# 🧠 Concepts Used

This project demonstrates several Python concepts:

* Lists
* User input with `input()`
* Type conversion (`int`)
* Random module
* `random.choices()`
* `random.shuffle()`
* String joining with `"".join()`
* Conditional statements (`if`, `else`)

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Day-05-Password-Generator
```

### 3️⃣ Run the program

```bash
python main.py
```

---

# 📁 Project Structure

```
Day-05-Password-Generator
│
├── main.py
└── README.md
```

