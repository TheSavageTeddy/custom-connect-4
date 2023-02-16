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
	def __init__(self, length: int, width: int, players: int) -> None:
		self.length = length
		self.width = width
		self.board = [[0 for _ in range(self.width)] for _ in range(self.length)]

		self.colour = Colors()
		self.colourList = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.YELLOW, Colors.CYAN, Colors.PURPLE, Colors.LIGHT_RED, Colors.LIGHT_BLUE, Colors.LIGHT_GREEN, Colors.LIGHT_PURPLE]
		self.players = {i:self.colourList[i-1] for i in range(1, players + 1)}
		

	
	def colour_markers(self, string: str):
		colouredString = ""
		for char in string:
			match char:
				case "0":
					colouredString += "."
				case _:
					if char in list(map(str, self.players.keys())):
						colouredString += self.players[int(char)] + char + self.colour.END
					else:
						colouredString += char
		return colouredString
			
	
	def display_board(self):
		[print(self.colour_markers(" ".join(map(str, row)))) in row for row in self.flip_dimension(self.board)]

	def flip_dimension(self, arr: list) -> list:
		'''
		Flips a 2 dimensional array
		'''
		return [[arr[i][e] for i in range(len(arr))] for e in range(len(arr[0]))]


	def check_win(self, board, player) -> bool:
		'''
		Check if a player has won, given the board and the player number
		'''
		if any([player * 4 in "".join(map(str, row)) for row in board]):
			return True
		if any([player * 4 in "".join(map(str, col)) for col in self.flip_dimension(board)]):
			return True
		return False

	def valid_move(self, column):
		return 0 in self.board[column]

	def make_move(self, column, player):
		self.board[column - 1]["".join(map(str, self.board[column - 1])).rindex("0")] = player


