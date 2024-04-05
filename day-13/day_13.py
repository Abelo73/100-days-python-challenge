# Day 13 | Debugging

# def my_function(): 
#     for i in range(1, 21): 
       
#         if i == 20:
#             print("you got it!.")
# my_function()

# # Reproduce the bug

# from random import randint

# dice_imgs = ["😢1", "😞2", "😟3", "😄4", "😕5", "😄6"]

# dice_number = randint(0, 5)
# print(dice_imgs[dice_number])

# # Play Computer

# year = int(input("What is year of birth? "))

# if year > 1980 and year < 1994: 
#     print("you are millennial")
# elif year >= 1994: 
#     print("you are a Gen Z.")

# # Fix the Errors


# age = int(input("How old are you?: "))

# if age > 18: 
#     print(f"You can drive at age {age}")

# # Print your Friend

# page = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))

# word_per_page = int(input("Number of words per page: "))
# print(pages)

# print(word_per_page)
# total_words =  pages * word_per_page

# print(total_words)


# # Debug Odd or Even Exercise

# number = int(input("Which number do you want to check?: "))

# if number % 2 == 0: 
#     print("This is an even number.")
# else:
#   print("This is an Odd number")

# # Debug leap year exercise

# year = int(input("Which year do you want to check?: "))

# if year % 4 ==0: 
#     if year % 100 ==0: 
#         if year % 400 ==0: 
#             print("Leap year.")
#         else: 
#             print("Not leap year.")
#     else: 
#         print("Leap year.")
# else: 
#     print("Not leap year.")

# Debug FizzBuzz exercise


for number in range(1, 101): 
    if number % 3 == 0 and number % 5 == 0: 
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    else: 
        print(number)