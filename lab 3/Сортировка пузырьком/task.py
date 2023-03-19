from copy import copy
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    container_ = copy(container)
    last_sorted_index = len(container_) - 1
    sorted = True
    while sorted:
        index = 0
        sorted_index = 0
        sorted = False
        while index < last_sorted_index:
            if container_[index] > container_[index + 1]:
                container_[index], container_[index + 1] = \
                    container_[index + 1], container_[index]
                sorted = True
                sorted_index = index
            index += 1
        last_sorted_index = sorted_index

    return container_


if __name__ == '__main__':
    x = [1, 2, 3]
    print(sort(x))

    x = [100, 101, 2, 3, 0, 100, 102, -1]
    print(sort(x))

    x = [1]
    print(sort(x))

    x = []
    print(sort(x))
