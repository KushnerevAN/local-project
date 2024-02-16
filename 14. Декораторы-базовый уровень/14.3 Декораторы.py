#Задача 1. Двойной вызов

#from typing import Callable, Any

#def do_twice(func: Callable) -> Any:

#    def wrapped_func(*args, **kwargs) -> Any:
#        func(*args, **kwargs)
#        return func(*args, **kwargs)
#    return wrapped_func

#@ do_twice
#def greeting(name):
#    print('Привет, {name}!'.format(name=name))

#greeting('Tom')

#Задача 2. Таймер 2
import time

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate

@time_track
def hard_func():
    return [x ** 2 ** x for x in range(22)]

hard_func()
