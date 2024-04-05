# Day 11 

import random

def deal_card(): 

    """ Returns random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7,8,9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, computer_score):
    if user_score == computer_score: 
        return "Draw 😢"
    elif computer_score == 0: 
        return "Lose, opponent has Blackjack 😞"
    elif user_score == 0: 
        return "Win with a Blackjack 😄"
    elif user_score > 21: 
        return "You went over. you lose 😄"
    elif computer_score > 21: 
        return "Opponent went over. you win 😖"
    elif user_score > computer_score: 
        return "You win 😕"
    else: 
        return "you lose 😃"

user_cards = []
computer_cards = []


def calculate_score(cards):
    if sum(cards) == 21 and length(cards) == 2: 
        return 0
    if 11 in cards and sum(cards) >21: 
        cards.remove(11)
        cards.append(1)
    return sum(cards)


for _ in range(2): 
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(deal_card())


is_game_over = False


# User while loop

while not is_game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21: 
        is_game_over = True
    else: 
        user_should_deal = input("Type 'y' to get another card, type 'n' for pass: ")
        if user_should_deal == "y": 
            user_cards.append(deal_card())
        else: 
            is_game_over = True

# if is_game_over: 
#     compare(user_score, computer_score)


while computer_score != 0 and computer_score < 17: 
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f"Computer score : {computer_score}")
print(f"Your score is : {user_score}")
    


print(compare(user_score, computer_score))






# calculate_score = sum(user_cards)
# print(calculate_score)
