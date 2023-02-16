from game import connectFour, Colors
import shutil

terminalWidth, terminalHeight = shutil.get_terminal_size()

def getNumber(prompt, minimum=0):
    a = input(prompt)
    while True:
        if a.isdecimal():
            if int(a) >= minimum:
                break
        print(Colors.RED + "Invalid number!" + Colors.END)
        a = input(prompt)
    return int(a)



if __name__ == "__main__":
    
    boardLength = getNumber("Enter board length (min 4): ", minimum=4)
    boardWidth = getNumber("Enter board width (min 4): ", minimum=4)
    boardWidth = getNumber("Enter amount of players (min 2): ", minimum=2)
    
    game = connectFour(boardLength, boardWidth, 2, terminalWidth, terminalHeight)
    game.display_board()

