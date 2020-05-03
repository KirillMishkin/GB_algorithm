""""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
считается не решённой.
"""


def search_str(n: str) -> dict:
    d_str = {}
    assert len(n) > 0, "Строка нулевая"
    found = set()
    my_str = n.split()
    for subs in my_str:
        len_subs = len(subs)
        for i in range(len(n) - len(subs) + 1):
            if subs == n[i:i + len_subs] and i not in found:
                if n[i:i + len_subs] == subs:
                    found.add(i)
                    if subs not in d_str:
                        d_str[subs] = [i]
                    else:
                        d_str[subs].append(i)
    return d_str


print('Использовать шаблон ? 1 - да, 2 - нет, введу строку самостоятельно')
choice = int(input('---> '))
while True:
    if choice == 1:
        with open('text', 'r', encoding='utf-8') as data:
            data = data.read().strip()
            print(data)
            print()
            answer = search_str(data)
        break
    elif choice == 2:
        my_str = input('Введите вашу строку: ')
        answer = search_str(my_str)
        break
    choice = int(input('Error\nИспользовать шаблон ? 1 - да, 2 - нет, введу строку самостоятельно'))

for k, v in answer.items():
    print(f'Подстрока {k} начинается с индексов {v}')
