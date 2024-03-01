# Задача 1. Счётчик 2
#
# Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов декорируемой функции.
# Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же декоратор,
# но уже с использованием знаний о локальных и глобальных переменных.
#
# Реализуйте декоратор двумя способами:
#
# используя глобальную переменную count;
# используя локальную переменную count внутри декоратора.
#
#
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции и методы,
# находящиеся во встроенном пространстве имён в Python.
#
#
#
# Результат выполнения команды:
#
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__'  ну и так далее.

global_count = {}


def decorator_counter(func):
    local_count = {}

    def wrapped_func(*args, **kwargs):
        global global_count
        nonlocal local_count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        print(global_count, local_count)
        return func(*args, **kwargs)

    wrapped_func.check_count = local_count  # добавим на всякий случай ссылку на этот локальный словарь
    return wrapped_func


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')


hello()
hello()
hello_2()
hello_2()
print(hello_2.check_count)

print('*' * 100)
print(dir(__builtins__))
