from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    # source - откуда начинаем движение, 0-я вершина
    # target- последняя ступень, куда мы должны прийти
    return nx.shortest_path_length(graph, source=0, target=len(graph)-1, weight='weight')  # число шагов до последней ступени лестницы


def create_stairway_graph(stairway: tuple[int]) -> nx.DiGraph:
    """
    Функция, которая формирует граф по стоимости ступеней.
    :param stairway: стоимость ступеней
    :return: взвешенный граф, nx.DiGraph
    """
    stairway_graph = nx.DiGraph()

    list_ = []
    len_ = len(stairway)
    last_step_to_go = len_ - 1
    for i in range(len_):
        list_.append((i, i + 1, stairway[i]))
        if i != last_step_to_go:
            list_.append((i, i + 2, stairway[i + 1]))

    stairway_graph.add_weighted_edges_from(list_)
    return stairway_graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    # построить граф
    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    stairway_graph = create_stairway_graph(stairway)

    # ручное создание взвешенного графа
    # stairway_graph.add_weighted_edges_from([
    #     (0, 1, 5),  # 5 - это цена ступени, 0 - это первая ступень
    #     (0, 2, 11),  # 11 - цена подняться на вторую ступень
    #     (1, 2, 11),
    #     (1, 3, 43),
    #     (2, 3, 43),
    #     (2, 4, 2),
    #     (3, 4, 2),
    #     (3, 5, 23),
    #     (4, 5, 23),
    #     (4, 6, 43),
    #     (5, 6, 43),
    #     (5, 7, 22),
    #     (6, 7, 22),
    #     (6, 8, 12),
    #     (7, 8, 12),
    #     (7, 9, 6),
    #     (8, 9, 6),
    #     (8, 10, 8),
    #     (9, 10, 8)  # 8 - 10я ступень. на кот-ю необходимо подняться
    # ])

    print(stairway_path(stairway_graph))  # 72
