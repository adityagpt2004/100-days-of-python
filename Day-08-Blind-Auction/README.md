# 💰 Day 08 - Blind Auction Program

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-CLI%20Application-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

The **Blind Auction Program** allows multiple users to place bids secretly, and at the end, determines the highest bidder.

---

# 🎯 Project Description

In this program:

* Multiple users can enter their **name and bid amount**
* Bids are stored in a dictionary
* Each bidder’s input is hidden from the next user
* At the end, the program determines the **highest bidder**

---

# ⚙️ How It Works

1. The program asks for:

   * Bidder's name
   * Bid amount

2. The data is stored in a dictionary:

```text
{name: bid}
```

3. The program asks if there are more bidders:

   * If **yes** → screen clears (simulated)
   * If **no** → winner is calculated

4. The highest bidder is displayed.

---

# 🖥️ Example Run

```text
What is Your Name?: Aditya
What is your Bid?: $100
Are there any other bidders? Type 'yes' or 'no'.
yes

What is Your Name?: Rahul
What is your Bid?: $250
Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Rahul with a bid of $250.
```

---

# 📂 Project Structure

```text
Day-08-Blind-Auction
│
├── main.py
├── art.py
└── README.md
```

### File Explanation

* **main.py** → Contains auction logic
* **art.py** → Contains ASCII logo

---

# 🧠 Concepts Used

This project demonstrates:

* Dictionaries
* Functions
* Loops (`while`)
* Conditional statements
* User input handling
* Data storage and comparison
* Iteration over dictionary

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Day-08-Blind-Auction
```

### 3️⃣ Run the program

```bash
python main.py
```

