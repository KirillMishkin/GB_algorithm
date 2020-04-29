# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import shuffle
import time


def dfs(vertex, graph, used):
    """
    Рекурсиваня функция dfs
    функция показывает как работате граф
    in: точка входа
    out: точка выхода
    :param vertex: вершина графа
    :param graph: созданный граф
    :param used: переменная хранит использованные вершины.
    :return:
    """
    used.add(vertex)
    print(f'in: {vertex}')
    time.sleep(0.5)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)
    print(f'out:{vertex}')
    time.sleep(0.5)


def G_2(count: int):
    """

    Функция генерирует вершины графа от 1 - 99 в рандомной порядке. Заполнение списка смежности производится в ручную.
    Будет вызываться строка с название вершины и предложением ввести смежную ей вершину.
    Если смежных вершин больше нет, то введите stop и перейтиде к заполнения новой вершины.
    При ошибке ввода, будет предложено еще раз ввести название вершины.
    :param count: количество вершин
    :return: возвращает грас словарьсписка смежности
    """
    name_vertex = [i for i in range(1, 100)]
    shuffle(name_vertex)
    graph_2 = {i: set() for i in name_vertex[:count + 1]}
    print(f'Доступыне вершины {[i for i in graph_2]}')
    for vertex in graph_2:
        while True:
            edge = input(f'Вершина {vertex} соеденена с - ').upper()
            if edge == 'STOP' or edge == '"STOP"':
                break
            while int(edge) not in graph_2:
                edge = input(f'ОШИБКА!!! Вершины не существует\nДоступные вершины {[i for i in graph_2]} '
                             f'посторите ввод - ')
            graph_2[vertex].add(int(edge))
    return graph_2


def G(count: int):
    """Функция генерирует вершины графа от A - Z . Заполнение списка смежности производится в ручную.
    Будет вызываться строка с название вершины и предложением ввести смежную ей вершину.
    Если смежных вершин больше нет, то введите stop и перейтиде к заполнения новой вершины.
    при ошибке ввода, будет предложено еще раз ввести название вершины.

    :param count: количество вершин
    :return: возвращает свловарь со списком смежности вершин
    """

    graph = {chr(i).upper(): set() for i in range(65, 65 + count)}
    print(f'Доступные вершины {[chr(i) for i in range(65, 65 + count)]}\nВведите "stop" для завершения ввода вершин ')
    for vertex in graph:
        while True:
            ed = input(f'Вершина {vertex} соеденена с - ').upper()
            if ed == 'STOP' or ed == '"STOP"':
                break
            while ed not in graph:
                ed = input(
                    f'ОШИБКА!!!\nВершины не существует\nДоступные вершины {[chr(i) for i in range(65, 65 + count)]} повторите ввод - ').upper()
            graph[vertex].add(ed)
    return graph


print("Как обозначить вершины?")
choice = input('1 - вершины как числа, А - вершины как буквы - ').upper()
while True:
    if choice == 'A' or choice == 'А':
        number = int(input('Введите количество вершин от 2 до 26 - '))
        graph = G(number)
        break
    elif choice == '1':
        number = int(input('Введите количество вершин от 2 до 99 - '))
        graph = G_2(number)
        break
    choice = input('ОШИБКА!!!\n1 - вершины как числа, А - вершины как буквы - ').upper()

used = set()
N = 0  # компоненты связанности
for vertex in graph:
    if vertex not in used:
        dfs(vertex, graph, used)
        N += 1

print(f'\nКомпонентов связанности {N}')
