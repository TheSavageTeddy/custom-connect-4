


def check_win(board, player) -> bool:
	for row in board:
		print(row)
		for item in row:
			print(item)


board = [
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0],
]

check_win(board, 0)