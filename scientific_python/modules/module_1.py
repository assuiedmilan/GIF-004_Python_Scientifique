"""Exercices sur module_1.numpy"""

import numpy
from numpy import dot
from numpy import ndarray
from numpy.linalg import inv


def creer_table(lines: int, columns: int, initial_value: float) -> ndarray:
    """
    Create a n*m array initialized at a fixed values

    Args:
        lines (int): number of lines
        columns (int): number of columns
        initial_value (float): initial value of the table

    Returns:
        a two dimensional ndarray
    """

    return numpy.ones((lines, columns)) * initial_value


def split(table_to_split: ndarray, lines_from_last: int, column_from_first: int) -> ndarray:
    """Extract an smaller array from an existing array

    Args:
        table_to_split (ndarray): the table from which to extract
        lines_from_last (int): this number of lines from the last one of the table will be extracted
        column_from_first (int): this number of columns from the first one of the table will be extracted

    Returns:
        a two dimensional ndarray
        """

    return table_to_split[-lines_from_last:, :column_from_first]


def resolve_linear_equation(coefficients_matrix: ndarray, second_member_matrix: ndarray) -> ndarray:
    """
    Resolve equation Ax = c and returns x

    Args:
        coefficients_matrix (ndarray): A matrix
        second_member_matrix (ndarray): c matrix

    Returns:
        a two dimensional ndarray
    """

    inverted_coefficients_matrix = inv(coefficients_matrix)
    return dot(inverted_coefficients_matrix, second_member_matrix)


def compute_mean(table: ndarray) -> float:
    """
    Compute mean of a table

    Args:
        table (ndarray): table to be processed

    Returns:
        the mean value
    """

    return numpy.mean(table)


def compute_variance(table: ndarray) -> float:
    """
    Compute mean of a table

    Args:
        table (ndarray): table to be processed

    Returns:
        the variance value
    """

    return numpy.var(table)


def compute_chess_matrix() -> ndarray:
    """
    Return a matrix representing a chess board

    Returns:
        an ndarray representing a chess board

    """
    chess_board_size = 8

    board = numpy.zeros((chess_board_size, chess_board_size))
    board[0::2, 1::2] = 1
    board[1::2, 0::2] = 1
    return board
