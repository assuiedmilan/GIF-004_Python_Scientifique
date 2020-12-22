"""
    La deuxième étape de la compression JPEG consiste à utiliser la compression RLE (Run-Length Encoding) pour gagner un maximum d'espace.

    Cet algorithme consiste à représenter une chaîne de données en utilisant le nombre d'itérations successives d'un même élément plutôt qu'en le répétant 𝑛
    fois, c'est à dire qu'au lieu d'écrire AAA, on écrit 3A. Par exemple, en appliquant RLE à AAABCCCCCCCCCCDAAAADDDDDD, on obtient 3A1D10C1D4A6D.

    Nous avons vu précédemment que nous avons mis à 0 de nombreuses fréquences grâce à la quantification.
    Cela signifie que nos blocs 8x8 sont composés d'énormément de 0.
    Ainsi, si nous créons une séquence à partir des blocs 8x8 et que nous arrivons à avoir un maximum de 0 consécutif, l'encodage RLE nous permettra de gagner énormément de place.

    Pour se faire, nous allons transformer nos blocs 8x8 en vecteur de 64 de longueur, en lisant nos blocs en zigzag, puis nous allons appliquer l'encodage RLE à ce vecteur.

    Voici ceque vous devez faire:

        Écrire une fonction zigzag_vecteur qui prend en entrée un bloc 8×8 et renvoie le vecteur associé en faisant la lecture en zigzag.
         Pour vous faciliter votre tâche, nous défini dans le contexte de cet exercice les coordonnées successives d'une matrice 8×8 parcourue en zigzag.
        Écrire une fonction RLE_encodage qui prend en entrée le vecteur précédent, et qui renvoie l'encodage RLE associé.
         Cette fonction renverra une liste de tuples de la forme suivante&punsp;: [(3, 'A'), (1, 'B'), (10, 'C'), (1, 'D'), (4, 'A'), (6, 'D')].
         Vous pouvez utiliser itertools.groupby pour écrire cette fonction.

    Ainsi, en appelant zigzag_vecteur puis RLE_encodage, vous devriez obtenir le vecteur Numpy suivant:

    array([[-49.,   1.],
           [  1.,   2.],
           [  0.,   1.],
           [  3.,   1.],
           [  1.,   1.],
           [  0.,   7.],
           [ -1.,   1.],
           [  1.,   1.],
           [  0.,   1.],
           [ -1.,   3.],
           [  0.,   5.],
           [ -1.,   2.],
           [  0.,  38.]])
"""
import os
from itertools import groupby

import numpy as np


def zigzag_path(side_length: int) -> list[tuple[int, int]]:
    """Generate a zigzag path through a squared matrix, starting from the top left corner and ending at the bottom right corner

    Args:
        side_length (int): number of lines or columns of the matrix

    Returns:
        An array containing the path to move though the matrix in zig zag.
    """

    def go_downward_diag(from_line, from_column):
        while from_column != 0 and from_line != lines:
            from_column = from_column - 1
            from_line = from_line + 1
            add_to_path(from_line, from_column)

        return from_line, from_column

    def go_upward_diag(from_line, from_column):
        while from_line != 0 and from_column != columns:
            from_column = from_column + 1
            from_line = from_line - 1
            add_to_path(from_line, from_column)

        return from_line, from_column

    def go_left_once(from_line, from_column):
        from_column = from_column + 1
        add_to_path(from_line, from_column)

        return from_line, from_column

    def go_down_once(from_line, from_column):
        from_line = from_line + 1
        add_to_path(from_line, from_column)

        return from_line, from_column

    def add_to_path(l, c):
        path.append((l, c))

    lines = side_length - 1
    columns = side_length - 1

    path = [(0, 0), (0, 1)]
    line, column = path[-1]

    while line != lines or column != columns:

        if line != lines:
            line, column = go_downward_diag(line, column)

        if line != lines:
            line, column = go_down_once(line, column)
        elif column != columns:
            line, column = go_left_once(line, column)

        if column != columns:
            line, column = go_upward_diag(line, column)

        if column != columns:
            line, column = go_left_once(line, column)
        elif line != lines:
            line, column = go_down_once(line, column)

    return path


def zigzag_vecteur(image: np.ndarray) -> list[np.float64]:
    zigzag = zigzag_path(image.shape[0])
    values = [image[case] for case in zigzag]

    return values


def RLE_encodage(vector: list[np.float64]) -> np.ndarray:
    groups = groupby(vector, key=None)
    return np.asarray([(key, len(list(group))) for key, group in groups])


def do_stuff():
    im_dct_quant_block = np.load(os.path.join('..', '..', 'tests', 'resources', 'im_dct_quant_block.npy'))
    return RLE_encodage(zigzag_vecteur(im_dct_quant_block))


expected_value = np.array([[-49., 1.],
                           [1., 2.],
                           [0., 1.],
                           [3., 1.],
                           [1., 1.],
                           [0., 7.],
                           [-1., 1.],
                           [1., 1.],
                           [0., 1.],
                           [-1., 3.],
                           [0., 5.],
                           [-1., 2.],
                           [0., 38.]])

assert (do_stuff() == expected_value).all()
