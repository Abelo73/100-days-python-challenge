print("Welcome to Treasure Island. \n Your mission is to find the treasure.")

left_Right = input('You are at a cross road, Where do you want to go? Type "left" or "right" ').lower()


if left_Right == "left":
    swim_wait = input('You come to lake, There is na island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim to cross. ').lower()
    if swim_wait == "wait":
        color = input('you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? Type "red" or "yellow" or "blue"? ').lower()
        if color == "yellow":
            print("You Found Treasure!. Congratulations!!")
        elif color == "blue":
            print("You chose a door that doesn't existing door. Gave over.")
        else:
            print("you entered room of beasts. Game Over.")
    else:
        print("You spiked while you are swimming. Game Over.")
else:
    print("You fell into a hole. Game Over.")