import re

def getNumber(prompt, minimum=0):
    a = input(prompt)
    while True:
        if a.isdecimal():
            if int(a) >= minimum:
                break
        print(Colors.RED + "Invalid number!" + Colors.END)
        a = input(prompt)
    return int(a)

class Colors:
    """
    ANSI color codes
    Source: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
    """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32



class connectFour:
    def __init__(self, boardHeight: int, boardWidth: int, players: int, terminalWidth: int, terminalHeight:int, scores: dict) -> None:
        self.height = boardHeight
        self.width = boardWidth
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.colour = Colors()
        self.colourList = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.YELLOW, Colors.CYAN, Colors.PURPLE, Colors.LIGHT_RED, Colors.LIGHT_BLUE, Colors.LIGHT_GREEN]
        self.players = {i:{'colour': self.colourList[i-1], 'icon': None} for i in range(1, players + 1)}
        
        if scores == []:
            self.scoreboard = {i:0 for i in range(1, players + 1)}
        else:
            self.scoreboard = {}
            for player in range(1, players + 1):
                if player in scores.keys():
                    self.scoreboard[player] = scores[player]
                else:
                    self.scoreboard[player] = 0

        self.terminalWidth, self.terminalHeight = terminalWidth, terminalHeight

    
    def center_ansi_text(self, string: str, width: int, char: str = " ") -> str:
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])') # https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
        true_string_length = len(ansi_escape.sub('', string)) # actual visual length of string - disregards ansi colouring codes
        right = (width - true_string_length) // 2
        left = width - right - true_string_length
        return f'''{right * char}{string}{left * char}'''

    def print_scoreboard(self):
        sorted_scoreboard = [[player, score] for player, score in self.scoreboard.items()]
        sorted_scoreboard = sorted(sorted_scoreboard, key=lambda x: x[1], reverse=True)
        for scorecard in sorted_scoreboard:
            player, score = scorecard
            print(f"Player {player}: {score}")

    def update_scoreboard(self, winning_player):
        if winning_player == None:
            for player in self.scoreboard:
                print(f"Player {self.scoreboard[player]} recieves 1.5 points ({self.scoreboard[player]} -> {self.scoreboard[player]+1.5})")
                self.scoreboard[player] += 1.5
            return self.scoreboard

        winner = winning_player
        losers = []
        for player in self.players:
            if player != winner:
                losers.append(player)

        print(f"Player {player} recieves 2 points ({self.scoreboard[winner]} -> {self.scoreboard[winner]+2})")
        self.scoreboard[winner] += 2
        for loser in losers:
            print(f"Player {player} recieves 1 point ({self.scoreboard[loser]} -> {self.scoreboard[loser]+1})")
            self.scoreboard[loser] += 1
          
        return self.scoreboard
    
    def colour_markers(self, string: str) -> str:
        colouredString = ""
        for i, char in enumerate(string):
            match char:
                case "0":
                    colouredString += self.colour.LIGHT_PURPLE + "." + self.colour.END
                case _:
                    if char in list(map(str, self.players.keys())):
                        colouredString += self.players[int(char)]['colour'] + char + self.colour.END
                    else:
                        colouredString += char
        return colouredString


    def display_board(self) -> None:
        for row in self.board:
            print(f'{self.center_ansi_text(self.colour_markers(" ".join(map(str, row))), self.terminalWidth)}')
        
        print(f'{self.center_ansi_text(Colors.BOLD + " ".join(map(str, range(1, self.width + 1))) + Colors.END, self.terminalWidth)}')

    def flip_dimension(self, arr: list) -> list:
        '''
        Flips a 2 dimensional array
        '''
        return [[arr[i][e] for i in range(len(arr))] for e in range(len(arr[0]))]

    def check_draw(self) -> bool:
        return not any([item == 0 for row in self.board for item in row])


    def check_win(self, player) -> bool:
        '''
        Check if a player has won, given the board and the player number
        '''

        # rows and columns
        if any([str(player) * 4 in "".join(map(str, row)) for row in self.board]):
            return True
        if any([str(player) * 4 in "".join(map(str, col)) for col in self.flip_dimension(self.board)]):
            return True
        
        # left down to right up diagonal
        for row in range(3, self.width):
            for col in range(0, self.height - 3):
                if str(player) * 4 == "".join(map(str, [self.board[row][col], self.board[row-1][col+1], self.board[row-2][col+2], self.board[row-3][col+3]])):
                    return True
        
        for row in range(3, self.width):
            for col in range(3, self.height):
                if str(player) * 4 == "".join(map(str, [self.board[row][col], self.board[row-1][col-1], self.board[row-2][col-2], self.board[row-3][col-3]])):
                    return True
        
        return False

    def valid_move(self, column) -> bool:
        return 0 in self.flip_dimension(self.board)[column - 1]

    def make_move(self, column, player):
        self.board["".join(map(str, self.flip_dimension(self.board)[column-1])).rindex("0")][column-1] = player

    def play_round(self):
        for playerNum in self.players:
            column = getNumber(f"Player {playerNum}: ", minimum=1)
