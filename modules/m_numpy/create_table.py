"""Exercise 1"""

import numpy
import pytest
from numpy import ndarray


def créer_table(lines: int, columns: int, initial_value: float) -> ndarray:
    """
    Create a n*m array initialized at a fixed values

    Args:
        lines (int): number of lines
        columns (int): number of columns
        initial_value (float): initial value of the table

    Returns:
        ndarray: a two dimensional array
    """

    return numpy.ones((lines, columns)) * initial_value


@pytest.mark.parametrize(argnames="lines, columns, initial_value",
                         argvalues=[(1, 1, 2), (5, 4, 2.1345), (2, 2, 1.1)]
                         )
def test_create_table(lines, columns, initial_value):
    """Test table creation"""
    table = créer_table(lines, columns, initial_value)

    assert table.size == lines * columns
    assert table.shape == (lines, columns)

    assert [x == initial_value for x in numpy.nditer(table)]
