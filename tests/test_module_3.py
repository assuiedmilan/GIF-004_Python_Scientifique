"""Tests for module 3"""

import math
import os

import numpy as np
from PIL import Image

from scientific_python.modules.module_3 import afficher_tf
from scientific_python.modules.module_3 import compute_pi
from scientific_python.modules.module_3 import solve_linear_equations


def test_solve_linear_equations():
    """Test linear equations solver"""

    expected_value = np.array([3., 5., 8.])
    A = np.array([[2, 3, 4], [3, 5, -4], [4, 7, -2]])
    b = np.array([53, 2, 31])

    assert (solve_linear_equations(A, b) == expected_value).all()


def test_pi():
    """Test pi value"""

    assert round(compute_pi(), 10) == round(math.pi, 10)


def test_filter_image():
    """Test image filtration"""

    filename = os.path.join(os.path.dirname(__file__), 'resources', 'joconde.jpg')
    image = np.array(Image.open(filename).convert('L'))
    afficher_tf(image)
