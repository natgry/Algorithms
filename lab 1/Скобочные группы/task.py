def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    open_bracket = '('
    close_bracket = ')'
    if brackets_row.startswith(close_bracket):
        return False

    counter = 0
    for bracket in brackets_row:
        if bracket == open_bracket:
            counter += 1
        elif bracket == close_bracket:
            counter -= 1
    return counter == 0


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False

