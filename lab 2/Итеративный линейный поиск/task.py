"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if len(arr) == 0:
        raise ValueError  # TODO реализовать итеративный линейный поиск

    min_ = arr[0]
    pos = 0

    for index, value in enumerate(arr):
        if value < min_:
            min_ = value
            pos = index
    return pos
