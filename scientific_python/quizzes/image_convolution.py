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


# image de test
test_image = numpy.array([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]).reshape(5, 5)

# noyau de test
noyau = numpy.array([1, 0, 1, 0, 1, 0, 1, 0, 1]).reshape(3, 3)

print(convoluer(noyau, test_image))
