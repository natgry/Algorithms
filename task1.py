def last_person(n: int, k: int) -> int:
    """
    Функция реализует игру-считалку.

    :param n: количество человек
    :param k: количество слогов
    :return: номер последнего оставшегося человека
    """
    if n == 0:
        raise ValueError
    if k == 0:
        raise ValueError

    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError

    list_ = [ndx for ndx in range(1, n + 1)]
    if len(list_) == 1:
        return list_[0]

    while len(list_) > 1:
        index = k % len(list_) - 1
        list_.pop(index)

        left_border = list_[index:]
        right_border = list_[:index]
        if index != -1:
            list_ = left_border + right_border

    return list_[0]


if __name__ == '__main__':
    print(last_person(5, 6))  # 4

    print(last_person(5, 1))  # 5

    print(last_person(5, 2))  # 3

    print(last_person(5, 3))  # 4

    print(last_person(1, 1))  # 1

    # checks for errors
    # print(last_person(0, '1'))  # value error
    # print(last_person(1, '1'))  # type error
    # print(last_person(1, 0))  # value error
    # print(last_person('1', 1))  # type error

