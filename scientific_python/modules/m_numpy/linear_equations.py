"""Exercise 3"""

import pytest
from numpy import ndarray, dot, array, around
from numpy.linalg import inv


def resolve_linear_equation(coefficients_matrix: ndarray, second_member_matrix: ndarray) -> ndarray:
    """
    Resolve equation Ax = c and returns x

    Args:
        coefficients_matrix (ndarray): A matrix
        second_member_matrix (ndarray): c matrix

    Returns:
        ndarray: a two dimensional array
    """

    inverted_coefficients_matrix = inv(coefficients_matrix)
    return dot(inverted_coefficients_matrix, second_member_matrix)


@pytest.mark.parametrize(argnames="coefficients_matrix, second_member_matrix, expected_result",
                         argvalues=[
                             (
                                     array([[1, 2, 3], [2, 3, 4], [3, 2, 3]]),
                                     array([3, 2, 1]),
                                     array([-1, -4, 4])
                             )
                         ]
                         )
def test_resolve_linear_equation(coefficients_matrix, second_member_matrix, expected_result):
    """Test resolve_linear_equation"""
    result = resolve_linear_equation(coefficients_matrix, second_member_matrix)
    comparison = around(result, 2) == expected_result
    assert comparison .all()
