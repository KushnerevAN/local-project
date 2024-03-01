#Задача 1. Таймер
#from contextlib import contextmanager
#from collections.abc import Iterator
#import time

#@contextmanager
#def timer() -> Iterator:
#    start = time.time()
#    try:
#        yield
#    except Exception as ex:
#        print('Ошибка', ex)
#    finally:
#        print('Время работы функции:', time.time() - start)

#with timer() as t_1:
#    print('Начало')
#    res = 10 * 100 ** 110001
#    res += 'ssdd'

#Задача 2. Директории

from contextlib import contextmanager
import os
@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())







