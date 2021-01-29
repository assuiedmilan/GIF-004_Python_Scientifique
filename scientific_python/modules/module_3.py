"""Exercices sur module_3.scipy"""
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy import fft  # pylint: disable=no-name-in-module
from scipy import integrate
from scipy.linalg import lu_factor
from scipy.linalg import lu_solve


def solve_linear_equations(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve a linear system of equations

    Args:
        A (np.ndarray): Coefficients matrix
        b (np.ndarray): Second member vector

    Returns:
        The solution vector as an ndarray
    """

    lu, piv = lu_factor(A)
    return lu_solve((lu, piv), b)


def compute_pi() -> float:
    """
    Computes pi

    Returns:
        A float approximation of pi
    """

    return 4 * integrate.quad(lambda x: np.sqrt(1 - x ** 2), 0, 1)[0]


def afficher_tf(image_to_transform: np.ndarray):
    """
    Display image transform Fourier and filtered image

    Args:
        image_to_transform (mp.ndarray): Image

    Returns:
        None
    """

    image_fft = fft.fft2(image_to_transform)
    fft_shift = fft.fftshift(image_fft)
    fft_masked = create_square_mask(fft_shift, 80)

    magnitude_spectrum = 20 * np.log(np.abs(fft_masked))
    plt.imshow(magnitude_spectrum.astype(np.uint8))
    plt.show()

    img_filtre = fft.ifft2(fft_masked)
    img_filtre = np.absolute(img_filtre)
    plt.imshow(img_filtre, cmap="gray")
    plt.show()


def create_square_mask(image_to_mask: np.ndarray, length: int):
    """
    Create a square mask for this image

    Args:
        image_to_mask (np.ndarray): Image
        length (int): size of square

    Returns:
        Masked image
    """

    center = (math.floor(image_to_mask.shape[0] / 2), math.floor(image_to_mask.shape[1] / 2))
    delta = math.floor(length / 2)
    image_to_mask[center[0] - delta:center[0] + delta, center[1] - delta:center[1] + delta] = 0
    return image_to_mask
