import numpy


def compute_chess_matrix():
    chess_board_size = 8

    board = numpy.zeros((chess_board_size, chess_board_size))
    board[0::2, 1::2] = 1
    board[1::2, 0::2] = 1
    return board


print(compute_chess_matrix())
