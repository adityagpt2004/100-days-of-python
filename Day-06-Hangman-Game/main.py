import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

placeholder = ""
word_length = len(chosen_word)
for letter in range(0,word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed that letter: {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over =  True
        print("You've Won")
    print(display)
    print(stages[lives])


