# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
operator = input('Битовый сдвиг << or >>: ').lower()
if operator == 'left' or operator == '<<':
    answer = a << 2
elif operator == 'right' or operator == '>>':
    answer = a >> 2
else:
    answer = 'Error'
print(answer)
