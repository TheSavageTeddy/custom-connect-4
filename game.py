
def flip_dimension(arr: list) -> list:
	'''
	Flips a 2 dimensional array
	For example 
	'''
	return [[arr[x][y] for x in range(len(arr))] for y in range(len(arr))]


def check_win(board, player) -> bool:
	'''
	Check if a player has won, given the board and the player number
	'''
	if any([player * 4 in "".join(map(str, row)) for row in board]):
		return True
	if any([player * 4 in "".join(map(str, col)) for col in flip_dimension(board)]):
		return True
	return False

def valid_move(board, column):
	return 0 in board[column]

def make_move(board, column, player):
	board[column]["".join(map(str, board[column])).rindex("0")] = player
	return board



board = [
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
]

print(make_move(board, 1, 1))
print(board)