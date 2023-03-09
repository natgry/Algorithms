def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError

    if not isinstance(n, int):
        raise TypeError

    if n == 0:
        return 1  # TODO реализовать итеративный алгоритм нахождения факториала

    result = 1
    for value in range(1, n + 1):
        result *= value

    return result
