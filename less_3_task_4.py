'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random

array = [random.randint(1, 5) for _ in range(10)]
top = 0  # Количество посторений цифры
num = 0  # Часто встречающаяся цифра
print(array)
for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            count += 1
    if count > top:
        top = count
        num = array[i]
print(f'Цифра {num} встречается {top} раз(а)')
