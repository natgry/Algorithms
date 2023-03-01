"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list

        TODO Описать где начало и конец очереди
        index 0 - начало очереди
        index -1 - конец очереди
        """
        self.queue = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди.
        O(1) для случая, когда index 0  - начало очереди

        :param elem: Элемент, который должен быть добавлен
        """

        self.queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди. O(N)

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError("Очередь пуста")
        else:
            elem = self.queue[0]
            del self.queue[0]
            return elem  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        O(1)
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целочисленного типа")

        if len(self.queue) <= ind < 0:
            return IndexError("Индекс вне границ очереди")
        return self.queue[ind]  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. O(1)"""
        self.queue.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. O(1)"""
        return len(self.queue)  # TODO реализовать метод __len__
