"""
Une image est simplement une grande matrice de pixels.
Pour filtrer une image (avec par exemple les filtres contenus dans photoshop), il s'agit essentiellement de convoluer l'image avec un noyau (parfois avec plusieurs),
 c'est-à-dire avec de petites matrices de coefficients qui viennent pondérer les valeurs de chaque pixel en effectuant une combinaison linéaire de ceux qui sont adjacents.
De cette manière, par exemple, on peut rendre une image plus floue ou, au contraire, la rendre plus contrastée. Tout dépend des coefficients du noyau utilisé par la convolution.

Dans le contexte d'une image possédant 𝑚 lignes et 𝑛 colonnes, donc une matrice 𝑚×𝑛, et d'un noyau 𝐾 de dimensions 𝑜×𝑝, la convolution 𝐼∗=𝐾∗𝐼 du noyau 𝐾 par l'image 𝐼
 est donnée par la formule suivante pour chacun des pixels (𝑖,𝑗) de l'image résultante:

    𝐼∗(𝑖,𝑗)=∑𝑘=−𝑎𝑎∑𝑙=−𝑏𝑏𝐾(𝑎+𝑘,𝑏+𝑙)×𝐼(𝑖+𝑘,𝑗+𝑙),  pour  𝑎≤𝑖≤𝑚−𝑎−1  et  −𝑏≤𝑗≤𝑛−𝑏−1
    où (𝑎,𝑏)=(⌊𝑜/2⌋,⌊𝑝/2⌋) correspond à la coordonnée du centre du noyau, avec la notation ⌊𝑥⌋ désignant le plus grand entier plus petit ou égal à 𝑥

    (la division entière qui tronque la partie fractionnaire). On suppose ici que les dimensions d'un noyau sont toujours impaires.

On vous demande de coder une fonction nommée convoluer qui accepte en argument:

    Un noyau de convolution 𝐾
    Une image à convoluer 𝐼

tous les deux sous la forme d'un tableau numpy à deux dimensions (voir leçon 12.1),
 et de retourner en sortie l'image résultante sous la forme d'un autre tableau numpy de la même dimension que l'image d'entrée,
mais en comblant le pourtour avec des zéros.

En utilisant des énoncés assert, assurez-vous dans votre fonction que les arguments reçus sont bien des instances de tableaux numpy (classe ndarray; utiliser la fonction isinstance)
 et que les dimensions du noyau sont bien impaires.

Indices - Pour résoudre ce problème:

    Déterminer les valeurs de 𝑎 et 𝑏 à partir des dimensions du noyau (attribut shape).
    Initialiser une matrice résultat remplie de zéros (fonction zeros), de la même taille que l'image d'entrée.
    Pour chaque ligne 𝑖∈[𝑎,𝑚−𝑎[:
        Et pour chaque colonne 𝑗∈[𝑏,𝑛−𝑏[:
            Découper dans l'image d'entrée l'empreinte du noyau en utilisant l'opérateur [] de ndarray.
            Multiplier le noyau par son empreinte dans l'image en utilisant l'opérateur * de ndarray.
            Calculer la somme des résultats de la multiplication en utilisant la méthode ndarray.sum.
    Retourner la matrice résultat.

Notez que ces étapes sont très simples et courtes si vous profitez bien des fonctionnalités de numpy.
"""

import numpy


def __validate_table_is_ndarray(table):
    assert isinstance(table, numpy.ndarray)


def __validate_core_size(table):
    assert all([x % 2 != 0 for x in table.shape])


def __compute_convolution_boundaries(table):
    return tuple([x // 2 for x in table.shape])


def __initialize_empty_matrix(table):
    return numpy.zeros(table.shape)


def __process_convolved_value(core, image, line, column, a, b):
    sub_table = image[line - a:line + a + 1, column - b:column + b + 1]
    core_print = core * sub_table
    return numpy.ndarray.sum(core_print)


def convoluer(core, image):
    __validate_table_is_ndarray(core)
    __validate_table_is_ndarray(image)
    __validate_core_size(core)

    result = __initialize_empty_matrix(image)

    (a, b) = __compute_convolution_boundaries(core)
    (m, n) = image.shape

    for i in range(a, m - a):
        for j in range(b, n - b):
            result[i, j] = __process_convolved_value(core, image, i, j, a, b)

    return result
