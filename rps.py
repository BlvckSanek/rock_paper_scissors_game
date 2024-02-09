import sys # This allows the game to end
import random # This allows computer to choose random numbers(1-3)
from enum import Enum # To let the game say I chose rock, paper or scissors

game_count = 0


def play_rps():
    
    class RPS(Enum):
        """
        This is used to store the variables that do not change.
        """
        ROCK = 1
        PAPER = 2
        SCISSORS = 3  
    
    # Player is allow to make a choice between rock, paper or scissors
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    # playerchoice type casted to an integer
    player = int(playerchoice)
    
    # Python chooses randomly between 1, 2, or 3    
    computerchoice = random.choice("123")

    # Python's choice is type casted into an integer
    computer = int(computerchoice)

    # The selection of the player is shown here
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    # The selection of the python is shown here
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
           return "🎉  You win!"
        elif player == 2 and computer == 1:
           return "🎉  You win!"
        elif player == 3 and computer == 2:
           return "🎉  You win!"
        elif player == computer:
           return "😲  Tie game!"
        else:
           return "🐍  Python wins!"
       
    game_result = decide_winner(player, computer)
    
    print(game_result)
        
    global game_count
    game_count += 1
    
    print("\nGame count: " + str(game_count))
    
    print("\nPlay again?")
    
    while True:
        # After each game the player is asked to continue or quit
        playagain = input(" \nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
        
    
    # The player input is converted to lower case
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")   # End of the game 
          
play_rps()