import random

# from replit import clear



# Display art
from art import logo, vs
from game_data import data

# formate teh account data into printable formate

score = 0


def format_data(account): 
  """Format the account data into printable table."""
  account_name = account_a["name"]
  account_descr = account_a["description"]
  account_country = account_a["country"]

  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count): 
  """Takes the user guess and follower counts and returns if they got it right"""
  if a_follower_count > b_follower_count: 
    return guess == "a"
  else: 
    return guess == "b"





print(logo)
# Generate a random account from the game


game_Should_continue = True

account_b = random.choice(data)


while game_Should_continue: 
  account_a = random.choice(data)

  if account_a == account_b: 
    account_a = account_b
    account_b = random.choice(data)
    
    # Making account at position B become the next account at position


  print(f"Compare A: {format_data(account_a)}")

  print(vs)
  print(f"against B: {format_data(account_b)}")


  # Ask user for a guess

  guess = input("Who has more followers? 'A' or 'B': ").lower()

  # Check if the user is correct.add()
  ## get follower count of each account

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]




  ## User if statement to check if the user is correct

  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  print(a_follower_count)
  print(b_follower_count)

  # Giv user feedback on their guess. 

  if is_correct: 
    score += 1
    print(f"You're right! current score: {score}.")
  else: 
    game_Should_continue = False
    print(f"Sorry, that is wrong!. Final score: {score}")


  # Score keeping

# Make the game repeatable



# Clear the screen  rounds.