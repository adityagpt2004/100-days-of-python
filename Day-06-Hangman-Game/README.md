# 🎮 Day 06 - Hangman Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-CLI%20Game-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

Hangman is a **text-based word guessing game** where the player must guess the hidden word letter by letter before running out of lives.

---

# 🎯 Game Description

The computer randomly selects a word from a predefined list.
The player must guess the word **one letter at a time**.

* Each wrong guess reduces the number of lives.
* The player starts with **6 lives**.
* The game ends when:

  * The player **guesses the word correctly**, or
  * The player **runs out of lives**.

---

# 🎮 How the Game Works

1. The program selects a random word from `hangman_words.py`.
2. The player guesses a letter.
3. If the letter is in the word:

   * It is revealed in the correct position.
4. If the guess is incorrect:

   * The player loses a life.
5. Hangman ASCII art updates after each wrong guess.

---

# 🖥️ Example Gameplay

```
****************************6/6 LIVES LEFT****************************
Guess a letter: a
_a___

****************************5/6 LIVES LEFT****************************
Guess a letter: e
_a_e_
```

The game continues until the player wins or loses.

---

# 📂 Project Structure

```
Day-06-Hangman
│
├── main.py
├── hangman_art.py
├── hangman_words.py
└── README.md
```

### File Explanation

* **main.py** → Contains the main game logic
* **hangman_words.py** → Contains the list of possible words
* **hangman_art.py** → Contains ASCII art for the Hangman stages and logo

---

# 🧠 Concepts Used

This project demonstrates several Python concepts:

* `random` module
* Lists
* Loops (`while`)
* Conditional statements (`if`, `elif`, `else`)
* String manipulation
* Importing modules
* Game state management
* ASCII art display

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Day-06-Hangman
```

### 3️⃣ Run the game

```bash
python main.py
```

