from game import connectFour





if __name__ == "__main__":
    game = connectFour(10, 6, 2)
    print(game.board)
    print(game.players)
    game.make_move(2,1)
    game.display_board()
    game.make_move(2,1)
    game.display_board()
    game.make_move(2,2)
    game.display_board()
