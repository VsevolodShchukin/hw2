"""Проект по расчету количества лунных кратеров."""
import typing

matrix: typing.List = []
craters = 0


def search_crater(row: int, index: int) -> bool:
    """Функция, которая проверяет значение в матрице на соответствие условиям кратера."""
    global matrix
    index_count = len(matrix[0])
    row_count = len(matrix)

    if row == row_count or row < 0:
        return False
    if index == index_count or index < 0:
        return False

    if matrix[row][index] == 1:
        matrix[row][index] = 0
        search_crater(row, index + 1)
        search_crater(row + 1, index)
        search_crater(row, index - 1)
        search_crater(row - 1, index)
        return True
    return False


def calculate(matrix: list) -> int:
    """Функция, которая отбирает 1 значение из матрицы для проверки на совпадение с условиями для кратера."""
    global craters
    for row in range(len(matrix)):
        for index in range(len(matrix[row])):
            if search_crater(row, index):
                craters = craters + 1
    print(craters)
    return craters


with open("craters.txt", "r") as file:
    for line in file:
        matrix.append(list(map(lambda x: int(x), list(line.strip()))))
    print(matrix)

calculate(matrix)
