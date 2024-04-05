# Day 8 | Functions

# Function in python





# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Is't the weather nice today?")
# # greet()

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# location = input("Where are you living?: ")


# def great_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#     print(f"Is't the weather nice today? {name}")
# # great_with_name(name)


# More than one parameter

# def great_with(name, age):
#     print(f"Hye my name is {name}. I'm {age} years old!.")
# great_with(name, age)


# def greet_location(name, location):
#     print(f"Hello, {name}")
#     print(f"What is like in {location}?")
# greet_location(name, location)



# Encrypt Function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt: \n")
text = input("enter your message!. \n").lower()
shift =  int(input("Type the number to shift!. \n"))


# def encode(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(cipher_text)
# encode(text, shift)


# def decode(text, sift):
#     plain_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(plain_text)
# decode(text, shift)


def cipher(text, shift, direction):
    end_code = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position + shift
        else:
            new_position = position - shift
        new_letter = alphabet[new_position]
        end_code += new_letter
    print(end_code)   
cipher(text, shift, direction)     