from copy import copy

from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    result = []
    if container:
        container_ = copy(container)
        min_ = 0
        max_ = max(container_)
        helper = {x: 0 for x in range(min_, max_ + 1)}
        for elem in container_:
            helper[elem] += 1

        for elem, counter in helper.items():
            [result.append(elem) for _ in range(counter)]
    return result


if __name__ == '__main__':
    x = []
    print(sort(x))

    x = [1]
    print(sort(x))

    x = [3, 1, 2, 2]
    print(sort(x))

    x = [100, 101, 2, 3, 0, 100, 102, 1]
    print(sort(x))
