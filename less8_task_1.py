from collections import deque

"""
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.

По условию задачи можно понять, что количество друзей это N вершин графа .
 В условие сказано, что каждый друг жмет руку всем остальным друзьям, из этого можно сделать вывод:
 1) Граф является полным. так как рукоможатие можно посчитать за ребро. И все друзья жмут руки друг другу.
 Следовательно все ребра соеденены.
  Но в тоже время можно посчтиать их направлены , нет смысла друзьям здороваться друг с другом еще раз
"""


def hello_friend(name_friends: list):
    hello = {}
    searched = set()  # Тут храним друзей которых уже проверили
    for name in name_friends:  # Перебираем друзей берем вршину vertex и смотрим кто с ней связан
        search_hi = deque(name_friends)  # Создаем очередь из друзей
        while search_hi:  # Пока очередь не пустая цикл работает
            person = search_hi.popleft()  # Берем друга из очереди
            if name != person:  # если имя друга равно его имени ,
                # То он сам с собой не здоровается
                if person not in searched:  # проверяем есть ли этот друг в списке првоеренных
                    if name not in hello:  # классическое создание словаря
                        hello[name] = {person}
                        searched.add(name)
                    else:
                        hello[name].add(person)
    else:
        hello[name_friends[-1]] = set()  # Добавляем последнего дргуа с словарь , показывая что с ним все поздоровались
    return hello


N = int(input("Введите количество друзей(от 2 до 26): "))
while  N > 26 or N <=1:
    N = int(input("\nВведите количество друзей: "))
A = [[0] * N for _ in range(N)]  # Список для матрицы сжежности
B = [[0] * N for _ in range(N)]  # Список для матрицы сжежности
list_friends_vertex = [chr(i).upper() for i in range(65, 65 + N)]  # Друзья по названия
list_friends_vertex_index = [list_friends_vertex.index(i) for i in list_friends_vertex]  # Друзья по индексам

print(f'Наши друзья : {list_friends_vertex}\n')

dict_friends_vertex = {list_friends_vertex[i]: set() for i in list_friends_vertex_index}  # Словарь друзей по имени
dict_friends_vertex_index = {i: set() for i in list_friends_vertex_index}  # Словарь друзей по индексу

for i, v in enumerate(list_friends_vertex):
    for j in range(N):
        if i != j:
            dict_friends_vertex[v].add(list_friends_vertex[j])
            dict_friends_vertex_index[i].add(j)

for k, v in dict_friends_vertex.items():
    print(f'Друг {k} должен поздороваться с {v}')

for i in range(N):
    for j in dict_friends_vertex_index[i]:  # Матрица смежности
        B[i][j] = 1
print()
print('Матрица смежности графа : \n')
for i in list_friends_vertex:
    print(f'\t{i}', end='')

print()

for line in range(len(B)):
    print(f'{list_friends_vertex[line]} | ', end='')
    for i in B[line]:
        print(f'{i:<4}', end='')
    print()
print()

for k, v in hello_friend(list_friends_vertex).items():
    if v != set():
        print(f'Друг {k} поздоровался с {v}')
    else:
        print(f'С другом {k} все поздоровались ')

for i in range(N):
    for j in hello_friend(list_friends_vertex_index)[i]:  # Матрица смежности
        A[i][j] = 1

print()

print('Матрица смежности ориентированного графа : \n')
for i in list_friends_vertex:
    print(f'\t{i}', end='')

print()

for line in range(len(A)):
    print(f'{list_friends_vertex[line]} | ', end='')
    for i in A[line]:
        print(f'{i:<4}', end='')
    print()

print(f'\nВсего рукопожатий {N * (N - 1) // 2}')
