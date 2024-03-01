#Задача 1. Повторение кода


#from typing import Callable
#import functools

#def sleep_func_num(value=2):
#    def slepp_func(func: Callable) -> Callable:
#        """Декоратор, выполняющий основную функцию с заданной задержкой"""
#        @functools.wraps(func)
#        def wrapped_func():
#            for i in range(1, value + 1):
#                func()
#                print('Функция выполнилась {} раз(а)'.format(i))
#        return wrapped_func
#    return slepp_func
#value = 5
#@sleep_func_num(value)
#def test():
#    pass

#test()

#Задача 2. Замедление кода 2

import time
from typing import Callable
import functools

def slepp_func(func: Callable) -> Callable:
    """Декоратор, выполняющий основную функцию с заданной задержкой"""
    @functools.wraps(func)
    def wrapped_func(value):
        time.sleep(value)
        func()
        print('Выполнение функции было задержано на {value} сек.'.format(value=value))
    return wrapped_func

@ slepp_func
def test():
    pass

test(2)