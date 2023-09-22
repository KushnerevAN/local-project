#Задача 1. Результаты
import os

#print(os.listdir())
#file_1 = os.path.join('task', 'Additional_info', 'group_1.txt')
#file_2 = os.path.join('task', 'Dont touch me', 'group_2.txt')
#open_file_1 = open(file_1, 'r', encoding='utf-8')
#open_file_2 = open(file_2, 'r', encoding='utf-8')

#summa = 0
#diff = 0
#compose = 0

#for i_line in open_file_1:
#    info = i_line.split()
#    print(info)
#    #if list(info):
#    #summa += int(info[2])
#    #diff -= int(info[2])

#for i_line in open_file_2:
#    info = i_line.split()
#    if list(info):
#        compose += int(info[2])

#open_file_1.close()
#open_file_2.close()
#print(summa)
#print(diff)
#print(compose)

#Задача 2. Поиск файла 2

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



