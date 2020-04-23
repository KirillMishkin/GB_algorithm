'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданыный случайнми числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random


def m_s(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    m_s(L)
    m_s(R)
    new_lst = merge(L, R)
    for i in range(len(new_lst)):
        A[i] = new_lst[i]
    return A


def merge(A: list, B: list):
    new_sort_lst = [0] * (len(A) + len(B))
    i = 0  # Индекс для А
    j = 0  # Индекс для B
    k = 0  # Индекс для new_sort_lst
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            new_sort_lst[k] = A[i]
            i += 1
            k += 1
        else:
            new_sort_lst[k] = B[j]
            j += 1
            k += 1
    while i < len(A):
        new_sort_lst[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        new_sort_lst[k] = B[j]
        j += 1
        k += 1
    return new_sort_lst


size = 50
array = [i for i in range(size)]
random.shuffle(array)
print(array)
print(m_s(array))
