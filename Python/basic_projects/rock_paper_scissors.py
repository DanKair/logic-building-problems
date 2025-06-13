# Rock Paper Scissors
 # 1. Ask user input to enter his choice, and computer will have random.choice value
 # 2. Verify if that choice exists in possible_choices list
 # 3. While user_choice not in possible_choices: input("Please enter the valid choice: ")
 # 4. While userWantsToPlay = True: play the game
 # 5. At the end of game, ask user input userWantToPlay = input("Do you wanna play again: (y/n)")
import tkinter as tk

"""
window = tk.Tk()
window.title("Rock Paper Scissors")

label = tk.Label(
    text="Welcome to the Game!",
    foreground="white",  # Set the text color to white
    background="#2F847C",  # Set the background color to black
    width=1024,
    height=768,
)
label.pack()
window.mainloop()
"""

def rock_paper_scissors():
    import random
    choices = ["rock", "scissors", "paper"]
    user_wants_to_play = "y"

    while user_wants_to_play != "n":
        user_choice = str(input("Rock, paper or Scissors?: ")).lower()
        while user_choice not in choices:
            print(f"Ooops, it seems that you have enter incorrect choice. \nPlease enter the choice from: {choices}")
            user_choice = str(input("Rock, paper or Scissor?")).lower()

        print(f"Your choice is: {user_choice}")
        bot_choices = random.choice(choices)
        print(f"Computer choice is: {bot_choices}")

        if user_choice != bot_choices:
            if user_choice == "rock" and bot_choices == "paper":
                print("You lose😢!")
            elif user_choice == "paper" and bot_choices == "scissors":
                print("You lose😢!")
            elif user_choice == "scissors" and bot_choices == "rock":
                print("You lose😢!")
            else:
                print("You win✨!")
        else:
            print("Tie")

        user_wants_to_play = input("Do you wanna play again? (y/n): ").lower()

        if user_wants_to_play == "n":
            print("Thanks for playing! Goodbye🎇!")
            break
        elif user_wants_to_play == "y":
            print("Alright, let's play again😎.")
            continue
            # user_choice = str(input("Rock, paper or Scissors?: ")).lower()
            # bot_choices = random.choice(choices)


print(rock_paper_scissors())

"""
def continue_game():
    match user_wants_to_play:
        case "y":
            continue_game = True
            print("Alright, let's play again😎.")
            rock_paper_scissors() 
            user_wants_to_play = input("Do you wanna play again? (y/n): ").lower()                
        case "n":
            continue_game = False
            return "Thanks for playing! Goodbye🎇!"    
        case _:
            print("Oops, it seems you have entered invalid option.")
            print("Please enter only 'y' or 'n'")
            user_wants_to_play = input("Do you wanna play again? (y/n): ").lower()
"""