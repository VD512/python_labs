"""меняет строки и столбцы местами"""


def transpose(mat: list[list[float | int]]) -> list[list]:
    """если матрица нулевая - остается без изменений"""
    if len(mat) == 0:
        return mat
    len_line = len(mat[0])
    len_column = len(mat)
    """проверяю матрицу на прямоугольность"""
    for line in mat:
        if len(line) != len_line:
            return ValueError
    """создаю новую матрицу, меняя количество строк и столбцов"""
    new_mat = [[0 for x in range(len_column)] for y in range(len_line)]
    """добавляю в новую матрицу значения оригинальной"""
    for x in range(len_column):
        for y in range(len_line):
            new_mat[y][x] = mat[x][y]
    return new_mat


"""считает сумму по каждой строке"""


def row_sums(mat: list[list[float | int]]) -> list[float]:
    same_len = len(mat[0])
    sum_mat = []
    """проверяем матрицу на прямоугольность и записываю суммы строк в отдельный список"""
    for line in mat:
        if len(line) != same_len:
            return ValueError
        sum_mat.append(sum(line))
    return sum_mat


"""считает сумму по каждому столбцу"""


def col_sums(mat: list[list[float | int]]) -> list[float]:
    same_len = len(mat[0])
    sum_mat = [0] * same_len
    """проверяем матрицу на прямоугольность"""
    for line in mat:
        if len(line) != same_len:
            return ValueError
    """суммирую элементы по столбцам и записываю суммы в отдельный список"""
    for x in range(same_len):
        for y in range(len(mat)):
            sum_mat[x] += mat[y][x]
    return sum_mat
