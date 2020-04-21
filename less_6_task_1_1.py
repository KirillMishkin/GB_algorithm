# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:37:55 2020

@author: mkv10
"""


"""
less_3_task_2
2. Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
"""

import random
import sys
from pympler import asizeof


def memory_func(mem):
    if type(mem) is tuple or type(mem) is list:
        return f'asizeof - {asizeof.asizeof(mem)}, sys - {sys.getsizeof(mem)}'  # для подсчета памяти tuple
    # sys показывает сам размер списка без его содержимого
    # asizeof показввает всю память вместе с содержимым списка
    return sys.getsizeof(mem)  # выводим размер если это int float str


def even_func(number):
    n_lst = tuple(random.randint(0, number * 2) for _ in range(number))
    # используем лист для хранения данных
    array_index_even = []
    for i, v in enumerate(n_lst):
        if v % 2 == 0:
            array_index_even.append(i)
    return print(f'Размер исходного кортежа {memory_func(n_lst)}\n'
                 f'Размер нового списка {memory_func(array_index_even)}\n'
                 f'Рамер переменной {memory_func(number)}')


number = 1000  # диапозон списка
even_func(number)

'''
Для хранения списка использовался кортеж , 
это самое оптимально испотльзование памяти для хранения статический объектов,
 которые в дальнейшем не планируются меняться. А вот для переменной с четными индексами 
 использовался список, туда и добавлялись все индексы , которые были найдены.
 самый оптимальный вариант из всех для хранения данных и дальнейшего его использования.
 Мой выбор Этот скрипт. Золотая серидина из всех. 
'''