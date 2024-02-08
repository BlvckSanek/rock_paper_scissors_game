import sys # This allows the game to end
import random # This allows computer to choose random numbers(1-3)
from enum import Enum # To let the game say I chose rock, paper or scissors

class RPS(Enum):
    """
    This is used to store the variables that do not change.
    """
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True # Palyagain variable assigned to a bool

# Loop of the whole game starts here
while playagain: # If the playagain variable is True
    # Player is allow to make a choice between rock, paper or scissors
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    # playerchoice type casted to an integer
    player = int(playerchoice)

    # Checks to for a viable input from the player
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")
    
    # Python chooses randomly between 1, 2, or 3    
    computerchoice = random.choice("123")

    # Python's choice is type casted into an integer
    computer = int(computerchoice)

    # The selection of the player is shown here
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    # The selection of the python is shown here
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    # There are some control flows going on here
    # Comparisons between the choices of the player and python
    if player == 1 and computer == 3:
        print("🎉  You win!")
    elif player == 2 and computer == 1:
        print("🎉  You win!")
    elif player == 3 and computer == 2:
        print("🎉  You win!")
    elif player == computer:
        print("😲  Tie game!")
    else:
        print("🐍  Python wins!")
    
    # After each game the player is asked to continue or quit
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
    
    # The player input is converted to lower case
    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False
        
sys.exit("Bye! 👋")   # End of the game   
        