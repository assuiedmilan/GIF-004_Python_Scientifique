"""Tests for module 5"""
import pytest

from scientific_python.modules.module_5 import créer_matrice


@pytest.mark.parametrize("lines, columns", [(3, 3), (1, 1), (4, 6), (7, 5)])
def test_créer_matrice(lines, columns):
    """Test fonction de création de matrice"""
    matrix = créer_matrice(lines, columns)

    assert matrix.shape == (lines, columns)

    for i in range(lines):
        for j in range(columns):
            assert matrix[i, j] == columns * i + j + 1
