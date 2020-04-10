# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
x = 5
y = 6

operator = input('Битовая операция "and" "or" "xor" "not": ').lower()
if operator == 'and' or operator == '&':
    answer = x & y
    print(answer)
elif operator == 'or' or operator == '|':
    answer = x | y
    print(answer)
elif operator == 'xor' or operator == '^':
    answer = x ^ y
    print(answer)

elif operator == 'not' or operator == '~':
    answer = f'{~x} {~y}'
    print(answer)
else:
    answer = 'Error'
    print(answer)

