"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = [[0 for i in range(5)] for _ in range(4)]

for index, line in enumerate(matrix):
    print(f'Строка {index + 1}')
    s = 0
    for i, v in enumerate(line):
        if i == len(line) - 1:
            line[i] = f'| {s}'
            break
        n = int(input())
        s += n

        line[i] = n

for line in matrix:
    for i in line:
        print(f'{i:<3}', end='')
    print()
