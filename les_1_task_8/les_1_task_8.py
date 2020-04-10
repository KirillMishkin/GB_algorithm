#  Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Число a: '))
b = int(input('Число b: '))
c = int(input('Число c: '))

if a < b < c:
    answer = 'b'
elif b < a < c:
    answer = 'a'
elif a < c < b:
    answer = 'c'
else:
    answer = 'Error'
if answer != 'Error':
    print(f'Среднее число {answer}')
else:
    print('Нет среднего числа')
