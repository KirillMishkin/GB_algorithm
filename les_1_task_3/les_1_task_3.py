from random import randint, uniform

# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы
# диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.
x, y = (int(i) for i in input("Диапозон 'a' (через пробел) от и до: ").split())
if x > y:
    x, y = y, x
answer = randint(x, y)
print(answer)

a, b = (int(i) for i in input("Диапозон 'b' (через пробел) от и до: ").split())
answer = uniform(a, b)
print(answer)

m, n = (i for i in input("Диапозон 'c' (через пробел) от и до: ").split())
abc = 'abcdefghijklmnopqrstuvwxyz'
if m > n:
    m, n = n, m
index = randint(abc.find(m), abc.find(n))
print(abc[index])
