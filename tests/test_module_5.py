import pytest

from scientific_python.modules.module_5 import creer_matrice


@pytest.mark.parametrize("m, n",[(3, 3), (1, 1), (4, 6), (7, 5)])
def test_créer_matrice(m , n):
    matrix = creer_matrice(m, n)

    assert matrix.shape == (m, n)

    for i in range(m):
        for j in range(n):
            assert matrix[i, j] == n * i + j + 1
