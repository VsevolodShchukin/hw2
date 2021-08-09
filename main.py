"""Проект по расчету количества лунных кратеров."""


def search_crater(matrix: list, row: int, index: int) -> bool:
    """Функция, которая проверяет значение в матрице на соответствие условиям кратера."""
    index_count = len(matrix[0])
    row_count = len(matrix)

    if row == row_count or row < 0:
        return False
    if index == index_count or index < 0:
        return False

    if matrix[row][index] == 1:
        matrix[row][index] = 0
        search_crater(matrix, row, index + 1)
        search_crater(matrix, row + 1, index)
        search_crater(matrix, row, index - 1)
        search_crater(matrix, row - 1, index)
        return True
    return False


def calculate(matrix: list) -> int:
    """Функция, которая отбирает 1 значение из матрицы для проверки на совпадение с условиями для кратера."""
    craters = 0
    for row in range(len(matrix)):
        for index in range(len(matrix[row])):
            if search_crater(matrix, row, index):
                craters = craters + 1
    print(craters)
    return craters


def main(file_name: str) -> int:
    """Функция, открывающая файл и преобразующая его в матрицу."""
    with open(file_name, "r") as file:
        matrix = []
        for line in file:
            matrix.append(list(map(lambda x: int(x), list(line.strip()))))
        print(matrix)
        return calculate(matrix)


if __name__ == "__main__":
    main("craters.txt")
