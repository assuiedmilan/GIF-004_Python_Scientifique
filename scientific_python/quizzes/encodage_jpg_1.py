"""
JPEG est une norme permettant de compresser des images.
Cette norme exploite la faible sensibilité de l'oeil humain à la chrominance et s'en sert pour réduire la taille des images sans trop affecter leur perception humaine.
Nous allons simplifier ici au maximum les explications, pour plus de détails, nous vous invitons à lire la page suivante.

Ce Quiz porte sur la première partie de l'encodage JPEG, c'est-à-dire la phase de compression.
Cette première étape est celle qui permet de réduire considérablement la taille de l'image au détriment d'une certaine perte de netteté.

La compression JPEG consiste à diviser une image en petits blocs de 8x8 pixels, et d'appliquer dans chacun de ces blocs la transformée en cosinus discrète (DCT),
 qui est une alternative de la transformée de Fourier.
Ce changement dans le domaine fréquentiel permet de filtrer les hautes fréquences (correspondant à des changements brusques d'intensité dans l'image) qui sont moins visibles par l'oeil humain.
Pour se faire, nous utilisons une des propriétés de la transformée utilisée:
 l'amplitude des basses fréquences sera enregistrée en haut à gauche des blocs 8x8, et les hautes fréquences en bas à droite.
Ainsi, il nous suffit de diviser chacun des blocs de notre image en une matrice 𝑄

8x8 pour atténuer les fréquences voulues (cette étape s'appelle la quantification).

Dans le contexte du Quiz, nous vous donnons une image nommée im transformée en niveau de gris ainsi que la matrice Q.

Voici ce que vous devez faire:

    Pour simplifier l'exercice, nous allons ignorer les bordures à droite et en bas de notre image pour avoir un nombre de lignes et de colonnes qui sont un multiple de 8.
        Pour ce faire, il suffit de découper l'image (tableau Numpy) pour enlever ces bordures. Par exemple, si l'image est de taille 41x33, vous devez la découper en une image 40x32.
    Redimensionnez l'image à l'aide de numpy.reshape afin d'avoir un tableau à quatre dimensions (ℎ,8,𝑤,8) de ℎ×𝑤 blocs de 8×8 pixels. Enregistrez le résultat dans la matrice im_divided.

Appliquez la transformée en cosinus à l'aide de scipy.fftpack.dctn sur les axes 1 et 3 de votre matrice redimensionnée, en utilisant la norme 'ortho'. Enregistrez le résultat dans im_dct.
Divisez chacun des blocs 8×8 par la matrice Q en arrondissant chacun des coefficients avec numpy.rint. Enregistrez le résultat dans la matrice im_dct_quant.
"""

import os
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.fftpack import dctn

Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])


def load_and_center(image: str) -> np.ndarray:
    """Load an image and return it centered

    Args:
        image (str) : Path to the image

    Returns:
        The centered image
    """

    image_to_center = np.array(Image.open(image).convert('L'), dtype=np.int16)
    return image_to_center - 128


def afficher_transformée(img_dct: np.ndarray, img_dct_quant: np.ndarray, width: int, height: int):
    """Display the cosine transform of the image

    Args:
       img_dct (np.ndarray): 4-D cosine transform of the image before quantification
       img_dct_quant (np.ndarray): 4-D cosine transform of the image after quantification
       width (int): image width
       height (int): image height

    Returns:
       None
    """

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Image reconstituée avec les transformées en cosinus')
    ax1.imshow(img_dct.reshape(width, height), vmax=np.max(im_dct) * 0.01, vmin=0)
    ax1.set_title("Avant la quantification")
    ax2.imshow(im_dct_quant.reshape(width, height), vmax=np.max(im_dct_quant) * 0.01, vmin=0)
    ax2.set_title("Après la quantification")

    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Bloc 8x8 de la transformée en cosinus')
    ax1.imshow(img_dct[29, :, 20, :], vmax=np.max(im_dct) * 0.01, vmin=0)
    ax1.set_title("Avant la quantification")
    ax2.imshow(img_dct_quant[29, :, 20, :], vmax=np.max(im_dct_quant) * 0.01, vmin=0)
    ax2.set_title("Après la quantification")

    plt.show()


def remove_right_and_bottom_borders(image_to_cut: np.ndarray, target_shape: Tuple[int, int]) -> np.ndarray:
    """Cut the image into a matrix of the specified shape

    Args:
        image_to_cut (np.ndarray): The image to cut
        target_shape (Tuple[int, int]): The image shape after it's cut

    Returns:
        The image without it's right and bottom borders
    """

    image_shape = image_to_cut.shape
    lines_to_remove = image_shape[0] % target_shape[0]
    columns_to_remove = image_shape[1] % target_shape[1]

    return image_to_cut[:- lines_to_remove, :-columns_to_remove]


def cut_into_sub_matrices(image_to_cut: np.ndarray, target_shape: Tuple[int, int]) -> np.ndarray:
    """Divide the matrix in blocks of the specified size

    Args:
        image_to_cut (np.ndarray): The image to cut
        target_shape (Tuple[int, int]): Shape of the sub matrices

    Returns:
        The image reshaped as sub matrices of the specified size.
    """

    image_shape = image_to_cut.shape

    if image_shape[0] % target_shape[0] != 0 or image_shape[1] % target_shape[1] != 0:
        raise AssertionError("Image must be divisible, image shape is {}, shape to divide by is {}".format(image_shape, target_shape))

    # noinspection PyArgumentList
    return image_to_cut.reshape(image_shape[0] // target_shape[0], target_shape[0], image_shape[1] // target_shape[1], target_shape[1])


def apply_cosine_discrete_transform(image_to_transform: np.ndarray) -> np.ndarray:
    """Compute a cosine discrete transform over the provided image

    Args:
        image_to_transform (np.ndarray): The image that will undergo a cosine discrete transform

    Returns:
        The discrete cosine transform
    """
    return dctn(image_to_transform, axes=[1, 3], norm='ortho')


def quantify(image_to_transform: np.ndarray, quantifier: np.ndarray) -> np.ndarray:
    """Quantify the image

    Args:
        image_to_transform (np.ndarray): Image to quantify
        quantifier (np.ndarray): The quantifier

    Returns:
        The quantified image
    """

    quantifier_reshaped = quantifier[np.newaxis, :, np.newaxis, :]
    return np.rint(image_to_transform / quantifier_reshaped)


im = load_and_center(os.path.join('..', '..', 'tests', 'resources', 'Joconde.jpg'))

plt.imshow(im)
plt.show()

image_shape_target = (8, 8)
im_cut = remove_right_and_bottom_borders(im, image_shape_target)
im_divided = cut_into_sub_matrices(im_cut, image_shape_target)
im_dct = apply_cosine_discrete_transform(im_divided)
im_dct_quant = quantify(im_dct, Q)

afficher_transformée(im_dct, im_dct_quant, im_cut.shape[0], im_cut.shape[1])
