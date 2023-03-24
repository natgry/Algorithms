# not finished yet

def get_cons_str(input_data: list[str]) -> str:
    """
    Функция реализует задачу консенсуса DNA ридов-считалку.

    :param input_data: входные данные
    :return: консенсус-строку
    """
    if not input_data:
        raise ValueError

    result_str: str = None
    my_str = 'ACCC'

    def get_max(str_to_search):
        expected = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for elem in str_to_search:
            expected[elem] += 1
        letter_max_found = list(expected.keys())[list(expected.values()).index(max(expected.values()))]
        return letter_max_found

    str_to_check = None
    for i in range(0, len(input_data)):
        row = input_data[i]
        for j in range(0, len(row)):
            x = row[i]
            ...
           # str_to_check += row[i]
        get_max(str_to_check)
    x = str_to_check

    return result_str


if __name__ == '__main__':
    input_data = [
        'ATTA',
        'ACTA',
        'AGCA',
        'ACAA'
    ]
    print(get_cons_str(input_data))  # ACTA
