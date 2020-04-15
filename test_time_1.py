'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random
import cProfile


def count_num(n):
    array = [random.randint(1, n//2) for _ in range(n)]
    top = 0  # Количество посторений цифры
    num = 0  # Часто встречающаяся цифра
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count > top:
            top = count
            num = array[i]
    return num, top


# print(count_num(100))
#cProfile.run('count_num(500)')

'''
1    0.000    0.000    0.000    0.000 test_time_1.py:9(count_num) 10
71 function calls in 0.000 seconds
____
1    0.000    0.000    0.000    0.000 test_time_1.py:9(count_num) 20
139 function calls in 0.001 seconds
____
1    0.000    0.000    0.001    0.001 test_time_1.py:9(count_num) 50
319 function calls in 0.001 seconds
____
1    0.005    0.005    0.006    0.006 test_time_1.py:9(count_num) 100
629 function calls in 0.006 seconds
____
1    0.014    0.014    0.015    0.015 test_time_1.py:9(count_num) 200
1283 function calls in 0.015 seconds
____
1    0.062    0.062    0.065    0.065 test_time_1.py:9(count_num) 500
3017 function calls in 0.065 seconds
'''
#  "task_3.count_num(10)"
# 1000 loops, best of 5: 23 usec per loop
#
# "task_3.count_num(20)"
# 1000 loops, best of 5: 61 usec per loop
#
# "task_3.count_num(50)"
# 1000 loops, best of 5: 288 usec per loop
#
# "task_3.count_num(100)"
# 1000 loops, best of 5: 1.03 msec per loop
#
# "task_3.count_num(200)"
# 1000 loops, best of 5: 3.89 msec per loop
#
# "task_3.count_num(500)"
# 1000 loops, best of 5: 25.4 msec per loop
