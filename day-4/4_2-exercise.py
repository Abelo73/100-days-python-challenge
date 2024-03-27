# Day 4 exercise 4.2 Biller

import random

names_string = input("Give me everybody's names, separated by a comma. : ")

names = names_string.split(", ")

# print(names[1])
num_items = len(names)

random_choice = random.randint(0, num_items - 1)

name = names[random_choice]

print(f"{name} is todays biller. That is amazing!")









# names = names_string[random_choice]

# print(f"{biller} is today biller.\n")