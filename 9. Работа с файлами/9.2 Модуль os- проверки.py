#Задача 1. Иконки
#import os

#path = input("Путь: ")
#print('Путь:', path)
#if os.path.exists(path):
#    if os.path.isfile(path):
#        print('Это файл.')
#        print('Размер', os.path.getsize(path), 'байт.')
#    elif os.path.isdir(path):
#        print('Это папка.')
#    elif os.path.islink(path):
#        print('Это ссылка.')
#else:
#    print('Такого пути не существует.')

#Задача 2. Поиск файла

import os
import random

def function(path_to, file, total_list):
    for i in os.listdir(path_to):
        path = os.path.join(path_to, i)
        if file == i:
            #print(os.path.join(path))
            total_list.append(os.path.join(path))
        elif os.path.isdir(path):
            function(path, file, total_list)
    return total_list


path_1 = input('Ищем в: ')
file_name = input('Имя файла: ')
#print('Найденый следующие пути:')
total_list = function(path_1, file_name, [])
number = random.randint(0, len(total_list) + 1)
print(total_list[number])



