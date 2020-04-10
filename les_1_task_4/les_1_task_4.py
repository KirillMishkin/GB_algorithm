# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится
# букв.

n = input().lower()
m = input().lower()
abc = 'abcdefghijklmnopqrstuvwxyz'

letter_1 = abc.find(n) + 1
letter_2 = abc.find(m) + 1

slice_number = letter_2-letter_1-1

print(f'Место в алфавите {n} - {letter_1}\nМесто в алфивите {m} - {letter_2}')
print(f'Между буквой {n} и {m} находятся {slice_number} букв(ы)')
