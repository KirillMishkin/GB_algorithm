import random

size = 10
array = [random.randint(0, 10) for _ in range(size)]

print(*array)
num_nim = array[0]
num_max = 0
mid_sum = 0
for value in array:
    if value > num_max:
        num_max = value
    if value < num_nim:
        num_nim = value

for i in range(len(array)):
    if array[i] != num_max and array[i] != num_nim:
        mid_sum += array[i]
print(f'Минимальное число: {num_nim}\nМаксимальное число: {num_max}')
print(f'Сумма чисел между {num_nim} и {num_max} = {mid_sum}')

