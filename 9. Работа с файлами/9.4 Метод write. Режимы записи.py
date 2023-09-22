#Задача 1. Сумма чисел
#import os
#print(os.listdir())
#file = os.path.abspath(os.path.join('Number.txt'))
#open_file = open(file, 'r', encoding='utf-8')
#closed_file = open('Number_1.txt', 'w')
#summ = 0
#for i in open_file:
#    summ += int(i)
#print(str(summ))
#closed_file.write(str(summ))
#closed_file.close()

#Задача 2. Всё в одном

import os
def rec(path_to, ending):
    all_path = []
    for i in os.listdir(path_to):
        path = os.path.join(path_to, i)
        if i.endswith(ending):
            all_path.append(os.path.abspath(path))
        elif os.path.isdir(path):
             res = rec(path, ending)
             if res:
                 all_path.extend(res)
    return all_path

def load(path_to_file):
    result = ''
    file = open(path_to_file, 'r', encoding='UTF-8')
    for i in file:
        result += i
    return result

#path = os.path.join('..', '..', 'local-project')
scripts = open('scripts.txt', 'w', encoding='UTF-8')
ending = '.py'
all_py_files = rec('..', ending)

for file_path in all_py_files:
    scripts.write(load(file_path))
    scripts.write("\n" * 2 + "*" * 80 + "\n" * 2)

