# Day 03 - Treasure Island 🏝️

This project is a **text-based adventure game written in Python** as part of the **100 Days of Python Bootcamp by Dr. Angela Yu**.

The goal of the game is to make the correct choices to find the hidden treasure on Treasure Island.

---

## 🎮 Game Description

The player starts at a crossroad on Treasure Island and must make a series of decisions to reach the treasure.

At each stage, the player chooses between different options. Some choices lead to victory, while others lead to **Game Over**.

The correct path to win the game is:

```
Left → Wait → Yellow
```

---

## 🕹️ How the Game Works

1. The game begins at a **crossroad**.
2. The player must choose **left** or **right**.
3. If the player chooses correctly, they reach a **lake**.
4. The player must decide whether to **wait for a boat** or **swim**.
5. If they reach the island safely, they must choose between **three doors**:

   * Red
   * Yellow
   * Blue
6. Only one door leads to the **treasure**.

---

## 💻 Example Gameplay

```
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a cross road. Where do you want to go?
Type 'left' or 'right':
left

You've come to a lake. There is an island in the middle of the lake.
Type 'wait' to wait for a boat. Type 'swim' to swim across:
wait

You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?
yellow

You found the treasure! You Win!
```

---

## 📚 Concepts Used

This project demonstrates several Python basics:

* `print()` statements
* `input()` for user interaction
* Conditional statements (`if`, `elif`, `else`)
* String methods like `.lower()`
* Nested conditionals
* ASCII art

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone https://github.com/adityagpt2004/100-days-of-python.git
```

2. Navigate to the project folder:

```
cd Day-03-Treasure-Island
```

3. Run the Python file:

```
python main.py
```

---

## 🎯 Learning Objective

The purpose of this project is to practice:

* Decision making using **if/else logic**
* Writing **interactive terminal programs**
* Building a simple **game flow**

