"""
7. В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random

size = 10
array = [random.randint(0, 10) for _ in range(size)]


lst_min = []

print(*array)

while len(lst_min) != 2:
    num_min = array[0]
    for i in array[:]:
        if i < num_min:
            num_min = i
    array.remove(num_min)
    lst_min.append(num_min)

print('Минимальные числа в массиве: ', *lst_min)
