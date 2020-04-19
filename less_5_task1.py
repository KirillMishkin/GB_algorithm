from collections import ChainMap, OrderedDict

count = int(input('Введите количество предприятий: '))
d = {}
d_mid_profit = {}
all_profit = 0
for _ in range(count):
    company, profit = input('Предприятнтие и выручка за 4 квартрала(через пробел): ').split()
    all_profit += (float(profit) / count) / 12
    d[company] = profit
    d_mid_profit[company] = float(profit) / 12
new_d = ChainMap(d, d_mid_profit)
print()
print(new_d.maps[0])
print(f'Средняя прибыль всех компаний {all_profit:.2f}')
d_min = OrderedDict()
d_max = OrderedDict()
for k, v in new_d.maps[1].items():
    if v < all_profit:
        d_min[k] = round(v, 2)
    else:
        d_max[k] = round(v, 2)

print(f'Компании с прибылью меньше средней {d_min}', )
print(f'Компании с прибылью большей или равной средней {d_max}')
