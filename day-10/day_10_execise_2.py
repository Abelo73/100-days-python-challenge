# Day 10 Exercise 10.2 | Calculator exercise

def add(n1, n2): 
    return n1 + n2 

def subtract(n1, n2): 
    return n1 - n2 

def multiplication(n1, n2): 
    return n1 * n2

def division(n1, n2): 
    return n1 / n2 
    
operations = {
    "+":add,
    "-":subtract,
    "*":multiplication,
    "/":division
}


is_continue = True
num1 = float(input("What is first number?: "))
for symbol in operations: 
    print(symbol)

while is_continue: 
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is Next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("Enter y to continue and n for finish!") == "y": 
        num1 = answer 
    else: 
        is_continue = False



