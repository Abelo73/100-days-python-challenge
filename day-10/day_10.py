# More On Functions

# num1 = int(input("First number to calculate: \n"))
# num2 = int(input("The Second number to calculate: \n"))

# operation = input("Please chose the operation to calculate, '+' or '*'")

# def addition(num1, num2): 
#     return num1 + num2
# def multiplication(num1, num2):
#     return num1 * num2


# if operation == '+': 
#     result = addition(num1, num2)
# else: 
#     result = multiplication(num1, num2)
# print(result)

# f_name = input("What is your name?: ")
# l_name = input("What is your last name?: ")

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name(f_name, l_name)
# print(formatted_string) 



def format_name(f_name, l_name): 
    if f_name == "" or l_name == "": 
        return
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"
print(format_name(input("What is your first name?: "), input("What is your last name?: ")))