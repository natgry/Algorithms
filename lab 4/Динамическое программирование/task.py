from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    table = []  # TODO решить задачу с помощью динамического программирования

    for i in range(n):
        list_ = [0] * m
        table.append(list_)

    for i in range(0, n):
        table[i][0] = 1
    for i in range(0, m):
        table[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1] + table[i - 1][j - 1]

    return table


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
    
    paths = car_paths(1, 1)
    print(paths[-1][-1])  # 1

    paths = car_paths(1, 2)
    print(paths[-1][-1])  # 1

    paths = car_paths(2, 2)
    print(paths[-1][-1])  # 3
