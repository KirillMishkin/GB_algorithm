'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

matrix = [[random.randint(0, 10) for _ in range(5)] for _ in range(5)]
column_min = list(matrix[0])


for line in matrix:
    for index, value in enumerate(line):
        if column_min[index] > value:
            column_min[index] = value
        print(f'{value:<4}', end="")
    print()

num_max = 0
print()
for i in column_min:
    if i > num_max:
        num_max = i
    print(f'{i:<4}', end='')

print(f'\nМаксимальный элемент  {num_max}')
