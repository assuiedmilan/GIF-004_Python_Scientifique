import wget
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# copier la joconde dans votre dossier Jupyter
filename = wget.download('https://python.gel.ulaval.ca/media/notebook/joconde.jpg')

im = np.array(Image.open("joconde.jpg").convert('L'), dtype=np.int16)
im = im - 128  # on centre entre -128 et 127

Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

plt.imshow(im)
plt.show()


def afficher_transformée(img_dct, img_dct_quant, w, h):
    """
    Permet d'afficher la transformée en cosinus
    Args:
       img_dct (matrice numpy): matrice de la transformée en cosinus à 4 dimensions AVANT la quantification
       img_dct_quant (matrice numpy): matrice de la transformée en cosinus à 4 dimensions APRES la quantification
       w (int): largeur de l'image
       h (int): hauteur de l'image
    """

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Image reconstituée avec les transformées en cosinus')
    ax1.imshow(img_dct.reshape(w, h), vmax=np.max(im_dct) * 0.01, vmin=0)
    ax1.set_title("Avant la quantification")
    ax2.imshow(im_dct_quant.reshape(w, h), vmax=np.max(im_dct_quant) * 0.01, vmin=0)
    ax2.set_title("Après la quantification")

    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Bloc 8x8 de la transformée en cosinus')
    ax1.imshow(img_dct[29, :, 20, :], vmax=np.max(im_dct) * 0.01, vmin=0)
    ax1.set_title("Avant la quantification")
    ax2.imshow(img_dct_quant[29, :, 20, :], vmax=np.max(im_dct_quant) * 0.01, vmin=0)
    ax2.set_title("Après la quantification")

    plt.show()

from scipy.fftpack import dctn


def remove_right_and_bottom_borders(image_to_cut, target_shape):
    """Cut the image into a matrix of the specified shape"""
    image_shape = image_to_cut.shape
    lines_to_remove = image_shape[0] % target_shape[0]
    columns_to_remove = image_shape[1] % target_shape[1]

    return image_to_cut[:- lines_to_remove, :-columns_to_remove]


def cut_into_sub_matrixes(image_to_cut, target_shape):
    """Divide the matrix in blocks of the specified size"""

    image_shape = image_to_cut.shape

    if image_shape[0] % target_shape[0] != 0 or image_shape[1] % target_shape[1] != 0:
        raise AssertionError("Image must be divisible, image shape is {}, shape to divide by is {}".format(image_shape, target_shape))

    return image_to_cut.reshape(image_shape[0] // target_shape[0], target_shape[0],
                                image_shape[1] // target_shape[1], target_shape[1])


def apply_cosine_discrete_transform(image_to_transform):
    return dctn(image_to_transform, axes=[1, 3], norm='ortho')


def quantify(image_to_transform, quantifier):
    quantifier_reshaped = quantifier[np.newaxis, :, np.newaxis, :]
    return np.rint(image_to_transform/quantifier_reshaped)


target_shape = (8, 8)
im_cut = remove_right_and_bottom_borders(im, target_shape)
im_divided = cut_into_sub_matrixes(im_cut, target_shape)
im_dct = apply_cosine_discrete_transform(im_divided)
im_dct_quant = quantify(im_dct, Q)
h = im_cut.shape[0]
w = im_cut.shape[1]
afficher_transformée(im_dct, im_dct_quant, w, h)