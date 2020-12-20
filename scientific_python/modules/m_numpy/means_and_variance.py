"""Exercise 3"""
import pytest
from numpy import ndarray, mean, var, array


def compute_mean(table: ndarray) -> float:
    """
    Compute mean of a table

    Args:
        table (ndarray): table to be processed

    Returns:
        float: the mean value
    """

    return mean(table)


def compute_variance(table: ndarray) -> float:
    """
    Compute mean of a table

    Args:
        table (ndarray): table to be processed

    Returns:
        float: the var value
    """

    return var(table)


@pytest.mark.parametrize(argnames="table, expected_mean, expected_var",
                         argvalues=[
                             (array([[1, 2, 3], [2, 3, 4], [3, 2, 3]]), 2.56, 0.69),
                             (array([3, 2, 1]), 2, 0.67),
                             (array([-1, -4, 4]), -0.33, 10.89)
                         ]
                         )
def test_resolve_linear_equation(table, expected_mean, expected_var):
    """Test variance and mean"""
    assert round(compute_mean(table), 2) == expected_mean
    assert round(compute_variance(table), 2) == expected_var
