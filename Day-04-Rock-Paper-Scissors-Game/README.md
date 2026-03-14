# ✊📄✂️ Day 04 - Rock Paper Scissors Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-CLI%20Game-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

It is a **command-line Rock Paper Scissors game** where the user plays against the computer.

---

# 🎮 Game Overview

Rock Paper Scissors is a simple hand game played between two players. In this program:

* The **user selects Rock, Paper, or Scissors**
* The **computer randomly selects one option**
* The program determines the winner based on the rules of the game.

---

# 🕹️ Game Rules

| Player Choice | Computer Choice | Result   |
| ------------- | --------------- | -------- |
| Rock          | Scissors        | You Win  |
| Rock          | Paper           | You Lose |
| Paper         | Rock            | You Win  |
| Paper         | Scissors        | You Lose |
| Scissors      | Paper           | You Win  |
| Scissors      | Rock            | You Lose |
| Same choice   | Same choice     | Draw     |

---

# 🧭 User Inputs

The user selects an option by typing a number:

```
0 → Rock
1 → Paper
2 → Scissors
```

If the user enters an invalid number, the program displays an error message.

---

# 🖥️ Example Gameplay

```
What do you choose. Type 0 for rock, 1 for paper and 2 for scissors: 1

Computer chose:

      _______
---'   ____ )____
          ______)
          _______)
         _______)
---.__________)

You Win!
```

---

# 🧠 Concepts Used

This project demonstrates several Python fundamentals:

* `random` module
* Lists
* Conditional statements (`if`, `elif`, `else`)
* User input with `input()`
* ASCII art for visual representation
* Game logic

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

### 2️⃣ Navigate to the project folder

```
cd Day-04-Rock-Paper-Scissors
```

### 3️⃣ Run the Python file

```
python main.py
```

---

# 📁 Project Structure

```
Day-04-Rock-Paper-Scissors
│
├── main.py
└── README.md
```
