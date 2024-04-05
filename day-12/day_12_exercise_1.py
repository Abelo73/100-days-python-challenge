# Day 12 Exercise 12.1 Number guessing game



# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# guess_number = random.randint(1,100)
# print(guess_number)



# if difficulty == "hard": 
#     attempts = 5;
# else: 
#     attempts = 10

# print(f"you have {attempts} remaining to guess the number")

# make_guess = int(input("Make a guess: "))

# is_game_over = False

# while not is_game_over:
#     if make_guess > guess_number: 
#         print("Too high")
#         attempts = attempts - 1;
#         is_game_over = True
#     elif make_guess == guess_number: 
#         print("you whin")
#         attempts = attempts - 1;
#         is_game_over = True


#     else: 
#         print("Too low")
#         attempts = attempts - 1;
#         is_game_over = True



# if attempts == 0: 
#     print("Game over")



# while not attempts ==0: 
#     attempts-=1
#     def guessing(attempts, difficulty, make_guess): 
#         if difficulty == "easy": 
#             attempts = 10
#             return attempts
#         else: 
#             attempts = 5
#             return attempts
#         print(attempts)
#         print(make_guess)

#     guessing(attempts, difficulty, make_guess)



# Choosing a random number between 1 and 100


import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns =0
def check_answer(guess, answer, turns): 
    if guess > answer: 
        print("Too high")
        return turns - 1
    elif guess < answer: 
        print("Too low")
        return turns - 1
    
    else: 
        print(f"you got it!., the number was {answer}")
        return

def set_difficulty(): 
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy": 
        return EASY_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TURNS
        
def game(): 
    print("Welcome to the number guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"answer is {answer}")

    # make function to set difficulty

    turns = set_difficulty()
    # Function to check user's guess against actual answer

    # Track the number of  turns and reduce by 1 if they get wrong

    guess = 0

    while guess != answer: 
        # let the user guess a number 
        print(f"you have {turns} attempts to guess the number")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0: 
            print("You've run out of guesses, you lose.")
            return
game()


# Repeat the guessing functionality if they get it wrong

