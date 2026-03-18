# 🔐 Day 07 - Caesar Cipher

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-Encryption-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

The **Caesar Cipher** is a basic encryption technique where each letter in a message is shifted by a certain number of positions in the alphabet.

---

# 🔍 Project Description

This program allows users to:

* **Encrypt (encode)** a message
* **Decrypt (decode)** a message
* Continue using the program multiple times

The cipher works by shifting each letter forward or backward in the alphabet.

---

# ⚙️ How It Works

* Each letter is shifted by a given number (`shift`)
* Encoding → shifts forward
* Decoding → shifts backward
* Wrap-around is handled using modulo (`%`)

Example:

```text
a shifted by 2 → c  
z shifted by 2 → b
```

---

# 🧭 User Inputs

The program asks the user for:

1. Operation:

```text
encode → Encrypt
decode → Decrypt
```

2. Message:

```text
Enter the text to process
```

3. Shift value:

```text
Enter the number of positions to shift
```

---

# 🖥️ Example Run

```text
type encode to 'encrypt', type 'decode' to decrypt:
encode

Type your message:
hello

Type the shift number:
5

Here is your encoded result: mjqqt
```

---

# 📂 Project Structure

```text
Day-07-Caesar-Cipher
│
├── main.py
├── art.py
└── README.md
```

### File Explanation

* **main.py** → Contains the cipher logic
* **art.py** → Contains ASCII art logo used in the program

---

# 🧠 Concepts Used

This project demonstrates:

* Functions
* Loops (`while`, `for`)
* Conditional statements
* String manipulation
* Lists and indexing
* Modulo operator (`%`)
* Importing modules
* User input handling

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Day-07-Caesar-Cipher
```

### 3️⃣ Run the program

```bash
python main.py
```

