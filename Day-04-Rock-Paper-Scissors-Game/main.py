import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

your_choice = int(input(f"What do you choose. Type 0 for rock, 1 for paper and 2 for scissors: "))
if your_choice >= 0 and your_choice <= 2:
    print(game_images[your_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print("You choose an invalid number\nYou lose")
elif your_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose")
elif computer_choice > your_choice:
    print("You lose")
elif your_choice > computer_choice:
    print("You Win!")
elif your_choice == computer_choice:
    print("It's a Draw!")


