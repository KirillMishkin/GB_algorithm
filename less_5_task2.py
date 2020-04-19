from collections import deque


def sum_hex(n, m, dict_hex: dict, lst_hex: list):
    """
    Функция возвращает сумму шестнадцатиричных чисел. Подсчет производитмся по правилам арифметики(в столбик).
    Под большим числом по количеству цифр находитмся меньшее число .Если длины чисел разные,
    то к меньшему по длине добавляется 0.
    Если число состоит из одной цифры,  то добавляется 0 к каждому числу, для правильного посчета.
    Если каждое число  например 5 и 5 , то првоеряется условие по наличию нулей по индексу 1,
    чтобы не допустить ошибку в подсчете и раньше закончить функцию.
    :param n: список первого числа
    :param m: список второго числа
    :param dict_hex: словарь с ключ значние по шестнадцатиричной системе
    :param lst_hex: лист для поиска значения по индексу шестнадцатиричной системе
    :return: возвращает раскрытый список через *.
    """
    if len(n) < len(m):
        n, m = m, n  # обмен  переменными , чтобы большее число по кол-ву цифр всегда было первое
        m.appendleft('0')
    elif len(n) > len(m):
        m.appendleft('0')
    elif len(n) == 1 and len(m) == 1:
        n.appendleft('0')
        m.appendleft('0')

    n.reverse()
    m.reverse()

    value = 0
    answer = deque([])
    for i, j in zip(n, m):
        digit = dict_hex[i] + dict_hex[j] + value
        if digit < 16:
            if n[1] == '0' and m[1] == '0':
                answer.appendleft(lst_hex[digit])
                return answer  # завершение функции если кажное число состоит  из 1 цифры и сумма меньше 16
            answer.appendleft(lst_hex[digit])
            value = 0
        elif digit >= 16:
            answer.appendleft(lst_hex[digit % 16])  # остаток от деления
            value = digit // 16  # число в уме
    return answer


def multi_hex(n_1, m_2, dict_hex: dict, lst_hex: list):
    """
    Функция возвращает список для сложения. Формат списка напримере A2 * C4F (79800,02880,0097E)
    Нули так же добавляеются для правильного сложения в функции sum_hex()

    :param n_1: список первого числа
    :param m_2: список второго числа
    :param dict_hex: словарь с ключ значние по шестнадцатиричной системе
    :param lst_hex:  лист для поиска значения по индексу шестнадцатиричной системе
    :return: возваращает напримере ([['7', '9', '8', '0', '0'], ['0', '2', '8', '8', '0'], ['0', '0', '9', '7', 'E']])
    """
    n_1.reverse()
    m_2.reverse()

    multi = ['0' for _ in range(len(n_1) + len(m_2))]  # список с 0,
    answer = deque([])
    dec = 1  # переменная для уменьшения основного индекса переменная (index)
    for i in m_2:
        value = 0  # число в умe
        index = (len(n_1) + len(m_2)) - dec  # основной  индекс для добавления переменной по этому индексу
        # уменьшается на 1
        # index(5)-dec(1) начинается отсчет индекса с конца. и при каждом проходе по for j  dec увеличивается на 1
        # index(5)-dec(2)
        # index(5) - dec(3) и т.д
        index_1 = 0  # переменная предназначен для добавления числа по индексу со здвигом.
        # Пример -  основной массив [0,0,0,0,0]. добавляем digit по индексу(index(4)-index_1(0))
        # index_1 +=1 увеличивается на 1 и обнуляется при выходе из цикла 'for j'
        # ['0', '0', '9', '7', 'E'] получаем на первом проходе по 'for j'
        for j in n_1:
            digit = dict_hex[i] * dict_hex[j] + value
            if digit < 16:
                multi[index - index_1] = lst_hex[digit]
                value = 0
            elif digit >= 16:
                multi[index - index_1] = lst_hex[digit % 16]
                value = digit // 16
            index_1 += 1 # сидвиг индекса на 1, обнуляется при выходе из for j
        multi[index - index_1] = str(value) # добавляем остаток в левую часть числа
        dec += 1
        answer.appendleft(multi.copy())
        multi.clear()
        multi = ['0' for _ in range(len(n_1) + len(m_2))]
    return answer


n_hex = deque(list(input().upper()))
m_hex = deque(list(input().upper()))

d_hex = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'A': 10,
         'B': 11,
         'C': 12,
         'D': 13,
         'E': 14,
         'F': 15}

l_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

answer_sum = sum_hex(n_hex.copy(), m_hex.copy(), d_hex, l_hex)
answer_multi = multi_hex(n_hex.copy(), m_hex.copy(), d_hex, l_hex)

zero_hex = answer_multi[-1]  # сохраняем последний список в переменную для дальнейшего сложения
for i in range(len(answer_multi) - 2, -1, -1):
    result = sum_hex(zero_hex, answer_multi[i], d_hex, l_hex)
    zero_hex = result

print(*answer_sum)
print(*zero_hex)
