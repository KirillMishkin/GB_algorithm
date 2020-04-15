'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random
import timeit
import cProfile


def count_num(n):
    d = {}
    array = [random.randint(1, n // 2) for _ in range(n)]
    # print(array)
    for i in array:
        if d.get(i) is None:
            d[i] = 0
        d[i] += 1
    count = 0
    num = 0
    for k, v in d.items():
        if v > count:
            count = v
            num = k
    return num, count


# print(count_num(20))
#cProfile.run('count_num(5000)')

'''
cProfile
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 10
 72 function calls in 0.000 seconds
 ___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 20
136 function calls in 0.000 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 50
316 function calls in 0.001 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 100
628 function calls in 0.001 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 200
1257 function calls in 0.002 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 500
3015 function calls in 0.001 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 1000
6034 function calls in 0.016 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 2000
12048 function calls in 0.014 seconds
___
1    0.000    0.000    0.000    0.000 test_time_2.py:10(count_num) 5000
33292 function calls in 0.057 seconds

'''
#  "task_4.count_num(10)"
# 1000 loops, best of 5: 12.3 usec per loop
#
# "task_4.count_num(20)"
# 1000 loops, best of 5: 22.1 usec per loop
#
# #"task_4.count_num(50)"
# 1000 loops, best of 5: 93.1 usec per loop
#
# "task_4.count_num(100)"
# 1000 loops, best of 5: 103 usec per loop
#
# "task_4.count_num(200)"
# 1000 loops, best of 5: 203 usec per loop
#
# "task_4.count_num(500)"
# 1000 loops, best of 5: 511 usec per loop
#
# "task5.count_num(1000)"
# 1000 loops, best of 5: 1.09 msec per loop
#
# "task5.count_num(2000)"
# 1000 loops, best of 5: 2.17 msec per loop
#
# "task_4.count_num(5000)"
# 1000 loops, best of 5: 5.8 msec per loop
