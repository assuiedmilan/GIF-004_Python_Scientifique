"""Exercise 2"""

import numpy
import pytest
from numpy import ndarray


def split(table_to_split: ndarray, lines_from_last: int, column_from_first: int) -> ndarray:
    """Extract an smaller array from an existing array

    Args:
        table_to_split (ndarray): the table from which to extract
        lines_from_last (int): this number of lines from the last one of the table will be extracted
        column_from_first (int): this number of columns from the first one of the table will be extracted

    Returns:
        ndarray: a two dimensional array
        """

    return table_to_split[-lines_from_last:, :column_from_first]


@pytest.mark.parametrize(argnames="lines, columns, lines_from_last, column_from_first", argvalues=[(20, 5, 7, 2)])
def test_split(lines, columns, lines_from_last, column_from_first):
    """Test table extraction"""
    table = numpy.random.random((lines, columns))
    extract = split(table, lines_from_last, column_from_first)

    test_line = (lines - lines_from_last)
    test_column = 0

    for _, value in numpy.ndenumerate(extract):
        assert value == table[test_line, test_column]

        test_column += 1
        if column_from_first == test_column:
            test_column = 0
            test_line += 1
