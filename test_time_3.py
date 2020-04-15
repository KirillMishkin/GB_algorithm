'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random
import timeit
import cProfile


def count_num(n):
    array = tuple(random.randint(1, n//2) for _ in range(n))
    #print(array)
    array_set = set(array)
    count = 0
    num = 0
    for i in array_set:
        if array.count(i) > count:
            count = array.count(i)
            num = i
    return num, count


#print(count_num(10))
#cProfile.run('count_num(5000)')

'''
cProfile
1    0.000    0.000    0.000    0.000 test_time_3.py:10(count_num) 10
83 function calls in 0.000 seconds
___
1    0.000    0.000    0.000    0.000 test_time_3.py:10(count_num) 20
143 function calls in 0.000 seconds
___
1    0.000    0.000    0.000    0.000 test_time_3.py:10(count_num) 50
348 function calls in 0.001 seconds
___
1    0.000    0.000    0.001    0.001 test_time_3.py:10(count_num) 100
680 function calls in 0.001 seconds
___
1    0.000    0.000    0.003    0.003 test_time_3.py:10(count_num) 200
1358 function calls in 0.003 seconds
___
1    0.000    0.000    0.007    0.007 test_time_3.py:10(count_num) 500
3243 function calls in 0.007 seconds
___
1    0.000    0.000    0.007    0.007 test_time_3.py:10(count_num) 1000
6474 function calls in 0.035 seconds
___
1    0.000    0.000    0.007    0.007 test_time_3.py:10(count_num) 2000
12924 function calls in 0.059 seconds
___
1    0.004    0.004    0.218    0.218 test_time_3.py:10(count_num) 5000
35316 function calls in 0.218 seconds

'''
# timeit
#
#  "task_4.count_num(10)"
# 1000 loops, best of 5: 12.6 usec per loop
#
# "task_4.count_num(20)"
# 1000 loops, best of 5: 22.5 usec per loop
#
# #"task_4.count_num(50)"
# 1000 loops, best of 5: 53.3 usec per loop
#
# "task_4.count_num(100)"
# 1000 loops, best of 5: 106 usec per loop
#
# "task_4.count_num(200)"
# 1000 loops, best of 5: 343 msec per loop
#
# "task_4.count_num(500)"
# 1000 loops, best of 5: 530 msec per loop
#
# "task_4.count_num(1000)"
# 1000 loops, best of 5: 1.05 msec per loop
#
# "task_4.count_num(2000)"
# 1000 loops, best of 5: 2.12 msec per loop
