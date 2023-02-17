from game import connectFour, Colors
import shutil

terminalWidth, terminalHeight = shutil.get_terminal_size()

def getNumber(prompt, minimum=0, maximum=None):
    a = input(prompt)
    while True:
        if a.isdecimal():
            if int(a) >= minimum:
                if maximum != None:
                    if int(a) <= maximum:
                        return int(a)
                else:
                    return int(a)
        print(Colors.RED + "Invalid number!" + Colors.END)
        a = input(prompt)



if __name__ == "__main__":
    
    boardHeight = getNumber("Enter board height (min 4): ", minimum=4)
    boardWidth = getNumber("Enter board width (min 4): ", minimum=4)
    players = getNumber("Enter amount of players (min 2): ", minimum=2)
    
    game = connectFour(boardHeight, boardWidth, players, terminalWidth, terminalHeight)
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
            if game.check_win(player):
                game.display_board()
                print(Colors.YELLOW + f"Player {player} wins!")
                exit()

