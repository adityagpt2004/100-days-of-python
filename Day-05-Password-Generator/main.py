import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

choice = input(f"What type of Password do you need. Type 'Easy' or 'Hard':\n").lower()

nr_letters = int(input("How many letters would you like in your Password?:\n"))
nr_symbols = int(input("How many symbols would you like in your Password?:\n"))
nr_numbers = int(input("How many numbers would you like in your Password?:\n"))

# easy level
if choice == "easy":

    random_letters = random.choices(letters, k=nr_letters)
    random_symbols = random.choices(symbols, k=nr_symbols)
    random_numbers = random.choices(numbers, k=nr_numbers)

    easy_password = ("".join(random_letters + random_symbols + random_numbers))
    print(easy_password)
else:
    # Hard level
    random_letters = random.choices(letters, k=nr_letters)
    random_symbols = random.choices(symbols, k=nr_symbols)
    random_numbers = random.choices(numbers, k=nr_numbers)

    hard_password = list("".join(random_letters + random_symbols + random_numbers))
    random.shuffle(hard_password)
    final_password = "".join(hard_password)
    print(final_password)