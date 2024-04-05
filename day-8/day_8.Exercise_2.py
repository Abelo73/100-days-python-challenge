#Day 8.2 Prime number checker

number =  int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"It's prime number")
    else:
        print(f"Its not prime number.")
prime_checker(number)