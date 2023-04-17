from game import connectFour, Colors
import shutil

terminalWidth, terminalHeight = shutil.get_terminal_size()

'''
Error handling functions
'''

# Gets a number from the user, given the minumum and maximum number it can be
# blankAllowed for the case where the user can enter nothing for the previously set value
# Keeps prompting until user enters a valid input
def getNumber(prompt, minimum = 0, maximum = None, blankAllowed = False) -> int:
    a = input(prompt)
    while True:
        if a.isdecimal():
            if int(a) >= minimum:
                if maximum != None:
                    if int(a) <= maximum:
                        return int(a)
                else:
                    return int(a)
        elif a == "" and blankAllowed:
            return ""
        print(Colors.RED + "Invalid number!" + Colors.END)
        a = input(prompt)

# Gets a yes or no from the user
# Keeps prompting until user enters a valid input
def getYesNo(prompt) -> bool:
    a = input(prompt)
    while True:
        match a.lower():
            case 'y' | 'yes':
                return True
            case 'n' | 'no':
                return False
            case _:
                print(Colors.RED + "Invalid input! Please enter 'yes' or 'no'" + Colors.END)
        a = input(prompt)

# Main function of the game
def main():
    gameFinished = False
    scoreboard = []
    
    # Prompt user for the customizable game settings
    boardHeight = getNumber("Enter board height (min 4): ", minimum=4)
    boardWidth = getNumber("Enter board width (min 4): ", minimum=4)
    players = getNumber("Enter amount of players (min 2, max 8): ", minimum=2, maximum=8)
    
    while True:
        # Initialize the game
        game = connectFour(boardHeight, boardWidth, players, terminalWidth, terminalHeight, scoreboard)
        while True:
            for player in range(1, players+1): # Each player takes a turn in placing a marker
                game.display_board()
                while True: # Make sure the move they enter is valid
                    column = getNumber(f"{game.players[player]['colour']}Player {player}'s move: {Colors.END}", minimum=1, maximum=boardWidth)
                    if game.valid_move(column):
                        game.make_move(column, player)
                        break
                    else:
                        print(Colors.RED + "Invalid column!" + Colors.END)
                if game.check_win(player): # Check if the player that just placed their marker has won
                    game.display_board()
                    print(Colors.YELLOW + f"Player {player} wins!")
                    scoreboard = game.update_scoreboard(player)
                    input(Colors.ITALIC + "Press enter to continue to scoreboard..." + Colors.END)
                    game.print_scoreboard()
                    gameFinished = True
                    break
                if game.check_draw(): # Check if its a Draw
                    game.display_board()
                    print(Colors.LIGHT_GRAY + f"It's a Draw!")
                    scoreboard = game.update_scoreboard(None)
                    input(Colors.ITALIC + "Press enter to continue to scoreboard..." + Colors.END)
                    game.print_scoreboard()
                    gameFinished = True
                    break
            if gameFinished:
                break # This break is required as the previous breaks out of the for loop
        
        gameFinished = False
        if not getYesNo(Colors.LIGHT_PURPLE + "Do you want to play again? (Yes/No) " + Colors.END):
            print("Exiting...")
            exit()
        
        # Option to re-enter game settings after the game has ended
        print("Please re-enter game settings, leave blank to use previous settings.")
        newBoardHeight = getNumber("Enter board height (min 4): ", minimum=4, blankAllowed=True)
        newBoardWidth = getNumber("Enter board width (min 4): ", minimum=4, blankAllowed=True)
        newPlayers = getNumber("Enter amount of players (min 2): ", minimum=2, maximum=8, blankAllowed=True)
        boardHeight = boardHeight if newBoardHeight == "" else newBoardHeight
        boardWidth = boardWidth if newBoardWidth == "" else newBoardWidth
        players = players if newPlayers == "" else newPlayers

if __name__ == "__main__":
    main()