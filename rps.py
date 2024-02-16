import sys # This allows the game to end
import random # This allows computer to choose random numbers(1-3)
from enum import Enum # To let the game say I chose rock, paper or scissors

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            """
            This is used to store the variables that do not change.
            """
            ROCK = 1
            PAPER = 2
            SCISSORS = 3  
        
        # Player is allow to make a choice between rock, paper or scissors
        playerchoice = input(f"\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        # playerchoice type casted to an integer
        player = int(playerchoice)
        
        # Python chooses randomly between 1, 2, or 3    
        computerchoice = random.choice("123")

        # Python's choice is type casted into an integer
        computer = int(computerchoice)

        # The selection of the player is shown here
        print(f"\n{name}, you chose  {str(RPS(player)).replace('RPS.', '').title()}.")
        # The selection of the python is shown here
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲  Tie game!"
            else:
                python_wins += 1
                return f"🐍  Python wins!\nSorry, {name}..😢"
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
            
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {(game_count)}")
        print(f"\n{name}'s wins: {(player_wins)}")
        print(f"\nPython wins: {(python_wins)}")
        
        print(f"\nPlay again, {name}?")
        
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
            sys.exit(f"Bye! {name} 👋")   # End of the game
        
    return play_rps
            


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )
    

    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()    