from game import connectFour, Colors
import shutil

terminalWidth, terminalHeight = shutil.get_terminal_size()

'''
Error handling functions
'''

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

def main():
    gameFinished = False
    scoreboard = []
    
    boardHeight = getNumber("Enter board height (min 4): ", minimum=4)
    boardWidth = getNumber("Enter board width (min 4): ", minimum=4)
    players = getNumber("Enter amount of players (min 2): ", minimum=2)
    
    while True:
        game = connectFour(boardHeight, boardWidth, players, terminalWidth, terminalHeight, scoreboard)
        while True:
            for player in range(1, players+1):
                game.display_board()
                while True:
                    column = getNumber(f"Player {player}'s move: ", minimum=1, maximum=boardWidth)
                    if game.valid_move(column):
                        game.make_move(column, player)
                        break
                    else:
                        print(Colors.RED + "Invalid column!" + Colors.END)
                if game.check_draw():
                    game.display_board()
                    print(Colors.YELLOW + f"It's a Draw!")
                    scoreboard = game.update_scoreboard(None)
                    game.print_scoreboard()
                    gameFinished = True
                    break
                if game.check_win(player):
                    game.display_board()
                    print(Colors.YELLOW + f"Player {player} wins!")
                    scoreboard = game.update_scoreboard(player)
                    game.print_scoreboard()
                    gameFinished = True
                    break
            if gameFinished:
                break
        
        gameFinished = False
        if not getYesNo(Colors.LIGHT_PURPLE + "Do you want to play again? (Yes/No) " + Colors.END):
            print("Exiting...")
            exit()
        
        print("Please re-enter game settings, leave blank to use previous settings.")
        newBoardHeight = getNumber("Enter board height (min 4): ", minimum=4, blankAllowed=True)
        newBoardWidth = getNumber("Enter board width (min 4): ", minimum=4, blankAllowed=True)
        newPlayers = getNumber("Enter amount of players (min 2): ", minimum=2, blankAllowed=True)
        boardHeight = boardHeight if newBoardHeight == "" else newBoardHeight
        boardWidth = boardWidth if newBoardWidth == "" else newBoardWidth
        players = players if newPlayers == "" else newPlayers

if __name__ == "__main__":
    main()