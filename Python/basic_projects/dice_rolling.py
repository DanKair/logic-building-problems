# 1. Create a tuple of 2 random dice numbers from 1 to 6
# 2. ask user whether he wants to roll a dice
# 3. While user_input != "y" or user_input != "n": keep asking user for valid input
# 4. if answer == "y": role_dice

import random

def role_dice():
    dice = random.randint(1, 6), random.randint(1, 6)
    return dice

"""
user_input = str(input("Roll the dice? (y/n): ")).lower()
while user_input != "y" or user_input != "n":
    print("Invalid Input!\nPlease enter only: 'y' or 'n'")
    user_input = str(input("Roll the dice? (y/n): ")).lower()

    if user_input == "y":
        role_dice()
    elif user_input == "n":
        print("Thanks for playing!")
"""
# Explanation: The issue here is due to a logical error in the while loop condition.
# The expression 'user_input != "y" or user_input != "n"' will always be True,
# because it's essentially checking if the variable is not equal to two different values ('y' and 'n') at the same time.
# This means that no matter what input the user provides, the loop will continue indefinitely.
# To fix this, we need to change the condition in the while loop to check for either "y" or "n", but not both.
# Here's the corrected code:

while True:
    user_input = str(input("Roll the dice? (y/n): ")).lower()

    if user_input == "y":
        print(role_dice())
    elif user_input == "n":
        print("Thanks for playing!")
        break 
    else:
        print("Invalid Input!\nPlease enter only: 'y' or 'n'")

              
