"""
5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""

import random

size = 10
array = [random.randint(-100, -1) for _ in range(size)]

num_index = 0
num_max = array[0]  # В переменную кладем значение по индексу 0
print(*array)

for i, value in enumerate(array):
    if value > num_max:
        num_max = value
        num_index = i
print(num_max, num_index)
