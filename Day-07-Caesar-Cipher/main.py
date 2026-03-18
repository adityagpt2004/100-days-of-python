from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(original_text, shift_amount, chosen_direction):
    output_text = ""
    if chosen_direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is your {chosen_direction}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input(f"type encode to 'encrypt', type 'decode' to decrypt:\n").lower()
    text = input(f"Type your message:\n").lower()
    shift = int(input("Type the shift number: "))

    caesar(original_text=text,shift_amount=shift,chosen_direction=direction)
    restart = input(f"Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")




