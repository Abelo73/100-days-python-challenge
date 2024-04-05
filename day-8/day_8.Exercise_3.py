#Day 8.3 Caesar Cipher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift =  int(input("Type the shift number:\n "))

# Create a function called encrypt that takes text and shift as input

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        # print(position)
        new_position = position +shift
        # print(new_position)
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
# encrypt(text, shift)

# Function for decoding the text

def decode(tex, shift):
    decoded_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"Decoded letter is {decoded_text}")
# decode(text, shift)

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decode(text, shift)
else:
    print("Please type 'encode' for Encrypt or 'decode' for dcrypt")



