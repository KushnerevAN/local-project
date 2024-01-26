#Задача 1. Функции

#from typing import Callable, Any

#def func_2(function: Callable, num: int) -> Any:
#    result = function(num)
#    return result ** 2

#def func_1(x):
    #return x + 10

#print(func_2(func_1, 9))

#Задача 2. Таймер

import time
from typing import Callable, Any

def timer(func: Callable, *args, **kwargs) -> Any:

    start_func = time.time()
    result = func(*args, **kwargs)
    end_func = time.time()
    res_time_count = end_func - start_func
    print('Время работы функции {} сек.'.format(res_time_count))
    return result


def function():
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([num ** 2 for num in range(1000)])
    #return result

def function_2(number):
    result = 0
    for _ in range(number + 1):
        result += sum([num ** 3 for num in range(1000)])
    #return result



time_count_f_1 = timer(function)
print(time_count_f_1)
time_count_f_2 = timer(function_2, 1000)
print(time_count_f_2)
