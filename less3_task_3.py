"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

array = [random.randint(1, 20) for _ in range(10)]
print(array)
for i in range(1, len(array)):
    if array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]

print(array)
