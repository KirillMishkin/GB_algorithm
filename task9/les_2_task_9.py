"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

s = 0
num_max = 0
numbers = ''

n = int(input('Количесво цифр для сравнения: '))

for i in range(1, n + 1):
    x = int(input(f'Число {i}: '))
    dig_sum = 0
    x_1 = x
    while x_1 != 0:
        dig_sum += x_1 % 10
        x_1 //= 10
    if dig_sum > s:
        s = dig_sum
        num_max = x
    numbers += f'{x} '

print(f'Число {num_max} с наибольшей суммой цифр {s} ')

