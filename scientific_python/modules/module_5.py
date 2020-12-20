"""Exercices sur module_5.tables_multidimensionelles"""
import numpy as np

def creer_matrice(m, n):
    """Créez une fonction créer_matrice qui prend en entrée deux entiers m et n et qui renvoie un tableau Numpy de taille (m, n) composé de valeurs allant de 1 à 𝑚×𝑛."""

    return np.arange(1, m*n+1).reshape(m, n)

def modify():
    """Soit A un tableau en forme de cube de taille 3×3×3 rempli de 0

    Remplacez par des 1 toutes les valeurs placées à l'indice 0 de la dernière dimension
    Remplacez par 2 la valeur au milieu du cube
    Remplacez par 3 les valeurs placées à l'indice 2 de la première dimension en excluant les valeurs de l'indice 0 de la dernière dimension
    """

    matrix = np.zeros((3, 3, 3))
    matrix[2, :, :] = np.ones((3, 3)) * 3
    matrix[:, :, 0] = np.ones((3,3))
    matrix[1, 1, 1] = 2

def operations_on_axeis():
    """Multipliez A et b selon la 3ème dimension de A, puis ajoutez-y b selon la 2ème dimension, enfin soustrayez b au résultat selon la 1ère dimension. Affecté le résultat de cette opération à la variable R."""

    A = np.ones((3, 3, 3))
    b = np.array([1, 2, 3])

    return A * b[np.newaxis, np.newaxis, :] + b[np.newaxis, :, np.newaxis] - b[:, np.newaxis, np.newaxis]

def multiply_using_submatrixes():
    """Soit A une matrice 9x10 remplie de 1 définie dans le contexte de l'exercice. En utilisant la méthode du cours, modifiez la matrice A pour que celle-ci soit de la forme:

    array([
       [ 1.,  2.,  3.,  4.,  5.,  1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.,  6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15., 11., 12., 13., 14., 15.],
       [ 1.,  2.,  3.,  4.,  5.,  1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.,  6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15., 11., 12., 13., 14., 15.],
       [ 1.,  2.,  3.,  4.,  5.,  1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.,  6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15., 11., 12., 13., 14., 15.]
       ])
   """

    A = np.ones((9, 10))
    matrice3_5 = np.arange(1, 16).reshape(3, 5)

    return (A.reshape(3, 3, 2, 5) * matrice3_5[:, np.newaxis]).reshape(9, 10)

def rotate():
    """Soit matrice4_4 une matrice 4x4 remplie de valeurs allant de 1 à 16. En utilisant la méthode reshape de manière adaptée,
     découpez cette matrice en 4 sous-matrices 2x2, puis faites une rotation de 90° en utilisant rot90, puis ré-utilisez la méthode reshape pour remettre matrice4_4 sous la forme d'une matrice 4x4.

    En notant 𝐴, 𝐵, 𝐶 et 𝐷

    les 4 sous-matrices 2x2 de matrice4_4, voici la transformation attendue :

    (𝐴𝐷𝐵𝐶)⇒(𝐷𝐶𝐴𝐵)
    """
    matrice4_4 = np.arange(1, 17).reshape(4, 4)

    return np.rot90(m=matrice4_4.reshape(2, 2, 2, 2), k=1).reshape(4, 4)