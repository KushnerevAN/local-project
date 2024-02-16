#Задача 1. Сэндвич

#from typing import Callable

#def ingredients(func: Callable) -> Callable:
#    print('#Помидоры#')
#    func()
#    print('~Салат~')
#    return ingredients

#def bread(func: Callable) -> Callable:
#    print('</----------\>')
#    ingredients(func)
#    print('<\______/>')
#    return bread

#@bread
#def sandwich():
#    print('--Ветчина--')

#Задача 2. Плагины

from typing import Callable

PLUGINS = dict()

def registration(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func

@registration
def say_hello(name):
    print('Hello {name}'.format(name=name))

def say_bye(name):
    print('Goodbye {name}'.format(name=name))

print(PLUGINS)
print(say_hello('Dfcz'))
