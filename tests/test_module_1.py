"""Tests for module 1"""

import numpy
import pytest
from numpy.random import random

from scientific_python.modules.module_1 import compute_mean
from scientific_python.modules.module_1 import compute_variance
from scientific_python.modules.module_1 import créer_table
from scientific_python.modules.module_1 import resolve_linear_equation
from scientific_python.modules.module_1 import split


@pytest.mark.parametrize(argnames="lines, columns, initial_value",
                         argvalues=[(1, 1, 2), (5, 4, 2.1345), (2, 2, 1.1)]
                         )
def test_create_table(lines, columns, initial_value):
    """Test table creation"""
    table = créer_table(lines, columns, initial_value)

    assert table.size == lines * columns
    assert table.shape == (lines, columns)

    assert [x == initial_value for x in numpy.nditer(table)]


@pytest.mark.parametrize(argnames="lines, columns, lines_from_last, column_from_first", argvalues=[(20, 5, 7, 2)])
def test_split(lines, columns, lines_from_last, column_from_first):
    """Test table extraction"""
    table = random((lines, columns))
    extract = split(table, lines_from_last, column_from_first)

    test_line = (lines - lines_from_last)
    test_column = 0

    for _, value in numpy.ndenumerate(extract):
        assert value == table[test_line, test_column]

        test_column += 1
        if column_from_first == test_column:
            test_column = 0
            test_line += 1


@pytest.mark.parametrize(argnames="coefficients_matrix, second_member_matrix, expected_result",
                         argvalues=[
                             (
                                     numpy.array([[1, 2, 3], [2, 3, 4], [3, 2, 3]]),
                                     numpy.array([3, 2, 1]),
                                     numpy.array([-1, -4, 4])
                             )
                         ]
                         )
def test_resolve_linear_equation(coefficients_matrix, second_member_matrix, expected_result):
    """Test resolve_linear_equation"""
    result = resolve_linear_equation(coefficients_matrix, second_member_matrix)
    comparison = numpy.around(result, 2) == expected_result
    assert comparison.all()


@pytest.mark.parametrize(argnames="table, expected_mean, expected_var",
                         argvalues=[
                             (numpy.array([[1, 2, 3], [2, 3, 4], [3, 2, 3]]), 2.56, 0.69),
                             (numpy.array([3, 2, 1]), 2, 0.67),
                             (numpy.array([-1, -4, 4]), -0.33, 10.89)
                         ]
                         )
def test_mean_and_variance(table, expected_mean, expected_var):
    """Test variance and mean"""
    assert round(compute_mean(table), 2) == expected_mean
    assert round(compute_variance(table), 2) == expected_var
